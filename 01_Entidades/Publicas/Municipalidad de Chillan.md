---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Ñuble (XVI Región)"
superior_jerarquico: "Concejo Municipal de Chillán (Autónoma)"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
  - "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
tags:
  - entidad/publica
  - municipio
  - chillan
  - caso-luminarias-led
---

# Municipalidad de Chillan

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Corporación edilicia de la capital regional de Ñuble. En el [[Caso Luminarias LED]] se investiga la licitación municipal de recambio de luminarias LED adjudicada a [[Itelecom Holding Chile SpA]] ([[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]]). Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

## Nexos y Licitaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Licitación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Empresa",
  firmante_destino AS "Funcionario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Luminarias: claves de la investigación por sobornos en municipios](https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) | Ex-Ante | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) |
| [Caso Luminarias LED: confirman prisión preventiva de dueño de Itelecom](https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) | El Dínamo | `secundaria` | 2021-06-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) |
