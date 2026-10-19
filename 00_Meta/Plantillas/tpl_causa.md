---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2023
tribunal_o_fiscalia: ""
fiscal_a_cargo: ""
estado_judicial: investigacion # investigacion | formalizada | juicio_oral | cerrada
delito_principal: ""
estado_verificacion: pendiente # verificado | parcial | desactualizado | sin_fuente | pendiente
fuentes:
  - url: "https://"
    titulo: ""
    medio: ""
    tipo: primaria # primaria (documento oficial) | secundaria (prensa / academia)
    fecha: YYYY-MM-DD
    archivo: "https://web.archive.org/"
    consultado: YYYY-MM-DD
tags:
  - causa
---

# {{title}}

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal`

## Resumen Ejecutivo
Descripción de la causa penal, hipótesis investigativa del Ministerio Público y querellantes (CDE).

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
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
