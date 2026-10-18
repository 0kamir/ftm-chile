---
tipo_nodo: entidad_publica
rut: "61.202.000-0"
categoria: Servicio Público Autónomo
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Ministerio de Economía, Fomento y Turismo (Supervigilancia)"
tags:
  - entidad/publica
  - fne
  - libre-competencia
  - carteles
---

# Fiscalia Nacional Economica

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Agencia pública descentralizada encargada de instruir investigaciones y perseguir infracciones contra la libre competencia (Decreto Ley N° 211). En el [[Caso Colusion del Papel Tissue]], desarticuló el cartel de más de una década entre [[Empresas CMPC SA]] y [[SCA Chile SA]], haciendo valer por primera vez en un caso de gran impacto masivo el mecanismo de delación compensada que derivó en la [[Sentencia-TDLC-160-Colusion-Tissue-2017]].

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
