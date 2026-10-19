---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-AUD-ORI-2023-001"
tipo_documento: "Registro de Audio Digital Periciado (Archivo WAV/MP3)"
fecha_emision: 2023-06-22
organismo_emisor: "[[Factop SpA]]"
fuente_osint: "Reportaje CIPER Chile (14-11-2023) / Carpeta Investigativa Fiscalía Metropolitana Oriente"
causa_vinculada: "[[Caso Audios]]"
nexo_respaldado: "[[TRX-2023-06-22-Reunion-Audios-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
    titulo: "Cinco claves para comprender el caso Audios"
    medio: "Emol"
    tipo: secundaria
    fecha: 2024-08-21
    consultado: 2026-10-19
  - url: "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
    titulo: "“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2023-11-14
    consultado: 2026-10-19
tags:
  - evidencia/audio
  - caso-audios
---

# Audio-Reunion-Edificio-Alonso-2023

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha del Registro**: `= this.fecha_emision`
- **Entidad Relacionada**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Grabación de aproximadamente 1 hora y 44 minutos efectuada el 22 de junio de 2023 en las oficinas del edificio Alonso de Córdova (Vitacura), donde [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] exponen ante el controlador de [[Factop SpA]] los montos y mecanismos de pago a funcionarios del [[Servicio Impuestos Internos]] ([[TRX-2023-06-22-Reunion-Audios-01]]), dando lugar a la formalización por [[Cohecho]] y [[Lavado de Activos]] en el [[Caso Audios]].

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
