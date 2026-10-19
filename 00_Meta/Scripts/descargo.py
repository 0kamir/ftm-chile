"""Descargo común para los reportes analíticos generados por los scripts del vault."""

DESCARGO_GENERAL = (
    "Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la "
    "estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una "
    "relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y "
    "`estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no "
    "exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación."
)

DESCARGOS_ESPECIFICOS = {
    "similitud": (
        "Los pares listados **no tienen un vínculo documentado**: el algoritmo solo indica que comparten vecinos "
        "en el grafo. Sirven para orientar una búsqueda de fuentes, nunca para afirmar una relación."
    ),
    "agrupamientos": (
        "Un agrupamiento es un conjunto de nodos densamente conectados en el grafo, casi siempre porque aparecen "
        "en la misma causa o expediente. **No es una organización, una asociación ni una red delictiva.**"
    ),
    "robustez": (
        "La simulación elimina nodos del grafo para medir su conectividad. Es un ejercicio matemático y no "
        "describe ni sugiere acciones sobre personas reales."
    ),
    "parentesco": (
        "Un vínculo familiar **no implica participación** en ningún hecho. Se registra solo cuando consta en "
        "fuentes públicas y es relevante para entender la red."
    ),
    "montos": (
        "Una desviación estadística en la distribución de montos no prueba manipulación ni fraude; puede deberse "
        "al tamaño reducido de la muestra o a cómo se registraron las cifras."
    ),
    "indicadores": (
        "Los umbrales (por ejemplo, el de toma de razón de la Contraloría) se usan como señales para revisar "
        "documentos, no como determinación de una irregularidad."
    ),
}


def descargo(tipo: str | None = None) -> list[str]:
    """Devuelve las líneas Markdown del descargo para insertar bajo el título de un reporte."""
    lineas = ["> [!WARNING] Análisis exploratorio, no prueba de responsabilidad", f"> {DESCARGO_GENERAL}"]
    if tipo in DESCARGOS_ESPECIFICOS:
        lineas += [">", f"> {DESCARGOS_ESPECIFICOS[tipo]}"]
    return lineas + [""]
