---
tipo_nodo: entidad_publica
rut: "61.970.200-K"
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
Dirección de Compras y Contratación Pública (administradora de la plataforma `mercadopublico.cl`), dependiente del Ministerio de Hacienda. En el [[Caso Compras Publicas]], los registros de órdenes de compra por trato directo ([[Orden-Compra-MercadoPublico-2023]]) permiten auditar contrataciones de consultoría como [[TRX-2023-08-14-Trato-Directo-ChileCompra-01]] adjudicadas a [[Consultora Gestion Publica SpA]] ([[Jorge Valdivia Correa]]).

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
