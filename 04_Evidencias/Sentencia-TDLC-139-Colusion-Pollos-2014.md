---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TDLC-139-2014"
tipo_documento: "Sentencia N° 139/2014 del Tribunal de Defensa de la Libre Competencia (Rol C-236-11)"
fecha_emision: 2014-09-25
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Tribunal de Defensa de la Libre Competencia (tdlc.cl) / Fiscalía Nacional Económica"
causa_vinculada: "[[Caso Colusion de los Pollos]]"
nexo_respaldado: "[[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
    titulo: "Sentencia TDLC N° 139/2014"
    medio: "TDLC / FNE"
    tipo: primaria
    fecha: 2014-09-25
    consultado: 2026-10-19
  - url: "https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/"
    titulo: "TDLC condenó a Agrosuper, Ariztía y Don Pollo por colusión"
    medio: "Fiscalía Nacional Económica"
    tipo: primaria
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - tdlc
  - colusion-pollos
  - libre-competencia
---

# Sentencia-TDLC-139-Colusion-Pollos-2014

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Sentencia**: `= this.fecha_emision`
- **Tribunal Resolutivo**: Tribunal de Defensa de la Libre Competencia (TDLC)
- **Órgano Jurisdiccional Superior**: `= this.organismo_emisor`
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Sentencia histórica del TDLC que acogió el requerimiento de la [[Fiscalia Nacional Economica]] y condenó a [[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]] por infringir el artículo 3° del D.L. 211, al haberse coludido acordando limitar la producción de carne de pollo en el mercado nacional y asignarse cuotas de producción y faenamiento. 

El fallo ordenó multas millonarias a beneficio fiscal y decretó la **disolución judicial forzosa de la Asociación de Productores Avícolas de Chile A.G.** ([[Asociacion de Productores Avicolas de Chile AG]]), al determinar que actuó como el instrumento coordinador del cartel.

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
