---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-SVS-LAN-2007-306"
tipo_documento: "Resolución Exenta N° 306 de la Superintendencia de Valores y Seguros (Multa por Uso de Información Privilegiada en LAN Airlines) y Expediente Banco de Talca (1982)"
fecha_emision: 2007-07-06
organismo_emisor: "[[Comision para el Mercado Financiero]]"
fuente_osint: "Comisión para el Mercado Financiero (cmfchile.cl — Resolución Exenta SVS N° 306/2007) / Poder Judicial de Chile"
causa_vinculada: "[[Caso LAN Informacion Privilegiada y Banco de Talca]]"
nexo_respaldado: "[[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/"
    titulo: "El directorio de Lan que se transformó en la peor pesadilla de Piñera"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2009-09-29
    consultado: 2026-10-19
alertas_verificacion:
  - "Falta el enlace a la Resolución Exenta 306 en cmfchile.cl."
tags:
  - evidencia/resolucion
  - caso-lan
  - banco-de-talca
  - cmf
---

# Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007

## Metadatos de Fuente Primaria (Cadena de Custodia OSINT)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Órgano Regulador Emisor**: `= this.organismo_emisor` (ex Superintendencia de Valores y Seguros — SVS)
- **Fuente Pública / OSINT**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (y [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]])

## Extracto y Relevancia Probatoria
Resolución administrativa sancionatoria dictada el 6 de julio de 2007 por la Superintendencia de Valores y Seguros (hoy [[Comision para el Mercado Financiero]]) en el [[Caso LAN Informacion Privilegiada y Banco de Talca]], que acreditó que el 24 de julio de 2006 [[Sebastian Pinera Echenique]] —estando en posesión de información privilegiada sobre los estados financieros de *LAN Airlines S.A.* conocida en sesión de directorio— no se abstuvo de operar e instruyó a [[Bancard Inversiones Ltda]] (*Inversiones Santa Cecilia S.A.*) adquirir **3.000.000 de acciones de LAN** por **`$5.300.000.000 CLP`** ([[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]]), imponiéndole una **multa de 11.470 UF (~US$ 363.000)** por infracción al artículo 165 de la Ley N° 18.045 de Mercado de Valores. El expediente complementa además los antecedentes judiciales del colapso del *Banco de Talca* de agosto de 1982 ([[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]]).

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
