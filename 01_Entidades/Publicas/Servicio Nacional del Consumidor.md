---
tipo_nodo: entidad_publica
rut: ""
categoria: Servicio Público Descentralizado
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Ministerio de Economía, Fomento y Turismo"
tags:
  - entidad/publica
  - sernac
  - proteccion-consumidor
---

# Servicio Nacional del Consumidor

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Servicio estatal encargado de velar por el cumplimiento de la Ley N° 19.496 sobre Protección de los Derechos de los Consumidores. En el [[Caso Colusion del Papel Tissue]], encabezó la mesa de negociación extrajudicial y el Procedimiento Voluntario Colectivo que concluyó en el histórico acuerdo compensatorio de **$97.500.000.000 CLP** pagados por [[Empresas CMPC SA]] a más de 13 millones de chilenos ([[Acuerdo-Compensatorio-SERNAC-CMPC-Tissue-2017]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
