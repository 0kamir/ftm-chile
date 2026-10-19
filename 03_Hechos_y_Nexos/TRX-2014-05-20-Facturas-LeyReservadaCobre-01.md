---
tipo_nodo: nexo_transaccion
fecha: 2014-05-20
tipo_nexo: transferencia
monto_clp: 6100000000
monto_origen: acusacion
entidad_origen: "[[Comando de Apoyo a la Fuerza del Ejercito]]"
entidad_destino: "[[Frasim Ltda]]"
firmante_origen: "[[Juan Miguel Fuente-Alba Poblete]]"
firmante_destino: "[[Jozo Santic Palomino]]"
causa_vinculada: "[[Caso Milicogate]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
evidencia_soporte: "[[Procesamientos-Ministra-Rutherford-Milicogate]]"
tags:
  - nexo/transaccion
  - transferencia
  - caso-milicogate
  - ley-reservada-del-cobre
---

# TRX-2014-05-20-Facturas-LeyReservadaCobre-01

## Ficha de Arista Reificada (Desfalco Fondos Ley Reservada del Cobre)
- **Fecha de Corte Pericial**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado Consolidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Repartición Militar de Origen**: `= this.entidad_origen`
- **Sociedad Receptora / Proveedora**: `= this.entidad_destino`
- **Mando Institucional**: `= this.firmante_origen`
- **Oficial Operador Condenado**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Fraude al Fisco]])
- **Evidencia Judicial**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Defraudación patrimonial por un monto que la investigación estimó en **$6.100.000.000 CLP** ejecutada mediante el pago de facturas ideológicamente falsas con cargo a los fondos de la Ley N° 13.196 Reservada del Cobre en el [[Comando de Apoyo a la Fuerza del Ejercito]] hacia proveedores coludidos como [[Frasim Ltda]] (con intervención de [[Jozo Santic Palomino]]) y sustracción de gastos reservados durante el mando de [[Juan Miguel Fuente-Alba Poblete]], imputada en [[Procesamientos-Ministra-Rutherford-Milicogate]] (un auto de procesamiento no es una condena) dentro del [[Caso Milicogate]].
