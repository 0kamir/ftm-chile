#!/usr/bin/env python3
"""
Exportador a Neo4j Cypher (Estándar ICIJ Offshore Leaks / Panama Papers).
Traduce todos los nodos y aristas reificadas del vault de Obsidian en sentencias Cypher
`MERGE` idempotentes para cargar la red completa en Neo4j / Memgraph.

Salida:
  05_Vistas_Analiticas/Exportaciones/icij_neo4j_import.cypher
"""

import json
import os
import re
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_CYPHER = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "icij_neo4j_import.cypher"
)

LABEL_MAP = {
    "persona": "Persona",
    "entidad_publica": "EntidadPublica",
    "entidad_privada": "EntidadPrivada",
    "partido_politico": "PartidoPolitico",
    "causa_judicial": "CausaJudicial",
    "evidencia_documental": "EvidenciaDocumental",
    "tipo_penal": "TipoPenal",
    "nexo_transaccion": "NexoTransaccion",
}

REL_MAP = {
    "entidad_origen": "ORIGEN_DE_FONDOS",
    "entidad_destino": "DESTINO_DE_FONDOS",
    "firmante_origen": "AUTORIZADO_POR",
    "firmante_destino": "SUSCRITO_POR",
    "causa_vinculada": "INVESTIGADO_EN",
    "delito_imputado": "CONFIGURA_DELITO",
    "evidencia_soporte": "RESPALDADO_POR",
    "afiliacion_politica": "MILITA_EN",
    "representante_legal": "REPRESENTADA_POR",
    "delito_principal": "DELITO_PRINCIPAL",
    "organismo_emisor": "EMITIDO_POR",
    "nexo_respaldado": "ACREDITA_NEXO",
}


def extract_wikilinks(value) -> list[str]:
    if value is None:
        return []
    return [
        m.strip()
        for m in re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(value))
        if m.strip()
    ]


def cypher_str(val) -> str:
    return json.dumps(str(val), ensure_ascii=False)


def main() -> int:
    os.makedirs(os.path.dirname(OUT_CYPHER), exist_ok=True)
    lines = [
        "// ============================================================================",
        "// SCRIPT DE IMPORTACIÓN NEO4J CYPHER — ESTÁNDAR ICIJ / GRAFO REIFICADO CHILE",
        "// ============================================================================",
        "CREATE CONSTRAINT nodo_id_unique IF NOT EXISTS FOR (n:NodoForense) REQUIRE n.id IS UNIQUE;",
        "",
        "// 1. Creación de Nodos Reificados y Entidades",
    ]

    edges = []

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fname), ROOT_DIR)
            if rel == "README.md" or rel.startswith("00_Meta/Plantillas/"):
                continue

            name = os.path.splitext(fname)[0]
            with open(os.path.join(dirpath, fname), "r", encoding="utf-8") as f:
                txt = f.read()
            m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
            if not m:
                continue
            meta = yaml.safe_load(m.group(1)) or {}
            tipo = str(meta.get("tipo_nodo", "Otro"))
            if tipo in ("vista_analitica", "meta_taxonomia"):
                continue

            label = LABEL_MAP.get(tipo, "Entidad")
            rut = str(meta.get("rut") or meta.get("ruc") or "")
            monto = int(meta.get("monto_clp", 0) or 0)
            fecha = str(meta.get("fecha") or meta.get("fecha_constitucion") or meta.get("fecha_emision") or "")

            lines.append(
                f"MERGE (n:NodoForense:{label} {{id: {cypher_str(name)}}}) "
                f"SET n.tipo_nodo = {cypher_str(tipo)}, n.rut = {cypher_str(rut)}, "
                f"n.monto_clp = {monto}, n.fecha = {cypher_str(fecha)};"
            )

            for prop, val in meta.items():
                for target in extract_wikilinks(val):
                    rel_type = REL_MAP.get(prop, prop.upper())
                    edges.append((name, target, rel_type, prop))

    lines.append("")
    lines.append("// 2. Creación de Relaciones Semánticas Dirigidas")
    for src, dst, rel_type, prop in edges:
        lines.append(
            f"MATCH (a:NodoForense {{id: {cypher_str(src)}}}), (b:NodoForense {{id: {cypher_str(dst)}}}) "
            f"MERGE (a)-[:{rel_type} {{propiedad_yaml: {cypher_str(prop)}}}]->(b);"
        )

    lines.extend(
        [
            "",
            "// ============================================================================",
            "// CONSULTAS CYPHER FORENSES RECOMENDADAS (ICIJ STYLE)",
            "// ============================================================================",
            "// A) Camino más corto entre dos imputados cualesquiera:",
            "// MATCH p = shortestPath((a:Persona {id: 'Daniel Andrade Schwarze'})-[*..10]-(b:Persona {id: 'Camila Polizzi Fonceca'})) RETURN p;",
            "//",
            "// B) Detectar Nodos Puente que reciben fondos de múltiples órganos públicos:",
            "// MATCH (pub:EntidadPublica)<-[:ORIGEN_DE_FONDOS]-(trx:NexoTransaccion)-[:DESTINO_DE_FONDOS]->(priv:EntidadPrivada)",
            "// WITH priv, count(DISTINCT pub) AS num_organos, sum(trx.monto_clp) AS total_clp WHERE num_organos >= 2",
            "// RETURN priv.id, num_organos, total_clp ORDER BY total_clp DESC;",
        ]
    )

    with open(OUT_CYPHER, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(
        f"[OK] Script Neo4j Cypher (ICIJ) generado: {os.path.relpath(OUT_CYPHER, ROOT_DIR)} ({len(edges)} relaciones Cypher)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
