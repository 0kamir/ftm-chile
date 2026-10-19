---
tipo_nodo: causa_judicial
ruc: "2101094520-3"
año_inicio: 2021
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Oriente / 9° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Lorena Parra / Constanza Encina"
estado_judicial: formalizada
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/"
    titulo: "Formalización de Cathy Barriga: qué delitos le imputan"
    medio: "CNN Chile"
    tipo: secundaria
    fecha: 2024-01-16
    consultado: 2026-10-19
  - url: "https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/"
    titulo: "Exalcaldesa Cathy Barriga será formalizada en enero de 2024"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2023-11-28
    consultado: 2026-10-19
  - url: "https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html"
    titulo: "Caso Maipú: Fiscalía Oriente reformalizará a Cathy Barriga"
    medio: "Meganoticias"
    tipo: secundaria
    fecha: 2024-08-19
    consultado: 2026-10-19
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
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
