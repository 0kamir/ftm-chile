#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kinship_and_clans.py
====================
Motor Analítico de Redes de Parentesco, Grupos familiares y Puentes Familiares
(Capa Multiplex `vinculos_familiares` sobre el Grafo de Aristas Reificadas).

Modela formalmente cómo los vínculos de consanguinidad y afinidad (`vinculos_familiares`)
operan como atajos geodésicos (Small-World Shortcuts) que acoplan macro-causas judiciales,
estudios jurídicos de lobby (ej. Caso Audios: Chadwick–Hermosilla–Piñera), privatizaciones
(grupo familiar Pinochet–Hiriart).

Genera: 05_Vistas_Analiticas/Redes_de_Parentesco.md
"""

import os
import json
from collections import defaultdict, deque
from descargo import descargo  # noqa: E402

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
METRICAS_JSON = os.path.join(VAULT_ROOT, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json")
OUTPUT_MD = os.path.join(VAULT_ROOT, "05_Vistas_Analiticas", "Redes_de_Parentesco.md")

CLAN_METADATA = {
    frozenset(["Sebastian Pinera Echenique", "Andres Chadwick Pinera"]): {
        "nombre_clan": "Grupo familiar Piñera–Chadwick",
        "tipo_parentesco": "Primos hermanos (hijos de hermanos Piñera Carvallo)",
        "descripcion": "Parentesco de conocimiento público. No implica participación conjunta en los hechos registrados.",
    },
    frozenset(["Augusto Pinochet Ugarte", "Lucia Hiriart Rodriguez", "Augusto Pinochet Hiriart", "Julio Ponce Lerou"]): {
        "nombre_clan": "Grupo familiar Pinochet–Hiriart",
        "tipo_parentesco": "Cónyuges, hijo y exyerno (Julio Ponce Lerou estuvo casado con Verónica Pinochet Hiriart)",
        "descripcion": "Parentesco de conocimiento público. No implica participación conjunta en los hechos registrados.",
    },
}


def fmt_clp(val: int) -> str:
    return "$" + f"{int(val):,}".replace(",", ".")


def bfs_shortest_path(adj: dict, start: str, goal: str):
    if start == goal:
        return [start]
    visited = {start}
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        curr = path[-1]
        for nxt in sorted(adj.get(curr, [])):
            if nxt == goal:
                return path + [nxt]
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])
    return None


def main():
    with open(METRICAS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = {n["id"]: n for n in data["nodos"]}
    edges = data["aristas"]

    # Build undirected graphs: full graph G and graph without kinship edges G_no_fam
    adj_full = defaultdict(set)
    adj_no_fam = defaultdict(set)
    adj_fam = defaultdict(set)
    fam_edges = []

    for e in edges:
        u, v, rel = e["source"], e["target"], e["relation"]
        if u not in nodes or v not in nodes:
            continue
        adj_full[u].add(v)
        adj_full[v].add(u)
        if rel == "vinculos_familiares":
            adj_fam[u].add(v)
            adj_fam[v].add(u)
            if u < v:
                fam_edges.append((u, v))
        else:
            adj_no_fam[u].add(v)
            adj_no_fam[v].add(u)

    # Map each person to their transactions (TRX) and causes
    person_trxs = defaultdict(set)
    person_causes = defaultdict(set)
    trx_amounts = {}
    trx_causes = {}

    for nid, n in nodes.items():
        if n.get("tipo_nodo") == "nexo_transaccion":
            amt = int(n.get("monto_clp", 0) or 0)
            trx_amounts[nid] = amt

    # Inspect edges from nexo_transaccion
    for e in edges:
        u, v, rel = e["source"], e["target"], e["relation"]
        if nodes.get(u, {}).get("tipo_nodo") == "nexo_transaccion":
            if rel == "causa_vinculada" and nodes.get(v, {}).get("tipo_nodo") == "causa_judicial":
                trx_causes[u] = v
            elif rel in ("firmante_origen", "firmante_destino") and nodes.get(v, {}).get("tipo_nodo") == "persona":
                person_trxs[v].add(u)

    for p, trxs in person_trxs.items():
        for t in trxs:
            if t in trx_causes:
                person_causes[p].add(trx_causes[t])

    # Connected components in adj_fam
    visited_fam = set()
    clans = []
    for p in sorted(adj_fam.keys()):
        if p not in visited_fam:
            comp = set()
            q = deque([p])
            visited_fam.add(p)
            while q:
                curr = q.popleft()
                comp.add(curr)
                for nxt in sorted(adj_fam[curr]):
                    if nxt not in visited_fam:
                        visited_fam.add(nxt)
                        q.append(nxt)
            clans.append(sorted(comp))

    # Enrich each clan with metrics
    clan_records = []
    total_clan_clp = 0
    all_clan_trxs = set()
    for members in clans:
        fset = frozenset(members)
        meta = CLAN_METADATA.get(fset, {
            "nombre_clan": "Grupo familiar " + " / ".join(members),
            "tipo_parentesco": "Parentesco / Afinidad Documentada",
            "descripcion": "Subgrafo familiar detectado automáticamente.",
        })
        trxs = set()
        causes = set()
        for m in members:
            trxs |= person_trxs.get(m, set())
            causes |= person_causes.get(m, set())
        monto_clan = sum(trx_amounts.get(t, 0) for t in trxs)
        all_clan_trxs |= trxs
        clan_records.append({
            "members": members,
            "nombre_clan": meta["nombre_clan"],
            "tipo_parentesco": meta["tipo_parentesco"],
            "descripcion": meta["descripcion"],
            "trxs": sorted(trxs),
            "causes": sorted(causes),
            "monto_clan": monto_clan,
        })

    clan_records.sort(key=lambda c: c["monto_clan"], reverse=True)
    total_clan_clp = sum(trx_amounts.get(t, 0) for t in all_clan_trxs)

    # Calculate Geodesic Shortcuts created by Kinship links
    shortcut_pairs = [
        ("Sebastian Pinera Echenique", "Luis Hermosilla Osorio", "Distancia entre ambos nodos con y sin la arista de parentesco"),
        ("Augusto Pinochet Ugarte", "SQM SA", "Distancia entre ambos nodos con y sin la arista de parentesco"),
        ("Caso Riggs", "Caso Cascadas", "Distancia entre ambas causas con y sin las aristas de parentesco"),
    ]

    shortcut_results = []
    for u, v, label in shortcut_pairs:
        path_with = bfs_shortest_path(adj_full, u, v)
        path_without = bfs_shortest_path(adj_no_fam, u, v)
        d_with = len(path_with) - 1 if path_with else None
        d_without = len(path_without) - 1 if path_without else None
        delta = (d_without - d_with) if (d_with is not None and d_without is not None) else None
        shortcut_results.append({
            "u": u,
            "v": v,
            "label": label,
            "d_with": d_with,
            "d_without": d_without,
            "delta": delta,
            "path_with": path_with,
        })

    # Write Markdown Analytical View
    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Redes de Parentesco, Grupos familiares y Puentes Familiares"',
        "actualizacion_automatica: true",
        "tags:",
        "  - vista-analitica",
        "  - parentesco",
        "  - clanes-familiares",
        "  - caso-audios",
        "  - grafos-multiplex",
        "---",
        "",
        "# Redes de Parentesco y Puentes Familiares ($G_{\\text{fam}}$)",
        "",
        *descargo("parentesco"),
        "",
        "> **Modelamiento Matemático de Parentesco en Grafos Multiplex**: En el análisis de redes, los lazos de consanguinidad (padres, hijos, primos hermanos) y afinidad (cónyuges, suegros, yernos, cuñados) conforman una capa estructural independiente ($E_{\\text{fam}}$) que se superpone a la red de transacciones financieras ($E_{\\text{trx}}$) y militancias políticas ($E_{\\text{pol}}$). Mediante el atributo YAML `vinculos_familiares` en el esquema `persona`, el motor de grafos cuantifica cómo los grupos familiares reducen la distancia geodésica ($\\Delta d$) entre macro-causas judiciales y concentran flujos patrimoniales.",
        "",
        "## 1. Resumen Ejecutivo de la Capa de Parentesco (`vinculos_familiares`)",
        f"- **Grupos familiares / Familiares Modelados**: **{len(clan_records)}** componentes conexas familiares.",
        f"- **Sujetos Integrados en Redes de Parentesco Explícito**: **{len(adj_fam)}** nodos de tipo `persona`.",
        f"- **Aristas de Parentesco Bidireccionales (`vinculos_familiares`)**: **{len(fam_edges)} pares familiares** ({len(fam_edges)*2} aristas dirigidas en el grafo).",
        f"- **Montos Registrados en Hechos con Integrantes de Grupos Familiares**: **`{fmt_clp(total_clan_clp)} CLP`** a través de **{len(all_clan_trxs)} transacciones reificadas**.",
        "",
        "---",
        "",
        "## 2. Grupos Familiares Registrados",
        "",
        "| Grupo familiar / Familiar | Tipo de Parentesco | Miembros (`persona`) | Macro-Causas Conectadas | N° TRX | Volumen Patrimonial Asociado (CLP) |",
        "| :--- | :--- | :--- | :--- | :---: | ---: |",
    ]

    for c in clan_records:
        members_links = ", ".join(f"[[{m}]]" for m in c["members"])
        causes_links = ", ".join(f"[[{ca}]]" for ca in c["causes"])
        lines.append(
            f"| **{c['nombre_clan']}** | {c['tipo_parentesco']} | {members_links} | {causes_links} | {len(c['trxs'])} | **{fmt_clp(c['monto_clan'])}** |"
        )

    lines.extend([
        "",
        "### Detalle por Grupo Familiar",
        "",
    ])

    for idx, c in enumerate(clan_records, 1):
        lines.append(f"#### 3.{idx}. {c['nombre_clan']}")
        lines.append(f"- **Vínculo Genealógico / Afinidad**: {c['tipo_parentesco']}.")
        lines.append(f"- **Integrantes en la Bóveda**: {', '.join(f'[[{m}]]' for m in c['members'])}.")
        lines.append(f"- **Macro-Causas Acopladas ({len(c['causes'])})**: {', '.join(f'[[{ca}]]' for ca in c['causes'])}.")
        lines.append(f"- **Aristas Reificadas Vinculadas ({len(c['trxs'])})**: {', '.join(f'[[{t}]]' for t in c['trxs'])}.")
        lines.append(f"- **Volumen Financiero Consolidado**: **`{fmt_clp(c['monto_clan'])} CLP`**.")
        lines.append(f"- **Síntesis de Captura de Red**: {c['descripcion']}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 3. Reducción de Distancia Geodésica ($\\Delta d$) por Atajos de Parentesco",
        "",
        "Para medir el impacto topológico de los vínculos familiares, comparamos la distancia geodésica más corta $d_{G}(u, v)$ en el grafo completo versus $d_{G \\setminus E_{\\text{fam}}}(u, v)$ cuando se remueven las aristas `vinculos_familiares`:",
        "",
        "| Nodo Origen ($u$) | Nodo Destino ($v$) | $d(u,v)$ Sin Parentesco | $d(u,v)$ Con Parentesco | Reducción $\\Delta d$ | Ruta Geodésica Mínima con Parentesco |",
        "| :--- | :--- | :---: | :---: | :---: | :--- |",
    ])

    for sr in shortcut_results:
        d_wo = str(sr["d_without"]) if sr["d_without"] is not None else "∞"
        d_w = str(sr["d_with"]) if sr["d_with"] is not None else "∞"
        delta_str = f"-{sr['delta']} saltos" if (sr["delta"] is not None and sr["delta"] > 0) else "0 saltos"
        path_str = " → ".join(f"[[{p}]]" for p in sr["path_with"]) if sr["path_with"] else "N/A"
        lines.append(
            f"| [[{sr['u']}]] | [[{sr['v']}]] | `{d_wo}` | **`{d_w}`** | **{delta_str}** | {path_str} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 4. Otros Nexos de Parentesco e Influencia Familiar Documentados en Causas",
        "",
        "Además de los clanes que conectan múltiples nodos `persona` entre distintas causas, la bóveda registra aristas donde el parentesco opera al interior de una misma causa o sociedad vehículo:",
        "- **[[Caso Caval]] ([[Natalia Compagnon Soto]])**: Socia del 50% de [[Exportadora y de Gestion Caval Ltda]], cónyuge de Sebastián Dávalos Bachelet y nuera de la entonces Presidenta de la República Michelle Bachelet Jeria, vínculo familiar decisivo en la reunión privada con la vicepresidencia de [[Banco de Chile]] para obtener el crédito de `$6.500.000.000 CLP` ([[TRX-2013-11-06-Reunion-Luksic-Compagnon-01]] y [[TRX-2014-02-07-Credito-BancoDeChile-Caval-01]]).",
        "- **[[Caso Pinocheques]] y [[Caso Riggs]] (Sucesión Pinochet–Hiriart)**: Utilización de cuentas mancomunadas, pasaportes ideológicamente falsos y sociedades *offshore* familiares en [[Riggs Bank y Sociedades Offshore Ashburton]] para distribuir fondos reservados entre el grupo familiar directo de [[Augusto Pinochet Ugarte]], [[Lucia Hiriart Rodriguez]] y [[Augusto Pinochet Hiriart]].",
        "",
    ])

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[OK] Vista analítica de parentesco generada en: {OUTPUT_MD}")
    print(f"     Grupos familiares detectados: {len(clan_records)} | Pares familiares: {len(fam_edges)} | Monto clanes: {fmt_clp(total_clan_clp)}")


if __name__ == "__main__":
    main()
