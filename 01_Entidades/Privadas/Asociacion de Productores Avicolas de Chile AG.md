---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Asociación de Productores Avícolas de Chile A.G. (APA)"
fecha_constitucion: 1980-04-10
objeto_social: "Asociación gremial de representación, coordinación y fomento de la industria avícola chilena"
representante_legal: "[[Juan Miguel Ovalle Garces]]"
tags:
  - entidad/privada
  - apa
  - gremio
  - colusion-pollos
  - disuelta-por-sentencia
---

# Asociacion de Productores Avicolas de Chile AG

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal Histórico**: [[Juan Miguel Ovalle Garces]]
- **Estado Legal**: **Disuelta por Orden Judicial** ([[Sentencia-TDLC-139-Colusion-Pollos-2014]] ratificada por [[Sentencia-Corte-Suprema-Colusion-Pollos-2015]])

## Contexto en Investigaciones Forenses
Asociación gremial que agrupaba a las empresas productoras de carne de ave en Chile ([[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]]). En el [[Caso Colusion de los Pollos]], la FNE y los tribunales acreditaron que la APA funcionó como la secretaría técnica y órgano ejecutivo del cartel: proyectaba la demanda de pollo a nivel país, fijaba las cuotas de faenamiento para cada productor y realizaba auditorías de verificación para sancionar a quienes rompieran los acuerdos colusorios.

En una resolución sin precedentes en el derecho chileno de la competencia, el TDLC y la Corte Suprema ordenaron su **disolución forzada**, al haberse demostrado que su objeto real era facilitar y ejecutar conductas ilícitas contrarias a la libre competencia.

## Auditoría Contable: Registros Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito Imputado"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
