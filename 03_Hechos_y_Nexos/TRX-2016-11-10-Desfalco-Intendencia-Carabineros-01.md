---
tipo_nodo: nexo_transaccion
fecha: 2016-11-10
tipo_nexo: transferencia
monto_clp: 28348928198
entidad_origen: "[[Direccion de Finanzas de Carabineros]]"
entidad_destino: "[[Direccion de Finanzas de Carabineros]]"
firmante_origen: "[[Flavio Echeverria Cortez]]"
firmante_destino: "[[Jaime Paz Meneses]]"
causa_vinculada: "[[Caso Pacogate]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
evidencia_soporte: "[[Sentencia-TOP-Santiago-Pacogate-2021]]"
tags:
  - nexo/transaccion
  - transferencia
  - caso-pacogate
---

# TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01

## Ficha de Arista Reificada (Desfalco Consolidado en Intendencia de Carabineros)
- **Fecha de Corte Pericial**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Órgano Público Defraudado**: `= this.entidad_origen`
- **Jefe de Cúpula Condenado**: `= this.firmante_origen`
- **Operador Contable Condenado**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Condenado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]])
- **Evidencia / Sentencia Firme**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Sustracción sistemática de caudales públicos desde las cuentas institucionales de la [[Direccion de Finanzas de Carabineros]] por un total acreditado judicialmente de **$28.348.928.198 CLP**. La operación consistía en alterar las nóminas electrónicas de pago de remuneraciones y desahucios enviadas al Banco Estado para abonar sumas millonarias a cuentas particulares y luego distribuir el retorno en efectivo a la cúpula encabezada por [[Flavio Echeverria Cortez]] y [[Jaime Paz Meneses]], sancionada mediante [[Sentencia-TOP-Santiago-Pacogate-2021]] en el [[Caso Pacogate]].
