---
tipo_nodo: entidad_privada
rut: "96.648.210-9"
razon_social: "KDM Empresas S.A. (Consorcio KDM / Demarco S.A. / Starco S.A.)"
fecha_constitucion: "1993-11-08"
objeto_social: "Recolección, transporte, tratamiento y disposición final de residuos sólidos domiciliarios e industriales"
representante_legal: "[[Fernando Leon Steffens]]"
tags:
  - entidad/privada
  - concesionaria-residuos
  - caso-basura
---

# KDM Empresas SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Ejecutivo y Representante**: `= this.representante_legal`

## Contexto Forense y Societario
Holding concesionario de recolección de basura y rellenos sanitarios (integrado por sus filiales Demarco S.A. y KDM Tratamiento S.A., filial del grupo Urbaser Danner). En el [[Caso Basura]] ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]), la Fiscalía Regional Metropolitana Occidente imputó que a través de su ejecutivo [[Fernando Leon Steffens]] y del operador municipal [[Marcelo Torres Ferrari]] se habrían canalizado sobornos para asegurar la adjudicación del contrato (el tribunal condenó en 2022 al exconcejal Marcelo Torres por pagos de KDM por $186,5 millones) de recolección de residuos de la [[Municipalidad de Maipu]] por **$18.500.000.000 CLP** ([[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]]) y contrataciones conexas en la [[Municipalidad de Cerro Navia]] bajo la alcaldía de [[Luis Plaza Sanchez]] ([[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]]).

## Historial de Licitaciones y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
