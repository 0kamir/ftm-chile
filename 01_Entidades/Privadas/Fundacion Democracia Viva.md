---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Fundación Democracia Viva"
fecha_constitucion: "2022-02-25"
objeto_social: "Participación ciudadana, formación política, estudios sociales y culturales"
representante_legal: "[[Daniel Andrade Schwarze]]"
tags:
  - entidad/privada
  - fundacion
  - caso-convenios
---

# Fundacion Democracia Viva

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut` (RUT de referencia forense)
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`

## Contexto Forense y Societario
Organización sin fines de lucro constituida en el año 2022 ante la Municipalidad de Ñuñoa e inscrita en el Registro de Personas Jurídicas Receptoras de Fondos Públicos pocos meses antes de adjudicarse trato directo con la [[Seremi MINVU Antofagasta]].

Su representante legal, [[Daniel Andrade Schwarze]] (militante de [[Revolucion Democratica]]), suscribió con el entonces Seremi [[Carlos Contreras Gutierrez]] el convenio [[TRX-2022-10-03-Convenio-DV-01]] por un total acumulado de **$426.000.000 CLP**, documentado en la [[Resolucion-Exenta-MINVU-Antofagasta-2022]] e investigado penalmente en el [[Caso Convenios]].

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
