---
tipo_nodo: nexo_transaccion
fecha: 2020-07-08
tipo_nexo: transferencia
monto_clp: 180000000
entidad_origen: "[[Itelecom Holding Chile SpA]]"
entidad_destino: "[[Factop SpA]]"
firmante_origen: "[[Leon Marcelo Lefort Hernandez]]"
firmante_destino: "[[Luis Hermosilla Osorio]]"
causa_vinculada: "[[Caso Luminarias LED]]"
delito_imputado: "[[Lavado de Activos]]"
evidencia_soporte: "[[Sentencia-TOP-Chillan-Luminarias-2023]]"
tags:
  - nexo/transaccion
  - transferencia
  - caso-luminarias-led
  - caso-audios
  - nexo-puente
---

# TRX-2020-07-08-Asesoria-Itelecom-Hermosilla-01

## Ficha de Arista Reificada (Nexo Puente Inter-Causal: Itelecom ↔ Hermosilla)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad / Entorno Destino**: `= this.entidad_destino`
- **Controlador Emisor**: `= this.firmante_origen`
- **Abogado Receptor**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada` (en cruce con [[Caso Audios]])
- **Hipótesis Penal**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Flujos financieros y pagos de honorarios/asesorías por **$180.000.000 CLP** entre [[Itelecom Holding Chile SpA]] (controlada por [[Leon Marcelo Lefort Hernandez]]) y el abogado [[Luis Hermosilla Osorio]], que conectan topológicamente el subgrafo de corrupción municipal del [[Caso Luminarias LED]] con la red financiera y judicial del [[Caso Audios]].
