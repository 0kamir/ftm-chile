#!/usr/bin/env python3
"""
Motor de Teoría Espectral de Grafos, Conectividad Algebraica de Fiedler y Bisección Espectral
=============================================================================================
Resuelve de manera exacta (algoritmo cíclico de rotaciones de Jacobi en Python puro)
el espectro de la Matriz de Adyacencia A y de la Matriz Laplaciana Combinatoria L = D - A
sobre el Componente Gigante Conectado (LCC) de la red operativa criminal/política:

1. Conectividad Algebraica de Fiedler (lambda_2 de L) y cotas isoperimétricas de Cheeger.
2. Vector de Fiedler (v_2) para Bisección Espectral en 2 Hemisferios Macro-Estructurales
   e identificación de la Línea de Falla Espectral (nodos con v_2(i) cercano a 0).
3. Radio Espectral de Adyacencia (rho(A) = mu_max), Centralidad de Autovector (Eigenvector Centrality)
   y Umbral Epidémico / Contagio Institucional (tau_c = 1 / rho(A)).

Genera `05_Vistas_Analiticas/Analisis_Espectral_y_Fiedler.md`.
"""

from collections import defaultdict, deque
import json
import math
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Exportaciones" / "metricas_red.json"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Analisis_Espectral_y_Fiedler.md"

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
    "causa_judicial",
}


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

    # Extraer el Componente Gigante Conectado (LCC)
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
    return best_comp, lcc_adj, nodes


