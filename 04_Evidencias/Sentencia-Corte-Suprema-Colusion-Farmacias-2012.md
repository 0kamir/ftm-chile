---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-2012-FAR"
tipo_documento: "Sentencia de la Tercera Sala de la Corte Suprema en Recursos de Reclamación (Rol 2.012-2012)"
fecha_emision: 2012-09-07
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Fiscalía Nacional Económica"
causa_vinculada: "[[Caso Colusion de las Farmacias]]"
nexo_respaldado: "[[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
    titulo: "Fallo Corte Suprema Rol 2578-2012 (caso Farmacias)"
    medio: "CentroCompetencia (copia del fallo)"
    tipo: primaria
    fecha: 2012-09-07
    consultado: 2026-10-19
  - url: "https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/"
    titulo: "Suprema rechaza reclamo de farmacias sobre multas"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2012-09-07
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - corte-suprema
  - colusion-farmacias
  - multa-maxima
---

# Sentencia-Corte-Suprema-Colusion-Farmacias-2012

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Sentencia Definitiva**: `= this.fecha_emision`
- **Tribunal Resolutivo**: Tercera Sala de la [[Corte Suprema de Chile]]
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Fallo definitivo e inapelable de la Corte Suprema que rechazó en todas sus partes los recursos de reclamación interpuestos por [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]], confirmando la existencia del cartel y la aplicación de la multa de **20.000 UTA** a cada una. La Corte dio por plenamente demostrado que ambas cadenas utilizaron a los laboratorios proveedores farmacéuticos para verificar el cumplimiento del acuerdo ilícito sobre los 222 medicamentos críticos.

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
