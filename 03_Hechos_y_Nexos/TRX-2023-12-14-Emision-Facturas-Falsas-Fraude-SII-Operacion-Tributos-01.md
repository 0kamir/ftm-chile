---
tipo_nodo: nexo_transaccion
fecha: 2023-12-14
tipo_nexo: factura_falsa
monto_clp: 240000000000
monto_origen: estimacion_oficial
entidad_origen: ""
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: ""
firmante_destino: ""
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
Hecho agregado que representa el perjuicio fiscal total estimado por el [[Servicio Impuestos Internos]] (**`$240.000.000.000 CLP`**) atribuido por la Fiscalía Metropolitana Occidente a seis grupos de imputados que habrían emitido más de 100.000 facturas falsas mediante sociedades de papel entre 2014 y 2020. No se atribuye a una persona individual; ver el detalle por grupo en [[Caso Megafraude Tributario Operacion Tributos]]. Hipótesis acusatoria sin sentencia.

