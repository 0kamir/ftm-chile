---
tipo_nodo: nexo_transaccion
fecha: 2017-09-23
tipo_nexo: montaje_policial
monto_clp: 0
monto_origen: sin_monto
entidad_origen: "[[Direccion de Inteligencia Policial de Carabineros]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Gonzalo Blu Rodriguez]]"
firmante_destino: "[[Alex Smith Leay]]"
causa_vinculada: "[[Caso Operacion Huracan]]"
delito_imputado: "[[Falsificacion de Instrumento Publico]]"
evidencia_soporte: "[[Sentencia-TOP-Temuco-OperacionHuracan-2026]]"
estado_verificacion: verificado
fuentes:
  - "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml"
tags:
  - nexo/montaje
  - operacion-huracan
  - dipolcar
  - falsificacion-evidencia
---

# TRX-2017-09-23-Detenciones-OperacionHuracan-01

## Ficha de Arista Reificada (Operativo Policial de Detención e Implantación de Pruebas Falsas)
- **Fecha del Operativo**: `= this.fecha` *(23 de septiembre de 2017)*
- **Tipo de Nexo**: `= this.tipo_nexo` *(Montaje judicial y detenciones bajo Ley Antiterrorista sustentadas en informes falsos)*
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Daño institucional y privación de libertad ilícita)*
- **Unidad Policial Ejecutora**: `= this.entidad_origen`
- **Ámbito Jurisdiccional Engañado**: `= this.entidad_destino`
- **Mando Responsable Origen**: `= this.firmante_origen`
- **Operador de Fabricación de Software**: `= this.firmante_destino`
- **Causa Penal Vinculada**: `= this.causa_vinculada`
- **Delito Acreditado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
El 23 de septiembre de 2017, la [[Direccion de Inteligencia Policial de Carabineros]] (UIOE) ejecutó la detención simultánea de ocho dirigentes y comuneros mapuche en La Araucanía. La acción policial se sustentó en los oficios N° 130 y 131 suscritos por el general [[Gonzalo Blu Rodriguez]] y el coronel [[Marcelo Teuber Munoz]], afirmando falsamente que a través del software «Antorcha» de [[Alex Smith Leay]] se habían interceptado comunicaciones de mensajería cifrada. 

Posteriormente, el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]) acreditó que los supuestos chats fueron redactados e implantados manualmente en los teléfonos por [[Leonardo Osses Sandoval]] y sus subalternos tras las incautaciones.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [El 'profesor' Smith condenado a 12 años de cárcel](https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) | El Dínamo | `secundaria` | 2026-04-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) |
| [Profesor Smith y otros 3 condenados en Operación Huracán presentan recurso para anular sentencia](https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) | BioBioChile | `secundaria` | 2026-05-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) |
