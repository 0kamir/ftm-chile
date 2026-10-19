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
tags:
  - nexo/montaje
  - operacion-huracan
  - dipolcar
  - falsificacion-evidencia
---

# TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01

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

## Descripción Forense del Hecho
El 23 de septiembre de 2017, la [[Direccion de Inteligencia Policial de Carabineros]] (UIOE) ejecutó la detención simultánea de ocho dirigentes y comuneros mapuche en La Araucanía. La acción policial se sustentó en los oficios N° 130 y 131 suscritos por el general [[Gonzalo Blu Rodriguez]] y el coronel [[Marcelo Teuber Munoz]], afirmando falsamente que a través del software «Antorcha» de [[Alex Smith Leay]] se habían interceptado comunicaciones de mensajería cifrada. 

Posteriormente, el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]) acreditó que los supuestos chats fueron redactados e implantados manualmente en los teléfonos por [[Leonardo Osses Sandoval]] y sus subalternos tras las incautaciones.
