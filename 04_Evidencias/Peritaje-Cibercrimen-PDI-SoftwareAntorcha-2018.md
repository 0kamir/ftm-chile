---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PDI-CIB-2018-ANT"
tipo_documento: "Informe Pericial Informático y Forense de la Brigada Investigadora del Cibercrimen de la PDI sobre Software Antorcha y Teléfonos Incautados"
fecha_emision: 2018-01-25
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Policía de Investigaciones de Chile (PDI) / Fiscalía Regional de La Araucanía / Peritaje Cibercrimen"
causa_vinculada: "[[Caso Operacion Huracan]]"
nexo_respaldado: "[[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml"
    titulo: "Huracán 2: formalización del creador de Antorcha y funcionario del Labocar"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2018-02-19
    consultado: 2026-10-19
tags:
  - evidencia/peritaje
  - cibercrimen-pdi
  - antorcha-farsa
  - operacion-huracan
---

# Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Órgano Pericial Técnico**: Brigada Investigadora del Cibercrimen de la PDI
- **Órgano Persecutor Solicitante**: Fiscalía Regional de La Araucanía / Fiscalía Nacional
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Informe técnico pericial clave que desarticuló la farsa de la [[Caso Operacion Huracan]]:
1. **Inexistencia Técnica de «Antorcha»**: La PDI acreditó que el supuesto código desarrollado por [[Alex Smith Leay]] carecía por completo de la capacidad de interceptar tráfico cifrado de aplicaciones como WhatsApp o Telegram en servidores remotos o en tránsito.
2. **Implantación Post-Incautación**: Se constató mediante análisis de metadatos del sistema de archivos (*MAC timestamps*) que los archivos de texto que contenían los supuestos diálogos entre comuneros fueron transferidos manualmente a los teléfonos incautados con posterioridad a la detención de los imputados, usando cables USB y computadores de la UIOE operados por [[Leonardo Osses Sandoval]] y [[Patricio Marin Lazo]].
3. **Fundamento del Sobreseimiento**: Este informe motivó la solicitud de sobreseimiento definitivo de todos los comuneros imputados y el inicio de la persecución penal contra el Alto Mando de Carabineros.

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
