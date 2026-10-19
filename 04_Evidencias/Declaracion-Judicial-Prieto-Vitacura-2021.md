---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-VIT-MP-2021-001"
tipo_documento: "Declaración Judicial / Autodenuncia y Peritaje Contable PDI"
fecha_emision: 2021-08-10
organismo_emisor: "[[Municipalidad de Vitacura]]"
fuente_osint: "Carpeta Investigativa Fiscalía Centro Norte / Querella Consejo de Defensa del Estado"
causa_vinculada: "[[Caso Vitacura]]"
nexo_respaldado: "[[TRX-2021-04-15-Subvencion-VitaDeportes-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.ex-ante.cl/?p=152080"
    titulo: "Audiencia de formalización de Raúl Torrealba"
    medio: "Ex-Ante"
    tipo: secundaria
    fecha: 2023-06-15
    consultado: 2026-10-19
tags:
  - evidencia/declaracion-judicial
  - caso-vitacura
---

# Declaracion-Judicial-Prieto-Vitacura-2021

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Relacionado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Declaración judicial prestada por [[Domingo Prieto Urrejola]] y respaldada por cartolas bancarias periciadas por la Brigada Investigadora Anticorrupción (BRIAC) de la PDI, que acredita las entregas mensuales de sobres con efectivo extraídos de las subvenciones de [[Vita Deportes]] ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]) a favor de [[Raul Torrealba del Pedregal]] en el [[Caso Vitacura]].

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
