#!/usr/bin/env python3
"""
Simulador de Robustez Topológica y Fragmentación de Redes (`percolation_analysis.py`).
Implementa el protocolo de Borgatti (Key Player Problem / Targeted Percolation):
1. Construye la red de entidades, personas, partidos y transacciones reificadas.
2. Calcula iterativamente la Centralidad de Intermediación (Brandes) para elegir el nodo más crítico.
3. Simula la remoción secuencial de los Top-6 Nodos Puente y mide:
   - Número de Componentes Conexas (Islas desconectadas)
   - Tamaño de la Mayor Componente Conexa (LCC %)
4. Genera `05_Vistas_Analiticas/Robustez_de_la_Red.md` con gráfico `xychart-beta` de Mermaid.
"""

from collections import defaultdict, deque
import json
import os
from descargo import descargo  # noqa: E402

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
JSON_PATH = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json"
)
OUT_MD = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Robustez_de_la_Red.md"
)

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
}


def get_components(nodes_set: set[str], adj: dict[str, set[str]]) -> list[set[str]]:
    visited = set()
    comps = []
    for v in nodes_set:
        if v not in visited:
            comp = set()
            q = deque([v])
            visited.add(v)
            while q:
                curr = q.popleft()
                comp.add(curr)
                for nb in adj[curr]:
                    if nb in nodes_set and nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            comps.append(comp)
    return sorted(comps, key=len, reverse=True)


def compute_betweenness_subset(nodes_set: set[str], adj: dict[str, set[str]]) -> dict[str, float]:
    vertices = list(nodes_set)
    cb = {v: 0.0 for v in vertices}
    for s in vertices:
        stack = []
        pred = {w: [] for w in vertices}
        sigma = {t: 0.0 for t in vertices}
        sigma[s] = 1.0
        dist = {t: -1 for t in vertices}
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in adj[v]:
                if w not in nodes_set:
                    continue
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = {v: 0.0 for v in vertices}
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                cb[w] += delta[w]
    return cb


def main() -> int:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    node_meta = {
        n["id"]: n
        for n in data["nodos"]
        if n["tipo_nodo"] in OPERATIONAL_TYPES
    }
    active_nodes = set(node_meta.keys())
    adj = defaultdict(set)

    for e in data["aristas"]:
        u, v = e["source"], e["target"]
        if u in active_nodes and v in active_nodes and u != v:
            adj[u].add(v)
            adj[v].add(u)

    initial_total = len(active_nodes)
    steps = []

    for step_idx in range(7):
        comps = get_components(active_nodes, adj)
        lcc_size = len(comps[0]) if comps else 0
        lcc_pct = round((lcc_size / initial_total) * 100.0, 1) if initial_total else 0.0

        if step_idx == 0:
            steps.append(
                {
                    "step": 0,
                    "removed": "Estado Inicial (Sin remoción)",
                    "tipo": "—",
                    "num_comps": len(comps),
                    "lcc_size": lcc_size,
                    "lcc_pct": lcc_pct,
                }
            )
        else:
            steps[-1]["num_comps"] = len(comps)
            steps[-1]["lcc_size"] = lcc_size
            steps[-1]["lcc_pct"] = lcc_pct

        if step_idx == 6:
            break

        # Elegir siguiente actor (no-TRX) con mayor intermediación adaptativa
        cb = compute_betweenness_subset(active_nodes, adj)
        candidates = [
            (n, score)
            for n, score in cb.items()
            if node_meta[n]["tipo_nodo"] != "nexo_transaccion"
        ]
        candidates.sort(key=lambda x: x[1], reverse=True)
        target_node, _ = candidates[0]
        active_nodes.remove(target_node)

        steps.append(
            {
                "step": step_idx + 1,
                "removed": target_node,
                "tipo": node_meta[target_node]["tipo_nodo"],
                "num_comps": 0,
                "lcc_size": 0,
                "lcc_pct": 0.0,
            }
        )

    x_labels = ", ".join(f'"Paso {s["step"]}"' for s in steps)
    lcc_series = ", ".join(str(s["lcc_pct"]) for s in steps)
    comp_series = ", ".join(str(s["num_comps"] * 5) for s in steps)

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Simulación de Percolación y Fragmentación de Nodos Clave (Key Player Problem)"',
        "actualizacion_automatica: true",
        "tags:",
        "  - dashboard",
        "  - percolacion",
        "  - robustez-red",
        "---",
        "",
        "# Robustez de la Red ante la Eliminación de Nodos (*Key Player Problem*)",
        "",
        *descargo("robustez"),
        "",
        "Modelamiento topológico basado en el protocolo de **percolación dirigida adaptativa** (Borgatti, 2006): evalúa cómo se fragmenta la Componente Gigante (`LCC`) de la red al eliminar secuencialmente los actores con mayor centralidad de intermediación recalculada en cada paso.",
        "",
        "---",
        "",
        "## 1. Curva de Degradación de la Componente Gigante (`LCC %`)",
        "",
        "```mermaid",
        "xychart-beta",
        '  title "Caída del Tamaño de la Componente Gigante (LCC %) tras Remoción Dirigida"',
        f"  x-axis [{x_labels}]",
        '  y-axis "Porcentaje de la Red Conectada (%)" 0 --> 100',
        f"  line [{lcc_series}]",
        f"  bar [{lcc_series}]",
        "```",
        "",
        "---",
        "",
        "## 2. Secuencia de Eliminación de Nodos Puente",
        "",
        "| Paso ($k$) | Nodo Eliminado | Tipo de Actor | Islas Resultantes (Componentes) | Nodos en Mayor Componente (`LCC`) | Cohesión Residual (`LCC %`) |",
        "| :---: | :--- | :--- | :---: | :---: | ---: |",
    ]

    for s in steps:
        nodo_str = (
            f"[[{s['removed']}]]"
            if not s["removed"].startswith("Estado")
            else s["removed"]
        )
        lines.append(
            f"| **{s['step']}** | {nodo_str} | `{s['tipo']}` | **{s['num_comps']}** | {s['lcc_size']} de {initial_total} | **{s['lcc_pct']}%** |"
        )

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(
        f"[OK] Simulación de Percolación generada: {os.path.relpath(OUT_MD, ROOT_DIR)} "
        f"(LCC cae de {steps[0]['lcc_pct']}% a {steps[-1]['lcc_pct']}%)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
