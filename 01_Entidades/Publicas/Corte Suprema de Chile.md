---
tipo_nodo: entidad_publica
rut: ""
categoria: Poder Judicial
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Corte Suprema de Justicia (Órgano Autónomo Constitucional)"
tags:
  - entidad/publica
  - poder-judicial
  - corte-suprema
---

# Corte Suprema de Chile

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Máximo tribunal de la República. En el [[Caso Colonia Dignidad]], designó al Ministro en Visita extraordinario [[Jorge Zepeda Arancibia]] para fragmentar la asociación ilícita encabezada por [[Paul Schafer Schneider]] e incautar los arsenales de guerra ocultos en Parral ([[TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01]]), confirmando las condenas definitivas en [[Sentencia-Corte-Suprema-ColoniaDignidad-2013]]. Asimismo, en noviembre de 2003, en el marco del [[Caso Spiniak]], el Pleno debió intervenir de urgencia tras la operación de extorsión con cámara oculta contra el juez Daniel Calvo Flores, removiéndolo de la investigación y designando como Ministro en Visita extraordinario a [[Sergio Munoz Gajardo]] ([[TRX-2003-11-05-Arista-Politica-Spiniak-01]]), quien instruyó la causa hasta la sentencia definitiva [[Sentencia-Corte-Suprema-CasoSpiniak-2008]]. Dos décadas más tarde, en las derivaciones del [[Caso Audios]], el peritaje del teléfono móvil de [[Luis Hermosilla Osorio]] reveló intercambios de mensajería y coordinaciones extraprocesales ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) con la entonces ministra de la Tercera Sala Constitucional [[Angela Vivanco Martinez]], lo que derivó en la apertura de un cuaderno de remoción y su destitución en 2024.

## Nexos y Gestiones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Gestión",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Externo",
  firmante_destino AS "Magistrado / Funcionario",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
