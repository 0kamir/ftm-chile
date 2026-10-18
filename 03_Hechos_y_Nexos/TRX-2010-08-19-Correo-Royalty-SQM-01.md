---
tipo_nodo: nexo_transaccion
fecha: 2010-08-19
tipo_nexo: cohecho
monto_clp: 730000000
entidad_origen: "[[SQM SA]]"
entidad_destino: "[[Union Democrata Independiente]]"
firmante_origen: "[[Patricio Contesse Gonzalez]]"
firmante_destino: "[[Pablo Longueira Montes]]"
causa_vinculada: "[[Caso SQM]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Querella-SII-Boletas-SQM-2015]]"
tags:
  - nexo/transaccion
  - cohecho
  - caso-sqm
  - captura-regulatoria
---

# TRX-2010-08-19-Correo-Royalty-SQM-01

## Ficha de Arista Reificada (Captura Regulatoria y Pagos vía Boletas Ideológicamente Falsas)
- **Fecha del Hecho Clave**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado Consolidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad / Entorno Político de Destino**: `= this.entidad_destino`
- **Ejecutivo Origen**: `= this.firmante_origen`
- **Autoridad Receptora**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Envío de minuta jurídica redactada por la gerencia general de [[SQM SA]] ([[Patricio Contesse Gonzalez]]) al entonces senador [[Pablo Longueira Montes]] ([[Union Democrata Independiente]]) el 19 de agosto de 2010 para modificar el régimen de invariabilidad tributaria del Royalty Minero, acompañado de flujos financieros por aproximadamente **$730.000.000 CLP** canalizados entre 2009 y 2015 mediante emisores de boletas ideológicamente falsas y fundaciones vinculadas, denunciados en [[Querella-SII-Boletas-SQM-2015]] y juzgados en el [[Caso SQM]].
