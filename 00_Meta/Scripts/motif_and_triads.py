#!/usr/bin/env python3
"""
Motor de Censo Triádico (Holland-Leinhardt), Clausura de Simmel y Ciclos Cuadrangulares (C_4)
=============================================================================================
Analiza las estructuras de orden superior (Higher-Order Network Motifs) sobre el grafo:
1. Triángulos Cerrados (Clausura Triádica Delta_uvw) y Lazos Fuertes de Simmel (Simmelian Ties).
2. Transitividad Global de Red T = 3 * |Delta| / |Wedges| y Clustering Promedio.
3. Cuadrángulos de Colusión / Ciclos de Orden 4 (C_4: u - x - v - y - u sin cuerda o con cuerda),
   que revelan pares de actores (u, v) que co-operan a través de múltiples intermediarios o transacciones.
Genera `05_Vistas_Analiticas/Censo_Triadico_y_Motivos_Superiores.md`.
"""

from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path
from descargo import descargo  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Exportaciones" / "metricas_red.json"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Censo_Triadico_y_Motivos_Superiores.md"

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
    "causa_judicial",
}

ACTOR_TYPES = {"persona", "entidad_publica", "entidad_privada", "partido_politico"}


def load_operational_graph():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = {
        n["id"]: n
        for n in data["nodos"]
        if n.get("tipo_nodo") in OPERATIONAL_TYPES
    }
    adj = defaultdict(set)
    for e in data["aristas"]:
        u, v = e["source"], e["target"]
        if u in nodes and v in nodes and u != v:
            adj[u].add(v)
            adj[v].add(u)
    active_nodes = {u: n for u, n in nodes.items() if len(adj[u]) > 0}
    return active_nodes, adj


def enumerate_triangles_and_wedges(nodes, adj):
    triangles = []
    wedges = 0
    local_cc = {}

    for u in sorted(nodes.keys()):
        nbrs = sorted(adj[u])
        k = len(nbrs)
        if k < 2:
            local_cc[u] = 0.0
            continue
        pairs = k * (k - 1) // 2
        wedges += pairs
        closed = 0
        for i in range(k):
            v = nbrs[i]
            for j in range(i + 1, k):
                w = nbrs[j]
                if w in adj[v]:
                    closed += 1
                    if u < v < w:
                        triangles.append((u, v, w))
        local_cc[u] = closed / pairs

    transitivity = (3.0 * len(triangles) / wedges) if wedges > 0 else 0.0
    avg_clustering = (sum(local_cc.values()) / len(nodes)) if nodes else 0.0
    return triangles, wedges, transitivity, avg_clustering, local_cc


def enumerate_simmelian_edges(nodes, adj):
    """
    Evalúa la incrustación estructural (Edge Embeddedness / Simmelian Tie Strength)
    de cada arista (u, v) como el número de triángulos que comparten |N(u) n N(v)|.
    """
    simmelian = []
    seen = set()
    for u in sorted(nodes.keys()):
        for v in sorted(adj[u]):
            if u < v and (u, v) not in seen:
                seen.add((u, v))
                common = sorted(adj[u] & adj[v])
                if common:
                    simmelian.append((u, v, len(common), common))
    return sorted(simmelian, key=lambda x: (-x[2], x[0], x[1]))


def enumerate_actor_quadrangles(nodes, adj):
    """
    Detecta motivos cuadrangulares bipartitos / multi-canal entre pares de actores (u, v)
    que comparten >= 2 vecinos intermedios (transacciones, partidos, órganos o causas).
    """
    actors = sorted(u for u in nodes if nodes[u].get("tipo_nodo") in ACTOR_TYPES)
    quads = []
    for i in range(len(actors)):
        u = actors[i]
        for j in range(i + 1, len(actors)):
            v = actors[j]
            shared = sorted(adj[u] & adj[v])
            if len(shared) >= 2:
                # Número de cuadrángulos C_4 formados por (u, v) a través de sus vecinos comunes
                num_c4 = len(shared) * (len(shared) - 1) // 2
                direct = v in adj[u]
                quads.append((u, v, len(shared), num_c4, direct, shared))
    return sorted(quads, key=lambda x: (-x[2], -x[3], x[0], x[1]))


