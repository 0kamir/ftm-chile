#!/usr/bin/env python3
"""
Revisor Preliminar de Riesgo de Difamación con un modelo local (Ollama).
Envía el texto de cada nota a un modelo local y recoge frases que afirman culpabilidad
sin respaldo, contradicen la situación procesal declarada, usan lenguaje peyorativo o
exponen datos personales. Es un filtro de triaje: cada hallazgo debe revisarlo un editor
contra las fuentes antes de modificar la nota. Las frases que no aparecen literalmente
en la nota se descartan (protección contra alucinaciones del modelo).

Uso:
  python3 00_Meta/Scripts/screen_defamation.py [--modelo qwen3:14b] [--carpetas 01_Entidades/Personas ...]
      [--salida 05_Vistas_Analiticas/Revision_Riesgo_Difamacion.md] [--limite N]
"""

import argparse
import json
import os
import re
import sys
import urllib.request

import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
CARPETAS_DEFECTO = ["01_Entidades/Personas", "01_Entidades/Privadas", "02_Causas", "03_Hechos_y_Nexos"]

PROMPT = """Eres un revisor legal chileno experto en difamación (injurias y calumnias) y presunción de inocencia.
Analiza la NOTA y devuelve SOLO JSON: {"hallazgos": [{"frase": "...", "riesgo": "alto|medio", "motivo": "...", "sugerencia": "..."}]}.
Marca únicamente frases que:
1. Afirman como hecho probado un delito ("acreditó", "pagó sobornos", "lavó", "defraudó") cuando la situación procesal NO es condenado o la causa no tiene sentencia.
2. Contradicen la situación procesal declarada en METADATOS (p. ej. dicen "condenado" y el campo dice absuelto/formalizado/acusado).
3. Usan lenguaje peyorativo o calificativos no judiciales ("criminal", "cartel", "clan criminal", "red de corrupción", "mafia", "testaferro") sobre personas sin condena.
4. Exponen datos personales o de la vida íntima/familiar ajenos al hecho de interés público.
5. Atribuyen a una persona hechos de terceros o montos totales de una causa colectiva.
Reglas: "frase" debe copiarse LITERALMENTE de la nota (máx. 300 caracteres). No marques frases que ya dicen "según la Fiscalía", "presunto", "habría", "acusación" o que describen una condena firme declarada en METADATOS. Si no hay problemas devuelve {"hallazgos": []}."""


def load_note(path: str) -> tuple[dict, str]:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not m:
        return {}, content
    meta = yaml.safe_load(m.group(1)) or {}
    body = re.sub(r"```.*?```", "", m.group(2), flags=re.DOTALL)
    body = re.sub(r"(?m)^- \*\*[^*]+\*\*: `= this\.[^`]+`.*$", "", body)
    return meta, re.sub(r"\n{3,}", "\n\n", body).strip()


def ask_model(modelo: str, meta: dict, body: str) -> list[dict]:
    resumen_meta = {k: meta.get(k) for k in (
        "tipo_nodo", "situacion_procesal", "medida_cautelar", "estado_judicial", "delito_imputado", "estado_verificacion")
        if meta.get(k) not in (None, "")}
    payload = {
        "model": modelo,
        "stream": False,
        "format": "json",
        "think": False,
        "options": {"temperature": 0, "num_ctx": 8192},
        "messages": [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": f"METADATOS: {json.dumps(resumen_meta, ensure_ascii=False, default=str)}\n\nNOTA:\n{body[:12000]}"},
        ],
    }
    req = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        data = json.loads(resp.read())
    try:
        hallazgos = json.loads(data["message"]["content"]).get("hallazgos", [])
    except (json.JSONDecodeError, AttributeError, KeyError):
        return []
    return [h for h in hallazgos if isinstance(h, dict)]


def normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", texto.replace("*", "").replace("`", "")).strip().lower()


def main() -> int:
    parser = argparse.ArgumentParser(description="Triaje de riesgo de difamación con un modelo local (Ollama).")
    parser.add_argument("--modelo", default="qwen3:14b")
    parser.add_argument("--carpetas", nargs="+", default=CARPETAS_DEFECTO)
    parser.add_argument("--salida", default="05_Vistas_Analiticas/Revision_Riesgo_Difamacion.md")
    parser.add_argument("--json", help="Ruta opcional para volcar los hallazgos en JSON")
    parser.add_argument("--limite", type=int, default=0, help="Procesar solo N notas (prueba)")
    args = parser.parse_args()

    notas = []
    for carpeta in args.carpetas:
        base = os.path.join(ROOT_DIR, carpeta)
        notas += [os.path.join(base, f) for f in sorted(os.listdir(base)) if f.endswith(".md")]
    if args.limite:
        notas = notas[: args.limite]

    resultados: dict[str, list[dict]] = {}
    descartados = 0
    for i, path in enumerate(notas, 1):
        rel = os.path.relpath(path, ROOT_DIR)
        meta, body = load_note(path)
        if not body:
            continue
        try:
            hallazgos = ask_model(args.modelo, meta, body)
        except Exception as exc:  # noqa: BLE001 - se informa y se continúa
            print(f"[{i}/{len(notas)}] [X] {rel}: {exc}", file=sys.stderr)
            continue
        cuerpo_norm = normalizar(body)
        validos = []
        for h in hallazgos:
            frase = str(h.get("frase", ""))
            if frase and normalizar(frase) in cuerpo_norm:
                validos.append(h)
            else:
                descartados += 1
        if validos:
            resultados[rel] = validos
        print(f"[{i}/{len(notas)}] {rel}: {len(validos)} hallazgo(s)", flush=True)

    altos = sum(1 for hs in resultados.values() for h in hs if h.get("riesgo") == "alto")
    lineas = [
        "---", "tipo_nodo: vista_analitica", "tags:", "  - vista/revision-legal", "---", "",
        "# Revisión Preliminar de Riesgo de Difamación", "",
        f"> Triaje automático con el modelo local `{args.modelo}` (Ollama). **No es un dictamen**: cada hallazgo "
        "debe contrastarse con las fuentes antes de editar la nota. Se descartaron "
        f"{descartados} frases que el modelo no copió literalmente.", "",
        f"Notas revisadas: {len(notas)} · Notas con hallazgos: {len(resultados)} · Riesgo alto: {altos}", "",
    ]
    for rel, hs in sorted(resultados.items()):
        nombre = os.path.splitext(os.path.basename(rel))[0]
        lineas.append(f"## [[{nombre}]]")
        for h in sorted(hs, key=lambda x: x.get("riesgo") != "alto"):
            lineas.append(f"- **{h.get('riesgo', '?')}** — {h.get('motivo', '')}")
            lineas.append(f"  - Frase: “{h.get('frase')}”")
            if h.get("sugerencia"):
                lineas.append(f"  - Sugerencia: {h['sugerencia']}")
        lineas.append("")
    with open(os.path.join(ROOT_DIR, args.salida), "w", encoding="utf-8") as f:
        f.write("\n".join(lineas) + "\n")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=1)
    print(f"Revisión generada: {args.salida} ({len(resultados)} notas con hallazgos, {altos} de riesgo alto)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
