---
tipo_nodo: causa_judicial
ruc: "2300918450-6"
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía de Alta Complejidad Centro Norte"
fiscal_a_cargo: "Giovanna Herrera"
estado_judicial: investigacion
delito_principal: "[[Negociacion Incompatible]]"
estado_verificacion: sin_fuente
fuentes: []
alertas_verificacion:
  - "CRÍTICO: no se encontró ninguna fuente pública para 'Consultora Gestion Publica SpA', 'Jorge Valdivia Correa' ni para esta causa. Puede ser un registro de ejemplo o ficticio: no publicar como hecho hasta verificarlo o retirarlo."
tags:
  - causa
  - compras-publicas
  - mercado-publico
---

# Caso Compras Publicas

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` *(Investigación penal desformalizada y sumario administrativo CGR)*
- **Delito Principal**: `= this.delito_principal`

## Resumen Ejecutivo
Investigación desformalizada originada a partir de cruces masivos de datos del Observatorio de Compras Públicas de la [[Direccion ChileCompra]] y auditorías de la Contraloría General de la República sobre adjudicaciones vía trato directo ([[TRX-2023-08-14-Trato-Directo-ChileCompra-01]]) a sociedades proveedoras constituidas recientemente o vinculadas a asesores externos ([[Consultora Gestion Publica SpA]], representada por [[Jorge Valdivia Correa]]), respaldadas en registros de [[Orden-Compra-MercadoPublico-2023]].

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Órgano Comprador",
  entidad_destino AS "Proveedor Adjudicado",
  firmante_destino AS "Representante Proveedor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Orden de Compra"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