def generate_report():
    nodes, adj = load_operational_graph()
    triangles, wedges, transitivity, avg_cc, local_cc = enumerate_triangles_and_wedges(nodes, adj)
    simmelian_edges = enumerate_simmelian_edges(nodes, adj)
    quadrangles = enumerate_actor_quadrangles(nodes, adj)

    # Clasificar triángulos por arquetipo
    tri_archetypes = []
    for u, v, w in triangles:
        types = sorted([nodes[u].get("tipo_nodo", ""), nodes[v].get("tipo_nodo", ""), nodes[w].get("tipo_nodo", "")])
        if "nexo_transaccion" in types and "causa_judicial" in types:
            arch = "Triángulo Procesal-Transaccional (`Actor ↔ TRX ↔ Causa`)"
        elif "partido_politico" in types:
            arch = "Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`)"
        else:
            arch = "Triángulo Directo (`Entidad ↔ Persona ↔ TRX`)"
        tri_archetypes.append((u, v, w, arch))

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Censo Triádico (Holland-Leinhardt), Lazos de Simmel y Cuadrángulos de Colusión (C4)"',
        "actualizacion_automatica: true",
        "tags:",
        "  - censo-triadico",
        "  - motivos-red",
        "  - lazos-simmel",
        "  - analisis-de-redes",
        "---",
        "",
        "# Censo Triádico, Lazos de Simmel y Motivos Superiores ($\\Delta, C_4$)",
        "",
        *descargo(),
        "",
        "> [!IMPORTANT] Topología de Orden Superior (Higher-Order Network Science)",
        "> Más allá de las aristas diádicas individuales, las redes operan mediante **motivos estructurales cerrados**:",
        "> 1. **Clausura Triádica ($\\Delta_{uvw}$) y Lazos de Georg Simmel**: Dos nodos unidos además por terceros comunes poseen un *lazo simmeliano* de alta cohesión y confianza clandestina.",
        "> 2. **Cuadrángulos Multi-Canal ($C_4: u - x - v - y - u$)**: Identifican pares de actores que interactúan de manera redundante a través de **múltiples transacciones o intermediarios paralelos** (p. ej. fraccionamiento de contratos o co-financiamiento ilegal).",
        "",
        "## 1. Métricas Globales del Censo de Motivos",
        "",
        f"- **Nodos Operativos Activos ($|V|$)**: `{len(nodes)}`",
        f"- **2-Caminos Abiertos (*Wedges* $\\wedge$)**: `{wedges}`",
        f"- **Triángulos Cerrados ($|\\Delta|$)**: **`{len(triangles)}`**",
        f"- **Índice de Transitividad Global ($T = 3|\\Delta| / |\\wedge|$)**: **`{transitivity:.4f}`**",
        f"- **Coeficiente de Clustering Local Promedio ($\\bar{{C}}$)**: **`{avg_cc:.4f}`**",
        f"- **Aristas Simmelianas (con incrustación $|N(u) \\cap N(v)| \\ge 1$)**: `{len(simmelian_edges)}`",
        f"- **Pares de Actores en Cuadrángulos Multi-Canal ($C_4$)**: **`{len(quadrangles)}`**",
        "",
        "---",
        "",
        "## 2. Cuadrángulos de Colusión y Redundancia Multi-Canal ($C_4$)",
        "",
        "Pares de actores (`Persona`, `Entidad Pública/Privada`, `Partido`) que comparten **2 o más nodos intermedios**, formando ciclos cerrados de orden 4 ($C_4$):",
        "",
        "| # | Actor A ($u$) | Actor B ($v$) | Canales Comunes | Ciclos $C_4$ | Enlace Directo | Nodos Intermediarios Compartidos ($N(u) \\cap N(v)$) |",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :--- |",
    ]

    for i, (u, v, k_sh, n_c4, direct, shared) in enumerate(quadrangles, 1):
        sh_str = ", ".join(f"[[{w}]]" for w in shared)
        dir_str = "Sí" if direct else "No"
        lines.append(
            f"| **{i}** | [[{u}]] | [[{v}]] | **`{k_sh}`** | `{n_c4}` | `{dir_str}` | {sh_str} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Lazos Fuertes de Simmel (Aristas con Mayor Incrustación Triádica)",
        "",
        "| # | Nodo A ($u$) | Nodo B ($v$) | Fuerza Simmeliana ($|N(u) \\cap N(v)|$) | Terceros Comunes en el Triángulo |",
        "| :---: | :--- | :--- | :---: | :--- |",
    ])

    for i, (u, v, cnt, common) in enumerate(simmelian_edges[:20], 1):
        c_str = ", ".join(f"[[{w}]]" for w in common)
        lines.append(f"| **{i}** | [[{u}]] | [[{v}]] | **`{cnt}`** | {c_str} |")

    lines.extend([
        "",
        "---",
        "",
        "## 4. Catálogo de Triángulos Cerrados Detectados ($\\Delta_{uvw}$)",
        "",
        "| # | Vértice 1 | Vértice 2 | Vértice 3 | Arquetipo Estructural del Motivo |",
        "| :---: | :--- | :--- | :--- | :--- |",
    ])

    for i, (u, v, w, arch) in enumerate(tri_archetypes, 1):
        lines.append(f"| **{i}** | [[{u}]] | [[{v}]] | [[{w}]] | {arch} |")

    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"[OK] Censo Triádico y Motivos Superiores generado: {REPORT_PATH.relative_to(VAULT_ROOT)} ({len(triangles)} triángulos, {len(quadrangles)} pares C4, T={transitivity:.4f})"
    )


if __name__ == "__main__":
    generate_report()
