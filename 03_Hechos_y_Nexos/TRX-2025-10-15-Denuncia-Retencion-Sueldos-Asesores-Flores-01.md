---
tipo_nodo: nexo_transaccion
fecha: 2025-10-15
tipo_nexo: desviacion_fondos
monto_clp: 35000000
monto_origen: acusacion
entidad_origen: "[[Senado de la Republica de Chile]]"
entidad_destino: "[[Camila Flores Oporto]]"
firmante_origen: "[[Senado de la Republica de Chile]]"
firmante_destino: "[[Camila Flores Oporto]]"
causa_vinculada: "[[Caso Asignaciones Parlamentarias y Cuota Flores]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Orden-Entrada-Registro-Congreso-Caso-Flores-2026]]"
tags:
  - nexo/transaccion
  - cuota-flores
  - asignaciones
  - fraude-al-fisco
  - senado
---

# TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01

## Ficha de Arista Reificada (Mecanismo de Retención de Asignaciones Legislativas / Cuota Flores)
- **Fecha de Inicio de Indagatoria**: `= this.fecha` *(Octubre de 2025)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto Imputado Preliminar (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Aproximadamente $35.000.000 CLP en aportes y retenciones de sueldos objeto de peritaje contable)*
- **Entidad Pagadora de Asignaciones**: `= this.entidad_origen`
- **Parlamentaria Receptora Investigada**: `= this.entidad_destino`
- **Órgano Emisor Institucional**: `= this.firmante_origen`
- **Autoridad Responsable**: `= this.firmante_destino`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción de la Operación
Esquema de recaudación denunciado por excolaboradores de la parlamentaria [[Camila Flores Oporto]], según el cual a funcionarios y asesores contratados con cargo a los fondos públicos de asignaciones del Congreso se les habría exigido la restitución en dinero en efectivo de parte significativa de sus salarios mensuales. La Fiscalía Regional de Valparaíso (URAC) investiga el mecanismo bajo la figura de fraude al Fisco en carácter reiterado.
