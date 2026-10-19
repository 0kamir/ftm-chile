---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-SPK-2008-001"
tipo_documento: "Sentencia Definitiva de Casación y Fallos de Instrucción en Visita Extraordinaria (Rol Crimen N° 9.327-2003)"
fecha_emision: 2008-05-07
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Expediente Rol 9.327-2003 del Ministro en Visita Sergio Muñoz Gajardo"
causa_vinculada: "[[Caso Spiniak]]"
nexo_respaldado: "[[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html"
    titulo: "Falleció Claudio Spiniak, empresario condenado por liderar una red de pedofilia"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2026-03-13
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-spiniak
  - corte-suprema
---

# Sentencia-Corte-Suprema-CasoSpiniak-2008

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (y [[TRX-2003-11-05-Arista-Politica-Spiniak-01]])

## Extracto y Relevancia Probatoria
Conjunto de resoluciones y sentencias definitivas dictadas en la Causa Rol N° `9.327-2003` del [[Caso Spiniak]], instruida en primera instancia por el Ministro en Visita extraordinario [[Sergio Munoz Gajardo]] y ratificada en casación por la Segunda Sala Penal de la [[Corte Suprema de Chile]] el 7 de mayo de 2008:
1. **Condena Penal y Patrimonial a la Red Spiniak**: Elevó de 10 a **12 años de presidio mayor en su grado medio** la condena efectiva contra [[Claudio Spiniak Vilensky]] como autor de delitos reiterados de abusos deshonestos, promoción de la prostitución infantil y producción de material pornográfico en las instalaciones operadas bajo [[Inversiones El Bosque Ltda]], incorporando las auditorías tributarias del [[Servicio Impuestos Internos]] ([[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]]).
2. **Resolución de la Arista Político-Judicial y Falso Testimonio**: Acreditó pericialmente la falsedad de los testimonios de Gema Bueno y del sacerdote José Luis Artiagoitía surgidos tras las denuncias públicas de la diputada [[Pia Guzman Mena]] ([[TRX-2003-11-05-Arista-Politica-Spiniak-01]]), condenando a los primeros por falso testimonio en causa criminal y sobreseyendo definitivamente en esta causa al senador de la [[Union Democrata Independiente]], [[Jovino Novoa Vasquez]].

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
