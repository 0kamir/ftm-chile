---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal de Vitacura (Autónoma)"
tags:
  - entidad/publica
  - municipio
  - vitacura
---

# Municipalidad de Vitacura

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Corporación edilicia encabezada entre 1996 y 2021 por el alcalde [[Raul Torrealba del Pedregal]]. En el [[Caso Vitacura]], el Ministerio Público y el Consejo de Defensa del Estado acreditaron el uso de corporaciones privadas sin fines de lucro ("Programas Vita", como [[Vita Deportes]]) para eludir los controles de la Contraloría sobre el presupuesto municipal y sustraer fondos públicos ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]).

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Subvención",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Autoridad Municipal",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
