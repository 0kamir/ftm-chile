---
tipo_nodo: nexo_transaccion
fecha: 2023-02-09
tipo_nexo: llamada
monto_clp: 0
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Angela Vivanco Martinez]]"
causa_vinculada: "[[Caso Audios]]"
delito_imputado: "[[Trafico de Influencias]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
tags:
  - nexo/transaccion
  - trafico-influencias
  - caso-audios
  - poder-judicial
---

# TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01

## Ficha de Arista Reificada (Gestión Extraprocesal / Llamada y Mensajería)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Nexo de influencia no monetizado directamente en acto administrativo)*
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Operador de Origen**: `= this.firmante_origen`
- **Autoridad de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Intercambio de comunicaciones directas (mensajería y llamadas) extraídas en la pericia forense al dispositivo móvil de [[Luis Hermosilla Osorio]] (incautado a raíz de [[Audio-Reunion-Edificio-Alonso-2023]]) con la entonces ministra de la [[Corte Suprema de Chile]], [[Angela Vivanco Martinez]]. Demuestra cómo la arquitectura de **aristas reificadas** permite modelar nexos de [[Trafico de Influencias]] (`tipo_nexo: llamada`, `monto_clp: 0`) conectando a un mismo operador ([[Luis Hermosilla Osorio]]) tanto con órganos fiscalizadores del Ejecutivo ([[Servicio Impuestos Internos]]) como con el [[Corte Suprema de Chile|Poder Judicial]].
