---
tipo_nodo: entidad_privada
rut: "65.184.310-3"
razon_social: "Fundación En Ti"
fecha_constitucion: "2018-05-14"
objeto_social: "Capacitación comunitaria, desarrollo social y apoyo barrial"
representante_legal: "[[Camila Polizzi Fonceca]]"
tags:
  - entidad/privada
  - fundacion
  - caso-convenios
  - biobio
---

# Fundacion En Ti

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Gestora**: `= this.representante_legal`

## Contexto Forense y Societario
Fundación utilizada mediante mecanismo de "arriendo de personalidad jurídica" por [[Camila Polizzi Fonceca]] para sortear el requisito de antigüedad mínima exigido por el [[GORE Biobio]] y adjudicarse el convenio [[TRX-2022-12-20-Convenio-EnTi-01]] por **$250.635.000 CLP**, respaldado en la [[Resolucion-GORE-Biobio-EnTi-2022]] e investigado en el [[Caso Convenios]].

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
