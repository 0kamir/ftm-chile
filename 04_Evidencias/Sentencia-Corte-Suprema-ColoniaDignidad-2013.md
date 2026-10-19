---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-CDG-2013-001"
tipo_documento: "Sentencias Definitivas de Casación (Roles N° 4.442-2011 y N° 5.234-2012 — Asociación Ilícita, Abusos Reiterados y Ley de Control de Armas)"
fecha_emision: 2013-01-24
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Expediente Ministro en Visita Jorge Zepeda Arancibia (Rol 2.182-1998)"
causa_vinculada: "[[Caso Colonia Dignidad]]"
nexo_respaldado: "[[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
    titulo: "Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2013-01-28
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-colonia-dignidad
  - corte-suprema
---

# Sentencia-Corte-Suprema-ColoniaDignidad-2013

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (junto a [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] y [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]])

## Extracto y Relevancia Probatoria
Sentencias definitivas dictadas por la Segunda Sala Penal de la [[Corte Suprema de Chile]] en el [[Caso Colonia Dignidad]] (confirmando los fallos de primera instancia del Ministro en Visita [[Jorge Zepeda Arancibia]]), que establecieron judicialmente:
1. **Existencia de Asociación Ilícita Jerarquizada y Arsenal de Guerra**: Confirmó que la cúpula de [[Sociedad Benefactora y Educacional Dignidad]] liderada por [[Paul Schafer Schneider]] operó como una organización estructurada para cometer delitos contra las personas, abusos sexuales reiterados de menores e infracción masiva a la Ley de Control de Armas tras el hallazgo de los arsenales subterráneos en Parral ([[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]]).
2. **Condenas Efectivas y Fuga de Hartmut Hopp**: Ratificó la pena de **5 años y un día de presidio efectivo** contra el subdirector y vocero [[Hartmut Hopp Miottel]] (prófugo en Alemania desde 2011) y condenas contra el resto del directorio del enclave.
3. **Embargos Patrimoniales e Indemnizaciones Civiles**: Mantuvo los embargos sobre los bienes transferidos al holding *Villa Baviera / Cerro Florido S.A.* tras la cancelación de la personalidad jurídica en 1991 y las fiscalizaciones del [[Servicio Impuestos Internos]] ([[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]]), condenando solidariamente al pago de indemnizaciones multimillonarias a las víctimas.

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
