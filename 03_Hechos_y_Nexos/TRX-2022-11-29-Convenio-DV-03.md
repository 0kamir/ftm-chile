---
tipo_nodo: nexo_transaccion
fecha: 2022-11-29
tipo_nexo: convenio_directo
monto_clp: 56000000
monto_origen: resolucion_administrativa
entidad_origen: "[[Seremi MINVU Antofagasta]]"
entidad_destino: "[[Fundacion Democracia Viva]]"
firmante_origen: "[[Carlos Contreras Gutierrez]]"
firmante_destino: "[[Daniel Andrade Schwarze]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-Exenta-MINVU-Antofagasta-2022]]"
tags:
  - nexo/transaccion
  - convenio-directo
  - caso-convenios
  - fraccionamiento-cgr
---

# TRX-2022-11-29-Convenio-DV-03

## Ficha de Arista Reificada (Transacción / Hecho — Convenio III de III)
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
**Tercer convenio de transferencia directa** ($56.000.000 CLP, equivalente a ~920 UTM de noviembre de 2022) para redes húmedas y prevención de incendios en campamentos de Antofagasta, suscrito entre [[Seremi MINVU Antofagasta]] ([[Carlos Contreras Gutierrez]]) y [[Fundacion Democracia Viva]] ([[Daniel Andrade Schwarze]]).

Completa el total exacto de **$426.000.000 CLP** junto a [[TRX-2022-10-03-Convenio-DV-01]] y [[TRX-2022-10-19-Convenio-DV-02]], respaldado en [[Resolucion-Exenta-MINVU-Antofagasta-2022]] e imputado como [[Fraude al Fisco]] reiterado en [[Caso Convenios]].
