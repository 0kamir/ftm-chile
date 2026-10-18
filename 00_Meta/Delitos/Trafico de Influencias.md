---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 240 bis del Código Penal"
bien_juridico: "Imparcialidad de las decisiones públicas y jurisdiccionales"
pena_referencial: "Reclusión menor en su grado medio a máximo, inhabilitación y multa"
prescripcion_anos: 5
tags:
  - delito/trafico-de-influencias
---

# Trafico de Influencias

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Sanciona al empleado público que, interesándose directa o indirectamente en cualquier clase de contrato u operación en que deba intervenir otro empleado público, ejerciere influencia en éste para obtener una decisión favorable a sus intereses o de terceros.

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Gestión",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo Nexo",
  entidad_origen AS "Origen",
  entidad_destino AS "Órgano Destino",
  firmante_origen AS "Operador",
  firmante_destino AS "Autoridad",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(delito_imputado), this.file.name)
SORT fecha DESC
```
