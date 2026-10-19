---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01"
fecha: 2002-04-12
tipo_nexo: factura_falsa
monto_clp: 450000000
metodo_adjudicacion: no_aplica
entidad_origen: "[[Gestion Ambiental y Territorial SA]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Hector Pena Veliz]]"
firmante_destino: "[[Carlos Cruz Lorenzen]]"
delito_imputado: "[[Delito Tributario]]"
causa_vinculada: "[[Caso MOP-Gate]]"
evidencia_soporte: "[[Sentencia-Corte-Suprema-MOPGate-2016]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
    titulo: "Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas"
    medio: "Emol"
    tipo: secundaria
    fecha: 2016-06-29
    consultado: 2026-10-19
alertas_verificacion:
  - "Sin fuente específica para el monto de $450 millones ni para facturas ante el SII; la condena del caso es por fraude al fisco."
tags:
  - nexo/factura-falsa
  - caso-mop-gate
---

# TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$450.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad Fiscalizadora Defraudada**: `= this.entidad_destino`
- **Firmante Emisor**: `= this.firmante_origen`
- **Destinatario Articulador**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Fraude al Fisco]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Contabilización de facturas y boletas de honorarios ideológicamente falsas por `$450.000.000 CLP` en la contabilidad de [[Gestion Ambiental y Territorial SA]] (GATE), dirigida por [[Hector Pena Veliz]], con el propósito de justificar tributariamente ante el [[Servicio Impuestos Internos]] la salida de los dineros líquidos que retornaban al circuito del [[Ministerio de Obras Publicas]] y [[Carlos Cruz Lorenzen]].

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
