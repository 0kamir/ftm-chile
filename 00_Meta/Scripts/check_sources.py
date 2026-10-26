#!/usr/bin/env python3
"""
Reporte de Cobertura de Fuentes y Alertas de Verificación del Vault OSINT.
1. Mide qué porcentaje de causas, evidencias y aristas TRX está respaldado por URLs.
   Entidades (personas, empresas, organismos, partidos) y anexos no exigen fuente, pero sus
   fuentes y alertas también se revisan.
   Una arista TRX cuenta como cubierta si tiene fuentes propias o si su `evidencia_soporte` las tiene.
2. Consolida las `alertas_verificacion` pendientes de revisión editorial.
3. Con `--links`, comprueba que cada URL responda (403/429 se informan como bloqueo anti-bot).
Genera `05_Vistas_Analiticas/Cobertura_de_Fuentes.md`.

Uso:
  python3 00_Meta/Scripts/check_sources.py [--links]
"""

import concurrent.futures
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

import yaml

import add_source

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPORT_PATH = os.path.join(ROOT_DIR, "05_Vistas_Analiticas", "Cobertura_de_Fuentes.md")
CARPETAS = {
    "entidad": "01_Entidades",
    "causa_judicial": "02_Causas",
    "nexo_transaccion": "03_Hechos_y_Nexos",
    "evidencia_documental": "04_Evidencias",
    "tipo_penal": "00_Meta/Delitos",
    "anexo_documental": "06_Anexos",
}


# Carpetas adicionales sin exigencia separada (integradas arriba).
CARPETAS_SIN_COBERTURA: list[str] = []


def load_notes() -> dict[str, dict]:
    notes = {}
    carpetas = [(tipo, c) for tipo, c in CARPETAS.items()] + [(None, c) for c in CARPETAS_SIN_COBERTURA]
    for tipo, carpeta in carpetas:
        base = os.path.join(ROOT_DIR, carpeta)
        for dirpath, _, filenames in os.walk(base):
            for fname in sorted(filenames):
                if not fname.endswith(".md"):
                    continue
                with open(os.path.join(dirpath, fname), "r", encoding="utf-8") as f:
                    txt = f.read()
                m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.DOTALL)
                meta = (yaml.safe_load(m.group(1)) if m else {}) or {}
                body = m.group(2) if m else ""
                if meta.get("fuentes"):
                    meta["fuentes"] = add_source.parse_fuentes_from_note(meta, body)
                notes[fname[:-3]] = {
                    "carpeta": os.path.relpath(dirpath, ROOT_DIR),
                    "tipo": tipo or str(meta.get("tipo_nodo", "")),
                    "meta": meta,
                }
    return notes


def first_link(value) -> str | None:
    m = re.search(r"\[\[([^\]|#]+)", str(value or ""))
    return m.group(1).strip() if m else None


def check_url(url: str) -> tuple[str, str]:
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 ftm-chile"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return url, str(resp.status)
    except urllib.error.HTTPError as exc:
        return url, str(exc.code)
    except Exception as exc:  # noqa: BLE001 - se reporta cualquier fallo de red
        return url, f"error: {type(exc).__name__}"


