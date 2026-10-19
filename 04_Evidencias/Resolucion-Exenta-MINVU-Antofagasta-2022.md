---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-MINVU-ANT-2022-001"
tipo_documento: "Resolución Exenta / Convenio de Transferencia de Recursos"
fecha_emision: 2022-10-03
organismo_emisor: "[[Seremi MINVU Antofagasta]]"
fuente_osint: "Portal de Transparencia Activa MINVU / Informe de Investigación Especial CGR N° 356-2023"
causa_vinculada: "[[Caso Convenios]]"
nexo_respaldado: "[[TRX-2022-10-03-Convenio-DV-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml"
    titulo: "Caso Democracia Viva: contratos evitaron revisión de Contraloría al ser pagados de forma parcializada"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2023-06-22
    consultado: 2026-10-19
  - url: "https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/"
    titulo: "Tras informe sobre Democracia Viva, contralor afirma que hubo corrupción"
    medio: "La Tercera"
    tipo: secundaria
    fecha: 2023-08-31
    consultado: 2026-10-19
tags:
  - evidencia/resolucion-exenta
  - caso-convenios
---

# Resolucion-Exenta-MINVU-Antofagasta-2022

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Emisor**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Conjunto de Resoluciones Exentas emitidas entre octubre y noviembre de 2022 por la [[Seremi MINVU Antofagasta]] mediante las cuales se aprueban los convenios de transferencia de recursos del Programa de Asentamientos Precarios hacia la [[Fundacion Democracia Viva]] por una suma total de **$426.000.000 CLP** (registrado en la arista [[TRX-2022-10-03-Convenio-DV-01]]).

### Firmantes Acreditados en el Instrumento Público
- **Por la Entidad Pública**: [[Carlos Contreras Gutierrez]] (SEREMI de Vivienda y Urbanismo Región de Antofagasta).
- **Por la Entidad Receptora**: [[Daniel Andrade Schwarze]] (Representante Legal de [[Fundacion Democracia Viva]]).

### Hallazgos de Contraloría General de la República
El Informe de Investigación Especial de la Contraloría Regional de Antofagasta constató:
1. Ausencia de fundamentos técnicos y de acto administrativo fundado que justificara la asignación por trato directo sin concurso público.
2. Contratación de personal con cargo a los fondos transferidos que prestaba funciones en la propia [[Seremi MINVU Antofagasta]].
3. Rendiciones de cuentas observadas y carentes de respaldo documental suficiente para acreditar la ejecución efectiva de las obras en campamentos.

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