def jacobi_eigen_symmetric(mat, max_sweeps=80, tol=1e-11):
    """
    Algoritmo clásico de rotaciones de Jacobi para matriz real simétrica N x N.
    Retorna (eigenvalues_sorted, eigenvectors_columns_sorted).
    """
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
                t = (1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)))
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
    lcc_nodes, lcc_adj, all_nodes = load_lcc_graph()
    n = len(lcc_nodes)
    idx_map = {u: i for i, u in enumerate(lcc_nodes)}

    # Construir Matriz de Adyacencia A y Laplaciana L = D - A
    A = [[0.0] * n for _ in range(n)]
    L = [[0.0] * n for _ in range(n)]
    for u, nbrs in lcc_adj.items():
        i = idx_map[u]
        L[i][i] = float(len(nbrs))
        for v in nbrs:
            j = idx_map[v]
            A[i][j] = 1.0
            L[i][j] = -1.0

    lap_vals, lap_vecs = jacobi_eigen_symmetric(L)
    adj_vals, adj_vecs = jacobi_eigen_symmetric(A)

    lambda_2 = lap_vals[1] if n > 1 else 0.0
    lambda_max = lap_vals[-1] if n > 0 else 0.0
    fiedler_vec = lap_vecs[1] if n > 1 else [0.0] * n

    # Orientar el vector de Fiedler de forma canónica (para que el primer nodo tenga signo consistente)
    if fiedler_vec and sum(1 for x in fiedler_vec if x > 0) < sum(1 for x in fiedler_vec if x < 0):
        fiedler_vec = [-x for x in fiedler_vec]

    rho_adj = adj_vals[-1] if n > 0 else 0.0
    dom_adj_vec = adj_vecs[-1] if n > 0 else [0.0] * n
    # Garantizar componentes positivas por teorema de Perron-Frobenius
    if sum(dom_adj_vec) < 0:
        dom_adj_vec = [-x for x in dom_adj_vec]
    eig_cent = {lcc_nodes[i]: abs(dom_adj_vec[i]) for i in range(n)}

    d_max = max(len(lcc_adj[u]) for u in lcc_nodes) if lcc_nodes else 1
    cheeger_lower = lambda_2 / 2.0
    cheeger_upper = math.sqrt(2.0 * d_max * max(lambda_2, 0.0))
    epidemic_threshold = (1.0 / rho_adj) if rho_adj > 0 else 0.0

    # Calcular el corte de Cheeger empírico inducido por el signo del Vector de Fiedler
    hemisphere_pos = [lcc_nodes[i] for i in range(n) if fiedler_vec[i] >= 0.0]
    hemisphere_neg = [lcc_nodes[i] for i in range(n) if fiedler_vec[i] < 0.0]
    pos_set = set(hemisphere_pos)

    cut_edges = []
    for u in hemisphere_pos:
        for v in lcc_adj[u]:
            if v not in pos_set:
                cut_edges.append((u, v))

    # Nodos en la Línea de Falla Espectral (menor |v_2(i)|)
    fault_line_nodes = sorted(
        [(lcc_nodes[i], fiedler_vec[i], eig_cent[lcc_nodes[i]], len(lcc_adj[lcc_nodes[i]])) for i in range(n)],
        key=lambda x: (abs(x[1]), -x[3], x[0]),
    )

    # Top por Centralidad de Autovector (Perron-Frobenius)
    top_eigenvector = sorted(
        [(lcc_nodes[i], eig_cent[lcc_nodes[i]], fiedler_vec[i], len(lcc_adj[lcc_nodes[i]])) for i in range(n)],
        key=lambda x: (-x[1], -x[3], x[0]),
    )

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Análisis Espectral Laplaciano, Valor de Fiedler y Centralidad de Perron-Frobenius"',
        "actualizacion_automatica: true",
        "tags:",
        "  - teoria-espectral",
        "  - fiedler-laplaciano",
        "  - perron-frobenius",
        "  - analisis-forense",
        "---",
        "",
        "# 🌈 Teoría Espectral de Grafos: Conectividad de Fiedler ($\\lambda_2$) y Bisección Laplaciana",
        "",
        "> [!IMPORTANT] Álgebra Lineal Espectral sobre el Componente Gigante Conectado (LCC)",
        "> Esta vista diagonaliza de forma exacta (rotaciones simétricas de Jacobi) la **Matriz Laplaciana Combinatoria ($L = D - A$)** y la **Matriz de Adyacencia ($A$)** sobre el Componente Gigante Conectado de la red operativa:",
        "> 1. **Conectividad Algebraica de Fiedler ($\\lambda_2$)**: Mide la robustez estructural frente a la escisión de la red (Desigualdad de Cheeger: $\\frac{\\lambda_2}{2} \\le h(G) \\le \\sqrt{2 d_{\\max} \\lambda_2}$).",
        "> 2. **Bisección Espectral por Vector de Fiedler ($v_2$)**: Divide el LCC en dos hemisferios polares ($v_2(i) \\ge 0$ vs. $v_2(i) < 0$) y localiza la **Línea de Falla Espectral ($v_2(i) \\approx 0$)** donde convergen los aparatos partidarios/tributarios y los aparatos regionales/municipales.",
        "> 3. **Autovector Principal de Perron-Frobenius ($\\rho(A)$)**: Cuantifica la influencia recursiva y el umbral de contagio institucional ($\\tau_c = 1/\\rho(A)$).",
        "",
        "## 1. Invariantes Espectrales del Componente Gigante (LCC)",
        "",
        f"- **Dimensión del Subespacio Conectado ($N_{{\\text{{LCC}}}}$)**: `{n}` nodos operativos",
        f"- **Conectividad Algebraica de Fiedler ($\\lambda_2$)**: **`{lambda_2:.6f}`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*",
        f"- **Mayor Autovalor Laplaciano ($\\lambda_{{\\max}}$)**: `{lambda_max:.4f}` | **Razón Espectral ($\\lambda_{{\\max}} / \\lambda_2$)**: `{lambda_max / max(lambda_2, 1e-12):.2f}`",
        f"- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[{cheeger_lower:.4f}, {cheeger_upper:.4f}]`",
        f"- **Radio Espectral de Adyacencia ($\\rho(A) = \\mu_{{\\max}}$)**: **`{rho_adj:.4f}`**",
        f"- **Umbral Crítico de Difusión / Contagio Institucional ($\\tau_c = 1/\\rho(A)$)**: **`{epidemic_threshold:.4f}`**",
        f"- **Partición de Hemisferios de Fiedler**:",
        f"  - **Hemisferio Positivo ($v_2(i) \\ge 0$)**: `{len(hemisphere_pos)}` nodos",
        f"  - **Hemisferio Negativo ($v_2(i) < 0$)**: `{len(hemisphere_neg)}` nodos",
        f"  - **Aristas en el Corte Espectral de Fiedler**: `{len(cut_edges)}` enlaces inter-hemisféricos",
        "",
        "---",
        "",
        "## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \\approx 0$)",
        "",
        "Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:",
        "",
        "| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |",
        "| :---: | :--- | :--- | :---: | :---: | :---: |",
    ]

    for idx, (u, f_val, e_val, deg) in enumerate(fault_line_nodes[:15], 1):
        tipo = all_nodes[u].get("tipo_nodo", "")
        lines.append(
            f"| **{idx}** | [[{u}]] | `{tipo}` | **`{f_val:+.5f}`** | `{e_val:.4f}` | `{deg}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \\ge 0 \\leftrightarrow v_2(v) < 0$)",
        "",
        "| # | Nodo Hemisferio Positivo ($v_2 \\ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |",
        "| :---: | :--- | :---: | :--- | :---: |",
    ])

    for i, (u, v) in enumerate(cut_edges, 1):
        fu = fiedler_vec[idx_map[u]]
        fv = fiedler_vec[idx_map[v]]
        lines.append(
            f"| **{i}** | [[{u}]] | `{fu:+.5f}` | [[{v}]] | `{fv:+.5f}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \\rho(A) x$)",
        "",
        "| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |",
        "| :---: | :--- | :--- | :---: | :---: | :---: |",
    ])

    for idx, (u, e_val, f_val, deg) in enumerate(top_eigenvector[:20], 1):
        tipo = all_nodes[u].get("tipo_nodo", "")
        lines.append(
            f"| **{idx}** | [[{u}]] | `{tipo}` | **`{e_val:.4f}`** | `{f_val:+.5f}` | `{deg}` |"
        )

    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"[OK] Análisis Espectral y Fiedler generado: {REPORT_PATH.relative_to(VAULT_ROOT)} (lambda_2={lambda_2:.5f}, rho(A)={rho_adj:.4f}, corte={len(cut_edges)} aristas)"
    )


if __name__ == "__main__":
    generate_report()
