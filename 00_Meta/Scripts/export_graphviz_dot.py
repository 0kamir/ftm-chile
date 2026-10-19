#!/usr/bin/env python3
"""
Exportador a Formato Graphviz DOT (`export_graphviz_dot.py`).
Genera `05_Vistas_Analiticas/Exportaciones/red_ftm_chile.dot` con estilos cromáticos
por tipo de entidad, listo para compilar con `dot -Tsvg` o `dot -Tpdf`.
"""

import json
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
JSON_PATH = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json"
)
OUT_DOT = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "red_ftm_chile.dot"
)

STYLE_MAP = {
    "persona": ('shape=ellipse, style=filled, fillcolor="#1e40af", fontcolor="#ffffff"',),
    "entidad_publica": ('shape=box, style="filled,rounded", fillcolor="#15803d", fontcolor="#ffffff"',),
    "entidad_privada": ('shape=component, style=filled, fillcolor="#c2410c", fontcolor="#ffffff"',),
    "partido_politico": ('shape=hexagon, style=filled, fillcolor="#7e22ce", fontcolor="#ffffff"',),
    "nexo_transaccion": ('shape=diamond, style=filled, fillcolor="#b91c1c", fontcolor="#ffffff"',),
    "causa_judicial": ('shape=folder, style=filled, fillcolor="#a16207", fontcolor="#ffffff"',),
    "evidencia_documental": ('shape=note, style=filled, fillcolor="#475569", fontcolor="#ffffff"',),
    "tipo_penal": ('shape=octagon, style=filled, fillcolor="#9f1239", fontcolor="#ffffff"',),
}


def q(text: str) -> str:
    return '"' + str(text).replace('"', '\\"') + '"'


def main() -> int:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    lines = [
        "digraph RedCorrupcionChile {",
        '  graph [rankdir=LR, bgcolor="#0f172a", fontname="Helvetica", pad="0.4", nodesep="0.45", ranksep="0.9"];',
        '  node [fontname="Helvetica", fontsize=10];',
        '  edge [fontname="Helvetica", fontsize=8, color="#64748b", fontcolor="#cbd5e1"];',
        "",
    ]

    valid_nodes = set()
    for n in data["nodos"]:
        tipo = n["tipo_nodo"]
        if tipo in ("vista_analitica", "meta_taxonomia", "dossier"):
            continue
        valid_nodes.add(n["id"])
        style = STYLE_MAP.get(
            tipo, ('shape=box, style=filled, fillcolor="#334155", fontcolor="#ffffff"',)
        )[0]
        label = n["id"]
        if tipo == "nexo_transaccion" and n["monto_clp"] > 0:
            fmt = "$" + f"{n['monto_clp']:,}".replace(",", ".")
            label = f"{n['id']}\\n({fmt} CLP)"
        lines.append(f"  {q(n['id'])} [label={q(label)}, {style}];")

    lines.append("")
    for e in data["aristas"]:
        if e["source"] in valid_nodes and e["target"] in valid_nodes:
            lines.append(
                f"  {q(e['source'])} -> {q(e['target'])} [label={q(e['relation'])}];"
            )

    lines.append("}")

    with open(OUT_DOT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(
        f"[OK] Archivo Graphviz DOT generado: {os.path.relpath(OUT_DOT, ROOT_DIR)} ({len(valid_nodes)} nodos)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
