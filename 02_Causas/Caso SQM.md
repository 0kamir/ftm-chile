---
tipo_nodo: causa_judicial
ruc: "1500189420-1"
año_inicio: 2015
tribunal_o_fiscalia: "Fiscalía Regional de Valparaíso / 8° Juzgado de Garantía de Santiago / 3° TOP de Santiago"
fiscal_a_cargo: "Claudia Perivancich / Pablo Gómez"
estado_judicial: juicio_oral
delito_principal: "[[Cohecho]]"
tags:
  - causa
  - caso-sqm
  - financiamiento-politico
---

# Caso SQM

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (junto a [[Delito Tributario]])

## Resumen Ejecutivo
Macrocausa sobre financiamiento ilegal de la política y captura regulatoria iniciada a partir de denuncias y querellas del [[Servicio Impuestos Internos]] ([[Querella-SII-Boletas-SQM-2015]]). La investigación acreditó que la minera no metálica [[SQM SA]], bajo la gerencia general de [[Patricio Contesse Gonzalez]], pagó cientos de millones de pesos mediante boletas y facturas ideológicamente falsas a personas vinculadas transversalmente a partidos políticos, incluyendo pagos por más de **$730.000.000 CLP** al entorno de [[Pablo Longueira Montes]] (histórico dirigente de [[Union Democrata Independiente]]) durante la tramitación legislativa del Royalty Minero en 2010 ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]).

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Pagador / Emisor",
  firmante_destino AS "Receptor Político",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
