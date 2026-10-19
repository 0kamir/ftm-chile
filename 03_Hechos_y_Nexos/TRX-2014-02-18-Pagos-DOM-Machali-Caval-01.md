---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2014-02-18-Pagos-DOM-Machali-Caval-01"
fecha: 2014-02-18
tipo_nexo: cohecho_soborno
monto_clp: 55030792
monto_origen: sentencia
metodo_adjudicacion: no_aplica
entidad_origen: ""
entidad_destino: "[[Municipalidad de Machali]]"
firmante_origen: ""
firmante_destino: "[[Jorge Silva Menares]]"
delito_imputado: "[[Cohecho]]"
causa_vinculada: "[[Caso Caval]]"
evidencia_soporte: "[[Sentencia-TOP-Rancagua-Caval-2018]]"
estado_verificacion: verificado
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
  - url: "https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/"
    titulo: "Caso Caval: 818 días remitidos y multa de 55 millones para segundo condenado"
    medio: "Radio Agricultura"
    tipo: secundaria
    fecha: 2018-01-28
    consultado: 2026-10-19
historial_correcciones:
  - "Corregido el 2026-10-19: el pago acreditado ($55.030.792) lo hizo Juan Díaz, no Caval; monto previo de $140 millones sin respaldo."
tags:
  - nexo/cohecho
  - caso-caval
---

# TRX-2014-02-18-Pagos-DOM-Machali-Caval-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$140.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante / Autorizador de Origen**: `= this.firmante_origen`
- **Funcionario Receptor**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Pagos directos o indirectos por **`$55.030.792 CLP`** del operador político y gestor inmobiliario Juan Díaz al entonces Director de Obras Municipales de la [[Municipalidad de Machali]], [[Jorge Silva Menares]], vinculados al cambio de uso de suelo de predios que luego adquirió [[Exportadora y de Gestion Caval Ltda]]. Silva fue condenado en procedimiento abreviado (enero de 2018) a 818 días con remisión condicional por cohecho reiterado. La acusación de soborno contra [[Mauricio Valero Illanes]] y la sociedad Caval **fue rechazada**: ambos fueron absueltos por el TOP de Rancagua en julio de 2018.

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
