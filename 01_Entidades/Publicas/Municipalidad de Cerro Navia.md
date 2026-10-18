---
tipo_nodo: entidad_publica
rut: "69.071.300-4"
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal de Cerro Navia (Autónoma)"
autoridad_vinculada: "[[Luis Plaza Sanchez]]"
tags:
  - entidad/publica
  - municipio
  - cerro-navia
  - caso-basura
---

# Municipalidad de Cerro Navia

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Autoridad Vinculada**: `= this.autoridad_vinculada` (y ex Administrador Municipal [[Marcelo Torres Ferrari]])

## Contexto en Investigaciones Forenses
Corporación edilicia del sector poniente de la Región Metropolitana. En el [[Caso Basura]], la Fiscalía Regional Metropolitana Occidente ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]) investigó al exalcalde [[Luis Plaza Sanchez]] y al exadministrador municipal [[Marcelo Torres Ferrari]] (ambos vinculados a [[Renovacion Nacional]]) por irregularidades, sobreprecios y direccionamiento de contrataciones de aseo, ornato y manejo de residuos vinculadas al circuito de [[KDM Empresas SA]] por **$1.120.000.000 CLP** ([[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]]).

## Nexos y Contratos Registrados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
