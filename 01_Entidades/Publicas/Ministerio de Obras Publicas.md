---
tipo_nodo: entidad_publica
rut: "61.202.000-0"
categoria: Ministerio
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Presidencia de la República de Chile"
autoridad_vinculada: "[[Carlos Cruz Lorenzen]]"
tags:
  - entidad/publica
  - ministerio
  - caso-mop-gate
---

# Ministerio de Obras Publicas

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Autoridad Vinculada**: `= this.autoridad_vinculada`

## Contexto en Investigaciones Forenses
Secretaría de Estado encargada de la infraestructura vial y concesiones públicas. En el [[Caso MOP-Gate]], la investigación judicial acreditó que bajo la gestión del ex Ministro [[Carlos Cruz Lorenzen]] se suscribieron contratos simulados o con sobreprecios deliberados con consultoras privadas como [[Gestion Ambiental y Territorial SA]] ([[Hector Pena Veliz]]) por **$1.253.000.000 CLP** para desviar caudales fiscales hacia el pago de sobresueldos y gastos extrapresupuestarios ([[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]], [[Sentencia-Corte-Suprema-MOPGate-2016]]).

## Historial de Nexos y Contratos Auditados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Consultora / Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
