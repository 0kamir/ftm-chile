---
tipo_nodo: nexo_transaccion
fecha: YYYY-MM-DD
tipo_nexo: convenio_directo # convenio_directo | transferencia | cohecho | llamada | reunion_lobby
monto_clp: 0
monto_origen: sin_monto # sentencia | resolucion_administrativa | registro_oficial | estimacion_oficial | acusacion | prensa | no_verificado | sin_monto
entidad_origen: "[[Entidad Origen]]"
entidad_destino: "[[Entidad Destino]]"
firmante_origen: "[[Firmante Origen]]"
firmante_destino: "[[Firmante Destino]]"
causa_vinculada: "[[Causa Vinculada]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Evidencia Soporte]]"
estado_verificacion: pendiente # verificado | parcial | desactualizado | sin_fuente | pendiente
fuentes:
  - "https://"
tags:
  - nexo/transaccion
---

# {{title}}

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

## Descripción de la Operación
Detalle de la transferencia, acto administrativo, fraccionamiento o reunión registrada.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Título del documento o nota](https://) | Medio | `primaria` | YYYY-MM-DD | [copia](https://web.archive.org/) |
