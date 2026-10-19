---
tipo_nodo: entidad_publica
rut: ""
categoria: Servicio Público Fiscalizador Autónomo
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Consejo de la Comisión para el Mercado Financiero (Relación vía Ministerio de Hacienda)"
autoridad_vinculada: "[[Carlos Pavez Tolosa]]"
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
