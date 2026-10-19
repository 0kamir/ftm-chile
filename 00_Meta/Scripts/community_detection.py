#!/usr/bin/env python3
"""
Detector de Agrupamientos de la red y Modularidad (Clauset-Newman-Moore Q)
=================================================================================
Analiza la topología del grafo del vault en `metricas_red.json`
mediante maximización aglomerativa de Modularidad de Newman-Girvan / Clauset-Newman-Moore (CNM)
sobre los nodos (`persona`, `entidad_publica`, `entidad_privada`,
`partido_politico`, `nexo_transaccion`, `causa_judicial`), excluyendo nodos de
catálogo penal o vistas para evitar falsos puentes jurídicos.
Identifica:
1. Agrupamientos autónomas y su flujo financiero registrado.
2. Nodos Broker Inter-Comunidad (con Coeficiente de Participación P_i de Guimerà & Amaral > 0).
3. Aristas Puente Estructurales entre Comunidades.
Genera el reporte en `05_Vistas_Analiticas/Agrupamientos_de_la_Red.md`.
"""

import json
from pathlib import Path
from collections import defaultdict
from descargo import descargo  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Exportaciones" / "metricas_red.json"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Agrupamientos_de_la_Red.md"

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
    "causa_judicial",
}


def load_graph():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = {
        n["id"]: n
        for n in data["nodos"]
        if n.get("tipo_nodo") in OPERATIONAL_TYPES
    }
    adj = defaultdict(lambda: defaultdict(float))
    edges = []
    for e in data["aristas"]:
        u, v = e["source"], e["target"]
        if u in nodes and v in nodes and u != v:
            adj[u][v] += 1.0
            adj[v][u] += 1.0
            edges.append((u, v, e.get("relacion", "vinculo")))
    # Filtrar solo nodos con grado > 0 en la red
    active_nodes = {u: n for u, n in nodes.items() if len(adj[u]) > 0}
    return active_nodes, adj, edges


def compute_modularity(adj, community_map, m2):
    if m2 == 0:
        return 0.0
    degrees = {u: sum(adj[u].values()) for u in community_map}
    q = 0.0
    for u in community_map:
        for v, w in adj[u].items():
            if v in community_map and community_map[u] == community_map[v]:
                q += w - (degrees[u] * degrees[v]) / m2
    for u in community_map:
        q -= (degrees[u] * degrees[u]) / m2
    # Recalcular exacto por suma sobre todos los pares (u, v) en la misma comunidad
    q_exact = 0.0
    for u in community_map:
        for v in community_map:
            if community_map[u] == community_map[v]:
                a_uv = adj[u].get(v, 0.0)
                q_exact += a_uv - (degrees[u] * degrees[v]) / m2
    return q_exact / m2


def cnm_greedy_modularity_communities(nodes, adj):
    """
    Maximización aglomerativa de Modularidad de Clauset-Newman-Moore (CNM):
    Fusiona iterativamente el par de comunidades conectadas que produce el mayor
    incremento positivo Delta_Q en la modularidad global de Newman-Girvan.
    """
    node_list = sorted(nodes.keys())
    comm = {u: i for i, u in enumerate(node_list)}
    degrees = {u: sum(adj[u].values()) for u in node_list}
    m2 = sum(degrees.values())
    if m2 == 0:
        return comm, 0.0

    while True:
        current_q = compute_modularity(adj, comm, m2)
        active_comms = sorted(set(comm.values()))
        # Encontrar pares de comunidades con al menos una arista entre ellas
        candidate_pairs = set()
        for u in node_list:
            for v in adj[u]:
                c_u, c_v = comm[u], comm[v]
                if c_u < c_v:
                    candidate_pairs.add((c_u, c_v))

        best_pair = None
        best_q = current_q

        for c1, c2 in sorted(candidate_pairs):
            trial_comm = {u: (c1 if c == c2 else c) for u, c in comm.items()}
            q_trial = compute_modularity(adj, trial_comm, m2)
            if q_trial > best_q + 1e-9:
                best_q = q_trial
                best_pair = (c1, c2)

        if best_pair is None:
            break

        c1, c2 = best_pair
        for u in comm:
            if comm[u] == c2:
                comm[u] = c1

    final_q = compute_modularity(adj, comm, m2)
    return comm, final_q


def compute_participation_coefficient(nodes, adj, comm):
    """
    Coeficiente de Participación de Guimerà & Amaral (2005):
    P_i = 1 - sum_s (k_{i,s} / k_i)^2
    """
    participation = {}
    for u in nodes:
        k_i = sum(adj[u].values())
        if k_i == 0:
            participation[u] = 0.0
            continue
        comm_weights = defaultdict(float)
        for v, w in adj[u].items():
            if v in comm:
                comm_weights[comm[v]] += w
        sum_sq = sum((w / k_i) ** 2 for w in comm_weights.values())
        participation[u] = round(1.0 - sum_sq, 4)
    return participation


