---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PJD-FORMALIZACION-1JG-13745-2023"
tipo_documento: "Acta de Audiencia de Formalización y Resolución de Medidas Cautelares RIT 13745-2023"
fecha_emision: 2023-12-22
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / 1° Juzgado de Garantía de Santiago"
causa_vinculada: "[[Caso Megafraude Tributario Operacion Tributos]]"
nexo_respaldado: "[[TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/nombres-55-empresarios-detenidos-fraude-fisco-grande-historia_20231215/"
    titulo: "Nombres de los 55 empresarios detenidos por el mayor fraude al fisco"
    medio: "CNN Chile"
    tipo: secundaria
    fecha: 2023-12-15
    consultado: 2026-10-19
tags:
  - evidencia/resolucion-judicial
  - poder-judicial
  - formalizacion
  - operacion-tributos
---

# Formalizacion-Megafraude-Operacion-Tributos-2023

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Emisor**: 1° Juzgado de Garantía de Santiago / `= this.organismo_emisor`
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Resolución del 1° Juzgado de Garantía de Santiago tras una maratónica audiencia de formalización de cargos contra 55 imputados por los delitos de asociación ilícita, fraude al Fisco, delitos tributarios reiterados y lavado de activos. El tribunal decretó la prisión preventiva de más de 30 cabecillas y operadores principales, incluyendo a [[Jose Antonio Pavez Campillay]], [[Ximena Jimenez Faras]], [[Andres Esteban Galaz Soto]], [[Olga Paz Barraza Quezada]] y [[Juan Alberto Croxatto Romero]], ordenando el embargo y retención preventiva de bienes muebles, inmuebles y cuentas bancarias.

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
