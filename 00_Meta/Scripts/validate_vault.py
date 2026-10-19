#!/usr/bin/env python3
"""
Auditor y Linter Forense para el Vault OSINT de Corrupción en Chile.
Verifica:
1. Sintaxis estricta de Frontmatter YAML en todas las notas.
2. Cumplimiento de campos obligatorios según `tipo_nodo`.
3. Algoritmo Módulo 11 para todos los RUT chilenos registrados.
4. Integridad referencial de todos los Wikilinks [[...]] (cero enlaces rotos).
5. Cuadratura contable de `monto_clp` en `03_Hechos_y_Nexos/`.
6. Esquema de `fuentes:` (URL, título, medio, tipo) y coherencia con `estado_verificacion`.
   Con `--estricto`, toda causa y evidencia debe tener al menos una fuente con URL.
"""

import os
import re
import sys
import yaml

from add_source import ESTADOS_VERIFICACION, TIPOS_FUENTE

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

REQUIRED_FIELDS = {
    "persona": [
        "rut",
        "aliases",
        "rol_principal",
        "afiliacion_politica",
        "situacion_procesal",
        "medida_cautelar",
    ],
    "entidad_publica": [
        "rut",
        "categoria",
        "region",
        "superior_jerarquico",
    ],
    "entidad_privada": [
        "rut",
        "razon_social",
        "fecha_constitucion",
        "objeto_social",
        "representante_legal",
    ],
    "causa_judicial": [
        "ruc",
        "año_inicio",
        "tribunal_o_fiscalia",
        "fiscal_a_cargo",
        "estado_judicial",
        "delito_principal",
    ],
    "nexo_transaccion": [
        "fecha",
        "tipo_nexo",
        "monto_clp",
        "entidad_origen",
        "entidad_destino",
        "firmante_origen",
        "firmante_destino",
        "causa_vinculada",
        "delito_imputado",
        "evidencia_soporte",
    ],
}


def validar_rut_chileno(rut_str: str) -> bool:
    """Valida el dígito verificador de un RUT chileno mediante Módulo 11."""
    if not rut_str or "-" not in rut_str:
        return False
    limpio = rut_str.upper().replace(".", "").strip()
    partes = limpio.split("-")
    if len(partes) != 2:
        return False
    cuerpo, dv = partes
    if not cuerpo.isdigit():
        return False

    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo = 2 if multiplo == 7 else multiplo + 1

    resto = 11 - (suma % 11)
    dv_calc = "0" if resto == 11 else ("K" if resto == 10 else str(resto))
    return dv == dv_calc


def extract_wikilinks(value) -> list[str]:
    """Extrae nombres de notas enlazadas mediante [[Nota]] o [[Nota|Alias]]."""
    if value is None:
        return []
    text = str(value)
    matches = re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", text)
    return [m.strip() for m in matches if m.strip()]


# Tipos de nodo cuya afirmación debe estar respaldada por al menos una fuente con URL.
TIPOS_CON_FUENTE = ("causa_judicial", "evidencia_documental")


def validar_fuentes(rel_path: str, meta: dict, estricto: bool, errors: list, warnings: list) -> None:
    fuentes = meta.get("fuentes")
    estado = meta.get("estado_verificacion")
    tipo = meta.get("tipo_nodo")

    if estado is not None and estado not in ESTADOS_VERIFICACION:
        errors.append(
            f"[{rel_path}] estado_verificacion '{estado}' fuera del vocabulario {ESTADOS_VERIFICACION}."
        )

    if fuentes is None:
        if tipo in TIPOS_CON_FUENTE:
            (errors if estricto else warnings).append(f"[{rel_path}] Sin bloque 'fuentes:'.")
        return
    if not isinstance(fuentes, list):
        errors.append(f"[{rel_path}] 'fuentes' debe ser una lista.")
        return

    for i, fuente in enumerate(fuentes):
        if not isinstance(fuente, dict):
            errors.append(f"[{rel_path}] fuentes[{i}] debe ser un diccionario.")
            continue
        url = str(fuente.get("url", ""))
        if not re.match(r"^https?://\S+$", url):
            errors.append(f"[{rel_path}] fuentes[{i}] sin URL http(s) válida: {url!r}.")
        if fuente.get("tipo") not in TIPOS_FUENTE:
            errors.append(f"[{rel_path}] fuentes[{i}].tipo debe ser uno de {TIPOS_FUENTE}.")
        for req in ("titulo", "medio"):
            if not str(fuente.get(req, "")).strip():
                errors.append(f"[{rel_path}] fuentes[{i}] sin '{req}'.")

    if estado == "verificado" and not fuentes:
        errors.append(f"[{rel_path}] estado_verificacion=verificado sin ninguna fuente.")
    if not fuentes and tipo in TIPOS_CON_FUENTE:
        (errors if estricto else warnings).append(
            f"[{rel_path}] Sin fuentes verificables (estado: {estado or 'sin declarar'})."
        )


