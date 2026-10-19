---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PJD-ALLANAMIENTO-CONGRESO-FLORES-2026"
tipo_documento: "Orden Judicial de Entrada, Registro e Incautación en Dependencias del Congreso Nacional"
fecha_emision: 2026-04-18
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Fiscalía Regional de Valparaíso"
causa_vinculada: "[[Caso Asignaciones Parlamentarias y Cuota Flores]]"
nexo_respaldado: "[[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.ciperchile.cl/2026/05/06/fiscalia-ingresa-al-senado-por-investigacion-contra-camila-flores-por-posible-fraude-al-fisco/"
    titulo: "Fiscalía ingresa al Senado por investigación contra Camila Flores"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2026-05-06
    consultado: 2026-10-19
tags:
  - evidencia/resolucion-judicial
  - allanamiento-congreso
  - cuota-flores
  - urac
  - os9
---

# Orden-Entrada-Registro-Congreso-Caso-Flores-2026

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión y Ejecución**: `= this.fecha_emision`
- **Tribunal Competente**: Juzgado de Garantía de Valparaíso
- **Órgano Policial Ejecutor**: Departamento OS9 de Carabineros y URAC de la Fiscalía de Valparaíso
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Resolución judicial que autorizó el allanamiento simultáneo e incautación de evidencia documental, computadores y dispositivos móviles en las oficinas legislativas de la senadora [[Camila Flores Oporto]] en el Congreso Nacional de Valparaíso y en su domicilio particular. La diligencia tuvo por objeto periciar la trazabilidad de los pagos de asignaciones a su personal de apoyo e indagar la exigencia de porcentajes de remuneración en efectivo.

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
