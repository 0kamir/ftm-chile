#!/usr/bin/env python3
"""
Analizador de Redes y Exportador GraphML / JSON (Compatible con Gephi y Cytoscape).
Construye el grafo bipartito/reificado completo desde el vault de Obsidian, calcula métricas de
centralidad (Grado, Flujo Financiero de Entrada/Salida, Intermediación) y exporta:
  - 05_Vistas_Analiticas/Exportaciones/red_corrupcion_chile.graphml
  - 05_Vistas_Analiticas/Exportaciones/metricas_red.json
"""

import json
import os
import re
import xml.etree.ElementTree as ET
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXPORT_DIR = os.path.join(ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones")


def extract_wikilinks(value) -> list[str]:
    if value is None:
        return []
    return [
        m.strip()
        for m in re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(value))
        if m.strip()
    ]


def main() -> int:
    os.makedirs(EXPORT_DIR, exist_ok=True)
    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        # 06_Anexos queda fuera del grafo y de los análisis (menciones documentales sin imputación).
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "06_Anexos"]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(full_path, ROOT_DIR)
            if rel_path == "README.md" or rel_path.startswith("00_Meta/Plantillas/"):
                continue

            node_id = os.path.splitext(fname)[0]
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()

            m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
            if not m:
                continue
            meta = yaml.safe_load(m.group(1)) or {}
            tipo_nodo = str(meta.get("tipo_nodo", "desconocido"))

            nodes[node_id] = {
                "id": node_id,
                "tipo_nodo": tipo_nodo,
                "rut": str(meta.get("rut", meta.get("ruc", ""))),
                "monto_clp": int(meta.get("monto_clp", 0) or 0),
                "path": rel_path,
                "in_degree": 0,
                "out_degree": 0,
                "flujo_emitido_clp": 0,
                "flujo_recibido_clp": 0,
                "estado_verificacion": str(meta.get("estado_verificacion") or ""),
                "monto_origen": str(meta.get("monto_origen") or ""),
                "situacion_procesal": str(meta.get("situacion_procesal") or ""),
                # Fuentes con URL http(s), para que el visor web las muestre como enlaces.
                "fuentes": [
                    {k: str(fu.get(k) or "") for k in ("url", "titulo", "medio", "tipo", "fecha")}
                    for fu in (meta.get("fuentes") or [])
                    if isinstance(fu, dict) and str(fu.get("url", "")).startswith(("http://", "https://"))
                ],
            }

            for prop, val in meta.items():
                for target in extract_wikilinks(val):
                    edges.append(
                        {
                            "source": node_id,
                            "target": target,
                            "relation": prop,
                            "weight": int(meta.get("monto_clp", 0) or 0)
                            if tipo_nodo == "nexo_transaccion"
                            else 1,
                        }
                    )

    # Calcular métricas de grado y flujo financiero por nodo
    for e in edges:
        src = e["source"]
        dst = e["target"]
        if src in nodes:
            nodes[src]["out_degree"] += 1
        if dst in nodes:
            nodes[dst]["in_degree"] += 1

        # Si el nodo origen es una arista reificada TRX, atribuir montos a entidades y firmantes
        if src in nodes and nodes[src]["tipo_nodo"] == "nexo_transaccion":
            monto = nodes[src]["monto_clp"]
            if e["relation"] in ("entidad_origen", "firmante_origen") and dst in nodes:
                nodes[dst]["flujo_emitido_clp"] += monto
            elif e["relation"] in ("entidad_destino", "firmante_destino") and dst in nodes:
                nodes[dst]["flujo_recibido_clp"] += monto

    # Exportar JSON de métricas
    ranking = sorted(
        nodes.values(),
        key=lambda n: (n["in_degree"] + n["out_degree"], n["flujo_emitido_clp"] + n["flujo_recibido_clp"]),
        reverse=True,
    )
    json_path = os.path.join(EXPORT_DIR, "metricas_red.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "resumen": {
                    "total_nodos": len(nodes),
                    "total_aristas": len(edges),
                    "monto_total_clp": sum(
                        n["monto_clp"] for n in nodes.values() if n["tipo_nodo"] == "nexo_transaccion"
                    ),
                },
                "nodos": ranking,
                "aristas": edges,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    # Exportar GraphML estándar para Gephi / Cytoscape
    graphml = ET.Element(
        "graphml",
        xmlns="http://graphml.graphdrawing.org/xmlns",
    )
    attrs = [
        ("d0", "node", "tipo_nodo", "string"),
        ("d1", "node", "rut", "string"),
        ("d2", "node", "monto_clp", "long"),
        ("d3", "node", "flujo_emitido_clp", "long"),
        ("d4", "node", "flujo_recibido_clp", "long"),
        ("d5", "edge", "relation", "string"),
        ("d6", "edge", "weight", "long"),
    ]
    for kid, kfor, kname, ktype in attrs:
        ET.SubElement(
            graphml,
            "key",
            id=kid,
            **{"for": kfor, "attr.name": kname, "attr.type": ktype},
        )

    graph_el = ET.SubElement(graphml, "graph", id="G", edgedefault="directed")
    for nid, ninfo in nodes.items():
        n_el = ET.SubElement(graph_el, "node", id=nid)
        for kid, key_name in [
            ("d0", "tipo_nodo"),
            ("d1", "rut"),
            ("d2", "monto_clp"),
            ("d3", "flujo_emitido_clp"),
            ("d4", "flujo_recibido_clp"),
        ]:
            d_el = ET.SubElement(n_el, "data", key=kid)
            d_el.text = str(ninfo[key_name])

    for idx, edge in enumerate(edges):
        e_el = ET.SubElement(
            graph_el,
            "edge",
            id=f"e{idx}",
            source=edge["source"],
            target=edge["target"],
        )
        d_rel = ET.SubElement(e_el, "data", key="d5")
        d_rel.text = edge["relation"]
        d_w = ET.SubElement(e_el, "data", key="d6")
        d_w.text = str(edge["weight"])

    graphml_path = os.path.join(EXPORT_DIR, "red_corrupcion_chile.graphml")
    tree = ET.ElementTree(graphml)
    ET.indent(tree, space="  ")
    tree.write(graphml_path, encoding="utf-8", xml_declaration=True)

    print(f"[OK] Grafo exportado a GraphML : {os.path.relpath(graphml_path, ROOT_DIR)}")
    print(f"[OK] Métricas exportadas a JSON: {os.path.relpath(json_path, ROOT_DIR)}")
    print(f"     Nodos: {len(nodes)} | Aristas dirigidas: {len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
