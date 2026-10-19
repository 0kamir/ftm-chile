---
tipo_nodo: causa_judicial
ruc: "1900418920-4"
año_inicio: 2019
tribunal_o_fiscalia: "Fiscalía Regional de Ñuble / Tribunal de Juicio Oral en lo Penal de Chillán"
fiscal_a_cargo: "Nayalet Mansilla / Paulina Valdebenito"
estado_judicial: formalizada
delito_principal: "[[Cohecho]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
    titulo: "Caso Luminarias: claves de la investigación por sobornos en municipios"
    medio: "Ex-Ante"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
    titulo: "Caso Luminarias LED: confirman prisión preventiva de dueño de Itelecom"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2021-06-30
    consultado: 2026-10-19
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
- **Estado Judicial**: `= this.estado_judicial` *(Acusación en arista Chillán; sin sentencia conocida al 2026-10-19)*
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Lavado de Activos]] y [[Violacion de Secreto]] / delitos tributarios)

## Resumen Ejecutivo
Investigación por presunta corrupción en licitaciones públicas de recambio de alumbrado municipal a tecnología LED en más de una decena de comunas de Chile. La empresa [[Itelecom Holding Chile SpA]], controlada por su gerente general [[Leon Marcelo Lefort Hernandez]], habría pagado sobornos, según la Fiscalía, a directivos y asesores municipales —como el administrador municipal de la [[Municipalidad de Chillan]], [[Marcelo Campos Henriquez]]— para manipular las bases técnicas y adjudicarse contratos ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]), según la hipótesis de la Fiscalía. Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

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

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
