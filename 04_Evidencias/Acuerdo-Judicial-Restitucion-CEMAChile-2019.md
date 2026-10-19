---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CDE-CEMA-2019-001"
tipo_documento: "Transacción Judicial, Disolución Corporativa y Restitución de 108 Inmuebles Fiscales al Estado (Rol 34.125-2016)"
fecha_emision: 2019-07-15
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
alertas_verificacion:
  - "No se encontró un 'acuerdo judicial de restitución' de 2019; la prensa describe el traspaso de bienes y la disolución vía CDE en 2021."
tags:
  - evidencia/sentencia
  - caso-cema-chile
  - bienes-fiscales
---

# Acuerdo-Judicial-Restitucion-CEMAChile-2019

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
Conjunto de resoluciones de embargo del Ministro en Visita Guillermo de la Barra Dünner (Causa Rol N° `34.125-2016`) y acuerdo judicial definitivo suscrito con el Consejo de Defensa del Estado y aprobado por los tribunales superiores en el [[Caso CEMA Chile]], mediante el cual se puso término a la administración vitalicia que [[Lucia Hiriart Rodriguez]] ejerció sobre la [[Fundacion CEMA Chile]], acreditando la venta comercial de bienes públicos por más de `$8.900.000.000 CLP` y ejecutando la disolución de la fundación junto con el traspaso gratuito de **108 inmuebles fiscales y municipales** y de la totalidad de sus fondos líquidos remanentes al Fisco de Chile (**`$10.500.000.000 CLP`** en activos recuperados en [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]).

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
