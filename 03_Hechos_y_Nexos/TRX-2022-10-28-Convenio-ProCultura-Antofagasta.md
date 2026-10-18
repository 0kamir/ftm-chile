---
tipo_nodo: nexo_transaccion
fecha: 2022-10-28
tipo_nexo: convenio_directo
monto_clp: 500000000
entidad_origen: "[[Seremi MINVU Antofagasta]]"
entidad_destino: "[[Fundacion ProCultura]]"
firmante_origen: "[[Carlos Contreras Gutierrez]]"
firmante_destino: "[[Alberto Larrain Salas]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-Exenta-MINVU-Antofagasta-2022]]"
tags:
  - nexo/transaccion
  - convenio-directo
  - caso-convenios
  - procultura
---

# TRX-2022-10-28-Convenio-ProCultura-Antofagasta

## Ficha de Arista Reificada (Transacción / Hecho)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante de Origen**: `= this.firmante_origen`
- **Firmante de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Convenios de transferencia directa suscritos en octubre de 2022 entre la [[Seremi MINVU Antofagasta]] ([[Carlos Contreras Gutierrez]]) y [[Fundacion ProCultura]] ([[Alberto Larrain Salas]]) por un total de **$500.000.000 CLP** para habitabilidad primaria en asentamientos precarios y recuperación de fachadas, investigados en el [[Caso Convenios]] por [[Fraude al Fisco]].
