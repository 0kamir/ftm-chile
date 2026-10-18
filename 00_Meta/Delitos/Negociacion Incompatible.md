---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 240 del Código Penal"
bien_juridico: "Imparcialidad y transparencia de la contratación pública"
pena_referencial: "Reclusión menor en su grado medio a máximo, inhabilitación y multa"
prescripcion_anos: 5
tags:
  - delito/negociacion-incompatible
---

# Negociacion Incompatible

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Delito de peligro abstracto que sanciona al empleado público que directa o indirectamente se interesare en cualquier negociación, actuación, contrato, operación o gestión en la cual hubiere de intervenir en razón de su cargo, o diere interés a personas vinculadas por parentesco, sociedad o asociación.

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Pública",
  entidad_destino AS "Contraparte",
  firmante_origen AS "Autorizador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(delito_imputado), this.file.name)
SORT fecha DESC
```
