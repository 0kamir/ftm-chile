#!/usr/bin/env python3
"""
Analizador de Redes y Exportador GraphML / JSON (Compatible con Gephi y Cytoscape).
Construye el grafo bipartito/reificado completo desde el vault de Obsidian, calcula métricas de
centralidad (Grado, Flujo Financiero de Entrada/Salida, Intermediación) y exporta:
  - 05_Vistas_Analiticas/Exportaciones/red_ftm_chile.graphml
  - 05_Vistas_Analiticas/Exportaciones/metricas_red.json
"""

import json
import os
import re
import xml.etree.ElementTree as ET
import yaml

import add_source

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXPORT_DIR = os.path.join(ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones")

# Valor promedio anual de la UF en CLP (Banco Central / SII) para normalizar montos históricos
UF_HISTORICA_CLP = {
    1989: 5032,
    1998: 14350,
    2000: 15450,
    2002: 16450,
    2006: 18150,
    2007: 18950,
    2008: 20500,
    2009: 20980,
    2010: 21180,
    2011: 21900,
    2012: 22580,
    2013: 23050,
    2014: 24050,
    2015: 25100,
    2016: 26080,
    2017: 26650,
    2018: 27200,
    2019: 27900,
    2020: 28750,
    2021: 29900,
    2022: 33150,
    2023: 36050,
    2024: 37500,
    2025: 38600,
    2026: 39500,
}


def clp_to_uf(monto_clp: int, year_str: str) -> float:
    if monto_clp <= 0:
        return 0.0
    m = re.search(r"\b(19\d\d|20\d\d)\b", str(year_str or ""))
    yr = int(m.group(1)) if m else 2024
    uf_val = UF_HISTORICA_CLP.get(yr, 37500 if yr >= 2024 else 15000)
    return round(monto_clp / uf_val, 1)


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
            fuentes_rich = add_source.parse_fuentes_from_note(meta, m.group(2))
            tipo_nodo = str(meta.get("tipo_nodo", "desconocido"))
            monto_clp = int(meta.get("monto_clp", 0) or 0)
            fecha_raw = str(meta.get("fecha") or meta.get("fecha_emision") or meta.get("año_inicio") or "")
            yr_match = re.search(r"\b(19\d\d|20\d\d)\b", fecha_raw)
            anio = int(yr_match.group(1)) if yr_match else 0
            causas_directas = extract_wikilinks(meta.get("causa_vinculada"))
            if tipo_nodo == "causa_judicial":
                causas_directas = [node_id]

            nodes[node_id] = {
                "id": node_id,
                "tipo_nodo": tipo_nodo,
                "rut": str(meta.get("rut", meta.get("ruc", ""))),
                "monto_clp": monto_clp,
                "monto_uf": clp_to_uf(monto_clp, fecha_raw) if tipo_nodo == "nexo_transaccion" else 0.0,
                "fecha": fecha_raw,
                "año": anio,
                "causas": sorted(set(causas_directas)),
                "path": rel_path,
                "in_degree": 0,
                "out_degree": 0,
                "flujo_emitido_clp": 0,
                "flujo_recibido_clp": 0,
                "flujo_emitido_uf": 0.0,
                "flujo_recibido_uf": 0.0,
                "estado_verificacion": str(meta.get("estado_verificacion") or ""),
                "monto_origen": str(meta.get("monto_origen") or ""),
                "situacion_procesal": str(meta.get("situacion_procesal") or ""),
                # Fuentes con URL http(s), para que el visor web y GraphML las muestren como enlaces.
                "fuentes": [
                    {k: str(fu.get(k) or "") for k in ("url", "titulo", "medio", "tipo", "fecha", "archivo")}
                    for fu in fuentes_rich
                    if isinstance(fu, dict) and str(fu.get("url", "")).startswith(("http://", "https://"))
                ],
                "fuente_principal_url": next(
                    (
                        str(fu.get("url"))
                        for fu in fuentes_rich
                        if isinstance(fu, dict) and str(fu.get("url", "")).startswith(("http://", "https://"))
                    ),
                    "",
                ),
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

        # Si el nodo origen es una arista reificada TRX, atribuir montos y causas a entidades y firmantes
        if src in nodes and nodes[src]["tipo_nodo"] == "nexo_transaccion":
            monto = nodes[src]["monto_clp"]
            monto_uf = nodes[src]["monto_uf"]
            if dst in nodes and nodes[src]["causas"]:
                nodes[dst]["causas"] = sorted(set(nodes[dst]["causas"]) | set(nodes[src]["causas"]))
            if e["relation"] in ("entidad_origen", "firmante_origen") and dst in nodes:
                nodes[dst]["flujo_emitido_clp"] += monto
                nodes[dst]["flujo_emitido_uf"] = round(nodes[dst]["flujo_emitido_uf"] + monto_uf, 1)
            elif e["relation"] in ("entidad_destino", "firmante_destino") and dst in nodes:
                nodes[dst]["flujo_recibido_clp"] += monto
                nodes[dst]["flujo_recibido_uf"] = round(nodes[dst]["flujo_recibido_uf"] + monto_uf, 1)

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
                    "monto_total_uf": round(
                        sum(n["monto_uf"] for n in nodes.values() if n["tipo_nodo"] == "nexo_transaccion"), 1
                    ),
                    "total_fuentes_url": sum(len(n["fuentes"]) for n in nodes.values()),
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
        ("d7", "node", "fuente_principal_url", "string"),
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
            ("d7", "fuente_principal_url"),
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

    graphml_path = os.path.join(EXPORT_DIR, "red_ftm_chile.graphml")
    tree = ET.ElementTree(graphml)
    ET.indent(tree, space="  ")
    tree.write(graphml_path, encoding="utf-8", xml_declaration=True)

    print(f"[OK] Grafo exportado a GraphML : {os.path.relpath(graphml_path, ROOT_DIR)}")
    print(f"[OK] Métricas exportadas a JSON: {os.path.relpath(json_path, ROOT_DIR)}")
    print(f"     Nodos: {len(nodes)} | Aristas dirigidas: {len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
