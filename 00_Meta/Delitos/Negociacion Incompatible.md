---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 240 del Código Penal"
bien_juridico: "Imparcialidad y transparencia de la contratación pública"
pena_referencial: "Reclusión menor en su grado medio a máximo, inhabilitación y multa"
prescripcion_anos: 5
estado_verificacion: verificado
fuentes:
  - "https://www.bcn.cl/leychile/navegar?idNorma=1984"
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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Código Penal de Chile — Artículo 240 (Negociación Incompatible)](https://www.bcn.cl/leychile/navegar?idNorma=1984) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 1874-11-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=1984) |
