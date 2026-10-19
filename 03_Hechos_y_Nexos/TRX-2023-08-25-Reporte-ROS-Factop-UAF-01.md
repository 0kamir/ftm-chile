---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2023-08-25-Reporte-ROS-Factop-UAF-01"
fecha: 2023-08-25
tipo_nexo: factura_falsa
monto_clp: 480000000
monto_origen: no_verificado
metodo_adjudicacion: no_aplica
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Unidad de Analisis Financiero]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Javier Cruz Tamburrino]]"
delito_imputado: "[[Lavado de Activos]]"
causa_vinculada: "[[Caso Audios]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
tags:
  - nexo/lavado-activos
  - ros-uaf
  - caso-audios
---

# TRX-2023-08-25-Reporte-ROS-Factop-UAF-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$480.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad Emisora (Origen)**: `= this.entidad_origen`
- **Órgano de Inteligencia Financiera (Destino)**: `= this.entidad_destino`
- **Operador Imputado**: `= this.firmante_origen`
- **Circuito de Trazabilidad UAF**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Operaciones de descuento de facturas ideológicamente falsas y triangulación bancaria ejecutadas a través de [[Factop SpA]] en el circuito de [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] por `$480.000.000 CLP`, cuyos flujos activaron reportes de inteligencia patrimonial ante la [[Unidad de Analisis Financiero]] y la [[Comision para el Mercado Financiero]] en el [[Caso Audios]].
