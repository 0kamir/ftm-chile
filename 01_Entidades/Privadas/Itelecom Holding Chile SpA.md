---
tipo_nodo: entidad_privada
rut: "76.284.190-8"
razon_social: "Itelecom Holding Chile SpA"
fecha_constitucion: "2013-07-22"
objeto_social: "Ingeniería eléctrica, eficiencia energética, telegestión y alumbrado público LED"
representante_legal: "[[Leon Marcelo Lefort Hernandez]]"
tags:
  - entidad/privada
  - proveedor-municipal
  - caso-luminarias-led
  - nodo-puente
---

# Itelecom Holding Chile SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Gerente General y Controlador**: `= this.representante_legal`

## Contexto Forense
Sociedad proveedora de alumbrado público investigada en el [[Caso Luminarias LED]]. La Fiscalía sostiene que, a través de su controlador [[Leon Marcelo Lefort Hernandez]], ofreció sobornos para adjudicarse contratos municipales como el de la [[Municipalidad de Chillan]] ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]). Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

## Historial de Nexos y Operaciones Investigadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
