---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-ICIJ-PNP-2016-001"
tipo_documento: "Base de Datos Offshore Leaks (Panama Papers ICIJ / CIPER Chile) e Informe de Fiscalización Internacional de 200 Sociedades Offshore del SII"
fecha_emision: 2016-04-03
organismo_emisor: "[[Servicio Impuestos Internos]]"
fuente_osint: "International Consortium of Investigative Journalists (offshoreleaks.icij.org) / CIPER Chile / Servicio de Impuestos Internos (sii.cl)"
causa_vinculada: "[[Caso Panama Papers Chile]]"
nexo_respaldado: "[[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]]"
estado_verificacion: parcial
fuentes:
  - url: "https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/"
    titulo: "The Panama Papers: los secretos de chilenos en paraísos fiscales"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2016-04-04
    consultado: 2026-10-19
  - url: "https://offshoreleaks.icij.org/"
    titulo: "ICIJ Offshore Leaks Database"
    medio: "ICIJ"
    tipo: primaria
    consultado: 2026-10-19
tags:
  - evidencia/informe
  - panama-papers
  - offshore
  - icij
---

# Filtracion-ICIJ-PanamaPapers-Chile-2016

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Órgano Fiscalizador en Chile**: `= this.organismo_emisor` (en coordinación con la [[Unidad de Analisis Financiero]])
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (junto a [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] y [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]])

## Extracto y Relevancia Probatoria
Acervo documental proveniente de los 11,5 millones de registros internos del bufete [[Mossack Fonseca y Sociedades Offshore Panama]] publicados por el Consorcio Internacional de Periodistas de Investigación (ICIJ) y analizados en Chile por CIPER en el [[Caso Panama Papers Chile]]:
1. **Identificación de 200 Estructuras *Offshore* Vinculadas a Chile**: Documentó la participación de [[Gonzalo Delaveau Swett]] (entonces presidente de *Chile Transparente*) en cinco sociedades en Bahamas ([[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]]), así como las fundaciones panameñas de [[Agustin Edwards Eastman]] y las sociedades de [[Alfredo Ovalle Rodriguez]] ([[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]]). Figurar en la filtración no implica ilegalidad: CIPER señaló en 2016 que no había evidencias de ilegalidades.
2. **Conexión Fiduciaria con el Caso Riggs**: Documentó los servicios registrales prestados por Mossack Fonseca a sociedades en Islas Vírgenes Británicas vinculadas a [[Riggs Bank y Sociedades Offshore Ashburton]], [[Oscar Aitken Lavanchy]] y [[Augusto Pinochet Ugarte]] ([[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]]).

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
