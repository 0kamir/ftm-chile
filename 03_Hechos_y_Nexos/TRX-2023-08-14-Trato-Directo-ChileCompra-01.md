---
tipo_nodo: nexo_transaccion
fecha: 2023-08-14
tipo_nexo: convenio_directo
monto_clp: 45800000
entidad_origen: "[[Direccion ChileCompra]]"
entidad_destino: "[[Consultora Gestion Publica SpA]]"
firmante_origen: "[[Rodrigo Diaz Worner]]"
firmante_destino: "[[Jorge Valdivia Correa]]"
causa_vinculada: "[[Caso Compras Publicas]]"
delito_imputado: "[[Negociacion Incompatible]]"
evidencia_soporte: "[[Orden-Compra-MercadoPublico-2023]]"
tags:
  - nexo/transaccion
  - trato-directo
  - compras-publicas
---

# TRX-2023-08-14-Trato-Directo-ChileCompra-01

## Ficha de Arista Reificada (Orden de Compra por Trato Directo)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad Compradora**: `= this.entidad_origen`
- **Sociedad Proveedora**: `= this.entidad_destino`
- **Autoridad Requirente**: `= this.firmante_origen`
- **Representante Proveedor**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Hipótesis Penal**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Adjudicación por trato directo bajo causal de "confianza y seguridad de los servicios" por **$45.800.000 CLP** (~724 UTM, exenta de Toma de Razón) a favor de [[Consultora Gestion Publica SpA]] (representada por [[Jorge Valdivia Correa]]) apenas 157 días después de la constitución de la sociedad, registrada en [[Orden-Compra-MercadoPublico-2023]] y monitoreada en [[Caso Compras Publicas]] por eventual [[Negociacion Incompatible]].
