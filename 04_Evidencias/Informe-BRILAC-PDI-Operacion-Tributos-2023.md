---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PDI-BRILAC-TRIBUTOS-2023"
tipo_documento: "Informe Policial y Actas de Allanamiento Masivo de la Brigada de Lavado de Activos (BRILAC)"
fecha_emision: 2023-12-14
organismo_emisor: "[[Direccion de Inteligencia Policial de Carabineros]]"
fuente_osint: "Policía de Investigaciones de Chile (investigaciones.cl) / Fiscalía de Chile"
causa_vinculada: "[[Caso Megafraude Tributario Operacion Tributos]]"
nexo_respaldado: "[[TRX-2023-12-14-Perjuicio-Fiscal-Operacion-Tributos-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml"
    titulo: "SII confirma que 55 empresarios detenidos concretaron el mayor fraude"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2023-12-15
    consultado: 2026-10-19
tags:
  - evidencia/policial
  - pdi
  - brilac
  - allanamientos
  - operacion-tributos
---

# Informe-BRILAC-PDI-Operacion-Tributos-2023

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Policial Ejecutor**: Brigada Investigadora de Lavado de Activos (BRILAC) - PDI
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Operativo de la Brigada Investigadora de Lavado de Activos (BRILAC) de la PDI en diciembre de 2023, con la detención de 55 personas e incautación de relojes, joyas y vehículos de alta gama avaluados por la prensa en más de $27.000 millones. El informe policial no es público.

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
