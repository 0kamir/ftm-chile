---
tipo_nodo: causa_judicial
ruc: "RIT-13745-2023-1JG"
año_inicio: 2023
tribunal_o_fiscalia: "1° Juzgado de Garantía de Santiago / Fiscalía Regional Metropolitana Occidente"
fiscal_a_cargo: "Eduardo Baeza Cervela / José Luis Pérez Calaf"
estado_judicial: formalizada_con_prisiones_preventivas
delito_principal: "[[Delito Tributario]]"
tags:
  - causa
  - operacion-tributos
  - megafraude-sii
  - facturas-falsas
  - lavado-de-activos
---

# Caso Megafraude Tributario Operacion Tributos

## Ficha Procesal, Regulatoria y Sancionatoria
- **Rol de Causa / Expediente Judicial**: `= this.ruc` *(Causa RIT 13745-2023 del 1° Juzgado de Garantía de Santiago)*
- **Año de Inicio / Formalización Pública**: `= this.año_inicio` (Período defraudatorio investigado: 2016–2023)
- **Tribunal Competente**: `= this.tribunal_o_fiscalia`
- **Fiscales a Cargo de la Persecución**: `= this.fiscal_a_cargo` (en coordinación con la Brigada de Lavado de Activos de la PDI y querellas del [[Servicio Impuestos Internos]] y CDE)
- **Estado Judicial**: `= this.estado_judicial` (55 empresarios y contadores formalizados; más de 30 en prisión preventiva o arresto domiciliario)
- **Delito Principal**: `= this.delito_principal` (con concurrencia de [[Asociacion Ilicita]], [[Fraude al Fisco]] y [[Lavado de Activos]])

## Resumen Ejecutivo de la Causa
Conocido como la **Operación Tributos**, constituye el mayor fraude tributario y patrimonial en la historia de la República de Chile, con un perjuicio fiscal consolidado superior a los **`$240.000.000.000 CLP`** (más de US$ 275 millones).

La investigación, liderada por la Fiscalía Regional Metropolitana Occidente junto a la Brigada Investigadora de Lavado de Activos (BRILAC) de la PDI y el [[Servicio Impuestos Internos]], desarticuló una megaestructura criminal conformada por 7 clanes delictivos independientes pero interconectados:
1. **Clan Pavez**: Liderado por [[Jose Antonio Pavez Campillay]] y su contadora de confianza [[Ximena Jimenez Faras]], operando mediante [[Inversiones y Asesorias Pavez SpA]] y decenas de empresas de papel para emitir más de 100.000 facturas falsas y solicitar devoluciones ilícitas de IVA exportador.
2. **Clan Galaz**: Encabezado por [[Andres Esteban Galaz Soto]], dedicado a la compraventa masiva de facturación ideológicamente falsa para rebajar base imponible y justificar créditos fiscales inexistentes.
3. **Clan Barraza**: Dirigido por [[Olga Paz Barraza Quezada]], enfocado en la provisión de documentos tributarios espurios a grandes empresas y transportistas.
4. **Clan Croxatto**: Conducido por [[Juan Alberto Croxatto Romero]], estructurando redes de sociedades fantasma para blanqueo de capitales.
5. **Clanes Nexus, Canessa y Polanco**: Redes de intermediación y corretaje de facturas ideológicamente falsas en diversas regiones del país.

El 14 de diciembre de 2023, la PDI ejecutó allanamientos simultáneos en 83 inmuebles en 10 regiones (Arica y Parinacota, Tarapacá, Antofagasta, Coquimbo, Valparaíso, Metropolitana, Maule, Biobío, Araucanía y Los Lagos), incautando vehículos de alta gama, armas de fuego, divisas extranjeras, lingotes de oro, criptomonedas y deteniendo a 55 imputados ([[Formalizacion-Megafraude-Operacion-Tributos-2023]]).

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Infracción / Delito",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
