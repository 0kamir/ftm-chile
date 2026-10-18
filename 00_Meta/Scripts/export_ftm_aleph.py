#!/usr/bin/env python3
"""
Exportador a Estándar OCCRP Aleph / FollowTheMoney (FtM JSONLines).
Traduce la ontología del vault de Obsidian (Personas, Entidades Públicas/Privadas, Causas,
Evidencias y Aristas Reificadas TRX) a entidades FtM (`Person`, `PublicBody`, `Organization`,
`CourtCase`, `Document`, `Payment` / `UnknownLink`).

Salida:
  05_Vistas_Analiticas/Exportaciones/aleph_entities.ftm.jsonl
"""

import hashlib
import json
import os
import re
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_FTM = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "aleph_entities.ftm.jsonl"
)


def ftm_id(name: str) -> str:
    return "cl-osint-" + hashlib.sha1(name.encode("utf-8")).hexdigest()[:16]


def clean_link(val) -> str:
    if val is None:
        return ""
    m = re.search(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val))
    return m.group(1).strip() if m else str(val).strip()


def main() -> int:
    os.makedirs(os.path.dirname(OUT_FTM), exist_ok=True)
    entities = []

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
            tipo = meta.get("tipo_nodo")
            eid = ftm_id(name)

            if tipo == "persona":
                ent = {
                    "id": eid,
                    "schema": "Person",
                    "caption": name,
                    "properties": {
                        "name": [name],
                        "idNumber": [str(meta.get("rut", ""))],
                        "alias": [str(a) for a in (meta.get("aliases") or [])],
                        "position": [str(meta.get("rol_principal", ""))],
                        "political": [clean_link(meta.get("afiliacion_politica"))],
                        "status": [str(meta.get("situacion_procesal", ""))],
                        "notes": [str(meta.get("medida_cautelar", ""))],
                        "nationality": ["cl"],
                    },
                }
                entities.append(ent)

            elif tipo == "entidad_publica":
                ent = {
                    "id": eid,
                    "schema": "PublicBody",
                    "caption": name,
                    "properties": {
                        "name": [name],
                        "idNumber": [str(meta.get("rut", ""))],
                        "sector": [str(meta.get("categoria", ""))],
                        "jurisdiction": ["cl"],
                        "mainCountry": ["cl"],
                        "summary": [f"Región: {meta.get('region', '')} | Superior: {meta.get('superior_jerarquico', '')}"],
                    },
                }
                entities.append(ent)

            elif tipo in ("entidad_privada", "partido_politico"):
                ent = {
                    "id": eid,
                    "schema": "Organization",
                    "caption": name,
                    "properties": {
                        "name": [str(meta.get("razon_social") or name)],
                        "idNumber": [str(meta.get("rut", ""))],
                        "incorporationDate": [
                            str(meta.get("fecha_constitucion") or meta.get("fecha_fundacion") or "")
                        ],
                        "jurisdiction": ["cl"],
                        "summary": [str(meta.get("objeto_social") or meta.get("coalicion") or "")],
                    },
                }
                entities.append(ent)

            elif tipo == "causa_judicial":
                ent = {
                    "id": eid,
                    "schema": "CourtCase",
                    "caption": name,
                    "properties": {
                        "name": [name],
                        "caseNumber": [str(meta.get("ruc", ""))],
                        "filingDate": [str(meta.get("año_inicio", ""))],
                        "court": [str(meta.get("tribunal_o_fiscalia", ""))],
                        "status": [str(meta.get("estado_judicial", ""))],
                        "category": [clean_link(meta.get("delito_principal"))],
                    },
                }
                entities.append(ent)

            elif tipo == "evidencia_documental":
                ent = {
                    "id": eid,
                    "schema": "Document",
                    "caption": name,
                    "properties": {
                        "title": [name],
                        "date": [str(meta.get("fecha_emision", ""))],
                        "summary": [str(meta.get("tipo_documento", ""))],
                        "publisher": [clean_link(meta.get("organismo_emisor"))],
                        "sourceUrl": [str(meta.get("fuente_osint", ""))],
                    },
                }
                entities.append(ent)

            elif tipo == "nexo_transaccion":
                e_orig = clean_link(meta.get("entidad_origen"))
                e_dest = clean_link(meta.get("entidad_destino"))
                f_orig = clean_link(meta.get("firmante_origen"))
                f_dest = clean_link(meta.get("firmante_destino"))
                causa = clean_link(meta.get("causa_vinculada"))
                evid = clean_link(meta.get("evidencia_soporte"))
                monto = int(meta.get("monto_clp", 0) or 0)

                ent = {
                    "id": eid,
                    "schema": "Payment" if monto > 0 else "UnknownLink",
                    "caption": f"{name} (${monto:,} CLP)".replace(",", "."),
                    "properties": {
                        "date": [str(meta.get("fecha", ""))],
                        "amount": [str(monto)],
                        "currency": ["CLP"],
                        "payer": [ftm_id(e_orig), ftm_id(f_orig)],
                        "beneficiary": [ftm_id(e_dest), ftm_id(f_dest)],
                        "program": [str(meta.get("tipo_nexo", ""))],
                        "project": [ftm_id(causa)],
                        "proof": [ftm_id(evid)],
                    },
                }
                entities.append(ent)

    with open(OUT_FTM, "w", encoding="utf-8") as f:
        for e in entities:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    print(
        f"[OK] Exportación OCCRP Aleph FtM: {os.path.relpath(OUT_FTM, ROOT_DIR)} ({len(entities)} entidades FtM)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
