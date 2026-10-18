---
tipo_nodo: entidad_publica
rut: "60.506.000-5"
categoria: Policía
region: "Nacional / Macrozona Sur (UIOE Temuco)"
superior_jerarquico: "Carabineros de Chile / Ministerio del Interior y Seguridad Pública"
tags:
  - entidad/publica
  - carabineros
  - dipolcar
  - uioe
  - caso-operacion-huracan
---

# Direccion de Inteligencia Policial de Carabineros

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
La Dirección de Inteligencia Policial de Carabineros (DIPOLCAR) y su Unidad de Inteligencia Operativa Especializada (UIOE) con base en Temuco fueron la estructura policial y de mando responsable del montaje de la [[Caso Operacion Huracan]], encabezada por el general [[Gonzalo Blu Rodriguez]], el excoronel [[Marcelo Teuber Munoz]], el exmayor [[Patricio Marin Lazo]], el excapitán [[Leonardo Osses Sandoval]] y el perito civil [[Alex Smith Leay]], bajo la jefatura institucional del general director [[Bruno Villalobos Krumm]]. La unidad fue clausurada tras descubrirse la implantación fraudulenta de supuestos chats de mensajería para incriminar a comuneros mapuche bajo la Ley Antiterrorista.

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
