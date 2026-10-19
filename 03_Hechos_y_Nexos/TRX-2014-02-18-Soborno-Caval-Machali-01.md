---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2014-02-18-Soborno-Caval-Machali-01"
fecha: 2014-02-18
tipo_nexo: cohecho_soborno
monto_clp: 140000000
metodo_adjudicacion: no_aplica
entidad_origen: "[[Exportadora y de Gestion Caval Ltda]]"
entidad_destino: "[[Municipalidad de Machali]]"
firmante_origen: ""
firmante_destino: "[[Jorge Silva Menares]]"
delito_imputado: "[[Cohecho]]"
causa_vinculada: "[[Caso Caval]]"
evidencia_soporte: "[[Sentencia-TOP-Rancagua-Caval-2018]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/"
    titulo: "Caso Caval: el sospechoso historial del destituido director de obras de Machalí"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2015-07-08
    consultado: 2026-10-19
  - url: "https://radio.uchile.cl/?p=478347"
    titulo: "Caso Caval: Tribunal condena a Natalia Compagnon por delito tributario"
    medio: "Radio Universidad de Chile"
    tipo: secundaria
    fecha: 2018-07-11
    consultado: 2026-10-19
alertas_verificacion:
  - "Monto de $140 millones corresponde a la acusación; no verificado en sentencia."
tags:
  - nexo/cohecho
  - caso-caval
---

# TRX-2014-02-18-Soborno-Caval-Machali-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$140.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante / Autorizador de Origen**: `= this.firmante_origen`
- **Funcionario Receptor**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Pagos por un total de `$140.000.000 CLP` (monto de la acusación) recibidos por el entonces Director de Obras Municipales de la [[Municipalidad de Machali]], [[Jorge Silva Menares]], vinculados al cambio de uso de suelo de los predios Santa Elena, San Diego y Santa Cecilia adquiridos por [[Exportadora y de Gestion Caval Ltda]]. Silva fue condenado por cohecho reiterado en enero de 2018. La acusación de soborno contra [[Mauricio Valero Illanes]] y la sociedad **fue rechazada**: ambos fueron absueltos por el TOP de Rancagua en julio de 2018.

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
