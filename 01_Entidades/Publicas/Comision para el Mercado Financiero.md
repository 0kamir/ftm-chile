---
tipo_nodo: entidad_publica
rut: ""
categoria: Servicio Público Fiscalizador Autónomo
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Consejo de la Comisión para el Mercado Financiero (Relación vía Ministerio de Hacienda)"
autoridad_vinculada: "[[Carlos Pavez Tolosa]]"
estado_verificacion: verificado
fuentes:
  - "https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/"
  - "https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20121128/pags-amp/20121128154834.html"
  - "https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html"
  - "https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia"
  - "https://www.cooperativa.cl/noticias/site/artic/20140902/pags-amp/20140902135102.html"
tags:
  - entidad/publica
  - regulador-financiero
  - cmf-svs
  - caso-cascadas
---

# Comision para el Mercado Financiero

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Ex Superintendente Vinculado**: `= this.autoridad_vinculada`

## Contexto en Investigaciones
Órgano regulador y supervisor del mercado de valores, seguros y bancos en Chile (continuador legal de la Superintendencia de Valores y Seguros, SVS). En julio de 2007 dictó la [[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]] en el [[Caso LAN Informacion Privilegiada y Banco de Talca]], multando con 11.470 UF a [[Sebastian Pinera Echenique]] por el uso de información privilegiada en la compra de acciones de *LAN Airlines* a través de [[Bancard Inversiones Ltda]] ([[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]]). Posteriormente, en el [[Caso Cascadas]], bajo la conducción de [[Carlos Pavez Tolosa]], emitió la histórica [[Resolucion-SVS-CasoCascadas-2014]] que sancionó a [[Julio Ponce Lerou]] y a los ejecutivos de [[Sociedad de Inversiones Pampa Calichera SA]] —matriz controladora de [[SQM SA]] ([[Patricio Contesse Gonzalez]])— por el esquema de transacciones bursátiles concertadas documentado en [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]]. Asimismo, sus fiscalizaciones sobre factoring no bancario conectan con la caída de [[Factop SpA]] en el [[Caso Audios]].

## Historial de Nexos y Fiscalizaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Fiscalizada",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [El directorio de Lan que se transformó en la peor pesadilla de Piñera](https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/) | CIPER Chile | `secundaria` | 2009-09-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/) |
| [Piñera acusó motivos políticos en sanción de la SVS, aunque pagará la multa](https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html) | Cooperativa | `secundaria` | 2007-07-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html) |
| [Suprema ratificó multa contra dueños de LAN por comprar acciones con información privilegiada](https://www.cooperativa.cl/noticias/site/artic/20121128/pags-amp/20121128154834.html) | Cooperativa | `secundaria` | 2012-11-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20121128/pags-amp/20121128154834.html) |
| [Piñera y caso Banco de Talca: 'Fui víctima de un acto injusto, ilegal y arbitrario'](https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html) | Emol | `secundaria` | 2009-07-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html) |
| [Del Banco de Talca a Exalmar: 5 momentos en que Piñera se vio complicado con la justicia](https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia) | El Desconcierto | `secundaria` | 2017-02-27 | [Wayback ↺](https://web.archive.org/web/*/https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia) |
| [Caso Cascadas: SVS aplicó multas por 164 millones de dólares](https://www.cooperativa.cl/noticias/site/artic/20140902/pags-amp/20140902135102.html) | Cooperativa | `secundaria` | 2014-09-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20140902/pags-amp/20140902135102.html) |
