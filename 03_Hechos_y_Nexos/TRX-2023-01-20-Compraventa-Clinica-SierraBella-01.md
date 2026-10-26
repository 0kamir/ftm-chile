---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2023-01-20-Compraventa-Clinica-SierraBella-01"
fecha: 2023-01-20
tipo_nexo: trato_directo
monto_clp: 0
monto_origen: sin_monto
metodo_adjudicacion: trato_directo
entidad_origen: "[[Municipalidad de Santiago]]"
entidad_destino: "[[Inmobiliaria San Valentino SpA]]"
firmante_origen: "[[Iraci Hassler Jacob]]"
firmante_destino: "[[Felipe Sanchez Perez]]"
delito_imputado: "[[Fraude al Fisco]]"
causa_vinculada: "[[Caso Sierra Bella]]"
evidencia_soporte: "[[Dictamen-CGR-SierraBella-2023]]"
historial_correcciones:
  - "La compraventa no se concretó: $8.200 millones fue el precio acordado y no un pago; monto ajustado a 0 (2026-10-19)."
estado_verificacion: parcial
fuentes:
  - "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
  - "https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml"
  - "https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/"
  - "https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html"
  - "https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/"
  - "https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/"
  - "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml"
tags:
  - nexo/trato-directo
  - sobreprecio-inmobiliario
  - caso-sierra-bella
---

# TRX-2023-01-20-Compraventa-Clinica-SierraBella-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Pactado (CLP)**: `$8.200.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad Compradora (Origen)**: `= this.entidad_origen`
- **Sociedad Vendedora (Destino)**: `= this.entidad_destino`
- **Alcaldesa Firmante**: `= this.firmante_origen`
- **Representante Vendedor**: `= this.firmante_destino`
- **Delito Investigado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Suscripción de escritura pública de compraventa por trato directo entre la [[Municipalidad de Santiago]] —representada por [[Iraci Hassler Jacob]]— e [[Inmobiliaria San Valentino SpA]] —constituida el 5 de abril de 2022 y representada por [[Felipe Sanchez Perez]]— por un monto de `$8.200.000.000 CLP` para adquirir la ex Clínica Sierra Bella. La operación activa la alerta de **Constitución Reciente (`< 365 días`, `290 días`)** y fue objetada por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) en el [[Dictamen-CGR-SierraBella-2023]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella](https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) | 24 Horas | `secundaria` | 2025-05-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) |
| [Contraloría objeta compra de clínica Sierra Bella](https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) | BioBioChile | `secundaria` | 2023-04-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) |
| [Compra de clínica Sierra Bella: Fiscalía pide documentos](https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) | CIPER Chile | `secundaria` | 2023-03-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) |
| [Cronología de la compra de Sierra Bella](https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) | Emol | `secundaria` | 2023-04-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) |
| [Sierra Bella: ningún querellante pidió reapertura y se cierra el telón del caso para Irací Hassler](https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) |
| [Tribunal admite querella de Santiago contra Irací Hassler por fraude al fisco](https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/) | El Mostrador | `secundaria` | 2026-06-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/) |
| [Desbordes tras querella contra Hassler por caso Sierra Bella: 'El informe de Contraloría es muy duro'](https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml) | BioBioChile | `secundaria` | 2026-06-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml) |
