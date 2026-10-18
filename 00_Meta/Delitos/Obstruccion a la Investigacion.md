---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 269 bis del Código Penal de Chile"
bien_juridico: "Correcta administración de justicia y eficacia de la persecución penal"
pena_referencial: "Presidio menor en sus grados mínimo a medio y multa de dos a doce UTM"
prescripcion_anos: 5
tags:
  - delito/obstruccion-investigacion
  - administracion-justicia
---

# Obstruccion a la Investigacion

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Sanciona a quien, a sabiendas, obstaculice gravemente la investigación de un crimen o simple delito aportando antecedentes falsos que condujeren al Ministerio Público a realizar actuaciones inútiles o perjudiciales para la investigación, o destruyendo, alterando u ocultando el cuerpo, los efectos o los instrumentos de un delito. Si quien incurre en esta conducta es un funcionario policial o del Ministerio Público, la pena se agrava en un grado.

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
