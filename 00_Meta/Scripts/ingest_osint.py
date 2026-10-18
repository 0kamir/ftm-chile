#!/usr/bin/env python3
"""
Ingestador OSINT de Transferencias y Convenios Públicos (Estándar Registros 19.862 / Transparencia).
Convierte filas CSV o registros JSON en nodos de aristas reificadas (.md) dentro de `03_Hechos_y_Nexos/`.

Uso:
  python3 00_Meta/Scripts/ingest_osint.py --input transferencias.csv [--dry-run]
"""

import argparse
import csv
import json
import os
import re
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
NEXOS_DIR = os.path.join(ROOT_DIR, "03_Hechos_y_Nexos")


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "-", text.strip())
    return re.sub(r"-+", "-", cleaned).strip("-")


def render_nexo_markdown(row: dict) -> tuple[str, str]:
    fecha = str(row.get("fecha", "2023-01-01")).strip()
    codigo = slugify(str(row.get("codigo", "Convenio-OSINT-01")))
    filename = f"TRX-{fecha}-{codigo}.md"

    tipo_nexo = str(row.get("tipo_nexo", "convenio_directo")).strip()
    monto_clp = int(float(row.get("monto_clp", 0)))
    entidad_origen = str(row.get("entidad_origen", "Entidad Origen")).strip()
    entidad_destino = str(row.get("entidad_destino", "Entidad Destino")).strip()
    firmante_origen = str(row.get("firmante_origen", "Firmante Origen")).strip()
    firmante_destino = str(row.get("firmante_destino", "Firmante Destino")).strip()
    causa_vinculada = str(row.get("causa_vinculada", "Caso Convenios")).strip()
    delito_imputado = str(row.get("delito_imputado", "Fraude al Fisco")).strip()
    evidencia_soporte = str(row.get("evidencia_soporte", "Evidencia Soporte")).strip()
    descripcion = str(
        row.get(
            "descripcion",
            "Registro ingestado automáticamente desde fuente pública OSINT (Ley N° 19.862 / Transparencia Activa).",
        )
    ).strip()

    content = f"""---
tipo_nodo: nexo_transaccion
fecha: {fecha}
tipo_nexo: {tipo_nexo}
monto_clp: {monto_clp}
entidad_origen: "[[{entidad_origen}]]"
entidad_destino: "[[{entidad_destino}]]"
firmante_origen: "[[{firmante_origen}]]"
firmante_destino: "[[{firmante_destino}]]"
causa_vinculada: "[[{causa_vinculada}]]"
delito_imputado: "[[{delito_imputado}]]"
evidencia_soporte: "[[{evidencia_soporte}]]"
tags:
  - nexo/transaccion
  - osint-ingested
---

# {os.path.splitext(filename)[0]}

## Ficha de Arista Reificada (Transacción / Hecho)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\\B(?=(\\d{{3}})+(?!\\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante de Origen**: `= this.firmante_origen`
- **Firmante de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
{descripcion}
"""
    return filename, content


def load_records(input_path: str) -> list[dict]:
    if input_path.endswith(".json"):
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ingesta registros OSINT (CSV/JSON) como aristas reificadas en 03_Hechos_y_Nexos/."
    )
    parser.add_argument("--input", required=True, help="Ruta al archivo CSV o JSON.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra las notas que se generarían sin escribirlas en disco.",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    for rec in records:
        fname, md = render_nexo_markdown(rec)
        out_path = os.path.join(NEXOS_DIR, fname)
        if args.dry_run:
            print(f"[DRY-RUN] Generaría: {out_path}")
        else:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"[OK] Creado: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
