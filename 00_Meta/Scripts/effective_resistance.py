#!/usr/bin/env python3
"""
Motor de Resistencia Efectiva de Kirchhoff, Pseudoinversa de Moore-Penrose L+ y Tiempos de Impacto (Tetali)
===========================================================================================================
Modela el Componente Gigante Conectado (LCC) de la red como una Red Eléctrica
de Resistores de 1 Ohm y como una Cadena de Markov Ergódica (Random Walk):

1. Pseudoinversa de Moore-Penrose de la Laplaciana: L^+ = sum_{k=2}^N (1 / lambda_k) v_k v_k^T.
2. Distancia de Resistencia Efectiva de Klein-Randić: Omega_{uv} = L^+_{uu} + L^+_{vv} - 2 L^+_{uv}.
3. Índice Total de Kirchhoff: Kf(G) = N * sum_{k=2}^N (1 / lambda_k).
4. Centralidad de Cercanía por Flujo de Corriente (Current-Flow Closeness / Information Centrality):
   C_CF(u) = (N - 1) / sum_{v != u} Omega_{uv}.
5. Tiempo Medio de Primer Impacto de Caminata Aleatoria (Exact Identity de Tetali 1991):
   H_{uv} = 0.5 * sum_{w in V} d_w * (Omega_{uv} + Omega_{vw} - Omega_{uw})
   y Constante de Kemeny K(G) = sum_v pi_v H_{uv}.

Genera `05_Vistas_Analiticas/Resistencia_Efectiva_y_Tiempos_de_Impacto.md`.
"""

from collections import defaultdict, deque
import json
import math
from pathlib import Path
from descargo import descargo  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Exportaciones" / "metricas_red.json"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Resistencia_Efectiva_y_Tiempos_de_Impacto.md"

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
    "causa_judicial",
}

ACTOR_TYPES = {"persona", "entidad_publica", "entidad_privada", "partido_politico"}


def load_lcc_graph():
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

    visited = set()
    best_comp = []
    for u in sorted(nodes.keys()):
        if u not in visited and len(adj[u]) > 0:
            comp = []
            q = deque([u])
            visited.add(u)
            while q:
                cur = q.popleft()
                comp.append(cur)
                for nxt in sorted(adj[cur]):
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            if len(comp) > len(best_comp):
                best_comp = sorted(comp)

    lcc_set = set(best_comp)
    lcc_adj = {u: sorted(v for v in adj[u] if v in lcc_set) for u in best_comp}
    active_total = sum(1 for u in nodes if len(adj[u]) > 0)
    return best_comp, lcc_adj, nodes, active_total


