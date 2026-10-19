---
tipo_nodo: anexo_documental
estado_verificacion: verificado
fuentes:
  - url: "https://www.justice.gov/epstein"
    titulo: "Epstein Library (archivos publicados por el DOJ)"
    medio: "U.S. Department of Justice"
    tipo: primaria
    fecha: 2026-01-30
    consultado: 2026-10-19
  - url: "https://cnnespanol.cnn.com/2025/12/23/eeuu/conclusiones-lote-archivos-epstein-trax"
    titulo: "Conclusiones del lote de archivos Epstein"
    medio: "CNN en Español"
    tipo: secundaria
    fecha: 2025-12-23
    consultado: 2026-10-19
  - url: "https://www.cnnchile.com/pais/cientifico-chileno-correos-jeffrey-epstein-eduardo-guendelman/"
    titulo: "Científico chileno en correos de Jeffrey Epstein (Eduardo Guendelman)"
    medio: "CNN Chile"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.elciudadano.com/?p=1143444"
    titulo: "Epstein Case Shakes Chile: Andrónico Luksic and Andrés Velasco Named as «Persons of Interest»"
    medio: "El Ciudadano (resumen de reportaje de BioBioChile)"
    tipo: secundaria
    consultado: 2026-10-19
historial_correcciones:
  - "2026-10-19: la causa 'Caso Archivos Epstein Menciones Chile', sus 3 TRX y la evidencia del DOJ se retiraron del grafo y se consolidaron en este anexo. Ninguna persona chilena mencionada está imputada ni investigada; incluirlas como nodos de una red de corrupción sugería culpa por asociación."
tags:
  - anexo/menciones-documentales
  - fuera-del-grafo
---

# Menciones de Chilenos en Archivos Epstein

> **Anexo documental fuera del grafo.** Esta nota no forma parte de la red de causas ni de los análisis del vault (comunidades, vínculos, flujos), y no enlaza a fichas de personas. Registra menciones que la prensa chilena reportó en documentos publicados en Estados Unidos. **Aparecer en estos archivos no constituye delito ni indicio de delito.** Ninguna de las personas nombradas aquí ha sido imputada ni investigada en Chile por estos hechos.

## Origen de los documentos
Tras la aprobación de la *Epstein Files Transparency Act* (noviembre de 2025), el Departamento de Justicia de EE.UU. publicó entre diciembre de 2025 y enero de 2026 millones de documentos relacionados con Jeffrey Epstein. Medios chilenos revisaron el material en busca de referencias a personas del país.

## Menciones reportadas
| Persona | Qué muestran los documentos, según la prensa | Contacto directo con Epstein |
| :--- | :--- | :--- |
| Andrés Velasco Brañes, exministro de Hacienda | Mención en relación con su precandidatura presidencial de 2013, en una comunicación entre terceros. | No acreditado |
| Andrónico Luksic Craig, empresario | Un correo del empresario emiratí Ahmed bin Sulayem consultaba a Epstein por él, a propósito de una posible reunión en Dubái. | No acreditado |
| Eduardo Guendelman, físico | Intercambió unos diez correos con Epstein entre 2015 y 2019 buscando financiamiento para un centro de física teórica en las Bahamas; según el reporte, desconocía las acusaciones previas contra Epstein. Los fondos no se concretaron. | Sí, epistolar y académico |

Radio BioBío describió a Luksic y Velasco como "personas de interés" en su revisión periodística, aclarando que no hay evidencia de contacto directo de Epstein con ellos.

## Criterio de inclusión
Este anexo existe para documentar qué se publicó y aclarar su alcance, no para vincular a nadie con delitos. Si en el futuro surge una investigación o imputación en Chile relacionada con estos documentos, se incorporará al grafo por el [[Flujo_Incorporacion_Informacion]] con su fuente.

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
