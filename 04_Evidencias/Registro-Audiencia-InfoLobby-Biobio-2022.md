---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-LOBBY-BIO-2022-001"
tipo_documento: "Acta de Audiencia Ley N° 20.730 (Portal InfoLobby)"
fecha_emision: 2022-09-12
organismo_emisor: "[[GORE Biobio]]"
fuente_osint: "Plataforma Ley del Lobby (leylobby.gob.cl) / InfoLobby CGR"
causa_vinculada: "[[Caso Convenios]]"
nexo_respaldado: "[[TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.latercera.com/nacional/noticia/fiscalia-avanza-en-arista-por-convenios-de-procultura-en-el-biobio-y-formalizara-a-alberto-larrain-y-constanza-gomez/"
    titulo: "Fiscalía avanza en arista por convenios de ProCultura en el Biobío"
    medio: "La Tercera"
    tipo: secundaria
    consultado: 2026-10-19
alertas_verificacion:
  - "Falta el enlace directo al registro de audiencia en leylobby.gob.cl."
tags:
  - evidencia/infolobby
  - caso-convenios
---

# Registro-Audiencia-InfoLobby-Biobio-2022

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Sujeto Pasivo**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Registro público de audiencia celebrada entre [[Alberto Larrain Salas]] (en representación de [[Fundacion ProCultura]]) y [[Rodrigo Diaz Worner]] (Gobernador del [[GORE Biobio]]) para presentar lineamientos de proyectos culturales y de innovación regional, antecedente directo del convenio [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] por **$2.553.000.000 CLP** investigado en el [[Caso Convenios]].

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
