---
tipo_nodo: causa_judicial
ruc: "1900418920-4"
año_inicio: 2019
tribunal_o_fiscalia: "Fiscalía Regional de Ñuble / Tribunal de Juicio Oral en lo Penal de Chillán"
fiscal_a_cargo: "Nayalet Mansilla / Paulina Valdebenito"
estado_judicial: cerrada
delito_principal: "[[Cohecho]]"
tags:
  - causa
  - caso-luminarias-led
  - itelecom
  - corrupcion-municipal
---

# Caso Luminarias LED

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` *(Condenas ejecutoriadas en arista Chillán y procedimiento abreviado nacional)*
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Lavado de Activos]] y [[Violacion de Secreto]] / delitos tributarios)

## Resumen Ejecutivo
Red de corrupción sistémica en licitaciones públicas de recambio de alumbrado municipal a tecnología LED en más de una decena de comunas de Chile. La empresa [[Itelecom Holding Chile SpA]], controlada por su gerente general [[Leon Marcelo Lefort Hernandez]], pagó sobornos a directivos y asesores municipales —como el administrador municipal de la [[Municipalidad de Chillan]], [[Marcelo Campos Henriquez]]— para manipular las bases técnicas y adjudicarse contratos por **$3.200.000.000 CLP** ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]), según acreditó la [[Sentencia-TOP-Chillan-Luminarias-2023]]. Asimismo, la investigación reveló flujos de asesoría legal y financiera con el abogado [[Luis Hermosilla Osorio]] ([[TRX-2020-07-08-Asesoria-Itelecom-Hermosilla-01]]), conectando topológicamente esta causa con el [[Caso Audios]].

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Pagador / Emisor",
  firmante_destino AS "Receptor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
