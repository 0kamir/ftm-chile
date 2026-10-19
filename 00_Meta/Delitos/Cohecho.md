---
tipo_nodo: tipo_penal
articulo_cp: "Artículos 248, 248 bis, 249 y 250 del Código Penal"
bien_juridico: "Probidad en la función pública e imparcialidad"
pena_referencial: "Reclusión menor en su grado medio a máximo, multa e inhabilitación"
prescripcion_anos: 5
tags:
  - delito/cohecho
---

# Cohecho

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Comprende tanto el **cohecho pasivo** (funcionario público que solicita o acepta un beneficio económico o de otra naturaleza para ejecutar u omitir un acto propio de su cargo o con infracción a sus deberes) como el **cohecho activo o soborno** (Art. 250 CP, particular que ofrece o consiente en dar dicho beneficio).

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