def main(estricto: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    note_index: set[str] = set()
    parsed_notes: dict[str, dict] = {}

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(full_path, ROOT_DIR)
            note_name = os.path.splitext(fname)[0]
            note_index.add(note_name)

            if rel_path == "README.md":
                continue

            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()

            m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
            if not m:
                errors.append(f"[{rel_path}] Sin bloque YAML Frontmatter válido.")
                continue

            try:
                frontmatter = yaml.safe_load(m.group(1))
            except Exception as exc:
                errors.append(f"[{rel_path}] Error de sintaxis YAML: {exc}")
                continue

            if not isinstance(frontmatter, dict):
                errors.append(f"[{rel_path}] El Frontmatter no es un diccionario YAML.")
                continue

            parsed_notes[rel_path] = {
                "meta": frontmatter,
                "body": m.group(2),
                "is_template": rel_path.startswith("00_Meta/Plantillas/"),
            }

    total_clp = 0
    total_nexos = 0
    ruts_validados = 0

    for rel_path, info in sorted(parsed_notes.items()):
        meta = info["meta"]
        is_tpl = info["is_template"]
        tipo = meta.get("tipo_nodo")

        if tipo in REQUIRED_FIELDS:
            for req in REQUIRED_FIELDS[tipo]:
                if req not in meta:
                    errors.append(
                        f"[{rel_path}] Falta propiedad obligatoria '{req}' para tipo_nodo='{tipo}'."
                    )

        if not is_tpl:
            if tipo == "persona" and meta.get("rut"):
                errors.append(
                    f"[{rel_path}] No se publica el RUT de personas naturales (dato personal): dejar rut vacío."
                )
            elif meta.get("rut") and not meta.get("fuentes"):
                errors.append(
                    f"[{rel_path}] RUT sin fuente que lo respalde: agregar la fuente o dejar rut vacío."
                )
            elif "rut" in meta and meta["rut"]:
                rut_val = str(meta["rut"])
                if not validar_rut_chileno(rut_val):
                    errors.append(
                        f"[{rel_path}] RUT inválido según Módulo 11: '{rut_val}'."
                    )
                else:
                    ruts_validados += 1

            if tipo == "nexo_transaccion":
                monto = meta.get("monto_clp")
                if not isinstance(monto, (int, float)) or monto < 0:
                    errors.append(
                        f"[{rel_path}] 'monto_clp' debe ser numérico >= 0 (actual: {monto!r})."
                    )
                else:
                    total_clp += int(monto)
                    total_nexos += 1

            validar_fuentes(rel_path, meta, estricto, errors, warnings)

            # Verificar integridad referencial de todos los wikilinks en el YAML
            for k, v in meta.items():
                for target in extract_wikilinks(v):
                    if target not in note_index:
                        errors.append(
                            f"[{rel_path}] Enlace roto en propiedad YAML '{k}': [[{target}]] no existe en el vault."
                        )

    print("=" * 72)
    print(" AUDITORÍA FORENSE Y VALIDACIÓN DE ESQUEMA DEL VAULT OSINT (CHILE)")
    print("=" * 72)
    print(f" Notas Markdown indexadas : {len(note_index)}")
    print(f" Notas con YAML validadas : {len(parsed_notes)}")
    print(f" RUTs validados (Mód. 11) : {ruts_validados}")
    print(f" Aristas reificadas (TRX) : {total_nexos}")
    print(f" Monto global auditado    : ${total_clp:,.0f} CLP".replace(",", "."))
    print("-" * 72)

    if warnings:
        print(f" ADVERTENCIAS ({len(warnings)}):")
        for w in warnings:
            print(f"  [!] {w}")

    if errors:
        print(f" ERRORES DE INTEGRIDAD DETECTADOS ({len(errors)}):")
        for e in errors:
            print(f"  [X] {e}")
        return 1

    print(" ESTADO: [OK] Cero errores de sintaxis YAML, Módulo 11 o enlaces rotos.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main(estricto="--estricto" in sys.argv))
