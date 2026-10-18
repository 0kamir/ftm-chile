#!/usr/bin/env python3
"""
Generador de Dossier Pericial Consolidado (`generate_dossier.py`).
Compila un informe forense estático autocontenido (sin dependencia de Dataview para exportación a PDF/impresión)
en `05_Vistas_Analiticas/Exportaciones/Dossier_Ejecutivo_Completo.md`.
"""

import os
import re
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DOSSIER = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "Dossier_Ejecutivo_Completo.md"
)


def clean_link(val) -> str:
    if val is None:
        return ""
    m = re.search(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val))
    return m.group(1).strip() if m else str(val).strip()


def fmt_clp(amount: int) -> str:
    return "$" + f"{int(amount):,}".replace(",", ".")


def main() -> int:
    os.makedirs(os.path.dirname(OUT_DOSSIER), exist_ok=True)
    causas, personas, nexos = [], [], []

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fname), ROOT_DIR)
            if rel == "README.md" or rel.startswith("00_Meta/Plantillas/") or rel.startswith("05_Vistas_Analiticas/Exportaciones/"):
                continue
            name = os.path.splitext(fname)[0]
            with open(os.path.join(dirpath, fname), "r", encoding="utf-8") as f:
                txt = f.read()
            m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
            if not m:
                continue
            meta = yaml.safe_load(m.group(1)) or {}
            tipo = meta.get("tipo_nodo")
            if tipo == "causa_judicial":
                causas.append((name, meta))
            elif tipo == "persona":
                personas.append((name, meta))
            elif tipo == "nexo_transaccion":
                nexos.append((name, meta))

    total_clp = sum(int(m.get("monto_clp", 0) or 0) for _, m in nexos)

    lines = [
        "---",
        "tipo_nodo: dossier_pericial",
        'titulo: "Dossier Ejecutivo Consolidado de Auditoría Forense en Chile"',
        "tags:",
        "  - dossier",
        "  - informe-pericial",
        "---",
        "",
        "# Dossier Ejecutivo Consolidado — Auditoría Forense de Corrupción en Chile",
        "",
        f"- **Causas Penales Auditadas**: **{len(causas)}**",
        f"- **Sujetos de Interés / Imputados**: **{len(personas)}**",
        f"- **Aristas Reificadas (`TRX`)**: **{len(nexos)}**",
        f"- **Perjuicio / Flujo Global Consolidado**: **{fmt_clp(total_clp)} CLP**",
        "",
        "---",
        "",
        "## 1. Resumen de Macrocausas Penales",
        "",
        "| Causa Judicial | RUC | Año Inicio | Estado Judicial | Delito Principal | Fiscalía / Tribunal |",
        "| :--- | :--- | :---: | :---: | :--- | :--- |",
    ]

    for cname, cmeta in sorted(causas, key=lambda x: int(x[1].get("año_inicio", 0))):
        lines.append(
            f"| [[{cname}]] | `{cmeta.get('ruc')}` | {cmeta.get('año_inicio')} | `{cmeta.get('estado_judicial')}` | {cmeta.get('delito_principal')} | {cmeta.get('tribunal_o_fiscalia')} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 2. Nómina de Condenados, Formalizados y Testigos",
            "",
            "| Persona | RUT | Rol / Cargo | Partido | Situación Procesal | Medida Cautelar / Condena |",
            "| :--- | :--- | :--- | :--- | :---: | :--- |",
        ]
    )

    for pname, pmeta in sorted(personas, key=lambda x: x[0]):
        lines.append(
            f"| [[{pname}]] | `{pmeta.get('rut')}` | {pmeta.get('rol_principal')} | {pmeta.get('afiliacion_politica')} | **`{pmeta.get('situacion_procesal')}`** | {pmeta.get('medida_cautelar') or '—'} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 3. Registro Maestro de Aristas Reificadas (`03_Hechos_y_Nexos/`)",
            "",
            "| ID Nexo | Fecha | Tipo | Origen | Destino | Firmante Origen | Firmante Destino | Monto (CLP) | Causa |",
            "| :--- | :---: | :---: | :--- | :--- | :--- | :--- | ---: | :--- |",
        ]
    )

    for nname, nmeta in sorted(nexos, key=lambda x: str(x[1].get("fecha", ""))):
        monto = int(nmeta.get("monto_clp", 0) or 0)
        lines.append(
            f"| [[{nname}]] | {nmeta.get('fecha')} | `{nmeta.get('tipo_nexo')}` | {nmeta.get('entidad_origen')} | {nmeta.get('entidad_destino')} | {nmeta.get('firmante_origen')} | {nmeta.get('firmante_destino')} | **{fmt_clp(monto)}** | {nmeta.get('causa_vinculada')} |"
        )

    with open(OUT_DOSSIER, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(
        f"[OK] Dossier Pericial Consolidado generado: {os.path.relpath(OUT_DOSSIER, ROOT_DIR)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
