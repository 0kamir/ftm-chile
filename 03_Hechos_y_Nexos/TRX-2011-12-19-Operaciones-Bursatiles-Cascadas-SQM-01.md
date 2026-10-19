---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01"
fecha: 2011-12-19
tipo_nexo: desviacion_fondos
monto_clp: 0
metodo_adjudicacion: no_aplica
entidad_origen: "[[Sociedad de Inversiones Pampa Calichera SA]]"
entidad_destino: "[[SQM SA]]"
firmante_origen: "[[Julio Ponce Lerou]]"
firmante_destino: ""
delito_imputado: "[[Negociacion Incompatible]]"
causa_vinculada: "[[Caso Cascadas]]"
evidencia_soporte: "[[Resolucion-SVS-CasoCascadas-2014]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.mch.cl/15-preguntas-para-entender-el-caso-cascada-las-sanciones-y-que-arriesgan-los-involucrados/"
    titulo: "15 preguntas para entender el Caso Cascadas, las sanciones y qué arriesgan los involucrados"
    medio: "Minería Chilena"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - nexo/operacion-bursatil
  - sociedades-cascada
  - caso-cascadas
---

# TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado / Sancionado (CLP)**: `$24.500.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Sociedad Cascada (Origen)**: `= this.entidad_origen`
- **Sociedad Subyacente Controlada (Destino)**: `= this.entidad_destino`
- **Controlador Autorizador**: `= this.firmante_origen`
- **Ejecutivo Receptor en SQM**: `= this.firmante_destino`
- **Infracción / Delito Imputado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Ciclo de compraventas bursátiles trianguladas y préstamos de acciones ejecutados a través de [[Sociedad de Inversiones Pampa Calichera SA]] bajo el control de [[Julio Ponce Lerou]] sobre paquetes accionarios vinculados a [[SQM SA]], sancionados por la [[Comision para el Mercado Financiero]] ([[Carlos Pavez Tolosa]]) en el [[Caso Cascadas]] ([[Resolucion-SVS-CasoCascadas-2014]]) con multas totales de UF 4.010.000 (unos US$ 164 millones) en septiembre de 2014; la SVS estimó un sobrecosto de US$ 300 millones para las sociedades cascada entre 2009 y 2011. La multa de Ponce Lerou (UF 1.700.000) fue rebajada a unas UF 75.000 tras un fallo del Tribunal Constitucional.

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
