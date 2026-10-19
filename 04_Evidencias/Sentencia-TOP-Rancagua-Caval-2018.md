---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TOP-RAN-2018-001"
tipo_documento: "Sentencia Definitiva Condenatoria Tribunal de Juicio Oral en lo Penal de Rancagua"
fecha_emision: 2018-07-11
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Querellas Servicio de Impuestos Internos y CDE"
causa_vinculada: "[[Caso Caval]]"
nexo_respaldado: "[[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
    titulo: "Lectura de sentencia Caso Caval"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2018-07-11
    consultado: 2026-10-19
  - url: "https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/"
    titulo: "Natalia Compagnon fue condenada por delito tributario"
    medio: "CNN Chile"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-caval
---

# Sentencia-TOP-Rancagua-Caval-2018

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor` (Tribunal de Juicio Oral en lo Penal de Rancagua)
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (y [[TRX-2014-02-18-Soborno-Caval-Machali-01]])

## Extracto y Relevancia Probatoria
Sentencias dictadas en el marco del [[Caso Caval]] (RUC `1500169916-0`) que condenaron a [[Natalia Compagnon Soto]] por delito tributario ante el [[Servicio Impuestos Internos]] ([[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]]) y absolvieron a su socio [[Mauricio Valero Illanes]] y a [[Exportadora y de Gestion Caval Ltda]] (TOP de Rancagua, julio de 2018), así como, en sentencia separada de enero de 2018, al ex Director de Obras Municipales de la [[Municipalidad de Machali]], [[Jorge Silva Menares]], por el delito de [[Cohecho]] reiterado en el proceso de cambio del Plan Regulador Intercomunal ([[TRX-2014-02-18-Soborno-Caval-Machali-01]]).

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
