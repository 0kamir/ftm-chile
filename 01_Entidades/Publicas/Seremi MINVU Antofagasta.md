---
tipo_nodo: entidad_publica
rut: "61.812.000-7"
categoria: Ministerio
region: "Antofagasta (II Región)"
superior_jerarquico: "Ministerio de Vivienda y Urbanismo (MINVU)"
tags:
  - entidad/publica
  - minvu
  - antofagasta
---

# Seremi MINVU Antofagasta

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Secretaría Regional Ministerial de Vivienda y Urbanismo de la Región de Antofagasta. Durante el período 2022–2023 estuvo dirigida por [[Carlos Contreras Gutierrez]], militante de [[Revolucion Democratica]], quien suscribió convenios de transferencia directa de recursos públicos del Programa de Asentamientos Precarios con entidades privadas sin experiencia previa acreditada en urbanismo o habitabilidad, entre ellas [[Fundacion Democracia Viva]].

Dichas asignaciones son investigadas en la causa [[Caso Convenios]] y respaldadas por actos administrativos como la [[Resolucion-Exenta-MINVU-Antofagasta-2022]].

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Convenio",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Firmante Público",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
