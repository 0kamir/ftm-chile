---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TOP-PAC-2021-001"
tipo_documento: "Sentencia Definitiva Condenatoria 4° Tribunal de Juicio Oral en lo Penal de Santiago"
fecha_emision: 2021-05-07
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial (pjud.cl) / Reportes de Operaciones Sospechosas UAF"
causa_vinculada: "[[Caso Pacogate]]"
nexo_respaldado: "[[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]"
estado_verificacion: desactualizado
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
    titulo: "Caso Pacogate: rechazan prisión preventiva para los 25 condenados"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-04-15
    consultado: 2026-10-19
alertas_verificacion:
  - "El juicio oral se postergó en 2021 y el veredicto es de abril de 2026: una 'sentencia 2021' del TOP no calza con las fuentes (podría ser un abreviado). Verificar."
tags:
  - evidencia/sentencia-judicial
  - caso-pacogate
---

# Sentencia-TOP-Santiago-Pacogate-2021

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
Fallo condenatorio unánime dictado contra la cúpula de los 31 principales acusados del [[Caso Pacogate]], incluyendo al general (r) [[Flavio Echeverria Cortez]] y al coronel (r) [[Jaime Paz Meneses]], dando por acreditado más allá de toda duda razonable el desfalco de **$28.348.928.198 CLP** en la [[Direccion de Finanzas de Carabineros]] ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]) por los delitos de [[Malversacion de Caudales Publicos]], [[Lavado de Activos]] y asociación ilícita.

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
