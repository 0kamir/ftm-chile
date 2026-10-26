---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2021
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Oriente / 9° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Lorena Parra / Constanza Encina"
estado_judicial: formalizada
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/"
  - "https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/"
  - "https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html"
tags:
  - causa
  - caso-maipu
  - corrupcion-municipal
---

# Caso Municipalidad de Maipu

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (junto a falsificación de instrumento público)

## Resumen Ejecutivo
Investigación penal contra la exalcaldesa de la [[Municipalidad de Maipu]], [[Cathy Barriga Guerra]] (vinculada políticamente a [[Union Democrata Independiente]]), por delitos reiterados de [[Fraude al Fisco]] y falsificación de instrumento público (certificados de disponibilidad presupuestaria y reportes anuales a la Contraloría). El perjuicio fiscal imputado por el Ministerio Público y el Consejo de Defensa del Estado asciende a **$30.972.000.000 CLP** ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]), respaldado por la auditoría [[Informe-Contraloria-Municipalidad-Maipu-2021]].

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Autoridad Imputada",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Formalización de Cathy Barriga: qué delitos le imputan](https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) | CNN Chile | `secundaria` | 2024-01-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) |
| [Exalcaldesa Cathy Barriga será formalizada en enero de 2024](https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) | El Mostrador | `secundaria` | 2023-11-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) |
| [Caso Maipú: Fiscalía Oriente reformalizará a Cathy Barriga](https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) | Meganoticias | `secundaria` | 2024-08-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) |
