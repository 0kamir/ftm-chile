---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TOP-PAC-VEREDICTO-2026"
tipo_documento: "Veredicto condenatorio del Tribunal de Juicio Oral en lo Penal de Santiago (juicio oral contra 28 acusados)"
fecha_emision: 2026-04-15
organismo_emisor: ""
fuente_osint: "Poder Judicial (pjud.cl) / Reportes de Operaciones Sospechosas UAF"
causa_vinculada: "[[Caso Pacogate]]"
nexo_respaldado: "[[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
    titulo: "Caso Pacogate: rechazan prisión preventiva para los 25 condenados"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-04-15
    consultado: 2026-10-19
  - url: "https://en.wikipedia.org/wiki/Pacogate"
    titulo: "Pacogate"
    medio: "Wikipedia"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - evidencia/sentencia-judicial
  - caso-pacogate
---

# Veredicto-TOP-Santiago-Pacogate-2026

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme. La prensa informa que el tribunal rechazó la prisión preventiva solicitada por la Fiscalía y mantuvo las cautelares vigentes. Los nombres individuales de los condenados no se verificaron en esta revisión.

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
