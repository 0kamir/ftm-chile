#!/usr/bin/env python3
"""
Motor de Predicción de Vínculos Ocultos y Homofilia Estructural (`link_prediction.py`).
Implementa los estimadores topológicos de Liben-Nowell & Kleinberg:
1. Índice de Adamic-Adar: AA(u, v) = sum_{w in N(u) n N(v)} 1 / ln(|N(w)|)
2. Coeficiente de Jaccard: J(u, v) = |N(u) n N(v)| / |N(u) u N(v)|

Evalúa pares de actores (Personas, Órganos Públicos, Entidades Privadas) que NO tienen una arista
directa pero comparten vecinos operativos (partidos, transacciones intermedias, órganos o contrapartes),
generando `05_Vistas_Analiticas/Prediccion_Vinculos_Ocultos.md`.
"""

from collections import defaultdict
import json
import math
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
JSON_PATH = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json"
)
OUT_MD = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Prediccion_Vinculos_Ocultos.md"
)

ACTOR_TYPES = {"persona", "entidad_publica", "entidad_privada"}
CONTEXT_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
}


def main() -> int:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = {
        n["id"]: n for n in data["nodos"] if n["tipo_nodo"] in CONTEXT_TYPES
    }
    adj = defaultdict(set)

    for e in data["aristas"]:
        u, v = e["source"], e["target"]
        if u in nodes and v in nodes and u != v:
            adj[u].add(v)
            adj[v].add(u)

    # Expandir vecindad a 2 saltos cuando el intermediario es un nodo TRX (colapso de arista reificada)
    effective_neighbors = defaultdict(set)
    for u in nodes:
        for nb in adj[u]:
            effective_neighbors[u].add(nb)
            if nodes[nb]["tipo_nodo"] == "nexo_transaccion":
                for nb2 in adj[nb]:
                    if nb2 != u:
                        effective_neighbors[u].add(nb2)

    actors = sorted(n_id for n_id, info in nodes.items() if info["tipo_nodo"] in ACTOR_TYPES)
    predictions = []

    for i in range(len(actors)):
        for j in range(i + 1, len(actors)):
            u, v = actors[i], actors[j]
            if v in adj[u]:
                continue  # Ya tienen enlace directo en YAML

            nu = effective_neighbors[u]
            nv = effective_neighbors[v]
            common = nu.intersection(nv)
            if not common:
                continue

            union_len = len(nu.union(nv))
            jaccard = round(len(common) / union_len, 4) if union_len else 0.0

            aa_score = 0.0
            for w in common:
                deg_w = len(effective_neighbors[w])
                if deg_w > 1:
                    aa_score += 1.0 / math.log(deg_w)
                else:
                    aa_score += 1.0
            aa_score = round(aa_score, 4)

            predictions.append(
                {
                    "u": u,
                    "u_type": nodes[u]["tipo_nodo"],
                    "v": v,
                    "v_type": nodes[v]["tipo_nodo"],
                    "common": sorted(common),
                    "aa": aa_score,
                    "jaccard": jaccard,
                }
            )

    predictions.sort(key=lambda x: (x["aa"], x["jaccard"], len(x["common"])), reverse=True)
    top_preds = predictions[:15]

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Predicción de Vínculos Ocultos (Índices Adamic-Adar y Jaccard)"',
        "actualizacion_automatica: true",
        "tags:",
        "  - dashboard",
        "  - link-prediction",
        "  - adamic-adar",
        "---",
        "",
        "# Predicción Forense de Vínculos Ocultos (*Link Prediction*)",
        "",
        "Aplicación de los algoritmos **Adamic-Adar ($AA$)** y **Coeficiente de Jaccard ($J$)** (Liben-Nowell & Kleinberg) sobre el grafo operativo para identificar pares de actores (`Persona`, `Entidad Pública`, `Entidad Privada`) que no poseen un enlace directo en su ficha, pero comparten intermediarios, partidos políticos o transacciones puente:",
        "",
        "$$AA(u, v) = \\sum_{w \\in \\Gamma(u) \\cap \\Gamma(v)} \\frac{1}{\\ln |\\Gamma(w)|}$$",
        "",
        "---",
        "",
        "## Top 15 Hipótesis de Asociación Estructural / Co-Operación Indirecta",
        "",
        "| Ranking | Actor A | Actor B | Índice Adamic-ar ($AA$) | Similitud Jaccard ($J$) | Nodos Puente / Vecinos Comunes ($\\Gamma(u) \\cap \\Gamma(v)$) |",
        "| :---: | :--- | :--- | ---: | ---: | :--- |",
    ]

    for idx, p in enumerate(top_preds, 1):
        comunes = ", ".join(f"[[{c}]]" for c in p["common"])
        lines.append(
            f"| **{idx}** | [[{p['u']}]] (`{p['u_type']}`) | [[{p['v']}]] (`{p['v_type']}`) | **`{p['aa']:.4f}`** | `{p['jaccard']:.4f}` | {comunes} |"
        )

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(
        f"[OK] Predicción de Vínculos Ocultos generada: {os.path.relpath(OUT_MD, ROOT_DIR)} "
        f"({len(predictions)} pares candidatos evaluados)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
