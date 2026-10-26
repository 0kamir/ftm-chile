#!/usr/bin/env python3
"""
Exportador de Planillas Contables CSV para Anexos Judiciales.
Genera en `05_Vistas_Analiticas/Exportaciones/`:
  - hechos.csv
  - personas.csv
  - entidades.csv
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
    personas = []
    entidades = []

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        # 06_Anexos queda fuera del grafo y de los análisis (menciones documentales sin imputación).
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "06_Anexos"]
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

            fuentes_urls = " | ".join(
                str(fu.get("url") if isinstance(fu, dict) else fu)
                for fu in (meta.get("fuentes") or [])
                if str(fu.get("url") if isinstance(fu, dict) else fu).startswith(("http://", "https://"))
            )

            if tipo == "nexo_transaccion":
                transacciones.append(
                    {
                        "id_nexo": name,
                        "fecha": str(meta.get("fecha", "")),
                        "tipo_nexo": str(meta.get("tipo_nexo", "")),
                        "monto_clp": int(meta.get("monto_clp", 0) or 0),
                        "monto_origen": str(meta.get("monto_origen") or ""),
                        "entidad_origen": clean_link(meta.get("entidad_origen")),
                        "entidad_destino": clean_link(meta.get("entidad_destino")),
                        "firmante_origen": clean_link(meta.get("firmante_origen")),
                        "firmante_destino": clean_link(meta.get("firmante_destino")),
                        "causa_vinculada": clean_link(meta.get("causa_vinculada")),
                        "delito_imputado": clean_link(meta.get("delito_imputado")),
                        "evidencia_soporte": clean_link(meta.get("evidencia_soporte")),
                        "fuentes_urls": fuentes_urls,
                    }
                )
            elif tipo == "persona":
                personas.append(
                    {
                        "nombre": name,
                        "rut": str(meta.get("rut", "")),
                        "rol_principal": str(meta.get("rol_principal", "")),
                        "afiliacion_politica": clean_link(meta.get("afiliacion_politica")),
                        "situacion_procesal": str(meta.get("situacion_procesal", "")),
                        "medida_cautelar": str(meta.get("medida_cautelar", "")),
                        "fuentes_urls": fuentes_urls,
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
                        "fuentes_urls": fuentes_urls,
                    }
                )

    trx_csv = os.path.join(EXPORT_DIR, "hechos.csv")
    with open(trx_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(transacciones[0].keys()))
        w.writeheader()
        w.writerows(sorted(transacciones, key=lambda x: x["fecha"]))

    imp_csv = os.path.join(EXPORT_DIR, "personas.csv")
    with open(imp_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(personas[0].keys()))
        w.writeheader()
        w.writerows(personas)

    ent_csv = os.path.join(EXPORT_DIR, "entidades.csv")
    with open(ent_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(entidades[0].keys()))
        w.writeheader()
        w.writerows(entidades)

    print(
        f"[OK] Planillas CSV de peritaje generadas en 05_Vistas_Analiticas/Exportaciones/ "
        f"({len(transacciones)} nexos, {len(personas)} personas, {len(entidades)} entidades)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
