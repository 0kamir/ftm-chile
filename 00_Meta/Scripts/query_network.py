#!/usr/bin/env python3
"""
Motor CLI de Consultas de Inteligencia de Redes (`query_network.py`).
Permite:
1. Encontrar el camino más corto (BFS) entre dos personas o entidades cualesquiera:
     python3 00_Meta/Scripts/query_network.py --shortest-path "Daniel Andrade Schwarze" "Camila Polizzi Fonceca"
2. Inspeccionar el perfil de un nodo y su vecindad a Profundidad 2:
     python3 00_Meta/Scripts/query_network.py --profile "Luis Hermosilla Osorio"
3. Ejecutar detector de Lobby Pre-Adjudicación (< 90 días):
     python3 00_Meta/Scripts/query_network.py --lobby-alerts
"""

import argparse
from collections import defaultdict, deque
from datetime import datetime
import json
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
JSON_PATH = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json"
)


def load_graph():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = {n["id"]: n for n in data["nodos"]}
    adj = defaultdict(list)
    for e in data["aristas"]:
        u, v, rel = e["source"], e["target"], e["relation"]
        if u in nodes and v in nodes:
            adj[u].append((v, f"--[{rel}]-->"))
            adj[v].append((u, f"<--[{rel}]--"))
    return nodes, adj


def shortest_path(nodes, adj, start: str, goal: str):
    if start == goal:
        return [(start, "")]
    visited = {start}
    queue = deque([[(start, "")]])
    while queue:
        path = queue.popleft()
        curr = path[-1][0]
        for nxt, rel in adj[curr]:
            nxt_type = nodes[nxt].get("tipo_nodo")
            if nxt != goal and nxt_type in ("causa_judicial", "tipo_penal", "evidencia_documental"):
                continue
            if nxt not in visited:
                new_path = path + [(nxt, rel)]
                if nxt == goal:
                    return new_path
                visited.add(nxt)
                queue.append(new_path)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Consultas sobre el Grafo Reificado.")
    parser.add_argument(
        "--shortest-path",
        nargs=2,
        metavar=("ORIGEN", "DESTINO"),
        help="Calcula la cadena relacional más corta entre dos entidades/personas.",
    )
    parser.add_argument(
        "--profile",
        metavar="NODO",
        help="Muestra el expediente y vecindad a Profundidad 2.",
    )
    args = parser.parse_args()

    nodes, adj = load_graph()

    if args.shortest_path:
        src, dst = args.shortest_path
        if src not in nodes or dst not in nodes:
            print(f"[X] Nodo no encontrado: {src!r} o {dst!r}")
            return 1
        path = shortest_path(nodes, adj, src, dst)
        if not path:
            print(f"Sin camino directo entre {src} y {dst}.")
            return 0
        print("=" * 72)
        print(f" CAMINO MÁS CORTO ({len(path) - 1} saltos): {src}  ===>  {dst}")
        print("=" * 72)
        for idx, (node_name, rel) in enumerate(path):
            n_info = nodes[node_name]
            if idx == 0:
                print(f"  [0] {node_name} ({n_info['tipo_nodo']})")
            else:
                print(f"   │   {rel}")
                print(f"  [{idx}] {node_name} ({n_info['tipo_nodo']})")
        print("=" * 72)

    if args.profile:
        target = args.profile
        if target not in nodes:
            print(f"[X] Nodo no encontrado: {target!r}")
            return 1
        n = nodes[target]
        print("=" * 72)
        print(f" FICHA: {n['id']}")
        print("=" * 72)
        print(f" Tipo de Nodo       : {n['tipo_nodo']}")
        print(f" RUT / RUC          : {n['rut'] or 'N/A'}")
        print(f" Flujo Emitido CLP  : ${n['flujo_emitido_clp']:,.0f} CLP".replace(",", "."))
        print(f" Flujo Recibido CLP : ${n['flujo_recibido_clp']:,.0f} CLP".replace(",", "."))
        hop1 = {nb for nb, _ in adj[target]}
        hop2 = set()
        for h1 in hop1:
            for nb2, _ in adj[h1]:
                if nb2 != target and nb2 not in hop1:
                    hop2.add(nb2)
        print(f" Vecindad Prof. 1   : {', '.join(sorted(hop1))}")
        print(f" Vecindad Prof. 2   : {', '.join(sorted(hop2))}")
        print("=" * 72)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
