---
tipo_nodo: tipo_penal
articulo_cp: "Artículos 246 y 247 del Código Penal de Chile"
bien_juridico: "Reserva de la información pública y deber de fidelidad funcionaria"
pena_referencial: "Suspensión del empleo en sus grados mínimo a medio y multa de seis a veinte UTM"
prescripcion_anos: 5
estado_verificacion: verificado
fuentes:
  - "https://www.bcn.cl/leychile/navegar?idNorma=1984"
tags:
  - delito/violacion-secreto
---

# Violacion de Secreto

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Tipifica al empleado público que descubre los secretos de que tenga conocimiento por razón de su oficio o entregare indebidamente papeles o copias de papeles que tenga a su cargo y no deban ser publicados, así como la revelación de secretos de particulares de los que tenga conocimiento por razón de su ministerio.

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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Código Penal de Chile — Artículos 246 y 247 (Violación de Secreto)](https://www.bcn.cl/leychile/navegar?idNorma=1984) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 1874-11-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=1984) |
