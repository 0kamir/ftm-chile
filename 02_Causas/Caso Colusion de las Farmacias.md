---
tipo_nodo: causa_judicial
ruc: "ROL-C-184-08-TDLC"
año_inicio: 2008
tribunal_o_fiscalia: "Tribunal de Defensa de la Libre Competencia (TDLC) / Corte Suprema de Chile"
fiscal_a_cargo: "Enrique Vergara Vial (Fiscal Nacional Económico) / TDLC"
estado_judicial: cerrada_con_condena
delito_principal: "[[Colusion y Atentado a la Libre Competencia]]"
estado_verificacion: verificado
fuentes:
  - url: "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
    titulo: "Sentencia TDLC N° 119/2012 y fallo Corte Suprema Rol 2578-2012"
    medio: "CentroCompetencia (copia del fallo)"
    tipo: primaria
    fecha: 2012-09-07
    consultado: 2026-10-19
  - url: "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
    titulo: "Suprema confirma acuerdo entre FNE y FASA por caso colusión"
    medio: "Diario Financiero"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
    titulo: "Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2019-12-20
    consultado: 2026-10-19
tags:
  - causa
  - libre-competencia
  - colusion-farmacias
  - fasa
  - cruz-verde
  - salcobrand
  - cartel-medicamentos
---

# Caso Colusion de las Farmacias

## Ficha Procesal, Regulatoria y Sancionatoria
- **Rol de Causa / Expediente TDLC**: `= this.ruc` *(Sentencia N° 119/2012 y Rol 2.012-2012 de la Corte Suprema)*
- **Año de Inicio / Requerimiento**: `= this.año_inicio` (Período del cartel: diciembre de 2007 a marzo de 2008)
- **Tribunales Resolutivos**: `= this.tribunal_o_fiscalia`
- **Órgano Persecutor Especializado**: `= this.fiscal_a_cargo` (en coordinación con el [[Servicio Nacional del Consumidor]])
- **Estado Judicial**: `= this.estado_judicial` (Sentencia condenatoria ejecutoriada y compensación civil dictaminada)
- **Infracción / Delito Económico Principal**: `= this.delito_principal`

## Resumen Ejecutivo de la Causa
Investigación y condena emblemática por la formación de un cartel de precios entre las tres principales cadenas farmacéuticas del país: [[Farmacias Ahumada SA]], [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]], las cuales concentraban más del 90% de las ventas de medicamentos en Chile.

La causa se estructuró en cuatro hitos determinantes:
1. **El Cartel de los 222 Medicamentos (2007–2008)**: Entre diciembre de 2007 y marzo de 2008, tras una guerra de descuentos, ejecutivos de las tres cadenas acordaron alzar simultáneamente y de manera escalonada los precios de venta a público de **222 medicamentos críticos** (destinados a tratar enfermedades crónicas como diabetes, hipertensión, asma, úlceras y afecciones cardíacas), utilizando a laboratorios farmacéuticos intermediarios para fiscalizar que ninguna rompiera el pacto ([[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]).
2. **Confesión de FASA y Requerimiento de la FNE (2008–2009)**: En diciembre de 2008, la [[Fiscalia Nacional Economica]] presentó requerimiento ante el TDLC. En marzo de 2009, [[Farmacias Ahumada SA]] liderada por [[Jose Codner Chijner]] suscribió un acuerdo conciliatorio con la FNE ([[Acuerdo-Conciliatorio-FNE-FASA-2009]]), reconociendo los hechos y aportando las pruebas que desnudaron la colusión de [[Farmacias Cruz Verde SA]] ([[Guillermo Harding Alvarado]]) y [[Farmacias Salcobrand SA]] ([[Roberto Belloni Pechini]]).
3. **Condenas Históricas del TDLC y la Corte Suprema (2012)**: En enero de 2012, el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) condenó a Cruz Verde y Salcobrand al pago de la multa máxima contemplada en la ley: **20.000 UTA a cada una** (cerca de US$ 38 millones en conjunto), fallo ratificado íntegramente por la [[Corte Suprema de Chile]] en septiembre de 2012 ([[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]).
4. **Indemnización a Consumidores y Reforma Penal (2016–2020)**: Tras la absolución penal por vacíos en la antigua norma de 1874 (art. 285 CP), el Congreso dictó la Ley N° 20.945 en 2016 restableciendo penas de cárcel efectiva para la colusión. En sede civil, el 10° Juzgado Civil de Santiago y la Corte de Apelaciones acogieron la demanda del [[Servicio Nacional del Consumidor]], obligando a Salcobrand y Cruz Verde a pagar más de **`$2.180.000.000 CLP`** en compensaciones directas a los consumidores afectados ([[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]).

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
