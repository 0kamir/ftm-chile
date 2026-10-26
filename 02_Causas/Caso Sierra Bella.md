---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía Metropolitana Centro Norte (fiscal Patricio Cooper, luego fiscal regional de Coquimbo) / Contraloría General de la República"
fiscal_a_cargo: "Patricio Cooper Monti"
estado_judicial: sobreseida_con_nueva_querella
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - "https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/"
  - "https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml"
  - "https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html"
  - "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
  - "https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/"
  - "https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/"
  - "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml"
tags:
  - causa
  - sobreprecio-inmobiliario
  - caso-sierra-bella
---

# Caso Sierra Bella

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal Investigador**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal`

## Síntesis de la Causa
Investigación penal y administrativa originada por el intento de adquisición mediante trato directo de la ex Clínica Sierra Bella por parte de la [[Municipalidad de Santiago]] —encabezada por la alcaldesa [[Iraci Hassler Jacob]] ([[Partido Comunista de Chile]])— a la sociedad [[Inmobiliaria San Valentino SpA]] (representada por [[Felipe Sanchez Perez]]) por un precio de **$8.200.000.000 CLP**, cuadruplicando el valor comercial y de adquisición previa del inmueble ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]). La operación fue objetada y frenada por la [[Contraloria General de la Republica]] bajo la dirección del Contralor [[Jorge Bermudez Soto]] mediante el [[Dictamen-CGR-SierraBella-2023]], tras objetar la Contraloría una diferencia de más de cuatro veces entre el precio pactado y el valor al que se habían adquirido los inmuebles.

## Transacciones y Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Desarrollo Judicial Posterior
En mayo de 2025 la Fiscalía decidió no perseverar y la causa quedó con sobreseimiento definitivo, confirmado por la Corte Suprema; Hassler nunca fue formalizada. En mayo de 2026 un sumario de la Contraloría dio por acreditada su responsabilidad administrativa en la compra. En junio de 2026 el 7° Juzgado de Garantía de Santiago declaró admisible una nueva querella de la Municipalidad de Santiago por fraude al fisco, que el Ministerio Público debe evaluar; Hassler sostiene que se trata de hechos ya juzgados y querelló por denuncia calumniosa contra el alcalde Mario Desbordes, acción que el tribunal también admitió. Rige la presunción de inocencia.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Compra de clínica Sierra Bella: Fiscalía pide documentos](https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) | CIPER Chile | `secundaria` | 2023-03-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) |
| [Contraloría objeta polémica compra de clínica Sierra Bella](https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) | BioBioChile | `secundaria` | 2023-04-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) |
| [Cronología de la compra de Sierra Bella](https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) | Emol | `secundaria` | 2023-04-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) |
| [Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella](https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) | 24 Horas | `secundaria` | 2025-05-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) |
| [Sierra Bella: ningún querellante pidió reapertura y se cierra el telón del caso para Irací Hassler](https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) |
| [Tribunal admite querella de Santiago contra Irací Hassler por fraude al fisco](https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/) | El Mostrador | `secundaria` | 2026-06-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/) |
| [Desbordes tras querella contra Hassler por caso Sierra Bella: 'El informe de Contraloría es muy duro'](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml) | BioBioChile | `secundaria` | 2026-06-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml) |
