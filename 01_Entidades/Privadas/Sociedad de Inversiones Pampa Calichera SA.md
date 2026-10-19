---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Sociedad de Inversiones Pampa Calichera S.A."
fecha_constitucion: "1988-06-21"
objeto_social: "Sociedad de inversiones y holding controlador de acciones serie A y B de SQM S.A."
representante_legal: "[[Julio Ponce Lerou]]"
tags:
  - entidad/privada
  - sociedad-cascada
  - caso-cascadas
---

# Sociedad de Inversiones Pampa Calichera SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Presidente y Controlador**: `= this.representante_legal`

## Contexto y Societario
Sociedad de inversión que forma el eslabón principal de las llamadas "Sociedades Cascada" a través de las cuales [[Julio Ponce Lerou]] ejerció el control de [[SQM SA]] (gerenciada operativamente por [[Patricio Contesse Gonzalez]]). En el [[Caso Cascadas]] ([[Resolucion-SVS-CasoCascadas-2014]]), la [[Comision para el Mercado Financiero]] (entonces SVS) acreditó que [[Sociedad de Inversiones Pampa Calichera SA]] vendió paquetes accionarios a precios subvalorados a sociedades relacionadas con su propio controlador para luego recomprarlos a sobreprecio, irrogando un perjuicio multimillonario a los accionistas minoritarios y AFPs ([[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]]).

## Historial de Operaciones y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
