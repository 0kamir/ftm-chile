---
tipo_nodo: nexo_transaccion
fecha: 2015-10-29
tipo_nexo: compensacion_reparatoria
monto_clp: 38400000000
monto_origen: sentencia
entidad_origen: "[[Agrosuper SA]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Gonzalo Vial Vial]]"
firmante_destino: "[[Manuel Ariztia Ruiz]]"
causa_vinculada: "[[Caso Colusion de los Pollos]]"
delito_imputado: "[[Colusion y Atentado a la Libre Competencia]]"
evidencia_soporte: "[[Sentencia-Corte-Suprema-Colusion-Pollos-2015]]"
tags:
  - nexo/transaccion
  - multa-corte-suprema
  - colusion-pollos
  - tdlc
  - libre-competencia
---

# TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01

## Ficha de Arista Reificada (Sanción Pecuniaria Máxima Aplicada al Cartel de los Pollos)
- **Fecha de Sentencia y Liquidación**: `= this.fecha` *(Octubre de 2015)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto Sancionatorio Liquidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(72.000 UTA fijadas por la Corte Suprema, equivalentes a más de $38.400.000.000 CLP / US$ 60 millones)*
- **Entidad Sancionada Principal**: `= this.entidad_origen`
- **Órgano Jurisdiccional Sancionador**: `= this.entidad_destino`
- **Controlador Agrosuper**: `= this.firmante_origen`
- **Controlador Ariztía**: `= this.firmante_destino`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Delito / Infracción Imputada**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción de la Operación
Liquidación y condena pecuniaria definitiva dictada por la Tercera Sala de la [[Corte Suprema de Chile]] que ratificó la condena del TDLC e impuso las mayores multas por infracción a la libre competencia en la historia del país hasta esa fecha: 30.000 UTA a [[Agrosuper SA]], 30.000 UTA a [[Empresas Ariztia SA]] y 12.000 UTA a [[Agricola Don Pollo Limitada]], alcanzando un monto global consolidado a beneficio fiscal de **`$38.400.000.000 CLP`** (aproximadamente US$ 60 millones), además de la disolución judicial forzosa de la [[Asociacion de Productores Avicolas de Chile AG]].
