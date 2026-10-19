---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Metropolitana de Santiago"
superior_jerarquico: "Ministerio de Hacienda"
tags:
  - entidad/publica
  - chilecompra
  - mercado-publico
---

# Direccion ChileCompra

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Dirección de Compras y Contratación Pública (administradora de la plataforma `mercadopublico.cl`), dependiente del Ministerio de Hacienda. Sus registros de órdenes de compra y tratos directos (API de datos abiertos) son fuente primaria para documentar nexos de contratación pública en el vault.

## Nexos y Órdenes de Compra Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Orden",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Proveedor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
