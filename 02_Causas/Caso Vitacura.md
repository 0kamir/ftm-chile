---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2021
tribunal_o_fiscalia: "Fiscalía Metropolitana Centro Norte / 4° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Francisco Jacir"
estado_judicial: formalizada
delito_principal: "[[Malversacion de Caudales Publicos]]"
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/"
  - "https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html"
tags:
  - causa
  - caso-vitacura
  - corrupcion-municipal
---

# Caso Vitacura

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (junto a [[Fraude al Fisco]], [[Lavado de Activos]] y delitos tributarios)

## Resumen Ejecutivo
Investigación penal contra el exalcalde de la [[Municipalidad de Vitacura]], [[Raul Torrealba del Pedregal]] (exmilitante de [[Renovacion Nacional]]), y directivos de las organizaciones comunitarias funcionales "Vita" (entre ellas [[Vita Deportes]], presidida por [[Domingo Prieto Urrejola]]). Según la acusación fiscal y la autodenuncia respaldada en [[Declaracion-Judicial-Prieto-Vitacura-2021]], se desviaron subvenciones municipales ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]) por más de **$759.000.000 CLP** mediante sobres con dinero en efectivo entregados mensualmente al edil y financiamiento de campañas.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Autorizador",
  firmante_destino AS "Receptor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Fiscalía formalizará a exalcalde Raúl Torrealba por fraude al fisco y asociación ilícita](https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) | La Tercera | `secundaria` | 2023-05-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) |
| [Formalizan a exalcalde Raúl Torrealba](https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) | Pauta | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) |
