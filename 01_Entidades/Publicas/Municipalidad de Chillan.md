---
tipo_nodo: entidad_publica
rut: "69.140.900-7"
categoria: Municipio
region: "Ñuble (XVI Región)"
superior_jerarquico: "Concejo Municipal de Chillán (Autónoma)"
tags:
  - entidad/publica
  - municipio
  - chillan
  - caso-luminarias-led
---

# Municipalidad de Chillan

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Corporación edilicia de la capital regional de Ñuble. En el [[Caso Luminarias LED]], el Tribunal de Juicio Oral en lo Penal de Chillán ([[Sentencia-TOP-Chillan-Luminarias-2023]]) dio por acreditado que el ex administrador municipal [[Marcelo Campos Henriquez]] recibió sobornos de [[Itelecom Holding Chile SpA]] ([[Leon Marcelo Lefort Hernandez]]) para adjudicar la licitación de recambio de luminarias LED por **$3.200.000.000 CLP** ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]).

## Nexos y Licitaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Licitación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Empresa",
  firmante_destino AS "Funcionario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
