---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-FMO-BAS-2017-001"
tipo_documento: "Acusación Fiscal y Autos de Apertura de Juicio Oral (RUC 1100849201-5)"
fecha_emision: 2017-01-18
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Fiscalía Regional Metropolitana Occidente / Querellas CDE"
causa_vinculada: "[[Caso Basura]]"
nexo_respaldado: "[[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf"
    titulo: "Comunicado Fiscalía Occidente Caso Basura"
    medio: "Fiscalía Regional Metropolitana Occidente (vía El Mostrador)"
    tipo: primaria
    fecha: 2025-06-03
    consultado: 2026-10-19
tags:
  - evidencia/acusacion-fiscal
  - caso-basura
---

# Acusacion-Fiscalia-Occidente-CasoBasura-2017

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor` (9° Juzgado de Garantía de Santiago / TOP Santiago)
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (y [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]])

## Extracto y Relevancia Probatoria
Acusación presentada por la Fiscalía Regional Metropolitana Occidente y el Consejo de Defensa del Estado (CDE) en el [[Caso Basura]] (RUC `1100849201-5`), que documentó mediante interceptaciones telefónicas, peritajes contables de la PDI y alzamientos de secreto bancario la red de pagos desde [[KDM Empresas SA]] ([[Fernando Leon Steffens]]) hacia [[Marcelo Torres Ferrari]] en la [[Municipalidad de Maipu]] ([[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]]) y los contratos irregulares ejecutados junto al exalcalde [[Luis Plaza Sanchez]] en la [[Municipalidad de Cerro Navia]] ([[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]]).

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
