---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TOP6-SANRAMON-2025"
tipo_documento: "Sentencia Condenatoria Definitiva (6° Tribunal de Juicio Oral en lo Penal de Santiago)"
fecha_emision: 2025-07-04
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial / 6° TOP de Santiago / Consejo de Defensa del Estado"
causa_vinculada: "[[Caso Municipalidad de San Ramon]]"
nexo_respaldado: "[[TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01]]"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/"
  - "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/07/04/exalcalde-aguilera-no-ira-a-la-carcel-por-corrupcion-le-quitaran-casa-y-debe-pagar-millonarias-multas.shtml"
tags:
  - evidencia/sentencia
  - san-ramon
---

# Sentencia Condenatoria 6° TOP de Santiago — Caso Municipalidad de San Ramón (2025)

## Síntesis Documental
Sentencia condenatoria dictada por el 6° Tribunal de Juicio Oral en lo Penal de Santiago y confirmada en agosto de 2025 en el [[Caso Municipalidad de San Ramon]]. El fallo estableció que entre enero de 2013 y septiembre de 2017, mientras ejercía como alcalde de la [[Municipalidad de San Ramon]], [[Miguel Angel Aguilera Sanhueza]] registró un incremento patrimonial injustificado de **$246.918.500 CLP** mediante depósitos en efectivo por caja y transferencias de terceros sin respaldo lícito, ocultando el origen de los fondos en la compra de una propiedad habitacional en la comuna de La Reina (decretada en comiso).

## Hechos y Transacciones Soportadas por esta Evidencia
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción / Hecho",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE evidencia_soporte = this.file.link
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Libertad vigilada, millonaria multa y adiós a casa en La Reina: la condena al exalcalde de San Ramón](https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/) | El Mostrador | `secundaria` | 2025-07-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/) |
| [Exalcalde Aguilera no irá a la cárcel por corrupción: le quitarán casa y debe pagar millonarias multas](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/07/04/exalcalde-aguilera-no-ira-a-la-carcel-por-corrupcion-le-quitaran-casa-y-debe-pagar-millonarias-multas.shtml) | BioBioChile | `secundaria` | 2025-07-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2025/07/04/exalcalde-aguilera-no-ira-a-la-carcel-por-corrupcion-le-quitaran-casa-y-debe-pagar-millonarias-multas.shtml) |
