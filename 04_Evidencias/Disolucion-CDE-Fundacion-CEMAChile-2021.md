---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CDE-CEMA-2019-001"
tipo_documento: "Transacción Judicial, Disolución Corporativa y Restitución de 108 Inmuebles Fiscales al Estado (Rol 34.125-2016)"
fecha_emision: 2021-09-01
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile / Consejo de Defensa del Estado (cde.cl) / Ministerio de Bienes Nacionales"
causa_vinculada: "[[Caso CEMA Chile]]"
nexo_respaldado: "[[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html"
    titulo: "Falleció Lucía Hiriart (menciona recuperación de bienes vía CDE)"
    medio: "Emol"
    tipo: secundaria
    fecha: 2021-12-16
    consultado: 2026-10-19
  - url: "https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/"
    titulo: "Caso CEMA Chile: querella por fraude al fisco"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2016-08-23
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-cema-chile
  - bienes-fiscales
---

# Disolucion-CDE-Fundacion-CEMAChile-2021

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor` (Corte de Apelaciones de Santiago / Consejo de Defensa del Estado)
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Proceso de disolución de la [[Fundacion CEMA Chile]] iniciado por el Consejo de Defensa del Estado en septiembre de 2021, tras el traspaso de sus bienes al Fisco y a fundaciones de beneficencia; según Emol, el Estado recuperó más de $18.000 millones. Antes, en 2016, el ministro en visita Guillermo de la Barra decretó el embargo preventivo de propiedades de la fundación tras una querella contra [[Lucia Hiriart Rodriguez]], quien negó haberse beneficiado. La arista penal no terminó en condena.

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
