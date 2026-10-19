---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "O'Higgins (VI Región)"
superior_jerarquico: "Concejo Municipal de Machalí (Autónoma)"
autoridad_vinculada: "[[Jorge Silva Menares]]"
tags:
  - entidad/publica
  - municipalidad
  - caso-caval
---

# Municipalidad de Machali

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Funcionario Investigado (DOM)**: `= this.autoridad_vinculada`

## Contexto Forense y Administrativo
Corporación edilicia de la Región de O'Higgins cuya Dirección de Obras Municipales (DOM), encabezada por [[Jorge Silva Menares]], intervino técnicamente en los informes favorables para el cambio de uso de suelo de rural a urbano de los 44 hectáreas de predios adquiridos por [[Exportadora y de Gestion Caval Ltda]] ([[Natalia Compagnon Soto]] y [[Mauricio Valero Illanes]]), con pagos por los que su director de obras fue condenado por cohecho en el [[Caso Caval]] (los socios de Caval fueron absueltos del soborno) ([[TRX-2014-02-18-Soborno-Caval-Machali-01]], [[Sentencia-TOP-Rancagua-Caval-2018]]).

## Historial de Nexos y Transacciones Auditadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
