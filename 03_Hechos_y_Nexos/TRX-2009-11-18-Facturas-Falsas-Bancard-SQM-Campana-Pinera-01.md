---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01"
fecha: 2009-11-18
tipo_nexo: factura_falsa
monto_clp: 340000000
metodo_adjudicacion: no_aplica
entidad_origen: "[[SQM SA]]"
entidad_destino: "[[Bancard Inversiones Ltda]]"
firmante_origen: "[[Patricio Contesse Gonzalez]]"
firmante_destino: "[[Santiago Valdes Gutierrez]]"
delito_imputado: "[[Delito Tributario]]"
causa_vinculada: "[[Caso SQM]]"
evidencia_soporte: "[[Querella-SII-Boletas-SQM-2015]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/"
    titulo: "Fiscalía reconstruye los pasos de Manuel Guerra: así se selló la salida del administrador electoral de Piñera del caso Penta"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2024-11-10
    consultado: 2026-10-19
  - url: "https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/"
    titulo: "Facturas de SQM aterrizan en campaña de Piñera: pagos de 2009 suman $103 millones"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2017-09-26
    consultado: 2026-10-19
alertas_verificacion:
  - "Hecho no adjudicado: investigación cerrada por prescripción (2019)."
tags:
  - nexo/factura-falsa
  - caso-sqm
  - financiamiento-politico
  - bancard
---

# TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$340.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen (Pagadora)**: `= this.entidad_origen`
- **Entidad de Destino (Emisora)**: `= this.entidad_destino` (y empresas proveedoras de campaña como *Vox Populi* / *Administradora Bancorp*)
- **Ejecutivo Autorizador en Origen**: `= this.firmante_origen`
- **Ejecutivo / Administrador Electoral en Destino**: `= this.firmante_destino` (en beneficio de la campaña presidencial de [[Sebastian Pinera Echenique]] y [[Renovacion Nacional]])
- **Delito Imputado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Pago de [[SQM SA]] a Bancorp, sociedad del grupo [[Bancard Inversiones Ltda]], por **$340.000.000 CLP** mediante 16 facturas (2009-2010) que la Fiscalía presumió ideológicamente falsas por no existir servicios que las justificaran. En 2015 SQM rectificó esos pagos ante el [[Servicio Impuestos Internos]]. [[Santiago Valdes Gutierrez]] sostuvo que la asesoría sí se prestó. En 2019 la Corte de Apelaciones sobreseyó a [[Santiago Valdes Gutierrez]] por prescripción (habían transcurrido más de cinco años desde los hechos al abrirse la investigación); no existe sentencia que declare falsas las facturas. Rige la presunción de inocencia.

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
