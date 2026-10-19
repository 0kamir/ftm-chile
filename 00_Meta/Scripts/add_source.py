#!/usr/bin/env python3
"""
Incorporador de Fuentes OSINT a notas del vault (cadena de custodia documental).
Agrega una fuente verificable (URL) al bloque YAML `fuentes:` de una nota, actualiza
`estado_verificacion` y, opcionalmente, registra alertas de verificación.
Edita el frontmatter como texto para no reformatear el resto de las propiedades.

Uso (una fuente):
  python3 00_Meta/Scripts/add_source.py --nota "Caso Caval" \
      --url https://www.biobiochile.cl/... --titulo "Lectura de sentencia" \
      --medio "BioBioChile" --tipo secundaria --fecha 2018-07-11 [--estado verificado]

Resolver una alerta ya atendida (coincidencia por texto):
  python3 00_Meta/Scripts/add_source.py --nota "Caso Caval" --resolver-alerta "Valero"

Uso (lote desde YAML {ruta_nota: {fuentes: [...], estado_verificacion, alertas: [...], resueltas: [...]}}):
  python3 00_Meta/Scripts/add_source.py --desde-yaml lote.yaml [--dry-run]
"""

import argparse
import datetime
import json
import os
import re
import sys

import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

TIPOS_FUENTE = ("primaria", "secundaria")
ESTADOS_VERIFICACION = ("verificado", "parcial", "desactualizado", "sin_fuente", "pendiente")
# Origen del monto de un hecho (TRX): de dónde sale la cifra, de más a menos firme.
ORIGENES_MONTO = ("sentencia", "resolucion_administrativa", "registro_oficial", "estimacion_oficial", "acusacion", "prensa", "no_verificado", "sin_monto")
CAMPOS_FUENTE = ("url", "titulo", "medio", "tipo", "fecha", "archivo", "consultado")

SECCION_FUENTES = """
## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
"""


def find_note(nombre: str) -> str:
    """Resuelve una nota por ruta relativa o por nombre (sin .md)."""
    candidato = os.path.join(ROOT_DIR, nombre)
    if os.path.isfile(candidato):
        return candidato
    objetivo = nombre[:-3] if nombre.endswith(".md") else nombre
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if objetivo + ".md" in filenames:
            return os.path.join(dirpath, objetivo + ".md")
    raise FileNotFoundError(f"No existe la nota '{nombre}' en el vault.")


def validar_fuente(fuente: dict) -> dict:
    url = str(fuente.get("url", "")).strip()
    if not re.match(r"^https?://\S+$", url):
        raise ValueError(f"URL inválida: {url!r}")
    if fuente.get("tipo") not in TIPOS_FUENTE:
        raise ValueError(f"'tipo' debe ser uno de {TIPOS_FUENTE} (fuente {url}).")
    for req in ("titulo", "medio"):
        if not str(fuente.get(req, "")).strip():
            raise ValueError(f"Falta '{req}' en la fuente {url}.")
    limpia = {k: fuente[k] for k in CAMPOS_FUENTE if fuente.get(k) not in (None, "")}
    limpia["url"] = url
    limpia.setdefault("consultado", datetime.date.today())
    return limpia


def render_valor(valor) -> str:
    if isinstance(valor, (datetime.date, datetime.datetime)):
        return valor.strftime("%Y-%m-%d")
    texto = str(valor)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", texto) or texto in TIPOS_FUENTE:
        return texto
    return json.dumps(texto, ensure_ascii=False)


def render_bloque(clave: str, items: list) -> str:
    if not items:
        return f"{clave}: []\n"
    lineas = [f"{clave}:"]
    for item in items:
        if isinstance(item, dict):
            primero = True
            for k in CAMPOS_FUENTE:
                if k in item:
                    prefijo = "  - " if primero else "    "
                    lineas.append(f"{prefijo}{k}: {render_valor(item[k])}")
                    primero = False
        else:
            lineas.append(f"  - {render_valor(item)}")
    return "\n".join(lineas) + "\n"


def quitar_bloque(fm: str, clave: str) -> str:
    """Elimina `clave:` y sus líneas indentadas del frontmatter."""
    return re.sub(rf"(?m)^{clave}:.*\n(?:(?:[ \t]+.*|[ \t]*)\n)*", "", fm)


