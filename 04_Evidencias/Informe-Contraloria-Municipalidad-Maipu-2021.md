---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CGR-MAI-2021-001"
tipo_documento: "Informe Final de Auditoría Contraloría General de la República"
fecha_emision: 2021-10-22
organismo_emisor: "[[Municipalidad de Maipu]]"
fuente_osint: "Buscador de Informes de Auditoría CGR (contraloria.cl) / Querella CDE"
causa_vinculada: "[[Caso Municipalidad de Maipu]]"
nexo_respaldado: "[[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/"
    titulo: "Expediente Cathy Barriga: las pruebas clave"
    medio: "La Tercera"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - evidencia/informe-contraloria
  - caso-maipu
---

# Informe-Contraloria-Municipalidad-Maipu-2021

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Registrado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Informe de auditoría financiera y presupuestaria practicado a la [[Municipalidad de Maipu]] que constató el déficit multimillonario generado durante la gestión de [[Cathy Barriga Guerra]] ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]) y remitió los antecedentes al Ministerio Público y al Consejo de Defensa del Estado para la persecución penal por [[Fraude al Fisco]] en el [[Caso Municipalidad de Maipu]].

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
