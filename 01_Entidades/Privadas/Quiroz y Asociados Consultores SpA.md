---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Quiroz y Asociados Consultores SpA"
fecha_constitucion: 1998-05-12
objeto_social: "Asesorías económicas, consultoría macroeconómica, estudios de mercado y libre competencia"
representante_legal: "[[Jorge Quiroz Castro]]"
tags:
  - entidad/privada
  - consultoria
  - libre-competencia
  - peritaje-economico
---

# Quiroz y Asociados Consultores SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Socio Principal**: `= this.representante_legal`

## Contexto en Investigaciones y Regulatorias
Firma de consultoría económica y financiera fundada y encabezada por el economista [[Jorge Quiroz Castro]]. La consultora prestó servicios y estudios económicos para diversas empresas y asociaciones gremiales investigadas por la [[Fiscalia Nacional Economica]] y sometidas a proceso ante el Tribunal de Defensa de la Libre Competencia (TDLC).

Entre sus principales encargos documentados en expedientes de libre competencia se encuentran los modelos de demanda y proyección confeccionados para la [[Asociacion de Productores Avicolas de Chile AG]] ([[Caso Colusion de los Pollos]]) e informes económicos de defensa para [[Farmacias Salcobrand SA]] ([[Caso Colusion de las Farmacias]]).

## Registros Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito Imputado"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
