---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 239 del Código Penal"
bien_juridico: "Probidad administrativa y patrimonio fiscal"
pena_referencial: "Presidio menor en su grado medio a presidio mayor en su grado medio (según monto en UTM)"
prescripcion_anos: 5
estado_verificacion: verificado
fuentes:
  - "https://www.bcn.cl/leychile/navegar?idNorma=1984"
tags:
  - delito/fraude-al-fisco
---

# Fraude al Fisco

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

El empleado público que en las operaciones en que interviniere por razón de su cargo, defraudare o consintiere que se defraude al Estado, a las municipalidades o a los establecimientos públicos de instrucción o de beneficencia, sea originándoles pérdida o privándoles de un lucro legítimo.

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Pública",
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
| [Código Penal de Chile — Artículo 239 (Fraude al Fisco)](https://www.bcn.cl/leychile/navegar?idNorma=1984) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 1874-11-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=1984) |