def generate_report():
    nodes, adj, edges = load_graph()
    comm, q_score = cnm_greedy_modularity_communities(nodes, adj)
    participation = compute_participation_coefficient(nodes, adj, comm)

    clusters = defaultdict(list)
    for u, c_id in comm.items():
        clusters[c_id].append(u)

    sorted_clusters = sorted(clusters.values(), key=lambda cl: (-len(cl), cl[0]))

    node_to_cluster_idx = {}
    cluster_names = {}
    for idx, members in enumerate(sorted_clusters, 1):
        causas = [m for m in members if nodes[m].get("tipo_nodo") == "causa_judicial"]
        if causas:
            label = " / ".join(sorted(causas)[:2])
        else:
            entidades = [m for m in members if nodes[m].get("tipo_nodo") in ("entidad_publica", "entidad_privada", "partido_politico")]
            label = sorted(entidades)[0] if entidades else sorted(members)[0]
        cluster_names[idx] = f"Agrupamiento #{idx:02d} ({label})"
        for m in members:
            node_to_cluster_idx[m] = idx

    inter_edges = []
    seen_pairs = set()
    for u, v, rel in edges:
        c_u = node_to_cluster_idx[u]
        c_v = node_to_cluster_idx[v]
        if c_u != c_v:
            pair = tuple(sorted([u, v])) + (rel,)
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                inter_edges.append((u, c_u, v, c_v, rel))

    brokers = sorted(
        [(u, participation[u], sum(adj[u].values()), node_to_cluster_idx[u]) for u in nodes if participation[u] > 0],
        key=lambda x: (-x[1], -x[2], x[0]),
    )

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Detección de Agrupamientos de la red y Modularidad (Newman-Girvan Q)"',
        "actualizacion_automatica: true",
        "tags:",
        "  - comunidades",
        "  - modularidad-newman",
        "  - analisis-de-redes",
        "---",
        "",
        "# Agrupamientos de la Red y Modularidad ($Q$)",
        "",
        *descargo("agrupamientos"),
        "",
        "> [!NOTE] Análisis de modularidad (Clauset-Newman-Moore & Guimerà-Amaral)",
        "> Esta vista aplica maximización aglomerativa de **Modularidad de Newman-Girvan ($Q$)** (algoritmo de Clauset-Newman-Moore sobre la red de actores, causas y transacciones, excluyendo artículos penales genéricos) para particionar el grafo en **Agrupamientos**, y calcula el **Coeficiente de Participación ($P_i$)** de Guimerà & Amaral (2005) para descubrir los *brokers* que conectan agrupamientos criminales o políticas distintas.",
        "",
        "## 1. Indicadores Globales de Partición",
        "",
        f"- **Nodos Operativos Analizados**: `{len(nodes)}`",
        f"- **Modularidad Global de Newman-Girvan ($Q$)**: `{q_score:.4f}` *(Valores $Q > 0.70$ indican alta compartimentación celular con puentes específicos de articulación)*",
        f"- **Total de Agrupamientos Detectadas**: `{len(sorted_clusters)}`",
        f"- **Enlaces Puente Inter-Comunidad Detectados**: `{len(inter_edges)}`",
        f"- **Nodos Articuladores Inter-Agrupamiento ($P_i > 0$)**: `{len(brokers)}`",
        "",
        "---",
        "",
        "## 2. Brokers Inter-Comunidad (Coeficiente de Participación $P_i > 0$)",
        "",
        "| Pos | Nodo Articulador | Tipo | Comunidad Base | Grado ($k_i$) | Coef. Participación ($P_i$) | Rol Topológico |",
        "| :--- | :--- | :--- | :--- | :---: | :---: | :--- |",
    ]

    for i, (u, p_val, deg, c_idx) in enumerate(brokers, 1):
        tipo = nodes[u].get("tipo_nodo", "desconocido")
        rol = "Hub Conector Multi-Agrupamiento" if p_val >= 0.30 else "Puente Inter-Clúster"
        lines.append(
            f"| **{i}** | [[{u}]] | `{tipo}` | {cluster_names[c_idx]} | `{int(deg)}` | **`{p_val:.4f}`** | {rol} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Puentes Estructurales entre Agrupamientos",
        "",
        "| Nodo A | Agrupamiento A | Relación | Nodo B | Agrupamiento B |",
        "| :--- | :--- | :---: | :--- | :--- |",
    ])

    for u, c_u, v, c_v, rel in inter_edges:
        lines.append(f"| [[{u}]] | {cluster_names[c_u]} | `{rel}` | [[{v}]] | {cluster_names[c_v]} |")

    lines.extend([
        "",
        "---",
        "",
        "## 4. Radiografía de Agrupamientos Detectadas",
        "",
    ])

    for idx, members in enumerate(sorted_clusters, 1):
        monto_cluster = sum(nodes[m].get("monto_clp", 0) or 0 for m in members if nodes[m].get("tipo_nodo") == "nexo_transaccion")
        personas = [f"[[{m}]]" for m in sorted(members) if nodes[m].get("tipo_nodo") == "persona"]
        instituciones = [f"[[{m}]]" for m in sorted(members) if nodes[m].get("tipo_nodo") in ("entidad_publica", "entidad_privada", "partido_politico")]
        trxs = [f"[[{m}]]" for m in sorted(members) if nodes[m].get("tipo_nodo") == "nexo_transaccion"]

        lines.extend([
            f"### {cluster_names[idx]}",
            f"- **Tamaño del Clúster**: `{len(members)}` nodos | **Flujo Registrado en la Agrupamiento**: `${monto_cluster:,.0f} CLP`".replace(",", "."),
            f"- **Personas Involucradas ({len(personas)})**: {', '.join(personas) if personas else '_Ninguna_'}",
            f"- **Entidades Públicas/Privadas ({len(instituciones)})**: {', '.join(instituciones) if instituciones else '_Ninguna_'}",
            f"- **Transacciones Reificadas ({len(trxs)})**: {', '.join(trxs) if trxs else '_Ninguna_'}",
            "",
        ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Reporte de Agrupamientos de la red generado en: {REPORT_PATH.relative_to(VAULT_ROOT)} (Q = {q_score:.4f}, {len(sorted_clusters)} agrupamientos)")


if __name__ == "__main__":
    generate_report()
