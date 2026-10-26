---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal de Vitacura (Autónoma)"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/?p=152080"
  - "https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/"
  - "https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html"
tags:
  - entidad/publica
  - municipio
  - vitacura
---

# Municipalidad de Vitacura

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Corporación edilicia encabezada entre 1996 y 2021 por el alcalde [[Raul Torrealba del Pedregal]]. En el [[Caso Vitacura]], el Ministerio Público y el Consejo de Defensa del Estado acreditaron el uso de corporaciones privadas sin fines de lucro ("Programas Vita", como [[Vita Deportes]]) para eludir los controles de la Contraloría sobre el presupuesto municipal y sustraer fondos públicos ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]).

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Subvención",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Autoridad Municipal",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Audiencia de formalización de Raúl Torrealba](https://www.ex-ante.cl/?p=152080) | Ex-Ante | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/?p=152080) |
| [Fiscalía formalizará a exalcalde Raúl Torrealba por fraude al fisco y asociación ilícita](https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) | La Tercera | `secundaria` | 2023-05-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) |
| [Formalizan a exalcalde Raúl Torrealba](https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) | Pauta | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) |
