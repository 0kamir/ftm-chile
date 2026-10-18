#!/usr/bin/env python3
"""
Exportador de Planillas Contables CSV para Anexos Periciales Judiciales.
Genera en `05_Vistas_Analiticas/Exportaciones/`:
  - peritaje_transacciones.csv
  - peritaje_imputados.csv
  - peritaje_entidades.csv
"""

import csv
import os
import re
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXPORT_DIR = os.path.join(ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones")


def clean_link(val) -> str:
    if val is None:
        return ""
    m = re.search(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val))
    return m.group(1).strip() if m else str(val).strip()


def main() -> int:
    os.makedirs(EXPORT_DIR, exist_ok=True)
    transacciones = []
    imputados = []
    entidades = []

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

            if tipo == "nexo_transaccion":
                transacciones.append(
                    {
                        "id_nexo": name,
                        "fecha": str(meta.get("fecha", "")),
                        "tipo_nexo": str(meta.get("tipo_nexo", "")),
                        "monto_clp": int(meta.get("monto_clp", 0) or 0),
                        "entidad_origen": clean_link(meta.get("entidad_origen")),
                        "entidad_destino": clean_link(meta.get("entidad_destino")),
                        "firmante_origen": clean_link(meta.get("firmante_origen")),
                        "firmante_destino": clean_link(meta.get("firmante_destino")),
                        "causa_vinculada": clean_link(meta.get("causa_vinculada")),
                        "delito_imputado": clean_link(meta.get("delito_imputado")),
                        "evidencia_soporte": clean_link(meta.get("evidencia_soporte")),
                    }
                )
            elif tipo == "persona":
                imputados.append(
                    {
                        "nombre": name,
                        "rut": str(meta.get("rut", "")),
                        "rol_principal": str(meta.get("rol_principal", "")),
                        "afiliacion_politica": clean_link(meta.get("afiliacion_politica")),
                        "situacion_procesal": str(meta.get("situacion_procesal", "")),
                        "medida_cautelar": str(meta.get("medida_cautelar", "")),
                    }
                )
            elif tipo in ("entidad_publica", "entidad_privada", "partido_politico"):
                entidades.append(
                    {
                        "nombre": name,
                        "tipo_entidad": tipo,
                        "rut": str(meta.get("rut", "")),
                        "categoria_o_giro": str(
                            meta.get("categoria")
                            or meta.get("objeto_social")
                            or meta.get("coalicion")
                            or ""
                        ),
                        "fecha_constitucion": str(
                            meta.get("fecha_constitucion")
                            or meta.get("fecha_fundacion")
                            or ""
                        ),
                        "representante_o_superior": clean_link(
                            meta.get("representante_legal")
                            or meta.get("superior_jerarquico")
                            or ""
                        ),
                    }
                )

    trx_csv = os.path.join(EXPORT_DIR, "peritaje_transacciones.csv")
    with open(trx_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(transacciones[0].keys()))
        w.writeheader()
        w.writerows(sorted(transacciones, key=lambda x: x["fecha"]))

    imp_csv = os.path.join(EXPORT_DIR, "peritaje_imputados.csv")
    with open(imp_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(imputados[0].keys()))
        w.writeheader()
        w.writerows(imputados)

    ent_csv = os.path.join(EXPORT_DIR, "peritaje_entidades.csv")
    with open(ent_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(entidades[0].keys()))
        w.writeheader()
        w.writerows(entidades)

    print(
        f"[OK] Planillas CSV de peritaje generadas en 05_Vistas_Analiticas/Exportaciones/ "
        f"({len(transacciones)} nexos, {len(imputados)} personas, {len(entidades)} entidades)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
