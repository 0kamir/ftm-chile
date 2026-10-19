---
tipo_nodo: nexo_transaccion
fecha: 2019-05-14
tipo_nexo: cohecho
monto_clp: 37000000
entidad_origen: "[[Itelecom Holding Chile SpA]]"
entidad_destino: "[[Municipalidad de Chillan]]"
firmante_origen: "[[Leon Marcelo Lefort Hernandez]]"
firmante_destino: "[[Marcelo Campos Henriquez]]"
causa_vinculada: "[[Caso Luminarias LED]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: ""
estado_verificacion: parcial
fuentes:
  - url: "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
    titulo: "Caso Luminarias: claves de la investigación por sobornos en municipios"
    medio: "Ex-Ante"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
    titulo: "Caso Luminarias LED: confirman prisión preventiva de dueño de Itelecom"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2021-06-30
    consultado: 2026-10-19
historial_correcciones:
  - "Monto ajustado a $37 millones (pago en efectivo reportado por la prensa) el 2026-10-19; el valor del contrato no consta en fuentes."
tags:
  - nexo/transaccion
  - cohecho
  - caso-luminarias-led
---

# TRX-2019-05-14-Soborno-Luminarias-Chillan-01

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

## Descripción Forense de la Operación
Presunta adjudicación irregular de la licitación pública de recambio de luminarias a tecnología LED en la [[Municipalidad de Chillan]] a favor de [[Itelecom Holding Chile SpA]] ([[Leon Marcelo Lefort Hernandez]]), que, según la Fiscalía, se habría obtenido mediante el pago de sobornos a [[Marcelo Campos Henriquez]] (integrante de la comisión evaluadora y administrador municipal), según la hipótesis de la Fiscalía en el [[Caso Luminarias LED]] (sin sentencia conocida al 2026-10-19).

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
