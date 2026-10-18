#!/usr/bin/env python3
"""
Motor de Descomposición k-Core (Batagelj-Zaversnik), Asortatividad de Newman y Agujeros Estructurales de Burt
=============================================================================================================
Analiza la jerarquía núcleo-periferia y las propiedades de mezcla topológica de la red operativa:
1. Descomposición k-Core y Capas de Cebolla (Onion Layers) de Batagelj & Zaversnik O(V + E).
2. Coeficiente de Asortatividad de Grado de Newman r in [-1, 1] (prueba de disasortatividad Hub-and-Spoke).
3. Restricción de Agujeros Estructurales de Ronald Burt (Constraint C_i: menor C_i = mayor arbitraje de información).
Genera `05_Vistas_Analiticas/Nucleos_KCore_y_Asortatividad.md`.
"""

from collections import defaultdict
import json
import math
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Exportaciones" / "metricas_red.json"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Nucleos_KCore_y_Asortatividad.md"

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
    "causa_judicial",
}


def load_operational_graph():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = {
        n["id"]: n
        for n in data["nodos"]
        if n.get("tipo_nodo") in OPERATIONAL_TYPES
    }
    adj = defaultdict(set)
    edges = set()
    for e in data["aristas"]:
        u, v = e["source"], e["target"]
        if u in nodes and v in nodes and u != v:
            adj[u].add(v)
            adj[v].add(u)
            edges.add(tuple(sorted((u, v))))
    active_nodes = {u: n for u, n in nodes.items() if len(adj[u]) > 0}
    return active_nodes, adj, sorted(edges)


def kcore_and_onion_decomposition(nodes, adj):
    """
    Algoritmo de pelado (Peeling) de Batagelj-Zaversnik para calcular:
    - core_number[u]: k-core máximo al que pertenece u.
    - onion_layer[u]: capa secuencial de extracción (de periferia a núcleo).
    """
    remaining = set(nodes.keys())
    cur_deg = {u: len(adj[u]) for u in remaining}
    core_num = {}
    onion_layer = {}
    k = 0
    layer = 0

    while remaining:
        min_d = min(cur_deg[u] for u in remaining)
        k = max(k, min_d)
        while True:
            to_remove = sorted([u for u in remaining if cur_deg[u] <= k])
            if not to_remove:
                break
            layer += 1
            for u in to_remove:
                core_num[u] = k
                onion_layer[u] = layer
                remaining.remove(u)
            for u in to_remove:
                for v in adj[u]:
                    if v in remaining:
                        cur_deg[v] -= 1

    return core_num, onion_layer


def compute_newman_assortativity(adj, edges):
    """
    Coeficiente de Asortatividad por Grado de Newman (2002):
    r = [ M^-1 sum_e (j_e * k_e) - (M^-1 sum_e 0.5*(j_e + k_e))^2 ] /
        [ M^-1 sum_e 0.5*(j_e^2 + k_e^2) - (M^-1 sum_e 0.5*(j_e + k_e))^2 ]
    """
    m = len(edges)
    if m == 0:
        return 0.0
    deg = {u: len(adj[u]) for u in adj}
    sum_jk = 0.0
    sum_j_plus_k = 0.0
    sum_j2_plus_k2 = 0.0
    for u, v in edges:
        j, k = float(deg[u]), float(deg[v])
        sum_jk += j * k
        sum_j_plus_k += 0.5 * (j + k)
        sum_j2_plus_k2 += 0.5 * (j * j + k * k)

    term1 = sum_jk / m
    term2 = (sum_j_plus_k / m) ** 2
    denom = (sum_j2_plus_k2 / m) - term2
    if abs(denom) < 1e-12:
        return 0.0
    return (term1 - term2) / denom


def compute_burt_constraint(nodes, adj):
    """
    Restricción Estructural de Ronald Burt (1992):
    C_i = sum_{j in N(i)} (p_{ij} + sum_{q in N(i), q != j} p_{iq} p_{qj})^2
    donde p_{ij} = A_{ij} / k_i.
    Menor C_i en nodos con grado >= 2 indica mayor acceso a "Agujeros Estructurales"
    (capacidad de intermediar entre actores desconectados entre sí).
    """
    constraint = {}
    for i in nodes:
        ni = adj[i]
        ki = len(ni)
        if ki == 0:
            constraint[i] = 1.0
            continue
        p_i = 1.0 / ki
        c_i = 0.0
        for j in ni:
            indirect = 0.0
            for q in ni:
                if q != j and j in adj[q]:
                    kq = len(adj[q])
                    if kq > 0:
                        indirect += p_i * (1.0 / kq)
            c_i += (p_i + indirect) ** 2
        constraint[i] = round(c_i, 4)
    return constraint


