---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Consejo Local de Deportes Vitacura (Vita Deportes)"
fecha_constitucion: "2001-06-12"
objeto_social: "Fomento del deporte comunal y administración de recintos deportivos en Vitacura"
representante_legal: "[[Domingo Prieto Urrejola]]"
tags:
  - entidad/privada
  - organizacion-comunitaria
  - caso-vitacura
---

# Vita Deportes

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`

## Contexto y Societario
Organización comunitaria funcional que recibía cuantiosas subvenciones anuales de la [[Municipalidad de Vitacura]]. En el [[Caso Vitacura]], su expresidente y representante legal [[Domingo Prieto Urrejola]] reveló mediante [[Declaracion-Judicial-Prieto-Vitacura-2021]] el mecanismo de extracción en efectivo de fondos provenientes de subvenciones municipales ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]) entregados a [[Raul Torrealba del Pedregal]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_destino AS "Firmante Receptor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
