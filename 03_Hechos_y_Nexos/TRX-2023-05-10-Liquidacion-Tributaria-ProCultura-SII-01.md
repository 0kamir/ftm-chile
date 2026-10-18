---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01"
fecha: 2023-05-10
tipo_nexo: factura_falsa
monto_clp: 315000000
metodo_adjudicacion: no_aplica
entidad_origen: "[[Fundacion ProCultura]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Alberto Larrain Salas]]"
firmante_destino: "[[Leonarda Villalobos Muth]]"
delito_imputado: "[[Delito Tributario]]"
causa_vinculada: "[[Caso Convenios]]"
evidencia_soporte: "[[Registro-Audiencia-InfoLobby-Biobio-2022]]"
tags:
  - nexo/factura-falsa
  - fiscalizacion-sii
  - caso-convenios
---

# TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$315.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad Fiscalizada (Origen)**: `= this.entidad_origen`
- **Órgano Fiscalizador (Destino)**: `= this.entidad_destino`
- **Director Ejecutivo Imputado**: `= this.firmante_origen`
- **Contraparte / Circuito de Fiscalización SII**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Fraude al Fisco]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Auditoría y recopilación de antecedentes por parte del [[Servicio Impuestos Internos]] respecto de rendiciones cruzadas, arriendos simulados y facturación de proveedores sin respaldo operativo por `$315.000.000 CLP` declarados por [[Fundacion ProCultura]] bajo la dirección de [[Alberto Larrain Salas]] con cargo a fondos regionales del [[Caso Convenios]]. Esta arista conecta estructuralmente el ecosistema de fundaciones regionales con el órgano fiscalizador tributario.
