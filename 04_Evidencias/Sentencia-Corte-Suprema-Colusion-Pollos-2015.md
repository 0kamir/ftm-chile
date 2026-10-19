---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-27175-2014"
tipo_documento: "Sentencia de la Corte Suprema en Recurso de Reclamación Rol N° 27.175-2014"
fecha_emision: 2015-10-29
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Fiscalía Nacional Económica"
causa_vinculada: "[[Caso Colusion de los Pollos]]"
nexo_respaldado: "[[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf"
    titulo: "Sentencia Corte Suprema Rol 27.181-2014"
    medio: "Corte Suprema (vía FNE)"
    tipo: primaria
    fecha: 2015-10-29
    consultado: 2026-10-19
  - url: "https://tdlc.cl/wp-content/uploads/sentencias/Sentencia_139_Corte_Suprema.pdf"
    titulo: "Sentencia 139 - Corte Suprema"
    medio: "TDLC"
    tipo: primaria
    consultado: 2026-10-19
alertas_verificacion:
  - "El rol del fallo publicado por la FNE es 27.181-2014; la nota usa 27.175-2014 en id_evidencia."
tags:
  - evidencia/sentencia
  - corte-suprema
  - libre-competencia
  - colusion-pollos
---

# Sentencia-Corte-Suprema-Colusion-Pollos-2015

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Sentencia Definitiva**: `= this.fecha_emision`
- **Tribunal Resolutivo Superior**: `= this.organismo_emisor` (Tercera Sala de la Corte Suprema)
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Sentencia definitiva y ejecutoriada dictada por la Tercera Sala de la [[Corte Suprema de Chile]] que desestimó los recursos de reclamación de las empresas y ratificó la condena por colusión. La Corte elevó al máximo legal las sanciones pecuniarias, imponiendo 30.000 UTA a [[Agrosuper SA]], 30.000 UTA a [[Empresas Ariztia SA]] y 12.000 UTA a [[Agricola Don Pollo Limitada]], acumulando 72.000 UTA (más de US$ 60 millones / $38.400 millones de pesos), ratificando a su vez la disolución forzada de la [[Asociacion de Productores Avicolas de Chile AG]].

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
