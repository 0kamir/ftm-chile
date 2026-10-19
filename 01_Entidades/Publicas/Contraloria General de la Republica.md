---
tipo_nodo: entidad_publica
rut: ""
categoria: Órgano Contralor Constitucionalmente Autónomo
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Autonomía Constitucional"
autoridad_vinculada: "[[Jorge Bermudez Soto]]"
tags:
  - entidad/publica
  - contraloria
  - toma-de-razon
  - fiscalizacion
---

# Contraloria General de la Republica

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Contralor General (2015-2023)**: `= this.autoridad_vinculada`

## Contexto en Investigaciones Forenses
Órgano superior de fiscalización de la Administración del Estado. En el grafo forense interviene directamente tanto en la detección del fraccionamiento de convenios bajo las `5.000 UTM` en el [[Caso Convenios]] ([[Seremi MINVU Antofagasta]] / [[Fundacion Democracia Viva]]) como en el bloqueo y auditoría de la compraventa con sobreprecio de la ex Clínica Sierra Bella en la [[Municipalidad de Santiago]] ([[Caso Sierra Bella]], [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]], [[Dictamen-CGR-SierraBella-2023]]).

## Historial de Nexos y Fiscalizaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Acto Fiscalizado",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Auditada",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