def jacobi_eigen_symmetric(mat, max_sweeps=60, tol=1e-10):
    n = len(mat)
    a = [[float(mat[i][j]) for j in range(n)] for i in range(n)]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for _ in range(max_sweeps):
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_off:
                    max_off = abs(a[i][j])
        if max_off < tol:
            break

        for p in range(n):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < tol:
                    continue
                app = a[p][p]
                aqq = a[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = 1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau))
                if tau < 0:
                    t = -t
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c

                a[p][p] = app - t * apq
                a[q][q] = aqq + t * apq
                a[p][q] = 0.0
                a[q][p] = 0.0

                for r in range(n):
                    if r != p and r != q:
                        arp = a[r][p]
                        arq = a[r][q]
                        a[r][p] = c * arp - s * arq
                        a[p][r] = a[r][p]
                        a[r][q] = s * arp + c * arq
                        a[q][r] = a[r][q]

                for r in range(n):
                    vrp = v[r][p]
                    vrq = v[r][q]
                    v[r][p] = c * vrp - s * vrq
                    v[r][q] = s * vrp + c * vrq

    eigvals = [a[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda idx: eigvals[idx])
    sorted_vals = [eigvals[i] for i in order]
    sorted_vecs = [[v[row][i] for row in range(n)] for i in order]
    return sorted_vals, sorted_vecs


def generate_report():
    lcc_nodes, lcc_adj, all_nodes, active_total = load_lcc_graph()
    n = len(lcc_nodes)
    idx_map = {u: i for i, u in enumerate(lcc_nodes)}

    L = [[0.0] * n for _ in range(n)]
    deg = [0] * n
    for u, nbrs in lcc_adj.items():
        i = idx_map[u]
        deg[i] = len(nbrs)
        L[i][i] = float(len(nbrs))
        for v in nbrs:
            j = idx_map[v]
            L[i][j] = -1.0

    eigvals, eigvecs = jacobi_eigen_symmetric(L)

    # Pseudoinversa de Moore-Penrose L^+ = sum_{k: lambda_k > 1e-7} (1 / lambda_k) v_k v_k^T
    L_pinv = [[0.0] * n for _ in range(n)]
    trace_pinv = 0.0
    for k in range(n):
        lam = eigvals[k]
        if lam > 1e-7:
            inv_lam = 1.0 / lam
            trace_pinv += inv_lam
            vec = eigvecs[k]
            for i in range(n):
                vi = vec[i] * inv_lam
                for j in range(i, n):
                    val = vi * vec[j]
                    L_pinv[i][j] += val
                    if i != j:
                        L_pinv[j][i] += val

    kirchhoff_index = n * trace_pinv
    avg_resistance = (2.0 * kirchhoff_index) / (n * (n - 1)) if n > 1 else 0.0

    # Matriz de Resistencias Efectivas Omega_{ij}
    omega = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r_ij = L_pinv[i][i] + L_pinv[j][j] - 2.0 * L_pinv[i][j]
            omega[i][j] = max(0.0, r_ij)
            omega[j][i] = omega[i][j]

    # Current-Flow Closeness Centrality C_CF(i)
    cf_closeness = {}
    for i, u in enumerate(lcc_nodes):
        tot_r = sum(omega[i][j] for j in range(n) if j != i)
        cf_closeness[u] = ((n - 1) / tot_r) if tot_r > 0 else 0.0

    # Identidad de Tetali (1991) para Tiempos de Primer Impacto H_{ij} y Constante de Kemeny
    m2 = float(sum(deg))
    # phi_i = sum_w d_w * Omega_{iw}
    phi = [sum(deg[w] * omega[i][w] for w in range(n)) for i in range(n)]
    # H_{ij} = 0.5 * (m2 * Omega_{ij} + phi[j] - phi[i])
    hitting_time = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                hitting_time[i][j] = 0.5 * (m2 * omega[i][j] + phi[j] - phi[i])

    # Constante de Kemeny K(G) = sum_j (d_j / 2m) H_{ij} (independiente de i)
    kemeny_constant = sum((deg[j] / m2) * hitting_time[0][j] for j in range(n)) if m2 > 0 else 0.0

    # Ranking de Centralidad por Flujo Eléctrico (Information Centrality)
    ranked_cf = sorted(
        [(u, cf_closeness[u], L_pinv[idx_map[u]][idx_map[u]], deg[idx_map[u]]) for u in lcc_nodes],
        key=lambda x: (-x[1], -x[3], x[0]),
    )

    # Pares de Actores NO conectados directamente con MENOR Resistencia Efectiva (Conductos Multi-Ruta de Alta Conductancia)
    actor_indices = [i for i, u in enumerate(lcc_nodes) if all_nodes[u].get("tipo_nodo") in ACTOR_TYPES]
    low_resistance_pairs = []
    for a_idx in range(len(actor_indices)):
        i = actor_indices[a_idx]
        u = lcc_nodes[i]
        for b_idx in range(a_idx + 1, len(actor_indices)):
            j = actor_indices[b_idx]
            v = lcc_nodes[j]
            if v not in lcc_adj[u]:
                low_resistance_pairs.append((
                    u,
                    v,
                    omega[i][j],
                    1.0 / omega[i][j] if omega[i][j] > 0 else 0.0,
                    hitting_time[i][j] + hitting_time[j][i],
                ))
    low_resistance_pairs.sort(key=lambda x: (x[2], x[4], x[0], x[1]))

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Resistencia Efectiva de Kirchhoff, Pseudoinversa L+ y Tiempos de Impacto de Markov"',
        "actualizacion_automatica: true",
        "tags:",
        "  - resistencia-efectiva",
        "  - indice-kirchhoff",
        "  - moore-penrose",
        "  - constante-kemeny",
        "---",
        "",
        "# Resistencia Efectiva de Kirchhoff ($\\Omega_{uv}$), Pseudoinversa $L^+$ y Tiempos de Impacto ($H_{uv}$)",
        "",
        *descargo(),
        "",
        "> [!IMPORTANT] Redes Eléctricas de Kirchhoff y Cadenas de Markov sobre Grafos",
        "> A diferencia de la distancia geodésica más corta (que ignora caminos alternativos), la **Distancia de Resistencia Efectiva de Klein & Randić ($\\Omega_{uv} = L^+_{uu} + L^+_{vv} - 2L^+_{uv}$)** modela cada vínculo como un resistor de $1\\,\\Omega$ y pondera simultáneamente **todos los caminos paralelos** entre dos sujetos:",
        "> 1. **Centralidad por Flujo de Corriente ($C_{\\text{CF}}(u)$)**: Identifica los nodos con menor impedancia global hacia el resto del aparato criminal/institucional.",
        "> 2. **Tiempo de Conmutación e Impacto de Tetali ($H_{uv} + H_{vu}$)** y **Constante de Kemeny ($K(G)$)**: Miden el número esperado de pasos de una auditoría o contagio estocástico para transitar entre dos actores cualesquiera.",
        "",
        "## 1. Invariantes Eléctricos y Estocásticos del Grafo",
        "",
        f"- **Cobertura del Componente Gigante Conectado (LCC)**: **`{n} / {active_total}` nodos (`{n / active_total * 100:.1f}%`)**",
        f"- **Índice Total de Kirchhoff ($Kf(G) = N \\operatorname{{Tr}}(L^+)$)**: **`{kirchhoff_index:.2f} Ω`**",
        f"- **Resistencia Efectiva Promedio entre Pares ($\\bar{{\\Omega}}$)**: **`{avg_resistance:.4f} Ω`**",
        f"- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`{kemeny_constant:.2f} pasos`**",
        "",
        "---",
        "",
        "## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\\text{CF}}(u)$ — Menor Impedancia Global)",
        "",
        "| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |",
        "| :---: | :--- | :--- | :---: | :---: | :---: |",
    ]

    for idx, (u, c_cf, l_uu, d_u) in enumerate(ranked_cf[:20], 1):
        tipo = all_nodes[u].get("tipo_nodo", "")
        lines.append(
            f"| **{idx}** | [[{u}]] | `{tipo}` | **`{c_cf:.4f}`** | `{l_uu:.4f}` | `{d_u}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)",
        "",
        "Pares de actores sin arista directa cuya **Resistencia Efectiva ($\\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:",
        "",
        "| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\\Omega_{uv}$) | Conductancia ($\\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |",
        "| :---: | :--- | :--- | :---: | :---: | :---: |",
    ])

    for i, (u, v, r_uv, cond, comm_t) in enumerate(low_resistance_pairs[:20], 1):
        lines.append(
            f"| **{i}** | [[{u}]] | [[{v}]] | **`{r_uv:.4f} Ω`** | `{cond:.4f} S` | `{comm_t:.1f} pasos` |"
        )

    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"[OK] Resistencia Efectiva y Tiempos de Impacto generados: {REPORT_PATH.relative_to(VAULT_ROOT)} (LCC={n}/{active_total} [{n / active_total * 100:.1f}%], Kf={kirchhoff_index:.1f}, Kemeny={kemeny_constant:.1f})"
    )


if __name__ == "__main__":
    generate_report()
