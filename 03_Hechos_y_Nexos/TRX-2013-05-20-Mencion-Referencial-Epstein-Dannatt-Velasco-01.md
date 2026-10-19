---
tipo_nodo: nexo_transaccion
fecha: 2013-05-20
tipo_nexo: correo_electronico
monto_clp: 0
entidad_origen: "[[Corte Suprema de Chile]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Andres Velasco Branes]]"
firmante_destino: "[[Andres Velasco Branes]]"
causa_vinculada: "[[Caso Archivos Epstein Menciones Chile]]"
delito_imputado: ""
evidencia_soporte: "[[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]"
estado_verificacion: sin_fuente
fuentes: []
alertas_verificacion:
  - "Mención documental sin imputación: se eliminó delito_imputado (2026-10-19). Aparecer en los archivos Epstein no constituye delito."
tags:
  - nexo/desclasificacion
  - epstein-files
  - mencion-referencial
  - descarte-probatorio
---

# TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01

## Ficha de Arista Reificada (Auditoría de Desclasificación / Mención Referencial de Terceros)
- **Fecha del Mensaje Desclasificado**: `= this.fecha` *(Mayo de 2013)*
- **Tipo de Registro**: `= this.tipo_nexo` *(Comentario epistolar entre terceros sin intervención del aludido)*
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Sin aportes ni flujos financieros)*
- **Ámbito Institucional de Verificación**: `= this.entidad_origen`
- **Sujeto Mencionado Referencialmente**: `= this.firmante_origen`
- **Causa / Expediente Asociado**: `= this.causa_vinculada`
- **Ámbito Tipológico Evaluado**: `= this.delito_imputado` *(Descarte de financiamiento irregular o tráfico de influencias)*
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Registro
En los correos desclasificados del litigio federal *Giuffre v. Maxwell*, figura un mensaje enviado por el escritor y curador británico Adrian Dannatt con el asunto *«Future President of Chile etc.»*, en el cual describe a [[Andres Velasco Branes]] como un *«brillante economista y profesor de Harvard»* y menciona informalmente un encuentro social en Londres en el marco de su precandidatura presidencial de 2013.

**Determinación Forense**:
Los expedientes judiciales no acreditan ninguna interacción, correo directo, reunión, aporte de campaña ni relación de ningún tipo entre [[Andres Velasco Branes]] y Jeffrey Epstein, tratándose únicamente de una mención contextual realizada por un tercero.

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
