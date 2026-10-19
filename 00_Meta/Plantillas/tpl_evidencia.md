---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-ORGANISMO-ROL-AAAA"
tipo_documento: ""
fecha_emision: YYYY-MM-DD
organismo_emisor: "[[Organismo Emisor]]"
fuente_osint: ""
causa_vinculada: "[[Causa Vinculada]]"
nexo_respaldado: "[[Nexo Respaldado]]"
estado_verificacion: pendiente # verificado | parcial | desactualizado | sin_fuente | pendiente
fuentes:
  - url: "https://"
    titulo: ""
    medio: ""
    tipo: primaria # primaria (documento oficial) | secundaria (prensa / academia)
    fecha: YYYY-MM-DD
    archivo: "https://web.archive.org/"
    consultado: YYYY-MM-DD
tags:
  - evidencia
---

# {{title}}

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Emisor**: `= this.organismo_emisor`
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Qué acredita el documento, citando textualmente los pasajes relevantes y su ubicación (página, considerando, numeral).

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
