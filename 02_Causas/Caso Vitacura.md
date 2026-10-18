---
tipo_nodo: causa_judicial
ruc: "2100783412-9"
año_inicio: 2021
tribunal_o_fiscalia: "Fiscalía Metropolitana Centro Norte / 4° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Francisco Jacir"
estado_judicial: formalizada
delito_principal: "[[Malversacion de Caudales Publicos]]"
tags:
  - causa
  - caso-vitacura
  - corrupcion-municipal
---

# Caso Vitacura

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (junto a [[Fraude al Fisco]], [[Lavado de Activos]] y delitos tributarios)

## Resumen Ejecutivo
Investigación penal contra el exalcalde de la [[Municipalidad de Vitacura]], [[Raul Torrealba del Pedregal]] (exmilitante de [[Renovacion Nacional]]), y directivos de las organizaciones comunitarias funcionales "Vita" (entre ellas [[Vita Deportes]], presidida por [[Domingo Prieto Urrejola]]). Según la acusación fiscal y la autodenuncia respaldada en [[Declaracion-Judicial-Prieto-Vitacura-2021]], se desviaron subvenciones municipales ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]) por más de **$759.000.000 CLP** mediante sobres con dinero en efectivo entregados mensualmente al edil y financiamiento de campañas.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Autorizador",
  firmante_destino AS "Receptor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
