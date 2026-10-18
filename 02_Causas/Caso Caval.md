---
tipo_nodo: causa_judicial
ruc: "1500169916-0"
año_inicio: 2015
tribunal_o_fiscalia: "Fiscalía Regional de O'Higgins / Tribunal de Juicio Oral en lo Penal de Rancagua"
fiscal_a_cargo: "Emiliano Arias Madariaga / Sergio Moya Domke"
estado_judicial: cerrada_con_condena
delito_principal: "[[Delito Tributario]]"
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

## Síntesis Forense de la Causa
Investigación penal originada por la compraventa especulativa de los predios Santa Elena, San Diego y Santa Cecilia en la comuna de Machalí por parte de [[Exportadora y de Gestion Caval Ltda]] —sociedad controlada por [[Natalia Compagnon Soto]] y [[Mauricio Valero Illanes]]—. La investigación acreditó dos aristas principales:
1. Pagos ilícitos de cohecho al entonces Director de Obras Municipales de la [[Municipalidad de Machali]], [[Jorge Silva Menares]], para impulsar la modificación del Plan Regulador Intercomunal de Rancagua y cambiar el uso de suelo de rural a urbano ([[TRX-2014-02-18-Soborno-Caval-Machali-01]]).
2. La contabilización de facturas ideológicamente falsas y declaraciones maliciosamente incompletas o falsas ante el [[Servicio Impuestos Internos]] para rebajar la carga impositiva de las utilidades de la operación inmobiliaria ([[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]]), concluyendo con las condenas ejecutoriadas en [[Sentencia-TOP-Rancagua-Caval-2018]].

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
