---
tipo_nodo: entidad_privada
rut: "93.007.000-9"
razon_social: "Sociedad Química y Minera de Chile S.A. (SQM)"
fecha_constitucion: "1968-06-29"
objeto_social: "Explotación minera no metálica, producción de litio, yodo y fertilizantes de especialidad"
representante_legal: "[[Patricio Contesse Gonzalez]]"
tags:
  - entidad/privada
  - minera
  - caso-sqm
---

# SQM SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Gerente General en Período Investigado**: `= this.representante_legal`

## Contexto Forense y Societario
Empresa minera investigada en el [[Caso SQM]] tras las denuncias y querellas del [[Servicio Impuestos Internos]] ([[Querella-SII-Boletas-SQM-2015]]) por contabilizar como gastos necesarios para producir la renta miles de boletas de honorarios y facturas ideológicamente falsas ([[Delito Tributario]]), empleadas para financiar campañas políticas y pagar beneficios económicos ([[Cohecho]]) asociados a la tramitación del artículo de invariabilidad tributaria del Royalty Minero ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]).

## Historial de Nexos y Pagos Investigados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Ejecutivo Origen",
  firmante_destino AS "Destinatario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
