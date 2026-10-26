---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 233 del Código Penal"
bien_juridico: "Patrimonio público y deber de custodia funcionaria"
pena_referencial: "Presidio menor en su grado medio a presidio mayor en su grado máximo e inhabilitación perpetua"
prescripcion_anos: 10
estado_verificacion: verificado
fuentes:
  - "https://www.bcn.cl/leychile/navegar?idNorma=1984"
tags:
  - delito/malversacion
---

# Malversacion de Caudales Publicos

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

El empleado público que, teniendo a su cargo caudales o efectos públicos o de particulares en depósito, consignación o secuestro, los substrajere o consintiere que otro los substraiga.

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Órgano Público",
  entidad_destino AS "Entidad Receptora",
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
| [Código Penal de Chile — Artículo 233 (Malversación de Caudales Públicos)](https://www.bcn.cl/leychile/navegar?idNorma=1984) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 1874-11-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=1984) |
