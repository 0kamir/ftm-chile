---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CM-MIL-2019-001"
tipo_documento: "Auto de Procesamiento y Sentencias Ministra en Visita Corte Marcial"
fecha_emision: 2019-02-14
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial (pjud.cl) / Comisión Investigadora Cámara de Diputados"
causa_vinculada: "[[Caso Milicogate]]"
nexo_respaldado: "[[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html"
    titulo: "Procesan a general (r) por defraudar al fisco con cerca de 1.800 millones"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2018-02-11
    consultado: 2026-10-19
alertas_verificacion:
  - "La fuente encontrada es un procesamiento de feb-2018 (general (r) Héctor Ureta); no se ubicó el auto de 2019 citado."
tags:
  - evidencia/auto-procesamiento
  - caso-milicogate
---

# Auto-Procesamiento-Ministra-Rutherford-2019

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Resoluciones y sentencias dictadas por la Ministra en Visita Extraordinaria de la Corte Marcial (designada por la [[Corte Suprema de Chile]]), Romy Rutherford Parentti, que acreditaron los mecanismos de defraudación de la Ley Reservada del Cobre en el [[Comando de Apoyo a la Fuerza del Ejercito]] a través de proveedores como [[Frasim Ltda]] ([[Jozo Santic Palomino]]) y la malversación de gastos reservados por parte de [[Juan Miguel Fuente-Alba Poblete]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]) en el [[Caso Milicogate]].

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
