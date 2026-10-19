---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-GORE-BIO-2022-001"
tipo_documento: "Resolución Exenta GORE Biobío / Convenio de Transferencia"
fecha_emision: 2022-12-20
organismo_emisor: "[[GORE Biobio]]"
fuente_osint: "Transparencia Activa GORE Biobío / Informe Contraloría Regional del Biobío"
causa_vinculada: "[[Caso Convenios]]"
nexo_respaldado: "[[TRX-2022-12-20-Convenio-EnTi-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/"
    titulo: "Formalización de Camila Polizzi en Caso Convenios"
    medio: "CNN Chile"
    tipo: secundaria
    fecha: 2023-11-29
    consultado: 2026-10-19
  - url: "https://www.radioagricultura.cl/nacional/2023/08/07/caso-convenios-pdi-allana-gobierno-regional-del-biobio/"
    titulo: "Caso Convenios: PDI allana Gobierno Regional del Biobío"
    medio: "Radio Agricultura"
    tipo: secundaria
    fecha: 2023-08-07
    consultado: 2026-10-19
tags:
  - evidencia/resolucion-exenta
  - caso-convenios
  - biobio
---

# Resolucion-GORE-Biobio-EnTi-2022

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Emisor**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Acto administrativo del [[GORE Biobio]] (administración de [[Rodrigo Diaz Worner]]) que aprueba la transferencia en una sola cuota de **$250.635.000 CLP** a favor de [[Fundacion En Ti]], gestionada por [[Camila Polizzi Fonceca]], dando origen al nexo [[TRX-2022-12-20-Convenio-EnTi-01]] dentro del [[Caso Convenios]] e imputaciones por [[Fraude al Fisco]] y [[Lavado de Activos]].

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
