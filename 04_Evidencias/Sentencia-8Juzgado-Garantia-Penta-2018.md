---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-8JG-PEN-2018-001"
tipo_documento: "Sentencia Condenatoria en Procedimiento Abreviado (RIT 6873-2014)"
fecha_emision: 2018-07-09
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Querellas Servicio de Impuestos Internos"
causa_vinculada: "[[Caso Penta]]"
nexo_respaldado: "[[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/"
    titulo: "Délano y Lavín terminaron clases de ética"
    medio: "CNN Chile"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-penta
---

# Sentencia-8Juzgado-Garantia-Penta-2018

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor` (8° Juzgado de Garantía de Santiago)
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (y [[TRX-2011-03-10-Pagos-Penta-Wagner-01]])

## Extracto y Relevancia Probatoria
Sentencia dictada por el 8° Juzgado de Garantía de Santiago (RIT `6873-2014`, RUC `1400637392-6`) en el [[Caso Penta]], que condenó a los controladores de [[Empresas Penta SA]], [[Carlos Alberto Delano Abbott]] y [[Carlos Eugenio Lavin Garcia-Huidobro]], como autores de delitos tributarios reiterados previstos en el artículo 97 N° 4 del Código Tributario denunciados por el [[Servicio Impuestos Internos]] ([[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]]), y al ex Subsecretario [[Pablo Wagner San Martin]] por enriquecimiento ilícito y delitos tributarios derivados de los pagos recibidos mientras ejercía su cargo público ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]).

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
