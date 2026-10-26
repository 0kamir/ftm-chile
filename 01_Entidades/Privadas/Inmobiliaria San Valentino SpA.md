---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Inmobiliaria e Inversiones San Valentino SpA"
fecha_constitucion: "2022-04-05"
objeto_social: "Inversiones inmobiliarias, compra, venta y arrendamiento de bienes raíces y establecimientos de salud"
representante_legal: "[[Felipe Sanchez Perez]]"
estado_verificacion: verificado
fuentes:
  - "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
  - "https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml"
  - "https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/"
  - "https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html"
  - "https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/"
  - "https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/"
tags:
  - entidad/privada
  - sociedad-inmobiliaria
  - caso-sierra-bella
---

# Inmobiliaria San Valentino SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal y Controlador**: `= this.representante_legal`

## Contexto y Societario
Sociedad por acciones constituida en abril de 2022 y representada por [[Felipe Sanchez Perez]]. Apenas meses después de adquirir el inmueble de calle Sierra Bella N° 1181 por cerca de `$2.080.000.000 CLP`, pactó en enero de 2023 su venta por trato directo a la [[Municipalidad de Santiago]] ([[Iraci Hassler Jacob]]) en **$8.200.000.000 CLP** (casi cuatro veces su valor de adquisición previa), lo que activó la bandera roja de **Constitución Societaria Reciente (`< 365 días`)** y el bloqueo administrativo de la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) en el [[Caso Sierra Bella]] ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]], [[Dictamen-CGR-SierraBella-2023]]).

## Historial de Contratos y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella](https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) | 24 Horas | `secundaria` | 2025-05-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) |
| [Contraloría objeta compra de clínica Sierra Bella](https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) | BioBioChile | `secundaria` | 2023-04-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) |
| [Compra de clínica Sierra Bella: Fiscalía pide documentos](https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) | CIPER Chile | `secundaria` | 2023-03-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) |
| [Cronología de la compra de Sierra Bella](https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) | Emol | `secundaria` | 2023-04-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) |
| [Sierra Bella: ningún querellante pidió reapertura y se cierra el telón del caso para Irací Hassler](https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) |
| [Tribunal admite querella de Santiago contra Irací Hassler por fraude al fisco](https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/) | El Mostrador | `secundaria` | 2026-06-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/) |