def generate_report():
    nodes, adj, edges = load_operational_graph()
    core_num, onion_layer = kcore_and_onion_decomposition(nodes, adj)
    r_assort = compute_newman_assortativity(adj, edges)
    burt_c = compute_burt_constraint(nodes, adj)

    max_k = max(core_num.values()) if core_num else 0
    max_layer = max(onion_layer.values()) if onion_layer else 0

    # Nodos en el núcleo profundo (k == max_k y mayores capas de cebolla)
    ranked_core = sorted(
        nodes.keys(),
        key=lambda u: (-core_num[u], -onion_layer[u], -len(adj[u]), u),
    )

    # Actores (Personas, Entidades, Partidos) con menor Restricción de Burt (Mayores Brokers de Agujeros Estructurales)
    actor_types = {"persona", "entidad_publica", "entidad_privada", "partido_politico"}
    structural_hole_brokers = sorted(
        [
            (u, burt_c[u], len(adj[u]), core_num[u], onion_layer[u])
            for u in nodes
            if nodes[u].get("tipo_nodo") in actor_types and len(adj[u]) >= 2
        ],
        key=lambda x: (x[1], -x[2], -x[4], x[0]),
    )

    regimen = (
        "Disasortativo (Arquitectura Hub-and-Spoke / Estrella: los grandes nodos articuladores operan a través de entidades instrumentales o testaferros periféricos)"
        if r_assort < 0
        else "Asortativo (Núcleo oligárquico densamente interconectado entre pares de alto grado)"
    )

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Descomposición k-Core, Capas de Cebolla, Asortatividad de Newman y Agujeros Estructurales de Burt"',
        "actualizacion_automatica: true",
        "tags:",
        "  - k-core",
        "  - asortatividad-newman",
        "  - agujeros-estructurales-burt",
        "  - analisis-forense",
        "---",
        "",
        "# 🧅 Núcleos $k$-Core, Asortatividad de Newman ($r$) y Agujeros Estructurales de Burt",
        "",
        "> [!NOTE] Topología Núcleo-Periferia y Arbitraje de Agujeros Estructurales",
        "> Esta vista implementa tres teoremas clásicos de la ciencia de redes criminales:",
        "> 1. **Descomposición $k$-Core y *Onion Layers* (Batagelj & Zaversnik)**: Pela iterativamente la periferia del grafo hasta aislar el **Núcleo Profundo ($k_{\\max}$)**.",
        "> 2. **Coeficiente de Asortatividad de Grado de Newman ($r \\in [-1, 1]$)**: Determina matemáticamente si la red es **disasortativa ($r < 0$)** —típico de células que compartimentan el riesgo mediante fundaciones u operadores satélite—.",
        "> 3. **Restricción Estructural de Ronald Burt ($C_i$)**: Identifica los actores que explotan **Agujeros Estructurales** (menor restricción $C_i$ implica mayor poder de corretaje e intermediación exclusiva entre grupos desconectados).",
        "",
        "## 1. Indicadores Estructurales Globales",
        "",
        f"- **Nodos Operativos Activos ($|V|$)**: `{len(nodes)}` | **Aristas No Dirigidas ($|E|$)**: `{len(edges)}`",
        f"- **Coeficiente de Asortatividad de Grado de Newman ($r$)**: **`{r_assort:.4f}`**",
        f"  - *Diagnóstico Topológico*: **{regimen}**",
        f"- **Degeneración / Coreness Máximo ($k_{{\\max}}$)**: `{max_k}-Core`",
        f"- **Profundidad Máxima de Pelado (*Onion Layers*)**: `{max_layer} capas`",
        "",
        "---",
        "",
        "## 2. Brokers de Agujeros Estructurales (Menor Restricción de Burt $C_i$)",
        "",
        "Actores institucionales, societarios y personales con grado $k_i \\ge 2$ ordenados por **menor Restricción de Burt ($C_i$)** (mayor capacidad de arbitraje entre clústeres sin redundancia):",
        "",
        "| Pos | Actor / Entidad | Tipo | Grado ($k_i$) | Restricción de Burt ($C_i$) | $k$-Core | Capa Cebolla |",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :---: |",
    ]

    for idx, (u, c_val, deg, kc, ol) in enumerate(structural_hole_brokers[:20], 1):
        tipo = nodes[u].get("tipo_nodo", "")
        lines.append(
            f"| **{idx}** | [[{u}]] | `{tipo}` | `{deg}` | **`{c_val:.4f}`** | `{kc}` | `Capa #{ol}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        f"## 3. Radiografía del Núcleo Profundo ($k$-Core = `{max_k}` y Capas Internas)",
        "",
        "| # | Nodo del Núcleo | Categoría | $k$-Core | Capa Cebolla (*Onion Layer*) | Grado ($k_i$) | Restricción $C_i$ |",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :---: |",
    ])

    for i, u in enumerate(ranked_core[:25], 1):
        tipo = nodes[u].get("tipo_nodo", "")
        lines.append(
            f"| **{i}** | [[{u}]] | `{tipo}` | **`{core_num[u]}`** | **`Capa #{onion_layer[u]}`** | `{len(adj[u])}` | `{burt_c[u]:.4f}` |"
        )

    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"[OK] Análisis k-Core, Asortatividad (r={r_assort:.4f}) y Burt generado: {REPORT_PATH.relative_to(VAULT_ROOT)} (k_max={max_k}, {max_layer} capas)"
    )


if __name__ == "__main__":
    generate_report()
