---
tipo_nodo: nexo_transaccion
fecha: 2023-12-15
tipo_nexo: transferencia
monto_clp: 25000000000
entidad_origen: "[[Inversiones y Asesorias Pavez SpA]]"
entidad_destino: "[[Comercializadora y Exportadora Global SpA]]"
firmante_origen: "[[Jose Antonio Pavez Campillay]]"
firmante_destino: "[[Andres Esteban Galaz Soto]]"
causa_vinculada: "[[Caso Megafraude Tributario Operacion Tributos]]"
delito_imputado: "[[Lavado de Activos]]"
evidencia_soporte: "[[Informe-BRILAC-PDI-Operacion-Tributos-2023]]"
tags:
  - nexo/transaccion
  - megafraude-sii
  - lavado-de-activos
  - operacion-tributos
---

# TRX-2023-12-15-Lavado-Activos-Bienes-Inmuebles-Clan-Pavez-01

## Ficha de Arista Reificada (Estructuración de Activos Ilícitos y Adquisición de Bienes de Lujo)
- **Fecha de Detección e Incautación**: `= this.fecha` *(Diciembre de 2023)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto de Activos Lavados Trazados (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Más de $25.000.000.000 CLP en activos patrimoniales identificados y embargados)*
- **Entidad de Origen de Fondos Ilícitos**: `= this.entidad_origen`
- **Sociedad Receptora de Capitales**: `= this.entidad_destino`
- **Cabecilla Inversionista**: `= this.firmante_origen`
- **Socio Operativo / Co-Imputado**: `= this.firmante_destino`
- **Causa Asociada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Esquema de blanqueo de capitales formalizado por la Fiscalía Metropolitana Occidente y documentado por la Brigada Investigadora de Lavado de Activos (BRILAC) de la PDI, en el cual las ganancias ilícitas del fraude tributario fueron estratificadas a través de [[Inversiones y Asesorias Pavez SpA]] hacia [[Comercializadora y Exportadora Global SpA]] y otras sociedades ficticias. Los fondos se destinaron a la compra de propiedades de alto valor, más de 30 vehículos de lujo (marcas Porsche, BMW, Mercedes-Benz), lingotes de oro, criptomonedas e inversiones financieras nacionales e internacionales, totalizando un monto patrimonial blanqueado estimado en más de **`$25.000.000.000 CLP`**.
