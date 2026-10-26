---
tipo_nodo: nexo_transaccion
fecha: 2019-05-14
tipo_nexo: cohecho
monto_clp: 37000000
monto_origen: acusacion
entidad_origen: "[[Itelecom Holding Chile SpA]]"
entidad_destino: "[[Municipalidad de Chillan]]"
firmante_origen: "[[Leon Marcelo Lefort Hernandez]]"
firmante_destino: "[[Marcelo Campos Henriquez]]"
causa_vinculada: "[[Caso Luminarias LED]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: ""
historial_correcciones:
  - "Monto ajustado a $37 millones (pago en efectivo reportado por la prensa) el 2026-10-19; el valor del contrato no consta en fuentes."
estado_verificacion: parcial
fuentes:
  - "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
  - "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
tags:
  - nexo/transaccion
  - cohecho
  - caso-luminarias-led
---

# TRX-2019-05-14-Licitacion-Luminarias-Chillan-01

## Ficha de Arista Reificada (Licitación Municipal Manipulada por Soborno)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto del Contrato Adjudicado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Empresa Oferente / Sobornante**: `= this.entidad_origen`
- **Municipio Licitante**: `= this.entidad_destino`
- **Controlador Privado**: `= this.firmante_origen`
- **Directivo Municipal Receptor**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Condenado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]])
- **Evidencia / Sentencia Firme**: `= this.evidencia_soporte`

## Descripción de la Operación
Presunta adjudicación irregular de la licitación pública de recambio de luminarias a tecnología LED en la [[Municipalidad de Chillan]] a favor de [[Itelecom Holding Chile SpA]] ([[Leon Marcelo Lefort Hernandez]]), que, según la Fiscalía, se habría obtenido mediante el pago de sobornos a [[Marcelo Campos Henriquez]] (integrante de la comisión evaluadora y administrador municipal), según la hipótesis de la Fiscalía en el [[Caso Luminarias LED]] (sin sentencia conocida al 2026-10-19).

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Luminarias: claves de la investigación por sobornos en municipios](https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) | Ex-Ante | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) |
| [Caso Luminarias LED: confirman prisión preventiva de dueño de Itelecom](https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) | El Dínamo | `secundaria` | 2021-06-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) |
