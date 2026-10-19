---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal de Maipú (Autónoma)"
tags:
  - entidad/publica
  - municipio
  - maipu
---

# Municipalidad de Maipu

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Corporación edilicia de la Región Metropolitana. Durante la administración 2016–2021 encabezada por [[Cathy Barriga Guerra]], se implementó una modificación en la estructura de control presupuestario que permitió comprometer gastos sin respaldo financiero real por **$30.972.000.000 CLP** ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]), según acreditó el [[Informe-Contraloria-Municipalidad-Maipu-2021]] en el marco del [[Caso Municipalidad de Maipu]].

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Autoridad Municipal",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
