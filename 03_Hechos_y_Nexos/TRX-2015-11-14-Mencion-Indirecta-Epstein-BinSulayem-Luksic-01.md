---
tipo_nodo: nexo_transaccion
fecha: 2015-11-14
tipo_nexo: consulta_terceros
monto_clp: 0
entidad_origen: "[[Corte Suprema de Chile]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Andronico Luksic Craig]]"
firmante_destino: "[[Andronico Luksic Craig]]"
causa_vinculada: "[[Caso Archivos Epstein Menciones Chile]]"
delito_imputado: "[[Trafico de Influencias]]"
evidencia_soporte: "[[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]"
tags:
  - nexo/desclasificacion
  - epstein-files
  - mencion-indirecta
  - descarte-probatorio
---

# TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01

## Ficha de Arista Reificada (Auditoría de Desclasificación / Mención Indirecta de Terceros)
- **Fecha del Mensaje Desclasificado**: `= this.fecha` *(Noviembre de 2015)*
- **Tipo de Registro**: `= this.tipo_nexo` *(Consulta epistolar entre terceros sin participación del sujeto mencionado)*
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Sin flujos financieros ni transacción económica)*
- **Ámbito Institucional de Verificación**: `= this.entidad_origen`
- **Sujeto Mencionado Referencialmente**: `= this.firmante_origen`
- **Causa / Expediente Asociado**: `= this.causa_vinculada`
- **Ámbito Tipológico Evaluado**: `= this.delito_imputado` *(Descarte de intermediación o tráfico de influencias)*
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Registro
En los correos desclasificados del caso *Giuffre v. Maxwell* ante la Corte Federal del Distrito Sur de Nueva York (SDNY), figura una cadena de correos entre el empresario emiratí Sultan Ahmed bin Sulayem (presidente de *DP World*) y Jeffrey Epstein. En dicha comunicación, Bin Sulayem adjuntó una reseña curricular de [[Andronico Luksic Craig]] consultando si lo conocía, a propósito de una visita comercial y reunión protocolar en Dubái con la comitiva chilena. 

**Determinación Forense**:
Los registros no exhiben ninguna respuesta de Epstein ni evidencia de llamadas, reuniones, correos ni contacto directo entre [[Andronico Luksic Craig]] y Jeffrey Epstein, descartándose judicial y periodísticamente cualquier involucramiento en ilícitos.
