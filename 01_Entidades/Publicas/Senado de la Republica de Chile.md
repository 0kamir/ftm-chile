---
tipo_nodo: entidad_publica
rut: "60.201.000-7"
categoria: Ministerio
region: "Valparaíso (V Región) / Nacional"
superior_jerarquico: "Congreso Nacional de Chile (Poder Legislativo)"
tags:
  - entidad/publica
  - senado
  - poder-legislativo
---

# Senado de la Republica de Chile

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria` *(Corporación del Poder Legislativo)*
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Cámara alta del Congreso Nacional. En el [[Caso Corpesca]], el tribunal acreditó mediante la [[Sentencia-3TOP-Santiago-Corpesca-2021]] que el entonces integrante de la Comisión de Intereses Marítimos, Pesca y Acuicultura del Senado, [[Jaime Orpis Bouchon]] ([[Union Democrata Independiente]]), actuó bajo mandato e instrucciones financieras de [[Corpesca SA]] ([[Francisco Mujica Ortuzar]]) a cambio de pagos por **$233.000.000 CLP** ([[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Cohecho",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen Privado",
  firmante_destino AS "Senador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
