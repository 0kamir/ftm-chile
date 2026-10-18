---
tipo_nodo: entidad_publica
rut: "61.101.000-1"
categoria: Ministerio
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Ejército de Chile / Ministerio de Defensa Nacional"
tags:
  - entidad/publica
  - ejercito
  - caso-milicogate
---

# Comando de Apoyo a la Fuerza del Ejercito

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Unidad logística del Ejército de Chile encargada de la gestión de adquisiciones y mantenimiento con cargo a los fondos de la Ley Reservada del Cobre. En el [[Caso Milicogate]], se acreditó la operación de un mecanismo de pago de facturas ideológicamente falsas a empresas proveedoras como [[Frasim Ltda]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]) por **$6.100.000.000 CLP**, con participación del coronel (r) [[Jozo Santic Palomino]] y bajo el período de mando institucional de [[Juan Miguel Fuente-Alba Poblete]] ([[Auto-Procesamiento-Ministra-Rutherford-2019]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Desfalco",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Proveedor",
  firmante_destino AS "Oficial Condenado",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
