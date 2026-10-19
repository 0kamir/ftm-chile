---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-2923-2018"
tipo_documento: "Sentencia Definitiva de la Tercera Sala de la Corte Suprema en Recurso de Reclamación (Rol 2.923-2018)"
fecha_emision: 2020-01-06
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Fiscalía Nacional Económica"
causa_vinculada: "[[Caso Colusion del Papel Tissue]]"
nexo_respaldado: "[[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
    titulo: "Suprema condena a CMPC y SCA por colusión"
    medio: "Emol"
    tipo: secundaria
    fecha: 2020-01-06
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - corte-suprema
  - colusion-tissue
  - multa-coaccion
---

# Sentencia-Corte-Suprema-Colusion-PapelTissue-2020

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Sentencia Definitiva**: `= this.fecha_emision`
- **Tribunal Resolutivo**: Tercera Sala de la [[Corte Suprema de Chile]]
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Fallo definitivo e inapelable de la Corte Suprema que revocó el beneficio de exención de multa que la FNE y el TDLC habían concedido a [[Empresas CMPC SA]] bajo la delación compensada. La Tercera Sala acreditó que CMPC no solo ideó el cartel, sino que **ejerció coacción económica sobre [[SCA Chile SA]]** para forzarla a permanecer en el acuerdo colusorio bajo amenaza de expulsarla del mercado minorista, imponiéndole a CMPC una multa a beneficio fiscal de **20.000 UTA** (aproximadamente US$ 15 millones) y confirmando igual sanción económica contra SCA Chile.

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
