---
tipo_nodo: nexo_transaccion
fecha: 2023-06-22
tipo_nexo: cohecho
monto_clp: 100000000
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Leonarda Villalobos Muth]]"
causa_vinculada: "[[Caso Audios]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
tags:
  - nexo/transaccion
  - cohecho
  - caso-audios
---

# TRX-2023-06-22-Reunion-Audios-01

## Ficha de Arista Reificada (Transacción / Hecho)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante / Operador de Origen**: `= this.firmante_origen`
- **Firmante / Operadora de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Acuerdo y articulación financiera por un monto referencial de **$100.000.000 CLP** ("caja negra") destinado al pago de sobornos a funcionarios públicos del [[Servicio Impuestos Internos]] y la CMF en beneficio de [[Factop SpA]]. El hecho quedó registrado en la grabación [[Audio-Reunion-Edificio-Alonso-2023]], en la que intervienen [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]], constituyendo la pieza probatoria basal del [[Caso Audios]].
