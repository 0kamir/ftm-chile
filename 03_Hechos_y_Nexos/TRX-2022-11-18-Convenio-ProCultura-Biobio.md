---
tipo_nodo: nexo_transaccion
fecha: 2022-11-18
tipo_nexo: convenio_directo
monto_clp: 2553000000
monto_origen: acusacion
entidad_origen: "[[GORE Biobio]]"
entidad_destino: "[[Fundacion ProCultura]]"
firmante_origen: "[[Rodrigo Diaz Worner]]"
firmante_destino: "[[Alberto Larrain Salas]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-GORE-Biobio-EnTi-2022]]"
tags:
  - nexo/transaccion
  - convenio-directo
  - caso-convenios
  - procultura
---

# TRX-2022-11-18-Convenio-ProCultura-Biobio

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
Convenio de transferencia directa suscrito entre el [[GORE Biobio]] (administración de [[Rodrigo Diaz Worner]]) y [[Fundacion ProCultura]] ([[Alberto Larrain Salas]]) por **$2.553.000.000 CLP** para el programa "Competitividad por medio de la Innovación Creativa y Cultural", investigado en el [[Caso Convenios]] por [[Fraude al Fisco]]. Este nexo une topológicamente la red del Biobío con la red de Antofagasta.
