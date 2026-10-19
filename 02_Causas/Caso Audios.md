---
tipo_nodo: causa_judicial
ruc: "2301248910-5"
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Oriente / 4° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Lorena Parra / Felipe Sepúlveda / Juan Pablo Araya"
estado_judicial: formalizada
delito_principal: "[[Cohecho]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
    titulo: "Cinco claves para comprender el caso Audios"
    medio: "Emol"
    tipo: secundaria
    fecha: 2024-08-21
    consultado: 2026-10-19
  - url: "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
    titulo: "Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2024-08-12
    consultado: 2026-10-19
  - url: "https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/"
    titulo: "Caso Audios: Luis Hermosilla será formalizado por la arista Parque Capital"
    medio: "CNN Chile"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - causa
  - caso-audios
  - factop
---

# Caso Audios

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (junto a [[Lavado de Activos]] y delitos tributarios)

## Resumen Ejecutivo
Investigación penal iniciada tras la divulgación en noviembre de 2023 de una grabación de audio de una reunión celebrada en junio de 2023 ([[Audio-Reunion-Edificio-Alonso-2023]]) entre los abogados [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] junto al empresario Daniel Sauer (controlador de [[Factop SpA]]). En dicho registro se coordina la conformación de una "caja negra" de gastos para el pago de sobornos a funcionarios del [[Servicio Impuestos Internos]] y de la [[Comision para el Mercado Financiero]] con el fin de obtener información reservada y destrabar fiscalizaciones tributarias y financieras ([[TRX-2023-06-22-Reunion-Audios-01]]). La incautación del teléfono de [[Luis Hermosilla Osorio]] abrió además aristas estructurales de [[Trafico de Influencias]]: los presuntos pagos desde [[Factop SpA]] (según la Fiscalía; Hermosilla sostiene que Daniel Sauer solo actuó como intermediario y que le reembolsó) para financiar la defensa en la Acusación Constitucional de 2019 y remesas por `$190.000.000 CLP` a su socio de oficina y exministro del Interior [[Andres Chadwick Pinera]] ([[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]), la red de nombramientos en la [[Corte Suprema de Chile]] con la exministra [[Angela Vivanco Martinez]] ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) y las indagatorias que mantienen en calidad de imputado al penalista [[Gabriel Zaliasnik Schilkrut]] por presuntas gestiones en designaciones judiciales ([[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]]).

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Sujeto Origen",
  firmante_destino AS "Sujeto Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
