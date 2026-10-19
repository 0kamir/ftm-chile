---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-FNE-FASA-CONC-2009"
tipo_documento: "Bases de Conciliación y Reconocimiento de Hechos entre FNE y Farmacias Ahumada S.A. ante el TDLC"
fecha_emision: 2009-03-13
organismo_emisor: "[[Fiscalia Nacional Economica]]"
fuente_osint: "Tribunal de Defensa de la Libre Competencia / Fiscalía Nacional Económica (fne.gob.cl)"
causa_vinculada: "[[Caso Colusion de las Farmacias]]"
nexo_respaldado: "[[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
    titulo: "Suprema confirma acuerdo entre FNE y FASA por caso colusión"
    medio: "Diario Financiero"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - evidencia/acuerdo
  - fne
  - fasa
  - confesion-colusion
---

# Acuerdo-Conciliatorio-FNE-FASA-2009

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Suscripción**: `= this.fecha_emision`
- **Órgano Investigador**: `= this.organismo_emisor`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Acuerdo judicial aprobado por el TDLC en marzo de 2009 mediante el cual [[Farmacias Ahumada SA]] (controlada en ese momento por [[Jose Codner Chijner]]) reconoció explícitamente haber participado en un mecanismo de coordinación de precios con [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]] entre diciembre de 2007 y marzo de 2008, obligándose a pagar a beneficio fiscal la suma de **$1.000.000 USD** e implementando un manual interno de libre competencia. La confesión desarticuló la estrategia procesal de las cadenas competidoras y aportó correos y planillas de precios claves para la condena final del cartel.

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
