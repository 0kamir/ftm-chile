#!/usr/bin/env python3
"""
Incorporador y Sincronizador de Fuentes OSINT a notas del vault (cadena de custodia documental).
Agrega fuentes verificables (URL) al bloque YAML `fuentes:` de una nota, actualiza
`estado_verificacion`, registra alertas de verificación y renderiza una tabla Markdown
con enlaces `[Título](https://...)` directamente clickeables bajo `## Fuentes Verificables`
(accesible en Obsidian sin depender de Dataview, en GitHub, en VS Code y en exportaciones).

Uso (una fuente):
  python3 00_Meta/Scripts/add_source.py --nota "Caso Caval" \
      --url https://www.biobiochile.cl/... --titulo "Lectura de sentencia" \
      --medio "BioBioChile" --tipo secundaria --fecha 2018-07-11 [--estado verificado]

Resolver una alerta ya atendida (coincidencia por texto):
  python3 00_Meta/Scripts/add_source.py --nota "Caso Caval" --resolver-alerta "Valero"

Uso (lote desde YAML {ruta_nota: {fuentes: [...], estado_verificacion, alertas: [...], resueltas: [...]}}):
  python3 00_Meta/Scripts/add_source.py --desde-yaml lote.yaml [--dry-run]

Sincronizar y propagar fuentes verificadas a todos los nodos del grafo (TRX, Entidades, Delitos):
  python3 00_Meta/Scripts/add_source.py --sync [--dry-run]
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
ORIGENES_MONTO = (
    "sentencia",
    "resolucion_administrativa",
    "registro_oficial",
    "estimacion_oficial",
    "acusacion",
    "prensa",
    "no_verificado",
    "sin_monto",
)
CAMPOS_FUENTE = ("url", "titulo", "medio", "tipo", "fecha", "archivo", "consultado")

# Fuentes normativas e institucionales base para nodos legales/estructurales
FUENTES_BASE_NODOS = {
    "Asociacion Ilicita": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículos 292, 293 y 294 (Asociación Ilícita)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Cohecho": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículos 248, 248 bis, 249 y 250 (Cohecho y Soborno)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Colusion y Atentado a la Libre Competencia": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=5872",
            "titulo": "Decreto Ley N° 211 — Defensa de la Libre Competencia (Art. 3° y Art. 62)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1973-12-22",
        },
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1094077",
            "titulo": "Ley N° 20.945 — Perfecciona el Sistema de Defensa de la Libre Competencia y tipifica la colusión",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "2016-08-30",
        },
    ],
    "Delito Tributario": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=6374",
            "titulo": "Código Tributario (D.L. N° 830) — Artículo 97 N° 4 (Delitos Tributarios)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1974-12-31",
        }
    ],
    "Falsificacion de Instrumento Publico": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículos 193, 194 y 196 (Falsificación de Instrumento Público)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Fraude al Fisco": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículo 239 (Fraude al Fisco)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Lavado de Activos": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=219119",
            "titulo": "Ley N° 19.913 — Crea la Unidad de Análisis Financiero y modifica normas sobre Lavado de Activos (Art. 27)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "2003-12-18",
        }
    ],
    "Malversacion de Caudales Publicos": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículo 233 (Malversación de Caudales Públicos)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Negociacion Incompatible": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículo 240 (Negociación Incompatible)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Obstruccion a la Investigacion": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículo 269 bis (Obstrucción a la Investigación)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Trafico de Influencias": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículo 240 bis (Tráfico de Influencias)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Violacion de Secreto": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=1984",
            "titulo": "Código Penal de Chile — Artículos 246 y 247 (Violación de Secreto)",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "1874-11-12",
        }
    ],
    "Direccion ChileCompra": [
        {
            "url": "https://www.bcn.cl/leychile/navegar?idNorma=213004",
            "titulo": "Ley N° 19.886 — Ley de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios",
            "medio": "Biblioteca del Congreso Nacional (BCN LeyChile)",
            "tipo": "primaria",
            "fecha": "2003-07-30",
        },
        {
            "url": "https://datos-abiertos.chilecompra.cl/",
            "titulo": "Portal de Datos Abiertos de ChileCompra y Mercado Público",
            "medio": "Dirección ChileCompra",
            "tipo": "primaria",
            "fecha": "2024-01-01",
        },
    ],
    "Loreto Letelier": [
        {
            "url": "https://www.t13.cl/noticia/politica/udi-manda-tribunal-supremo-candidaturas-loreto-letelier-y-rodrigo-perez",
            "titulo": "UDI manda al Tribunal Supremo candidaturas de Loreto Letelier y Rodrigo Pérez",
            "medio": "T13",
            "tipo": "secundaria",
            "fecha": "2017-10-02",
        },
        {
            "url": "https://www.cnnchile.com/pais/las-reacciones-tras-los-dichos-de-loreto-letelier-sobre-el-caso-quemados/",
            "titulo": "Las reacciones tras los dichos de Loreto Letelier sobre el caso Quemados",
            "medio": "CNN Chile",
            "tipo": "secundaria",
            "fecha": "2017-09-27",
        },
    ],
    "Partido Comunista de Chile": [
        {
            "url": "https://www.servel.cl/partidos-politicos/partidos-constituidos/",
            "titulo": "Registro de Partidos Políticos Constituidos — Servicio Electoral de Chile",
            "medio": "Servel",
            "tipo": "primaria",
            "fecha": "2024-01-01",
        }
    ],
    "Partido Socialista de Chile": [
        {
            "url": "https://www.servel.cl/partidos-politicos/partidos-constituidos/",
            "titulo": "Registro de Partidos Políticos Constituidos — Servicio Electoral de Chile",
            "medio": "Servel",
            "tipo": "primaria",
            "fecha": "2024-01-01",
        }
    ],
}


def render_seccion_fuentes(fuentes: list) -> str:
    """Renderiza una tabla Markdown estática con links URL directamente clickeables y respaldo Wayback."""
    lineas = [
        "## Fuentes Verificables",
        "",
        "| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |",
        "| :--- | :--- | :---: | :---: | :---: |",
    ]
    for f in fuentes:
        if not isinstance(f, dict) or not f.get("url"):
            continue
        url = str(f.get("url", "")).strip()
        titulo = str(f.get("titulo") or url).replace("|", "\\|").strip()
        medio = str(f.get("medio") or "—").replace("|", "\\|").strip()
        tipo = f"`{f.get('tipo')}`" if f.get("tipo") else "—"
        fecha = str(f.get("fecha") or f.get("consultado") or "—")
        archivo_url = str(f.get("archivo") or "").strip()
        if archivo_url.startswith(("http://", "https://")):
            archivo = f"[copia]({archivo_url})"
        else:
            archivo = f"[Wayback ↺](https://web.archive.org/web/*/{url})"
        lineas.append(f"| [{titulo}]({url}) | {medio} | {tipo} | {fecha} | {archivo} |")
    return "\n" + "\n".join(lineas) + "\n"


def parse_fuentes_from_note(meta: dict, body: str = "") -> list[dict]:
    """
    Extrae la lista enriquecida de fuentes ({url, titulo, medio, tipo, fecha, archivo})
    combinando el bloque YAML `fuentes:` (que puede ser lista de URLs para compatibilidad
    visual con Propiedades de Obsidian o lista de dicts) con la tabla Markdown `## Fuentes Verificables`.
    """
    by_url: dict[str, dict] = {}

    # 1. Extraer metadatos enriquecidos desde la tabla Markdown ## Fuentes Verificables
    if body and "## Fuentes Verificables" in body:
        sec = body.split("## Fuentes Verificables", 1)[1]
        for line in sec.splitlines():
            line = line.strip()
            if not line.startswith("|") or line.startswith("| :---") or "Fuente (Link URL)" in line:
                continue
            cols = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
            if len(cols) < 4:
                continue
            m_link = re.search(r"\[(.+?)\]\((https?://[^\s)]+)\)", cols[0])
            if not m_link:
                continue
            titulo = m_link.group(1).replace("\\|", "|").strip()
            url = m_link.group(2).strip()
            medio = cols[1].replace("\\|", "|").strip()
            tipo_raw = cols[2].strip("` ").lower()
            tipo = tipo_raw if tipo_raw in TIPOS_FUENTE else "secundaria"
            fecha = cols[3].strip()
            entry: dict = {"url": url, "titulo": titulo, "medio": medio, "tipo": tipo}
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", fecha):
                entry["fecha"] = fecha
            if len(cols) >= 5:
                m_arch = re.search(r"\[copia\]\((https?://[^\s)]+)\)", cols[4])
                if m_arch:
                    entry["archivo"] = m_arch.group(1).strip()
            by_url[url] = entry

    # 2. Combinar con el orden y entradas de meta["fuentes"]
    resultado: list[dict] = []
    seen: set[str] = set()
    for item in meta.get("fuentes") or []:
        if isinstance(item, dict) and item.get("url"):
            u = str(item["url"]).strip()
            merged = {**by_url.get(u, {}), **{k: v for k, v in item.items() if v not in (None, "")}}
            merged["url"] = u
            if u not in seen:
                resultado.append(merged)
                seen.add(u)
        elif isinstance(item, str) and item.strip().startswith(("http://", "https://")):
            u = item.strip()
            if u in by_url:
                entry = by_url[u]
            else:
                entry = {"url": u, "titulo": u, "medio": "Fuente OSINT", "tipo": "secundaria"}
            if u not in seen:
                resultado.append(entry)
                seen.add(u)

    for u, entry in by_url.items():
        if u not in seen:
            resultado.append(entry)
            seen.add(u)

    return resultado


SECCION_FUENTES = render_seccion_fuentes([])


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
        if clave == "fuentes" and isinstance(item, dict) and item.get("url"):
            # En Obsidian Properties (multitext), una lista plana de URLs se muestra como enlaces
            # clickeables limpios en vez de JSON crudo [{"url":...}]. El detalle vive en la tabla Markdown.
            lineas.append(f"  - {render_valor(str(item['url']).strip())}")
        elif isinstance(item, dict):
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


def actualizar_nota(
    path: str,
    fuentes_nuevas: list,
    estado: str | None,
    alertas: list | None,
    resueltas: list | None = None,
    dry_run: bool = False,
) -> str:
    with open(path, "r", encoding="utf-8") as f:
        contenido = f.read()

    m = re.match(r"^---\n(.*?\n)---\n(.*)$", contenido, re.DOTALL)
    if not m:
        raise ValueError(f"[{path}] Sin frontmatter YAML.")
    fm, body = m.group(1), m.group(2)
    meta = yaml.safe_load(fm) or {}

    existentes = [validar_fuente(x) for x in parse_fuentes_from_note(meta, body)]
    urls = {str(x.get("url")) for x in existentes}
    for fuente in fuentes_nuevas:
        limpia = validar_fuente(fuente)
        if limpia["url"] not in urls:
            existentes.append(limpia)
            urls.add(limpia["url"])

    alertas_finales = [
        a
        for a in meta.get("alertas_verificacion") or []
        if not any(r.lower() in str(a).lower() for r in resueltas or [])
    ]
    for a in alertas or []:
        if a not in alertas_finales:
            alertas_finales.append(a)

    if estado is None:
        estado = meta.get("estado_verificacion") or ("verificado" if existentes else "sin_fuente")
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

    # Reemplazar o agregar la sección ## Fuentes Verificables con links Markdown clickeables
    body = re.sub(r"\n*## Fuentes Verificables\n.*$", "", body, flags=re.DOTALL).rstrip("\n")
    if existentes:
        body = body + "\n" + render_seccion_fuentes(existentes)
    else:
        body = body + "\n"

    nuevo = f"---\n{fm}---\n{body}"
    yaml.safe_load(fm)  # garantiza que el frontmatter resultante siga siendo YAML válido
    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(nuevo)
    return os.path.relpath(path, ROOT_DIR)


def _wlinks(val) -> list[str]:
    if val is None:
        return []
    return [x.strip() for x in re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val)) if x.strip()]


def sincronizar_vault(dry_run: bool = False) -> int:
    """
    Sincroniza y propaga fuentes verificadas a todos los nodos del grafo:
    1. Evidencias y Causas mantienen sus fuentes directas.
    2. Aristas reificadas (TRX) heredan las fuentes de su `evidencia_soporte` y `causa_vinculada`.
    3. Entidades (Personas, Públicas, Privadas, Partidos) y Delitos incorporan las fuentes de los
       TRX, Evidencias y Causas en los que participan (más sus fuentes normativas/propias).
    4. Todas las notas regeneran la tabla Markdown `## Fuentes Verificables` con links URL directos.
    """
    carpetas_dominio = (
        "00_Meta/Delitos",
        "01_Entidades",
        "02_Causas",
        "03_Hechos_y_Nexos",
        "04_Evidencias",
        "06_Anexos",
    )
    notes: dict[str, dict] = {}
    for carpeta in carpetas_dominio:
        base = os.path.join(ROOT_DIR, carpeta)
        if not os.path.isdir(base):
            continue
        for dp, _, fns in os.walk(base):
            for fn in sorted(fns):
                if not fn.endswith(".md"):
                    continue
                path = os.path.join(dp, fn)
                with open(path, "r", encoding="utf-8") as f:
                    txt = f.read()
                m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.DOTALL)
                if not m:
                    continue
                meta = yaml.safe_load(m.group(1)) or {}
                name = fn[:-3]
                fuentes = [validar_fuente(x) for x in parse_fuentes_from_note(meta, m.group(2))]
                if name in FUENTES_BASE_NODOS:
                    urls = {x["url"] for x in fuentes}
                    for fb in FUENTES_BASE_NODOS[name]:
                        limpia = validar_fuente(fb)
                        if limpia["url"] not in urls:
                            fuentes.append(limpia)
                            urls.add(limpia["url"])
                notes[name] = {
                    "path": path,
                    "rel": os.path.relpath(path, ROOT_DIR),
                    "meta": meta,
                    "body": m.group(2),
                    "fuentes": fuentes,
                }

    def add_unique(dst_list: list, src_list: list, node_name: str = "", max_items: int = 8) -> None:
        urls = {x["url"] for x in dst_list}
        tokens = [
            w.lower()
            for w in re.findall(r"[a-zA-ZáéíóúñÁÉÍÓÚÑ]{4,}", node_name)
            if w.lower()
            not in (
                "caso",
                "fundacion",
                "empresa",
                "empresas",
                "partido",
                "chile",
                "nacional",
                "ministerio",
                "municipalidad",
                "sociedad",
                "corporacion",
            )
        ]

        def score(f: dict) -> tuple[int, int]:
            haystack = (str(f.get("titulo", "")) + " " + str(f.get("url", ""))).lower()
            matches = sum(1 for t in tokens if t in haystack)
            is_prim = 1 if f.get("tipo") == "primaria" else 0
            return (-matches, -is_prim)

        ordered = sorted(src_list, key=score) if tokens else src_list
        for f in ordered:
            if len(dst_list) >= max_items:
                break
            if f["url"] not in urls:
                dst_list.append(f)
                urls.add(f["url"])

    # Paso 1: Propagar a TRX desde evidencia_soporte y causa_vinculada
    for name, n in notes.items():
        if n["meta"].get("tipo_nodo") == "nexo_transaccion":
            candidatas = []
            for k in ("evidencia_soporte", "causa_vinculada"):
                for target in _wlinks(n["meta"].get(k)):
                    if target in notes:
                        candidatas.extend(notes[target]["fuentes"])
            add_unique(n["fuentes"], candidatas, node_name=name, max_items=8)

    # Paso 2: Propagar a Entidades (Personas, Públicas, Privadas, Partidos) desde TRX, Evidencias y Causas
    for name, n in notes.items():
        if n["rel"].startswith("01_Entidades/"):
            candidatas = []
            # Desde representante_legal si existe
            for rep in _wlinks(n["meta"].get("representante_legal")):
                if rep in notes:
                    candidatas.extend(notes[rep]["fuentes"])
            # Desde TRX donde la entidad es origen/destino/firmante
            for tn in notes.values():
                if tn["meta"].get("tipo_nodo") == "nexo_transaccion":
                    for k in ("entidad_origen", "entidad_destino", "firmante_origen", "firmante_destino"):
                        if name in _wlinks(tn["meta"].get(k)):
                            candidatas.extend(tn["fuentes"])
            # Desde enlaces directos en la nota a Evidencias, Causas o TRX
            all_links = _wlinks(n["body"]) + [x for v in n["meta"].values() for x in _wlinks(v)]
            for target in all_links:
                if target in notes and notes[target]["meta"].get("tipo_nodo") in (
                    "evidencia_documental",
                    "causa_judicial",
                    "nexo_transaccion",
                ):
                    candidatas.extend(notes[target]["fuentes"])
            # Desde Causas o Evidencias que mencionan a esta entidad
            for cn in notes.values():
                if cn["meta"].get("tipo_nodo") in ("evidencia_documental", "causa_judicial"):
                    clinks = _wlinks(cn["body"]) + [x for v in cn["meta"].values() for x in _wlinks(v)]
                    if name in clinks:
                        candidatas.extend(cn["fuentes"])
            add_unique(n["fuentes"], candidatas, node_name=name, max_items=6)

    # Paso 3: Propagar a Partidos desde sus militantes si aún tienen menos de 2 fuentes
    for name, n in notes.items():
        if n["meta"].get("tipo_nodo") == "partido_politico":
            candidatas = []
            for pn in notes.values():
                if pn["meta"].get("tipo_nodo") == "persona" and name in _wlinks(
                    pn["meta"].get("afiliacion_politica")
                ):
                    candidatas.extend(pn["fuentes"])
            add_unique(n["fuentes"], candidatas, node_name=name, max_items=6)

    # Paso 4: Escribir todas las notas con su YAML y tabla Markdown ## Fuentes Verificables
    actualizadas = 0
    for name, n in sorted(notes.items()):
        estado_actual = n["meta"].get("estado_verificacion")
        actualizar_nota(
            n["path"],
            n["fuentes"],
            estado=estado_actual,
            alertas=None,
            resueltas=None,
            dry_run=dry_run,
        )
        actualizadas += 1

    print(f"[OK] Sincronización de fuentes completada en {actualizadas} nodos del vault.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Agrega y sincroniza fuentes verificables en el vault.")
    parser.add_argument("--nota", help="Nombre o ruta relativa de la nota")
    parser.add_argument("--url")
    parser.add_argument("--titulo")
    parser.add_argument("--medio")
    parser.add_argument("--tipo", choices=TIPOS_FUENTE)
    parser.add_argument("--fecha", help="Fecha de publicación del documento (YYYY-MM-DD)")
    parser.add_argument("--archivo", help="Copia archivada (web.archive.org / archive.ph)")
    parser.add_argument("--estado", choices=ESTADOS_VERIFICACION)
    parser.add_argument("--alerta", action="append", help="Alerta de verificación (repetible)")
    parser.add_argument(
        "--resolver-alerta",
        action="append",
        help="Elimina las alertas que contengan este texto (repetible)",
    )
    parser.add_argument("--desde-yaml", help="Archivo YAML con un lote de fuentes por nota")
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Sincroniza y propaga fuentes verificadas y tablas Markdown URL en todos los nodos",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.sync:
        return sincronizar_vault(dry_run=args.dry_run)

    lote: dict = {}
    if args.desde_yaml:
        with open(args.desde_yaml, "r", encoding="utf-8") as f:
            lote = yaml.safe_load(f) or {}
    elif args.nota:
        fuentes = []
        if args.url:
            fuentes.append(
                {
                    "url": args.url,
                    "titulo": args.titulo,
                    "medio": args.medio,
                    "tipo": args.tipo,
                    "fecha": args.fecha,
                    "archivo": args.archivo,
                }
            )
        lote = {
            args.nota: {
                "fuentes": fuentes,
                "estado_verificacion": args.estado,
                "alertas": args.alerta,
                "resueltas": args.resolver_alerta,
            }
        }
    else:
        parser.error("Indique --nota, --desde-yaml o --sync.")

    errores = 0
    for nota, spec in lote.items():
        try:
            rel = actualizar_nota(
                find_note(nota),
                spec.get("fuentes") or [],
                spec.get("estado_verificacion"),
                spec.get("alertas"),
                spec.get("resueltas"),
                dry_run=args.dry_run,
            )
            n = len(spec.get("fuentes") or [])
            print(f"[OK] {rel}: +{n} fuente(s), estado={spec.get('estado_verificacion') or 'auto'}")
        except (ValueError, FileNotFoundError) as exc:
            errores += 1
            print(f"[X] {nota}: {exc}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
