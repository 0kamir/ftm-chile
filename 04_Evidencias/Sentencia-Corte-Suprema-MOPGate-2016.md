---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-MOP-2016-001"
tipo_documento: "Sentencia Definitiva de Casación Corte Suprema y Fallo Ministra en Visita Gloria Ana Chevesich"
fecha_emision: 2016-07-15
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Consejo de Defensa del Estado (CDE)"
causa_vinculada: "[[Caso MOP-Gate]]"
nexo_respaldado: "[[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
    titulo: "Corte Suprema dicta sentencia definitiva en el caso MOP-Gate"
    medio: "Emol"
    tipo: secundaria
    fecha: 2016-06-29
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-mop-gate
---

# Sentencia-Corte-Suprema-MOPGate-2016

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (y [[TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01]])

## Extracto y Relevancia Probatoria
Fallo definitivo de la Segunda Sala Penal de la [[Corte Suprema de Chile]] que confirmó las condenas dictadas por la Ministra en Visita Extraordinaria Gloria Ana Chevesich Ruiz en el [[Caso MOP-Gate]], dando por acreditado el perjuicio fiscal superior a `$1.253.000.000 CLP` ocasionado al [[Ministerio de Obras Publicas]] mediante la triangulación de contratos con [[Gestion Ambiental y Territorial SA]] (GATE, [[Hector Pena Veliz]]) bajo la dirección del ex Ministro [[Carlos Cruz Lorenzen]] ([[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]) y el uso de documentación tributaria falsa ante el [[Servicio Impuestos Internos]] ([[TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01]]).

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
