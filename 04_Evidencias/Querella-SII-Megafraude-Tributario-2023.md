---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-SII-QUERELLA-2023-TRIBUTOS"
tipo_documento: "Querella Criminal por Delitos Tributarios Reiterados y Asociación Ilícita"
fecha_emision: 2023-12-14
organismo_emisor: "[[Servicio Impuestos Internos]]"
fuente_osint: "Servicio de Impuestos Internos (sii.cl) / Poder Judicial (pjud.cl)"
causa_vinculada: "[[Caso Megafraude Tributario Operacion Tributos]]"
nexo_respaldado: "[[TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml"
    titulo: "SII confirma que 55 empresarios detenidos concretaron el mayor fraude"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2023-12-15
    consultado: 2026-10-19
tags:
  - evidencia/querella
  - sii
  - megafraude-tributario
  - operacion-tributos
---

# Querella-SII-Megafraude-Tributario-2023

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión / Presentación**: `= this.fecha_emision`
- **Organismo Emisor**: `= this.organismo_emisor`
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Querella criminal interpuesta por el [[Servicio Impuestos Internos]] ante el 1° Juzgado de Garantía de Santiago en contra de [[Jose Antonio Pavez Campillay]], [[Ximena Jimenez Faras]], [[Andres Esteban Galaz Soto]], [[Olga Paz Barraza Quezada]], [[Juan Alberto Croxatto Romero]] y más de medio centenar de empresarios y contadores. La acción denuncia la comisión sistemática y reiterada de los delitos tipificados en el artículo 97 N° 4 incisos 1 y 2 del Código Tributario, consistente en la facilitación de más de 100.000 facturas falsas y la obtención fraudulenta de devoluciones tributarias con un perjuicio fiscal directo consolidado superior a los $240.000 millones de pesos.

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
