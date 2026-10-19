---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TOP-CHI-2023-001"
tipo_documento: "Sentencia Definitiva Condenatoria Tribunal de Juicio Oral en lo Penal de Chillán"
fecha_emision: 2023-04-28
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial (pjud.cl) / Fiscalía Regional de Ñuble"
causa_vinculada: "[[Caso Luminarias LED]]"
nexo_respaldado: "[[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]"
estado_verificacion: sin_fuente
fuentes: []
alertas_verificacion:
  - "CRÍTICO: no se encontró sentencia del TOP de Chillán en el caso Luminarias. Verificar su existencia o retirar la nota."
tags:
  - evidencia/sentencia-judicial
  - caso-luminarias-led
---

# Sentencia-TOP-Chillan-Luminarias-2023

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Sentencia condenatoria dictada por el Tribunal de Juicio Oral en lo Penal de Chillán (integrante del Poder Judicial encabezado por la [[Corte Suprema de Chile]]) en el [[Caso Luminarias LED]], que condenó a penas efectivas de cárcel a [[Marcelo Campos Henriquez]] por [[Cohecho]] y [[Lavado de Activos]] en la licitación de **$3.200.000.000 CLP** de la [[Municipalidad de Chillan]] ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]) adjudicada a [[Itelecom Holding Chile SpA]] ([[Leon Marcelo Lefort Hernandez]]).

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
