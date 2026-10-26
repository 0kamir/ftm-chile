---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal / Contraloría General de la República"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/"
  - "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/07/04/exalcalde-aguilera-no-ira-a-la-carcel-por-corrupcion-le-quitaran-casa-y-debe-pagar-millonarias-multas.shtml"
  - "https://www.meganoticias.cl/nacional/491103-sentencian-condenan-cuatro-anos-exalcalde-san-ramon-miguel-angel-aguilera-corrupcion-brk-4-7-2025.html"
tags:
  - entidad/publica
  - municipalidad
  - san-ramon
---

# Municipalidad de San Ramón

## Rol Institucional y Vínculos en la Red
Corporación autónoma de derecho público encargada de la administración local de la comuna de San Ramón, en la zona sur de la Región Metropolitana. Durante la gestión alcaldicia de [[Miguel Angel Aguilera Sanhueza]] (2012–2021), el municipio fue epicentro del [[Caso Municipalidad de San Ramon]], acreditándose judicialmente ante el 6° TOP de Santiago un incremento patrimonial injustificado de **$246.918.500 CLP** y maniobras de [[Lavado de Activos]] para adquirir bienes raíces con fondos de origen ilícito ([[Sentencia-TOP-Santiago-SanRamon-Aguilera-2025]], [[TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01]]).

## Flujos Financieros de Salida (Egresos / Pagos / Contratos)
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción",
  fecha AS "Fecha",
  entidad_destino AS "Destinatario",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa Judicial"
FROM "03_Hechos_y_Nexos"
WHERE entidad_origen = this.file.link
SORT fecha ASC
```

## Flujos Financieros de Entrada
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa Judicial"
FROM "03_Hechos_y_Nexos"
WHERE entidad_destino = this.file.link
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Libertad vigilada, millonaria multa y adiós a casa en La Reina: la condena al exalcalde de San Ramón](https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/) | El Mostrador | `secundaria` | 2025-07-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/) |
| [Exalcalde Aguilera no irá a la cárcel por corrupción: le quitarán casa y debe pagar millonarias multas](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/07/04/exalcalde-aguilera-no-ira-a-la-carcel-por-corrupcion-le-quitaran-casa-y-debe-pagar-millonarias-multas.shtml) | BioBioChile | `secundaria` | 2025-07-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/07/04/exalcalde-aguilera-no-ira-a-la-carcel-por-corrupcion-le-quitaran-casa-y-debe-pagar-millonarias-multas.shtml) |
| [Condenan a cuatro años de libertad vigilada a exalcalde de San Ramón Miguel Ángel Aguilera por corrupción](https://www.meganoticias.cl/nacional/491103-sentencian-condenan-cuatro-anos-exalcalde-san-ramon-miguel-angel-aguilera-corrupcion-brk-4-7-2025.html) | Meganoticias | `secundaria` | 2025-07-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/491103-sentencian-condenan-cuatro-anos-exalcalde-san-ramon-miguel-angel-aguilera-corrupcion-brk-4-7-2025.html) |
