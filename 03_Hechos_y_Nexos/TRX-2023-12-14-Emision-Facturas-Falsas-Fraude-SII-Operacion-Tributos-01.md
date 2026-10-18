---
tipo_nodo: nexo_transaccion
fecha: 2023-12-14
tipo_nexo: factura_falsa
monto_clp: 240000000000
entidad_origen: "[[Inversiones y Asesorias Pavez SpA]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Jose Antonio Pavez Campillay]]"
firmante_destino: "[[Ximena Jimenez Faras]]"
causa_vinculada: "[[Caso Megafraude Tributario Operacion Tributos]]"
delito_imputado: "[[Delito Tributario]]"
evidencia_soporte: "[[Querella-SII-Megafraude-Tributario-2023]]"
tags:
  - nexo/transaccion
  - megafraude-sii
  - operacion-tributos
  - facturas-falsas
  - iva-falso
---

# TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01

## Ficha de Arista Reificada (Megafraude Tributario y Obtención Indebida de Devoluciones de IVA)
- **Fecha de Detección e Imputación Judicial**: `= this.fecha` *(Diciembre de 2023)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto Defraudado Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Perjuicio fiscal récord consolidado de $240.000.000.000 CLP cuantificado por el SII)*
- **Entidad Emisora / Fachada Concentradora**: `= this.entidad_origen`
- **Órgano Tributario Defraudado**: `= this.entidad_destino`
- **Cabecilla de la Organización**: `= this.firmante_origen`
- **Operadora Contable / Financiera**: `= this.firmante_destino`
- **Causa Asociada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
En el marco de la investigación de la Fiscalía Metropolitana Occidente y la BRILAC de la PDI, se formalizó a 55 imputados liderados por [[Jose Antonio Pavez Campillay]] y su contadora [[Ximena Jimenez Faras]] por la creación de un holding ilícito de más de 300 sociedades de papel destinadas a la emisión de más de 100.000 facturas falsas. Mediante este mecanismo, el cartel defraudó al Fisco de Chile por un monto consolidado de **`$240.000.000.000 CLP`**, mediante la obtención ilegal de devoluciones del IVA exportador y la venta de créditos fiscales fraudulentos a empresas operativas para evadir el Impuesto a la Renta.
