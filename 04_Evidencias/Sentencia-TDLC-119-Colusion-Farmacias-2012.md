---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TDLC-119-2012"
tipo_documento: "Sentencia N° 119/2012 del Tribunal de Defensa de la Libre Competencia (Rol C-184-08)"
fecha_emision: 2012-01-31
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Tribunal de Defensa de la Libre Competencia (tdlc.cl) / Fiscalía Nacional Económica"
causa_vinculada: "[[Caso Colusion de las Farmacias]]"
nexo_respaldado: "[[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
    titulo: "Sentencia TDLC N° 119/2012"
    medio: "CentroCompetencia (copia del fallo)"
    tipo: primaria
    fecha: 2012-01-31
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - tdlc
  - colusion-farmacias
  - libre-competencia
---

# Sentencia-TDLC-119-Colusion-Farmacias-2012

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Sentencia**: `= this.fecha_emision`
- **Tribunal Resolutivo**: Tribunal de Defensa de la Libre Competencia (TDLC)
- **Órgano Jurisdiccional Superior**: `= this.organismo_emisor`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Sentencia de término del TDLC que acogió el requerimiento de la [[Fiscalia Nacional Economica]] en el [[Caso Colusion de las Farmacias]], acreditando que [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]] incurrieron en una práctica concertada para alzar coordinadamente los precios de venta a público de 222 medicamentos entre diciembre de 2007 y marzo de 2008. El tribunal aplicó la sanción máxima legal de 20.000 UTA a cada una de las dos cadenas no acogidas a conciliación.

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
