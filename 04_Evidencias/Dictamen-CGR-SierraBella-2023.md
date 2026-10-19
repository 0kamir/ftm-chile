---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CGR-SBE-2023-001"
tipo_documento: "Dictamen y Oficio de Fiscalización Contraloría General de la República N° E336249/2023"
fecha_emision: 2023-04-13
organismo_emisor: "[[Contraloria General de la Republica]]"
fuente_osint: "Contraloría General de la República (contraloria.cl) / Expediente RUC 2300094812-3"
causa_vinculada: "[[Caso Sierra Bella]]"
nexo_respaldado: "[[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml"
    titulo: "Contraloría objeta compra de clínica Sierra Bella"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2023-04-13
    consultado: 2026-10-19
tags:
  - evidencia/dictamen-cgr
  - caso-sierra-bella
---

# Dictamen-CGR-SierraBella-2023

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Órgano Fiscalizador Emisor**: `= this.organismo_emisor` (suscrito bajo la dirección de [[Jorge Bermudez Soto]])
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Pronunciamiento oficial de la [[Contraloria General de la Republica]] encabezado por el Contralor General [[Jorge Bermudez Soto]] que concluyó que no se encontraba justificado el precio de **$8.200.000.000 CLP** pactado por la [[Municipalidad de Santiago]] ([[Iraci Hassler Jacob]]) con [[Inmobiliaria San Valentino SpA]] ([[Felipe Sanchez Perez]]) en el [[Caso Sierra Bella]] ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]), advirtiendo vulneraciones al principio de probidad y al resguardo del patrimonio municipal debido a la enorme disparidad respecto del precio de adquisición previa y el avalúo fiscal.

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
