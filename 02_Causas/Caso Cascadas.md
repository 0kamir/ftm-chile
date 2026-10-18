---
tipo_nodo: causa_judicial
ruc: "1400918240-2"
año_inicio: 2012
tribunal_o_fiscalia: "Superintendencia de Valores y Seguros (CMF) / Fiscalía Centro Norte / Corte Suprema"
fiscal_a_cargo: "Carlos Pavez Tolosa (Superintendente SVS) / Andrés Montes Cruz"
estado_judicial: cerrada_con_condena
delito_principal: "[[Negociacion Incompatible]]"
tags:
  - causa
  - mercado-valores
  - caso-cascadas
---

# Caso Cascadas

## Ficha Procesal y Regulatoria
- **RUC / Expediente**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Órgano Sancionador / Tribunal**: `= this.tribunal_o_fiscalia`
- **Autoridad Instructora**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Infracción / Delito Principal**: `= this.delito_principal` (operaciones bursátiles ficticias y perjuicio patrimonial a accionistas minoritarios y fondos de pensiones)

## Síntesis Forense de la Causa
Investigación sancionatoria y penal encabezada por la [[Comision para el Mercado Financiero]] (ex Superintendencia de Valores y Seguros, dirigida por [[Carlos Pavez Tolosa]]) y ratificada por la [[Corte Suprema de Chile]] ([[Resolucion-SVS-CasoCascadas-2014]]), que acreditó un esquema sistemático de compraventas bursátiles concertadas entre 2009 y 2011 ejecutado por [[Julio Ponce Lerou]] a través de las sociedades cascada como [[Sociedad de Inversiones Pampa Calichera SA]], controladoras de [[SQM SA]] (donde ejercía como gerente general [[Patricio Contesse Gonzalez]]). Las operaciones permitieron extraer utilidades y mantener el control político-económico de la minera no metálica que paralelamente financiaba campañas en el [[Caso SQM]] ([[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]]).

## Transacciones y Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