def resolve_wayback_snapshot(url: str) -> str | None:
    """Consulta la API pública de Wayback Machine para obtener la captura archivada más cercana."""
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(api, method="GET", headers={"User-Agent": "Mozilla/5.0 ftm-chile"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        closest = (data.get("archived_snapshots") or {}).get("closest") or {}
        if closest.get("available") and str(closest.get("url", "")).startswith(("http://", "https://")):
            return str(closest["url"]).replace("http://web.archive.org/", "https://web.archive.org/")
    except Exception:  # noqa: BLE001
        return None
    return None


def auto_archive_missing(notes: dict[str, dict], limit: int = 25) -> int:
    """Resuelve y persiste URLs de Wayback Machine para fuentes sin campo `archivo:`."""
    candidatas = sorted(
        {
            str(f.get("url"))
            for v in notes.values()
            for f in v["meta"].get("fuentes") or []
            if isinstance(f, dict)
            and str(f.get("url", "")).startswith(("http://", "https://"))
            and not f.get("archivo")
        }
    )[:limit]
    if not candidatas:
        return 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        resueltas = dict(zip(candidatas, pool.map(resolve_wayback_snapshot, candidatas)))
    halladas = {u: snap for u, snap in resueltas.items() if snap}
    if not halladas:
        return 0
    actualizadas = 0
    for nombre, info in notes.items():
        fuentes = info["meta"].get("fuentes") or []
        cambio = False
        for f in fuentes:
            if isinstance(f, dict) and not f.get("archivo") and f.get("url") in halladas:
                f["archivo"] = halladas[f["url"]]
                cambio = True
        if cambio:
            path = add_source.find_note(nombre)
            add_source.actualizar_nota(path, fuentes, info["meta"].get("estado_verificacion"), None)
            actualizadas += 1
    return actualizadas


def main() -> int:
    notes = load_notes()
    if "--auto-archive" in sys.argv:
        n_arch = auto_archive_missing(notes)
        print(f"  [Wayback] Notas enriquecidas con snapshot archivado: {n_arch}")
        notes = load_notes()

    def tiene_fuentes(nombre: str | None) -> bool:
        return bool(nombre in notes and notes[nombre]["meta"].get("fuentes"))

    filas_cobertura = []
    sin_cubrir: dict[str, list[str]] = {t: [] for t in CARPETAS}
    for tipo, carpeta in CARPETAS.items():
        grupo = [n for n, v in notes.items() if v["tipo"] == tipo]
        cubiertas = 0
        for nombre in grupo:
            ok = tiene_fuentes(nombre)
            if not ok and tipo == "nexo_transaccion":
                ok = tiene_fuentes(first_link(notes[nombre]["meta"].get("evidencia_soporte")))
            if ok:
                cubiertas += 1
            else:
                sin_cubrir[tipo].append(nombre)
        pct = 100 * cubiertas / len(grupo) if grupo else 0
        filas_cobertura.append((carpeta, len(grupo), cubiertas, pct))

    estados: dict[str, int] = {}
    for v in notes.values():
        if v["tipo"] in ("causa_judicial", "evidencia_documental"):
            e = v["meta"].get("estado_verificacion") or "sin_declarar"
            estados[e] = estados.get(e, 0) + 1

    montos_origen: dict[str, list[int]] = {}
    for v in notes.values():
        if v["tipo"] == "nexo_transaccion":
            origen = str(v["meta"].get("monto_origen") or "sin_declarar")
            acc = montos_origen.setdefault(origen, [0, 0])
            acc[0] += 1
            acc[1] += int(v["meta"].get("monto_clp") or 0)

    alertas = [
        (nombre, a)
        for nombre, v in sorted(notes.items())
        for a in v["meta"].get("alertas_verificacion") or []
    ]

    resultados_links: list[tuple[str, str]] = []
    if "--links" in sys.argv:
        urls = sorted({
            str(f.get("url"))
            for v in notes.values()
            for f in v["meta"].get("fuentes") or []
            if isinstance(f, dict)
        })
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
            resultados_links = sorted(pool.map(check_url, urls))

    lineas = [
        "---",
        "tipo_nodo: vista_analitica",
        "tags:",
        "  - vista/fuentes",
        "  - meta/verificacion",
        "---",
        "",
        "# Cobertura de Fuentes y Alertas de Verificación",
        "",
        f"> Generado por `check_sources.py` el {datetime.date.today():%Y-%m-%d}. "
        "Una arista TRX se considera cubierta si su evidencia soporte tiene fuentes.",
        "",
        "## Cobertura por Carpeta",
        "| Carpeta | Notas | Con fuente | Cobertura |",
        "| :--- | ---: | ---: | ---: |",
    ]
    lineas += [f"| `{c}` | {n} | {k} | {p:.0f}% |" for c, n, k, p in filas_cobertura]
    lineas += ["", "## Estado de Verificación (Causas y Evidencias)",
               "| Estado | Notas |", "| :--- | ---: |"]
    lineas += [f"| `{e}` | {n} |" for e, n in sorted(estados.items())]
    lineas += ["", "## Montos por Origen",
               "> Una cifra de sentencia o resolución está acreditada; una de acusación, estimación o prensa no. "
               "No se suman como si tuvieran la misma calidad.", "",
               "| Origen del monto | Hechos | Monto (CLP) |", "| :--- | ---: | ---: |"]
    for origen in ("sentencia", "resolucion_administrativa", "registro_oficial", "estimacion_oficial",
                   "acusacion", "prensa", "no_verificado", "sin_monto", "sin_declarar"):
        if origen in montos_origen:
            n, total = montos_origen[origen]
            lineas.append(f"| `{origen}` | {n} | ${total:,.0f} |".replace(",", "."))
    lineas += ["", f"## Alertas de Verificación Pendientes ({len(alertas)})", ""]
    lineas += [f"- **[[{n}]]**: {a}" for n, a in alertas] or ["- Sin alertas pendientes."]
    lineas += ["", "## Notas sin Fuente Verificable", ""]
    for tipo, carpeta in CARPETAS.items():
        if sin_cubrir[tipo]:
            lineas.append(f"### `{carpeta}` ({len(sin_cubrir[tipo])})")
            lineas += [f"- [[{n}]]" for n in sin_cubrir[tipo]]
            lineas.append("")
    if resultados_links:
        caidos = [(u, c) for u, c in resultados_links if c != "200"]
        lineas += ["", f"## Comprobación de Enlaces ({len(resultados_links)} URLs, "
                   f"{len(caidos)} sin respuesta 200)", ""]
        for url, code in caidos:
            nota = " (bloqueo anti-bot; verificar en navegador)" if code in ("403", "429") else ""
            lineas.append(f"- `{code}` {url}{nota}")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas) + "\n")

    print("Reporte de cobertura de fuentes generado:", os.path.relpath(REPORT_PATH, ROOT_DIR))
    for c, n, k, p in filas_cobertura:
        print(f"  {c:<20} {k:>3}/{n:<3} ({p:.0f}%)")
    print(f"  Alertas de verificación pendientes: {len(alertas)}")
    rotos = [c for _, c in resultados_links if c not in ("200", "403", "429")]
    if rotos:
        print(f"  [X] {len(rotos)} enlaces rotos o sin respuesta.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
