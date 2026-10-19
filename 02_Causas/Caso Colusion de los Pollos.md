---
tipo_nodo: causa_judicial
ruc: "ROL-C-236-11-TDLC"
año_inicio: 2011
tribunal_o_fiscalia: "Tribunal de Defensa de la Libre Competencia (TDLC) / Corte Suprema de Chile"
fiscal_a_cargo: "Felipe Irarrázabal Philippi (Fiscal Nacional Económico) / TDLC"
estado_judicial: cerrada_con_condena
delito_principal: "[[Colusion y Atentado a la Libre Competencia]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
    titulo: "FNE presenta requerimiento por colusión en la producción y comercialización de carne de pollo"
    medio: "Fiscalía Nacional Económica"
    tipo: primaria
    fecha: 2011-12-01
    consultado: 2026-10-19
  - url: "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
    titulo: "Sentencia TDLC N° 139/2014 (Rol C-236-2011)"
    medio: "TDLC / FNE"
    tipo: primaria
    fecha: 2014-09-25
    consultado: 2026-10-19
  - url: "https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/"
    titulo: "Corte Suprema confirma multas por colusión contra Agrosuper, Ariztía y Don Pollo"
    medio: "Fiscalía Nacional Económica"
    tipo: primaria
    fecha: 2015-10-29
    consultado: 2026-10-19
tags:
  - causa
  - libre-competencia
  - colusion-pollos
  - cartel-avicola
  - agrosuper
  - ariztia
  - don-pollo
---

# Caso Colusion de los Pollos

## Ficha Procesal, Regulatoria y Sancionatoria
- **Rol de Causa / Expediente TDLC**: `= this.ruc` *(Sentencia N° 139/2014 y Recurso de Reclamación Rol 27.175-2014 ante Corte Suprema)*
- **Año de Requerimiento Público**: `= this.año_inicio` (Período colusorio acreditado: 1994–2011)
- **Tribunales Resolutivos**: `= this.tribunal_o_fiscalia`
- **Órgano Persecutor Especializado**: `= this.fiscal_a_cargo` (en coordinación con el [[Servicio Nacional del Consumidor]])
- **Estado Judicial**: `= this.estado_judicial` (Fallo definitivo ejecutoriado con multas máximas y disolución gremial)
- **Infracción / Delito Económico Principal**: `= this.delito_principal`

## Resumen Ejecutivo de la Causa
Investigación y condena emblemática por colusión empresarial en el mercado de producción y comercialización de carne de pollo faenada en Chile, protagonizada por las tres principales productoras que concentraban más del 92% de la oferta nacional: [[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]], operando mediante la coordinación gremial de la [[Asociacion de Productores Avicolas de Chile AG]] (APA), presidida por [[Juan Miguel Ovalle Garces]].

La trama se estructuró a través de tres hitos trascendentales:
1. **Asignación Clandestina de Cuotas de Producción (1994–2011)**: Las empresas acordaron limitar la producción total nacional para evitar caídas de precios y eliminar la competencia interna ([[TRX-2008-01-15-Colusion-Cuotas-Produccion-Pollos-01]]). A través de la APA, se proyectaba la demanda de consumo de carne de ave en Chile y se distribuía entre las tres avícolas una cuota fija de faenamiento anual en toneladas, fiscalizada con auditorías e informes mensuales.
2. **Requerimiento de la FNE y Sentencia TDLC (2011–2014)**: La [[Fiscalia Nacional Economica]] presentó requerimiento en diciembre de 2011 tras allanamientos con incautación de computadores y correos electrónicos. En septiembre de 2014, el TDLC dictó la [[Sentencia-TDLC-139-Colusion-Pollos-2014]], imponiendo multas millonarias y ordenando por primera vez en la historia de la judicatura económica chilena la **disolución forzada de una asociación gremial** ([[Asociacion de Productores Avicolas de Chile AG]]) por haber sido instrumentalizada como cartel delictivo.
3. **Ratificación de la Corte Suprema y Multas Máximas (2015)**: En octubre de 2015, la [[Corte Suprema de Chile]] ratificó íntegramente la sentencia y elevó las multas al techo legal máximo de 30.000 UTA para Agrosuper y Ariztía, y 12.000 UTA para Don Pollo, totalizando 72.000 UTA (aproximadamente **`$38.400.000.000 CLP`** / US$ 60 millones) ([[TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01]]). Además, el material probatorio derivó directamente en la posterior investigación del Cartel de los Supermercados.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Infracción / Delito",
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
