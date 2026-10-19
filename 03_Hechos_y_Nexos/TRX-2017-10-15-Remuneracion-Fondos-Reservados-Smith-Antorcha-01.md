---
tipo_nodo: nexo_transaccion
fecha: 2017-10-15
tipo_nexo: desvio_fondos_reservados
monto_clp: 25000000
monto_origen: acusacion
entidad_origen: "[[Direccion de Inteligencia Policial de Carabineros]]"
entidad_destino: "[[Direccion de Inteligencia Policial de Carabineros]]"
firmante_origen: "[[Patricio Marin Lazo]]"
firmante_destino: "[[Alex Smith Leay]]"
causa_vinculada: "[[Caso Operacion Huracan]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
evidencia_soporte: "[[Sentencia-TOP-Temuco-OperacionHuracan-2026]]"
tags:
  - nexo/transaccion
  - operacion-huracan
  - fondos-reservados
  - dipolcar
---

# TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01

## Ficha de Arista Reificada (Pago de Honorarios y Fondos Reservados por Software Fraudulento)
- **Fecha de Desembolso / Período**: `= this.fecha` *(Octubre de 2017)*
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Aproximadamente $25.000.000 CLP en contratos a honorarios y pagos informales con cargo a gastos reservados de DIPOLCAR)*
- **Entidad Pagadora**: `= this.entidad_origen`
- **Repartición Receptora**: `= this.entidad_destino`
- **Mando Autorizador**: `= this.firmante_origen`
- **Perito Beneficiario**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Durante el desarrollo de la [[Caso Operacion Huracan]], el jefe operativo de la UIOE, mayor [[Patricio Marin Lazo]], con la anuencia del general [[Gonzalo Blu Rodriguez]], gestionó y autorizó desembolsos periódicos y remuneraciones con cargo a los gastos reservados de la [[Direccion de Inteligencia Policial de Carabineros]] a favor del civil [[Alex Smith Leay]]. Los recursos tuvieron por objeto retribuir el supuesto desarrollo técnico y mantenimiento de los aplicativos fraudulentos «Antorcha» y «Tubicación».
