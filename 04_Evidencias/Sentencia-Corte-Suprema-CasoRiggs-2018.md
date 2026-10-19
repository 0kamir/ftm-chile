---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-RGS-2018-001"
tipo_documento: "Sentencia Definitiva de Casación y Comiso Patrimonial (Rol N° 16.865-2017) e Informe del Senado de EE.UU. sobre Riggs Bank"
fecha_emision: 2018-08-24
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / US Senate Permanent Subcommittee on Investigations / Peritaje FEN Universidad de Chile"
causa_vinculada: "[[Caso Riggs]]"
nexo_respaldado: "[[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
    titulo: "Caso Riggs fue cerrado por la Corte Suprema tras 14 años"
    medio: "CNN Chile"
    tipo: secundaria
    fecha: 2018-08-24
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - caso-riggs
  - caso-pinocheques
  - corte-suprema
---

# Sentencia-Corte-Suprema-CasoRiggs-2018

## Metadatos de la Fuente
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Poder del Estado**: `= this.organismo_emisor`
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada` (y antecedentes conexos del [[Caso Pinocheques]])
- **Nexo Respaldado**: `= this.nexo_respaldado` (junto a [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] y [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]])

## Extracto y Relevancia Probatoria
Sentencia definitiva dictada el 24 de agosto de 2018 por la Segunda Sala Penal de la [[Corte Suprema de Chile]] (Rol N° `16.865-2017`) en el [[Caso Riggs]], sobre la base de la instrucción iniciada por el Ministro en Visita [[Sergio Munoz Gajardo]], las querellas del [[Servicio Impuestos Internos]] y el peritaje contable de la Universidad de Chile:
1. **Acreditación del Origen Ilícito de la Fortuna (US$ 17,86 Millones)**: Estableció como hecho probado que [[Augusto Pinochet Ugarte]] acumuló en [[Riggs Bank y Sociedades Offshore Ashburton]] más de US$ 21,32 millones, de los cuales **US$ 17,86 millones** provinieron directamente de la sustracción de fondos públicos de gastos reservados de la Comandancia en Jefe del Ejército ([[Comando de Apoyo a la Fuerza del Ejercito]]) y de triangulaciones que incluyeron caudales originados en el [[Caso Pinocheques]] ([[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]]).
2. **Condenas Penales y Comiso Patrimonial a Favor del Fisco**: Condenó a tres oficiales de Ejército encargados de las cuentas secretas como autores de [[Malversacion de Caudales Publicos]] y ordenó el **comiso definitivo a favor del Fisco de Chile de US$ 1.649.142 en instrumentos financieros, 24 bienes inmuebles y una flota de vehículos** pertenecientes al patrimonio de [[Augusto Pinochet Ugarte]], [[Lucia Hiriart Rodriguez]] y sus sociedades pantalla estructuradas por [[Oscar Aitken Lavanchy]].

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
