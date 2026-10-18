---
tipo_nodo: entidad_privada
rut: "76.419.820-4"
razon_social: "Factop SpA"
fecha_constitucion: "2016-08-10"
objeto_social: "Operaciones de factoring, descuento de documentos y servicios financieros"
representante_legal: "[[Luis Hermosilla Osorio]]"
tags:
  - entidad/privada
  - factoring
  - caso-audios
---

# Factop SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante / Asesor Legal en la Operación**: `= this.representante_legal`

## Contexto Forense y Societario
Sociedad de factoring investigada en el [[Caso Audios]] por emisión de facturas ideológicamente falsas, [[Lavado de Activos]] y [[Cohecho]]. En la reunión registrada en [[Audio-Reunion-Edificio-Alonso-2023]], sus asesores legales [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] estructuraron el fondo de sobornos [[TRX-2023-06-22-Reunion-Audios-01]] dirigido a funcionarios del [[Servicio Impuestos Internos]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Operador Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
