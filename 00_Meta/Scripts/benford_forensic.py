#!/usr/bin/env python3
"""
Auditoría Estadística de Ley de Benford y Detección de Sesgo de Redondeo Artificial (`benford_forensic.py`).
Analiza todos los montos monetarios (`monto_clp > 0`) en `03_Hechos_y_Nexos/`:
1. Compara la frecuencia observada del primer dígito significativo (1..9) con la Ley de Benford:
     P(d) = log10(1 + 1/d)
2. Detecta operaciones con "Sesgo de Monto Redondo Discrecional" (múltiplos exactos de $10.000.000 CLP),
   indicador clásico de asignaciones fijadas sin cubicación o presupuesto técnico real.
3. Genera la vista `05_Vistas_Analiticas/Distribucion_de_Montos_Benford.md` con gráfico `xychart-beta` de Mermaid.
"""

from collections import Counter
import math
import os
import re
import yaml
from descargo import descargo  # noqa: E402

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_MD = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Distribucion_de_Montos_Benford.md"
)

BENFORD_EXPECTED = {d: round(math.log10(1.0 + 1.0 / d) * 100.0, 1) for d in range(1, 10)}


def clean_link(val) -> str:
    if val is None:
        return ""
    m = re.search(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val))
    return m.group(1).strip() if m else str(val).strip()


def fmt_clp(amount: int) -> str:
    return "$" + f"{int(amount):,}".replace(",", ".")


def main() -> int:
    nexos = []
    nexos_dir = os.path.join(ROOT_DIR, "03_Hechos_y_Nexos")

    for fname in sorted(os.listdir(nexos_dir)):
        if not fname.endswith(".md"):
            continue
        name = os.path.splitext(fname)[0]
        with open(os.path.join(nexos_dir, fname), "r", encoding="utf-8") as f:
            txt = f.read()
        m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
        if not m:
            continue
        meta = yaml.safe_load(m.group(1)) or {}
        monto = int(meta.get("monto_clp", 0) or 0)
        if monto > 0:
            first_digit = int(str(monto)[0])
            es_redondo_10m = (monto % 10_000_000) == 0
            nexos.append(
                {
                    "id": name,
                    "fecha": str(meta.get("fecha", "")),
                    "tipo_nexo": str(meta.get("tipo_nexo", "")),
                    "monto_clp": monto,
                    "first_digit": first_digit,
                    "es_redondo_10m": es_redondo_10m,
                    "origen": clean_link(meta.get("entidad_origen")),
                    "destino": clean_link(meta.get("entidad_destino")),
                    "causa": clean_link(meta.get("causa_vinculada")),
                }
            )

    total_n = len(nexos)
    counts = Counter(nx["first_digit"] for nx in nexos)
    observed_pct = {
        d: round((counts.get(d, 0) / total_n) * 100.0, 1) if total_n > 0 else 0.0
        for d in range(1, 10)
    }

    redondos = [nx for nx in nexos if nx["es_redondo_10m"]]
    pct_redondos = round((len(redondos) / total_n) * 100.0, 1) if total_n > 0 else 0.0

    obs_list_str = ", ".join(str(observed_pct[d]) for d in range(1, 10))
    ben_list_str = ", ".join(str(BENFORD_EXPECTED[d]) for d in range(1, 10))

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Auditoría Estadística de Ley de Benford y Sesgo de Montos Redondos"',
        "actualizacion_automatica: true",
        "tags:",
        "  - dashboard",
        "  - ley-de-benford",
        "  - analisis-de-montos",
        "---",
        "",
        "# Distribución de Montos: Ley de Benford y Montos Redondos",
        "",
        *descargo("montos"),
        "",
        f"- **Operaciones Monetarias Analizadas (`monto_clp > 0`)**: **{total_n}**",
        f"- **Operaciones con Monto Redondo Discrecional (Múltiplos de `$10.000.000 CLP`)**: **{len(redondos)} de {total_n} ({pct_redondos}%)**",
        "",
        "---",
        "",
        "## 1. Curva de Primer Dígito Significativo vs. Ley de Benford (`xychart-beta`)",
        "",
        "```mermaid",
        "xychart-beta",
        '  title "Distribución del Primer Dígito: Observado (%) vs. Teórico Benford (%)"',
        '  x-axis ["Dígito 1", "Dígito 2", "Dígito 3", "Dígito 4", "Dígito 5", "Dígito 6", "Dígito 7", "Dígito 8", "Dígito 9"]',
        '  y-axis "Frecuencia (%)" 0 --> 45',
        f"  bar [{obs_list_str}]",
        f"  line [{ben_list_str}]",
        "```",
        "",
        "| Primer Dígito ($d$) | Conteo Observado | Frecuencia Observada (%) | Frecuencia Esperada Benford (%) | Desviación ($\\Delta$) |",
        "| :---: | :---: | ---: | ---: | ---: |",
    ]

    for d in range(1, 10):
        diff = round(observed_pct[d] - BENFORD_EXPECTED[d], 1)
        sign = "+" if diff > 0 else ""
        lines.append(
            f"| **{d}** | {counts.get(d, 0)} | {observed_pct[d]}% | {BENFORD_EXPECTED[d]}% | `{sign}{diff}%` |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 2. Detección de Sesgo de Redondeo Artificial (Múltiplos Exactos de `$10.000.000 CLP`)",
            "",
            "En contabilidad, los presupuestos basados en cubicaciones reales de obra o nóminas efectivas rara vez terminan en múltiplos exactos de diez millones de pesos (ej. [[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]] por `$28.348.928.198` o [[TRX-2022-12-20-Convenio-EnTi-01]] por `$250.635.000`). Por el contrario, las asignaciones discrecionales o cajas negras suelen fijarse en cifras cerradas:",
            "",
            "| Nexo (`TRX`) | Fecha | Tipo | Origen | Destino | Monto Redondo (CLP) | Causa |",
            "| :--- | :---: | :---: | :--- | :--- | ---: | :--- |",
        ]
    )

    for nx in sorted(redondos, key=lambda x: x["monto_clp"], reverse=True):
        lines.append(
            f"| [[{nx['id']}]] | {nx['fecha']} | `{nx['tipo_nexo']}` | [[{nx['origen']}]] | [[{nx['destino']}]] | **{fmt_clp(nx['monto_clp'])}** | [[{nx['causa']}]] |"
        )

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(
        f"[OK] Distribución de montos (Benford) generada: {os.path.relpath(OUT_MD, ROOT_DIR)} "
        f"({len(redondos)}/{total_n} montos redondos detectados)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
