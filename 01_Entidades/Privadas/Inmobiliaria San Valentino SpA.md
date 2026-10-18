---
tipo_nodo: entidad_privada
rut: "77.418.920-3"
razon_social: "Inmobiliaria e Inversiones San Valentino SpA"
fecha_constitucion: "2022-04-05"
objeto_social: "Inversiones inmobiliarias, compra, venta y arrendamiento de bienes raíces y establecimientos de salud"
representante_legal: "[[Felipe Sanchez Perez]]"
tags:
  - entidad/privada
  - sociedad-inmobiliaria
  - caso-sierra-bella
---

# Inmobiliaria San Valentino SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal y Controlador**: `= this.representante_legal`

## Contexto Forense y Societario
Sociedad por acciones constituida en abril de 2022 y representada por [[Felipe Sanchez Perez]]. Apenas meses después de adquirir el inmueble de calle Sierra Bella N° 1181 por cerca de `$2.080.000.000 CLP`, pactó en enero de 2023 su venta por trato directo a la [[Municipalidad de Santiago]] ([[Iraci Hassler Jacob]]) en **$8.200.000.000 CLP** (casi cuatro veces su valor de adquisición previa), lo que activó la bandera roja de **Constitución Societaria Reciente (`< 365 días`)** y el bloqueo administrativo de la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) en el [[Caso Sierra Bella]] ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]], [[Dictamen-CGR-SierraBella-2023]]).

## Historial de Contratos y Nexos Reificados
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
