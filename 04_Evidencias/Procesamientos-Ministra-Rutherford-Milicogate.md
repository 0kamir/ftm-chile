---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CM-MIL-2019-001"
tipo_documento: "Auto de Procesamiento y Sentencias Ministra en Visita Corte Marcial"
fecha_emision: 2018-02-11
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
  - url: "https://vlex.cl/vid/corte-marcial-revoca-condena-844999287"
    titulo: "Corte Marcial revoca condena por fraude a general (r) Santic"
    medio: "vLex Chile"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.elciudadano.com/?p=683869"
    titulo: "Fraude en el Ejército: Corte Marcial disminuye condenas a cuatro uniformados"
    medio: "El Ciudadano"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - evidencia/auto-procesamiento
  - caso-milicogate
---

# Procesamientos-Ministra-Rutherford-Milicogate

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Extracto y Relevancia Probatoria
Autos de procesamiento y sentencias de primera instancia dictados por la Ministra en Visita de la Corte Marcial, Romy Rutherford Parentti, en el [[Caso Milicogate]] sobre facturas por bienes y servicios inexistentes pagadas con fondos de la Ley Reservada del Cobre a proveedores como [[Frasim Ltda]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]). Entre ellos, el procesamiento del general (r) Héctor Ureta (feb-2018) y las condenas de primera instancia (nov-2019) del general (r) [[Jozo Santic Palomino]] a 10 años y un día y 3 años y un día, que la Corte Marcial redujo a 5 años y un día por falsedad en la arista Tecnodata II. Un auto de procesamiento no es una condena. La investigación sobre gastos reservados de [[Juan Miguel Fuente-Alba Poblete]] es una arista distinta.

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
