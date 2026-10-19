---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PHOTO-TC-CERIMEDO-RN-2022"
tipo_documento: "Registro Fotográfico Periodístico (The Clinic)"
fecha_emision: 2022-09-04
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "The Clinic (theclinic.cl) / Archivo Prensa Chilena"
causa_vinculada: "[[Caso Operaciones Digitales e Injerencia Electoral]]"
nexo_respaldado: "[[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/"
    titulo: "El día que el 'rey de los trolls' llegó a la sede de RN"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2026-08-28
    consultado: 2026-10-19
tags:
  - evidencia/fotografia
  - the-clinic
  - cerimedo
  - renovacion-nacional
  - rechazo-2022
---

# Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022

## Metadatos de Fuente Primaria (Cadena de Custodia Legal y Periodística)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Registro**: `= this.tipo_documento`
- **Fecha de Captura**: `= this.fecha_emision` *(4 de septiembre de 2022)*
- **Lugar de Captura**: Sede Nacional de [[Renovacion Nacional]], Antonio Varas 454, Providencia, Santiago
- **Medio Revelador**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Fotografía periodística revelada por el medio *The Clinic* que documenta la presencia física del consultor digital argentino [[Fernando Cerimedo]] en el interior de la sede nacional de [[Renovacion Nacional]] durante la noche del 4 de septiembre de 2022, en el marco de la celebración del triunfo electoral de la opción Rechazo en el Plebiscito Constitucional.

En el registro, Cerimedo se encuentra sentado junto al entonces prosecretario de Renovación Nacional, Manuel José Errázuriz, su socio chileno en [[Numen Publicidad SpA]] Enrique García Arancibia, y colaboradoras vinculadas a centros de estudios del sector como Teresa Zañartu y Carolina Marzuca, evidenciando su inserción en el cuartel general de campaña de la centroderecha durante dicha jornada.

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
