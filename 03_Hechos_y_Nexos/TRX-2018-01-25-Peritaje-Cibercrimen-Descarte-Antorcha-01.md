---
tipo_nodo: nexo_transaccion
fecha: 2018-01-25
tipo_nexo: peritaje_forense
monto_clp: 0
monto_origen: sin_monto
entidad_origen: "[[Corte Suprema de Chile]]"
entidad_destino: "[[Direccion de Inteligencia Policial de Carabineros]]"
firmante_origen: "[[Leonardo Osses Sandoval]]"
firmante_destino: "[[Alex Smith Leay]]"
causa_vinculada: "[[Caso Operacion Huracan]]"
delito_imputado: "[[Obstruccion a la Investigacion]]"
evidencia_soporte: "[[Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018]]"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml"
  - "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml"
tags:
  - nexo/peritaje
  - operacion-huracan
  - descarte-antorcha
  - cibercrimen
---

# TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01

## Ficha de Arista Reificada (Peritaje Técnico de Descarte y Descubrimiento del Montaje)
- **Fecha del Hito**: `= this.fecha` *(Enero de 2018)*
- **Tipo de Registro**: `= this.tipo_nexo`
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Diligencia probatoria)*
- **Ámbito Jurisdiccional**: `= this.entidad_origen`
- **Unidad Policial Investigada**: `= this.entidad_destino`
- **Oficial Identificado en Implantación**: `= this.firmante_origen`
- **Autor del Código Fraudulento**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Constatado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
El 25 de enero de 2018, la Fiscalía Regional de La Araucanía remitió al Juzgado de Garantía de Temuco los resultados concluyentes del informe de la Brigada del Cibercrimen de la PDI ([[Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018]]). La diligencia constató de manera científica que el software «Antorcha» de [[Alex Smith Leay]] no existía funcionalmente y que los archivos con las supuestas conversaciones de mensajería fueron introducidos intencionalmente en los teléfonos por el capitán [[Leonardo Osses Sandoval]] y personal de la UIOE para obstruir la labor del Ministerio Público.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Huracán 2: formalización del creador de Antorcha y funcionario del Labocar](https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml) | BioBioChile | `secundaria` | 2018-02-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml) |
| [El 'profesor' Smith condenado a 12 años de cárcel por montaje en Operación Huracán](https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) | El Dínamo | `secundaria` | 2026-04-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) |
| [Profesor Smith y otros 3 condenados en Operación Huracán presentan recurso para anular sentencia](https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) | BioBioChile | `secundaria` | 2026-05-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) |
