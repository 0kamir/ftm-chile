---
tipo_nodo: nexo_transaccion
fecha: 2018-01-25
tipo_nexo: peritaje_forense
monto_clp: 0
entidad_origen: "[[Corte Suprema de Chile]]"
entidad_destino: "[[Direccion de Inteligencia Policial de Carabineros]]"
firmante_origen: "[[Leonardo Osses Sandoval]]"
firmante_destino: "[[Alex Smith Leay]]"
causa_vinculada: "[[Caso Operacion Huracan]]"
delito_imputado: "[[Obstruccion a la Investigacion]]"
evidencia_soporte: "[[Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018]]"
tags:
  - nexo/peritaje
  - operacion-huracan
  - descarte-antorcha
  - cibercrimen
---

# TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01

## Ficha de Arista Reificada (Peritaje Técnico de Descarte y Descubrimiento del Montaje)
- **Fecha del Hito Pericial**: `= this.fecha` *(Enero de 2018)*
- **Tipo de Registro**: `= this.tipo_nexo`
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Diligencia pericial probatoria)*
- **Ámbito Jurisdiccional**: `= this.entidad_origen`
- **Unidad Policial Investigada**: `= this.entidad_destino`
- **Oficial Identificado en Implantación**: `= this.firmante_origen`
- **Autor del Código Fraudulento**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Constatado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
El 25 de enero de 2018, la Fiscalía Regional de La Araucanía remitió al Juzgado de Garantía de Temuco los resultados concluyentes del informe pericial de la Brigada del Cibercrimen de la PDI ([[Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018]]). La diligencia constató de manera científica que el software «Antorcha» de [[Alex Smith Leay]] no existía funcionalmente y que los archivos con las supuestas conversaciones de mensajería fueron introducidos intencionalmente en los teléfonos por el capitán [[Leonardo Osses Sandoval]] y personal de la UIOE para obstruir la labor del Ministerio Público.
