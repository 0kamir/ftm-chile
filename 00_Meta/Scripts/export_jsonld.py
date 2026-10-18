#!/usr/bin/env python3
"""
Exportador a Grafo de Conocimiento Semántico W3C JSON-LD (`export_jsonld.py`).
Mapea las notas del vault a un documento `@graph` JSON-LD interoperable con `schema.org` y SPARQL/RDF.

Salida:
  05_Vistas_Analiticas/Exportaciones/red_corrupcion_chile.jsonld
"""

import json
import os
import re
import urllib.parse
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_JSONLD = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "red_corrupcion_chile.jsonld"
)


def uri_for(name: str) -> str:
    return "urn:cl-osint:node:" + urllib.parse.quote(name.replace(" ", "_"))


def clean_link(val) -> str:
    if val is None:
        return ""
    m = re.search(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val))
    return m.group(1).strip() if m else str(val).strip()


def main() -> int:
    os.makedirs(os.path.dirname(OUT_JSONLD), exist_ok=True)
    graph_items = []

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fname), ROOT_DIR)
            if (
                rel == "README.md"
                or rel.startswith("00_Meta/Plantillas/")
                or rel.startswith("05_Vistas_Analiticas/Exportaciones/")
            ):
                continue
            name = os.path.splitext(fname)[0]
            with open(os.path.join(dirpath, fname), "r", encoding="utf-8") as f:
                txt = f.read()
            m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
            if not m:
                continue
            meta = yaml.safe_load(m.group(1)) or {}
            tipo = str(meta.get("tipo_nodo", ""))
            if tipo in ("vista_analitica", "meta_taxonomia"):
                continue

            item = {
                "@id": uri_for(name),
                "@type": f"osint:{tipo}",
                "schema:name": name,
            }
            if meta.get("rut") or meta.get("ruc"):
                item["schema:identifier"] = str(meta.get("rut") or meta.get("ruc"))
            if tipo == "nexo_transaccion":
                item["schema:amount"] = {
                    "@type": "schema:MonetaryAmount",
                    "schema:currency": "CLP",
                    "schema:value": int(meta.get("monto_clp", 0) or 0),
                }
                item["osint:entidadOrigen"] = {"@id": uri_for(clean_link(meta.get("entidad_origen")))}
                item["osint:entidadDestino"] = {"@id": uri_for(clean_link(meta.get("entidad_destino")))}
                item["osint:firmanteOrigen"] = {"@id": uri_for(clean_link(meta.get("firmante_origen")))}
                item["osint:firmanteDestino"] = {"@id": uri_for(clean_link(meta.get("firmante_destino")))}
                item["osint:causaVinculada"] = {"@id": uri_for(clean_link(meta.get("causa_vinculada")))}

            graph_items.append(item)

    doc = {
        "@context": {
            "schema": "https://schema.org/",
            "osint": "https://followthemoney.tech/ns#",
        },
        "@graph": graph_items,
    }

    with open(OUT_JSONLD, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    print(
        f"[OK] Grafo Semántico JSON-LD generado: {os.path.relpath(OUT_JSONLD, ROOT_DIR)} ({len(graph_items)} recursos RDF)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
