---
tipo_nodo: nexo_transaccion
fecha: 2022-10-03
tipo_nexo: convenio_directo
monto_clp: 200000000
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

# TRX-2022-10-03-Convenio-DV-01

## Ficha de Arista Reificada (Transacción / Hecho — Convenio I de III)
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
**Primer convenio de transferencia directa** ($200.000.000 CLP, equivalente a ~3.316 UTM de octubre de 2022) para obras de habitabilidad primaria en el Campamento Irarrázaval Etapa I (Antofagasta), suscrito entre la [[Seremi MINVU Antofagasta]] ([[Carlos Contreras Gutierrez]]) y la [[Fundacion Democracia Viva]] ([[Daniel Andrade Schwarze]]).

Junto con [[TRX-2022-10-19-Convenio-DV-02]] ($170.000.000 CLP) y [[TRX-2022-11-29-Convenio-DV-03]] ($56.000.000 CLP), conforma el paquete fraccionado de **$426.000.000 CLP** (~7.063 UTM) diseñado para que cada resolución individual quedara bajo el umbral de **5.000 UTM** exigido para el trámite de Toma de Razón ante la Contraloría General de la República, documentado en [[Resolucion-Exenta-MINVU-Antofagasta-2022]] e investigado en [[Caso Convenios]].
