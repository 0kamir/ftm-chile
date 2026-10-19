---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-SII-SQM-2015-001"
tipo_documento: "Querella Criminal SII por Delitos Tributarios y Pericia de Correos Electrónicos"
fecha_emision: 2015-03-24
organismo_emisor: "[[Servicio Impuestos Internos]]"
fuente_osint: "Poder Judicial (pjud.cl) / Carpeta Investigativa Caso SQM"
causa_vinculada: "[[Caso SQM]]"
nexo_respaldado: "[[TRX-2010-08-19-Correo-Royalty-SQM-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
    titulo: "Juicio oral caso SQM tras 8 años de espera"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2023-02-13
    consultado: 2026-10-19
historial_correcciones:
  - "Los acusados del juicio oral fueron absueltos (oct-2025); el tribunal no dio por acreditada la falsedad ideológica de boletas y facturas."
tags:
  - evidencia/querella-sii
  - caso-sqm
---

# Querella-SII-Boletas-SQM-2015

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Querellante**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Querellas y denuncias interpuestas en marzo de 2015 por la Dirección Nacional del [[Servicio Impuestos Internos]] contra los representantes legales de [[SQM SA]] ([[Patricio Contesse Gonzalez]]) por [[Delito Tributario]] (Art. 97 N° 4 del Código Tributario), que habilitaron la incautación de la contabilidad de la minera y el hallazgo de los pagos y correos vinculados a [[Pablo Longueira Montes]] ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]) en el [[Caso SQM]].

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
