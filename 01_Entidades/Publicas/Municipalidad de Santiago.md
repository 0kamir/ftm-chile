---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal de Santiago (Autónoma)"
autoridad_vinculada: "[[Iraci Hassler Jacob]]"
tags:
  - entidad/publica
  - municipio
  - santiago
  - caso-sierra-bella
---

# Municipalidad de Santiago

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Autoridad Vinculada**: `= this.autoridad_vinculada`

## Contexto en Investigaciones Forenses
Corporación edilicia de la comuna capital de Chile. En el [[Caso Sierra Bella]], bajo la administración de la alcaldesa [[Iraci Hassler Jacob]] (militante del [[Partido Comunista de Chile]]), suscribió una escritura de compraventa por **$8.200.000.000 CLP** para adquirir el inmueble de [[Inmobiliaria San Valentino SpA]] ([[Felipe Sanchez Perez]]) cuyo avalúo fiscal e historial de compra previa rondaba los `$2.080.000.000 CLP`, operación objetada por la [[Contraloria General de la Republica]] dirigida por [[Jorge Bermudez Soto]] ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]], [[Dictamen-CGR-SierraBella-2023]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
