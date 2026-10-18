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

## Contexto Forense y Rol de Nodo Puente
Sociedad proveedora de alumbrado público protagonista del [[Caso Luminarias LED]]. A través de su controlador [[Leon Marcelo Lefort Hernandez]], estructuró pagos de sobornos para adjudicarse contratos municipales como el de la [[Municipalidad de Chillan]] por **$3.200.000.000 CLP** ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]], sancionado en [[Sentencia-TOP-Chillan-Luminarias-2023]]). Adicionalmente, actúa como **nodo puente inter-causal** al conectar financieramente con el abogado [[Luis Hermosilla Osorio]] mediante [[TRX-2020-07-08-Asesoria-Itelecom-Hermosilla-01]], enlazando la red municipal de Ñuble con la red del [[Caso Audios]].

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
