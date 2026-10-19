---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-SERNAC-PVC-2017"
tipo_documento: "Acuerdo de Procedimiento Voluntario Colectivo de Compensación entre SERNAC, Asociaciones de Consumidores (Conadecus / Odecu) y CMPC"
fecha_emision: 2017-03-03
organismo_emisor: "[[Servicio Nacional del Consumidor]]"
fuente_osint: "Servicio Nacional del Consumidor (sernac.cl) / BancoEstado / Conadecus"
causa_vinculada: "[[Caso Colusion del Papel Tissue]]"
nexo_respaldado: "[[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html"
    titulo: "Acuerdo por colusión tissue: CMPC pagará US$150 millones para compensar a consumidores"
    medio: "Emol"
    tipo: secundaria
    fecha: 2017-01-27
    consultado: 2026-10-19
  - url: "https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html"
    titulo: "CMPC pagará compensación de 150 millones de dólares: por consumidor serán 7.000 pesos"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2017-01-27
    consultado: 2026-10-19
tags:
  - evidencia/acuerdo
  - sernac
  - compensacion-historica
  - siete-lucas-confort
---

# Acuerdo-Compensatorio-SERNAC-CMPC-Tissue-2017

## Metadatos de Fuente Primaria (Cadena de Custodia Administrativa)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Suscripción**: `= this.fecha_emision`
- **Órgano Público Garante**: `= this.organismo_emisor`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Acuerdo de mediación colectiva inédito en la historia económica de Chile mediante el cual [[Empresas CMPC SA]] reconoció el perjuicio patrimonial causado a la población por la colusión del papel tissue y transfirió a un fondo fiduciario en BancoEstado la suma de **`$97.500.000.000 CLP`** (aproximadamente US$ 150 millones). Dicho fondo fue distribuido a razón de **$7.000 CLP** a cada persona mayor de 18 años con cédula de identidad chilena a contar del 1 de agosto de 2018.

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
