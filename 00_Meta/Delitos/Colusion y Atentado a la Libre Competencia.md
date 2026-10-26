---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 3° inciso segundo letra a) del Decreto Ley N° 211 y Artículo 62 (Ley N° 20.945)"
bien_juridico: "Libre competencia, orden público económico y bienestar de los consumidores"
pena_referencial: "Presidio menor en su grado máximo a presidio mayor en su grado mínimo (3 años y un día a 10 años) y multas a beneficio fiscal"
prescripcion_anos: 5
estado_verificacion: verificado
fuentes:
  - "https://www.bcn.cl/leychile/navegar?idNorma=5872"
  - "https://www.bcn.cl/leychile/navegar?idNorma=1094077"
tags:
  - delito/colusion
  - libre-competencia
  - carteles
---

# Colusion y Atentado a la Libre Competencia

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Sancionatorio**: `= this.pena_referencial`

Sanciona los acuerdos o prácticas concertadas que involucren a competidores entre sí, que consistan en fijar precios de venta o de compra, limitar la producción, asignarse zonas o cuotas de mercado, o afectar el resultado de procesos de licitación. Con la promulgación de la Ley N° 20.945 en 2016, la colusión entre competidores en bienes o servicios de primera necesidad fue recriminalizada en Chile con pena privativa de libertad efectiva.

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
| [Decreto Ley N° 211 — Defensa de la Libre Competencia (Art. 3° y Art. 62)](https://www.bcn.cl/leychile/navegar?idNorma=5872) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 1973-12-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=5872) |
| [Ley N° 20.945 — Perfecciona el Sistema de Defensa de la Libre Competencia y tipifica la colusión](https://www.bcn.cl/leychile/navegar?idNorma=1094077) | Biblioteca del Congreso Nacional (BCN LeyChile) | `primaria` | 2016-08-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.bcn.cl/leychile/navegar?idNorma=1094077) |
