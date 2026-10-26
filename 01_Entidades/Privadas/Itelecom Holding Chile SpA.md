---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Itelecom Holding Chile SpA"
fecha_constitucion: "2013-07-22"
objeto_social: "Ingeniería eléctrica, eficiencia energética, telegestión y alumbrado público LED"
representante_legal: "[[Leon Marcelo Lefort Hernandez]]"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
  - "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-casi-5-anos-de-presidio-dos-ex"
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-otros-tres-acusados-incluido-un-ex"
tags:
  - entidad/privada
  - proveedor-municipal
  - caso-luminarias-led
  - nodo-puente
---

# Itelecom Holding Chile SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Gerente General y Controlador**: `= this.representante_legal`

## Contexto
Sociedad proveedora de alumbrado público investigada en el [[Caso Luminarias LED]]. La Fiscalía sostiene que, a través de su controlador [[Leon Marcelo Lefort Hernandez]], ofreció sobornos para adjudicarse contratos municipales como el de la [[Municipalidad de Chillan]] ([[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]]). Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

## Historial de Nexos y Operaciones Investigadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Luminarias: claves de la investigación por sobornos en municipios](https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) | Ex-Ante | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) |
| [Caso Luminarias LED: confirman prisión preventiva de dueño de Itelecom](https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) | El Dínamo | `secundaria` | 2021-06-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) |
| [Caso Luminarias LED: condenan a casi 5 años de presidio a dos exconcejales de Iquique por fraude al fisco y cohecho](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-casi-5-anos-de-presidio-dos-ex) | Fiscalía de Chile | `primaria` | 2023-05-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-casi-5-anos-de-presidio-dos-ex) |
| [Caso Luminarias LED: condenan a otros tres acusados, incluido un exconcejal de Iquique](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-otros-tres-acusados-incluido-un-ex) | Fiscalía de Chile | `primaria` | 2023-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-otros-tres-acusados-incluido-un-ex) |