def actualizar_nota(path: str, fuentes_nuevas: list, estado: str | None, alertas: list | None,
                    resueltas: list | None = None, dry_run: bool = False) -> str:
    with open(path, "r", encoding="utf-8") as f:
        contenido = f.read()

    m = re.match(r"^---\n(.*?\n)---\n(.*)$", contenido, re.DOTALL)
    if not m:
        raise ValueError(f"[{path}] Sin frontmatter YAML.")
    fm, body = m.group(1), m.group(2)
    meta = yaml.safe_load(fm) or {}

    existentes = list(meta.get("fuentes") or [])
    urls = {str(x.get("url")) for x in existentes if isinstance(x, dict)}
    for fuente in fuentes_nuevas:
        limpia = validar_fuente(fuente)
        if limpia["url"] not in urls:
            existentes.append(limpia)
            urls.add(limpia["url"])

    alertas_finales = [
        a for a in meta.get("alertas_verificacion") or []
        if not any(r.lower() in str(a).lower() for r in resueltas or [])
    ]
    for a in alertas or []:
        if a not in alertas_finales:
            alertas_finales.append(a)

    if estado is None:
        estado = meta.get("estado_verificacion") or ("parcial" if existentes else "sin_fuente")
        if estado == "verificado" and not existentes:
            estado = "sin_fuente"
    if estado not in ESTADOS_VERIFICACION:
        raise ValueError(f"estado_verificacion '{estado}' no está en {ESTADOS_VERIFICACION}.")

    for clave in ("fuentes", "alertas_verificacion", "estado_verificacion"):
        fm = quitar_bloque(fm, clave)

    bloque = f"estado_verificacion: {estado}\n" + render_bloque("fuentes", existentes)
    if alertas_finales:
        bloque += render_bloque("alertas_verificacion", alertas_finales)

    if re.search(r"(?m)^tags:", fm):
        fm = re.sub(r"(?m)^tags:", lambda _: bloque + "tags:", fm, count=1)
    else:
        fm += bloque

    if "## Fuentes Verificables" not in body:
        body = body.rstrip("\n") + "\n" + SECCION_FUENTES

    nuevo = f"---\n{fm}---\n{body}"
    yaml.safe_load(fm)  # garantiza que el frontmatter resultante siga siendo YAML válido
    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(nuevo)
    return os.path.relpath(path, ROOT_DIR)


def main() -> int:
    parser = argparse.ArgumentParser(description="Agrega fuentes verificables a notas del vault.")
    parser.add_argument("--nota", help="Nombre o ruta relativa de la nota")
    parser.add_argument("--url")
    parser.add_argument("--titulo")
    parser.add_argument("--medio")
    parser.add_argument("--tipo", choices=TIPOS_FUENTE)
    parser.add_argument("--fecha", help="Fecha de publicación del documento (YYYY-MM-DD)")
    parser.add_argument("--archivo", help="Copia archivada (web.archive.org / archive.ph)")
    parser.add_argument("--estado", choices=ESTADOS_VERIFICACION)
    parser.add_argument("--alerta", action="append", help="Alerta de verificación (repetible)")
    parser.add_argument("--resolver-alerta", action="append",
                        help="Elimina las alertas que contengan este texto (repetible)")
    parser.add_argument("--desde-yaml", help="Archivo YAML con un lote de fuentes por nota")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    lote: dict = {}
    if args.desde_yaml:
        with open(args.desde_yaml, "r", encoding="utf-8") as f:
            lote = yaml.safe_load(f) or {}
    elif args.nota:
        fuentes = []
        if args.url:
            fuentes.append({"url": args.url, "titulo": args.titulo, "medio": args.medio,
                            "tipo": args.tipo, "fecha": args.fecha, "archivo": args.archivo})
        lote = {args.nota: {"fuentes": fuentes, "estado_verificacion": args.estado,
                            "alertas": args.alerta, "resueltas": args.resolver_alerta}}
    else:
        parser.error("Indique --nota o --desde-yaml.")

    errores = 0
    for nota, spec in lote.items():
        try:
            rel = actualizar_nota(find_note(nota), spec.get("fuentes") or [],
                                  spec.get("estado_verificacion"), spec.get("alertas"),
                                  spec.get("resueltas"), dry_run=args.dry_run)
            n = len(spec.get("fuentes") or [])
            print(f"[OK] {rel}: +{n} fuente(s), estado={spec.get('estado_verificacion') or 'auto'}")
        except (ValueError, FileNotFoundError) as exc:
            errores += 1
            print(f"[X] {nota}: {exc}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
