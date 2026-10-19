---
tipo_nodo: causa_judicial
ruc: "1400637392-6"
año_inicio: 2014
tribunal_o_fiscalia: "Fiscalía Nacional / Fiscalía Regional Metropolitana Oriente / 8° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Carlos Gajardo Pinto / Manuel Guerra Fuenzalida"
estado_judicial: cerrada_con_condena
delito_principal: "[[Delito Tributario]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
    titulo: "Lavín y Délano comenzaron las clases de ética tras condena del caso Penta"
    medio: "24 Horas"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
    titulo: "Cartas: 'Good bye' a las clases de ética"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2024-06-07
    consultado: 2026-10-19
alertas_verificacion:
  - "Prensa: la condena de 2018 (procedimiento abreviado) fue por delitos tributarios; CIPER señala que nadie fue condenado por cohecho. Revisar TRX-2011-03-10-Soborno-Penta-Wagner-01."
tags:
  - causa
  - financiamiento-politico
  - caso-penta
---

# Caso Penta

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscales Investigadores**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Cohecho]] y [[Lavado de Activos]])

## Síntesis Forense de la Causa
Investigación penal iniciada a partir de denuncias y querellas del [[Servicio Impuestos Internos]] por devoluciones fraudulentas de impuestos que destapó una estructura sistemática de financiamiento ilegal de campañas políticas de la [[Union Democrata Independiente]] mediante la emisión de boletas de honorarios y facturas ideológicamente falsas contra [[Empresas Penta SA]] ([[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] y [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]]), dirigida por sus controladores [[Carlos Alberto Delano Abbott]] y [[Carlos Eugenio Lavin Garcia-Huidobro]] en beneficio de dirigentes como [[Pablo Longueira Montes]] y el exsenador [[Jovino Novoa Vasquez]] (primer político condenado en juicio abreviado en diciembre de 2015). Asimismo, acreditó pagos periódicos de sobornos al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] mientras ejercía su cargo público ([[TRX-2011-03-10-Soborno-Penta-Wagner-01]]), concluyendo con las sentencias condenatorias documentadas en [[Sentencia-8Juzgado-Garantia-Penta-2018]].

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
