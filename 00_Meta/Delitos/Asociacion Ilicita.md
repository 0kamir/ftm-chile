---
tipo_nodo: tipo_penal
articulo_cp: "Artículos 292, 293 y 294 del Código Penal de Chile"
bien_juridico: "Seguridad y orden público"
pena_referencial: "Presidio mayor en cualquiera de sus grados para jefes/organizadores; presidio menor para partícipes"
prescripcion_anos: 10
estado_verificacion: verificado
fuentes:
  - "https://www.bcn.cl/leychile/navegar?idNorma=1984"
tags:
  - delito/asociacion-ilicita
---

# Asociacion Ilicita

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Toda asociación formada con el fin de atentar contra el orden social, contra las buenas costumbres, contra las personas o las propiedades, importa un delito que existe por el solo hecho de organizarse. Se aplica a organizaciones criminales estructuradas, clanes de fraude tributario organizado (como en la Operación Tributos) y redes de cohecho y corrupción sistemática.

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(delito_imputado), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Código Penal de Chile — Artículos 292, 293 y 294 (Asociación Ilícita)](https://www.bcn.cl/leychile/navegar?idNorma=1984) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 1874-11-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=1984) |
