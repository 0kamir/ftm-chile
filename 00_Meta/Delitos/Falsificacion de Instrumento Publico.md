---
tipo_nodo: tipo_penal
articulo_cp: "Artículos 193, 194 y 196 del Código Penal de Chile"
bien_juridico: "Fe pública, autenticidad probatoria y veracidad de documentos estatales"
pena_referencial: "Presidio menor en su grado máximo a presidio mayor en su grado mínimo"
prescripcion_anos: 5
tags:
  - delito/falsificacion-instrumento-publico
  - fe-publica
---

# Falsificacion de Instrumento Publico

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Sanciona al empleado público que, abusando de su oficio, cometiere falsedad contrahaciendo o fingiendo letra, firma o rúbrica, alterando fechas verdaderas, haciendo en documento verdadero cualquier alteración o intercalación que varíe su sentido, atribuyendo a los que han intervenido en él declaraciones o manifestaciones diferentes de las que hubieren hecho, o faltando a la verdad en la narración de hechos sustanciales.

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  firmante_origen AS "Sujeto Origen",
  firmante_destino AS "Sujeto Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(delito_imputado), this.file.name)
SORT fecha DESC
```
