---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2015
tribunal_o_fiscalia: "Fiscalía Regional de O'Higgins / Tribunal de Juicio Oral en lo Penal de Rancagua"
fiscal_a_cargo: "Emiliano Arias Madariaga / Sergio Moya Domke"
estado_judicial: cerrada_con_condena
delito_principal: "[[Delito Tributario]]"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
  - "https://www.elciudadano.com/?p=524007"
tags:
  - causa
  - especulacion-inmobiliaria
  - caso-caval
---

# Caso Caval

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscales Investigadores**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Cohecho]], [[Negociacion Incompatible]] y [[Trafico de Influencias]])

## Síntesis de la Causa
Investigación penal originada por la compraventa especulativa de los predios Santa Elena, San Diego y Santa Cecilia en la comuna de Machalí por parte de [[Exportadora y de Gestion Caval Ltda]] —sociedad controlada por [[Natalia Compagnon Soto]] y [[Mauricio Valero Illanes]]—. La investigación tuvo dos aristas principales:
1. Pagos al entonces Director de Obras Municipales de la [[Municipalidad de Machali]], [[Jorge Silva Menares]], para impulsar la modificación del Plan Regulador Intercomunal de Rancagua y cambiar el uso de suelo de rural a urbano ([[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]]).
2. La contabilización de facturas ideológicamente falsas y declaraciones maliciosamente incompletas o falsas ante el [[Servicio Impuestos Internos]] para rebajar la carga impositiva de las utilidades de la operación inmobiliaria ([[TRX-2015-01-29-Facturas-Caval-SII-01]]).

El Tribunal de Juicio Oral en lo Penal de Rancagua (julio de 2018) condenó a [[Natalia Compagnon Soto]] por delito tributario (541 días de pena remitida y multa) y **absolvió a [[Mauricio Valero Illanes]] y a [[Exportadora y de Gestion Caval Ltda]]** de los cargos, incluido el de soborno; la Corte Suprema rechazó la nulidad de Compagnon. Por separado, el ex director de obras [[Jorge Silva Menares]] fue condenado en enero de 2018 por cohecho reiterado (818 días con remisión condicional). Ver [[Sentencia-TOP-Rancagua-Caval-2018]].

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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
| [Mauricio Valero fue absuelto](https://www.elciudadano.com/?p=524007) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=524007) |
