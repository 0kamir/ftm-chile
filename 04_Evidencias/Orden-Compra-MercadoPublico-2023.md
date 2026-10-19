---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-MP-OC-2023-001"
tipo_documento: "Ficha de Orden de Compra y Resolución de Trato Directo (Portal Mercado Público)"
fecha_emision: 2023-08-14
organismo_emisor: "[[Direccion ChileCompra]]"
fuente_osint: "API Datos Abiertos ChileCompra (datos-abiertos.chilecompra.cl)"
causa_vinculada: "[[Caso Compras Publicas]]"
nexo_respaldado: "[[TRX-2023-08-14-Trato-Directo-ChileCompra-01]]"
estado_verificacion: sin_fuente
fuentes: []
alertas_verificacion:
  - "CRÍTICO: sin número de orden de compra ni fuente verificable (ver Caso Compras Publicas)."
tags:
  - evidencia/mercado-publico
  - compras-publicas
---

# Orden-Compra-MercadoPublico-2023

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Plataforma Emisora**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Registro electrónico extraído del portal de Datos Abiertos de [[Direccion ChileCompra]] que documenta el trato directo [[TRX-2023-08-14-Trato-Directo-ChileCompra-01]] por **$45.800.000 CLP** adjudicado a [[Consultora Gestion Publica SpA]] ([[Jorge Valdivia Correa]]), incorporado al expediente OSINT [[Caso Compras Publicas]].

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
