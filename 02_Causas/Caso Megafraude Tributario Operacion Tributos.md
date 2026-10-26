---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2023
tribunal_o_fiscalia: "1° Juzgado de Garantía de Santiago / Fiscalía Regional Metropolitana Occidente"
fiscal_a_cargo: "Eduardo Baeza Cervela / José Luis Pérez Calaf"
estado_judicial: formalizada_con_prisiones_preventivas
delito_principal: "[[Delito Tributario]]"
historial_correcciones:
  - "Personas renombradas el 2026-10-19 según el listado publicado por La Tercera (Pavez Canessa, Galaz Rojas, Sacco Croxatto, Jiménez Farías). Se retiraron dos sociedades y un TRX de lavado sin fuente."
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml"
  - "https://www.latercera.com/nacional/noticia/megafraude-tributario-clan-de-pavez-canessa-vendia-facturas-falsas-y-contaba-con-un-notario-suplente-en-la-organizacion/552EKQIRDRFKBNGSSO2I3L2N3I/"
  - "https://cooperativa.cl/noticias/pais/judicial/denuncias-de-corrupcion/caso-tributos-fiscalia-pide-prision-preventiva-para-26-empresarios/2023-12-18/164214.html"
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
- **Estado Judicial**: `= this.estado_judicial` (55 imputados formalizados en diciembre de 2023; la Fiscalía pidió prisión preventiva para 26)
- **Delito Principal**: `= this.delito_principal` (con concurrencia de [[Asociacion Ilicita]], [[Fraude al Fisco]] y [[Lavado de Activos]])

## Resumen Ejecutivo de la Causa
Conocido como la **Operación Tributos**, constituye el mayor fraude tributario y patrimonial en la historia de la República de Chile, con un perjuicio fiscal consolidado superior a los **`$240.000.000.000 CLP`** (más de US$ 275 millones).

La investigación, liderada por la Fiscalía Regional Metropolitana Occidente junto a la Brigada Investigadora de Lavado de Activos (BRILAC) de la PDI y el [[Servicio Impuestos Internos]], atribuye el fraude a seis grupos o 'clanes' (hipótesis de la Fiscalía según el expediente del SII reportado por La Tercera; sin sentencia):
1. **Clan Canessa**: atribuido a [[Jose Antonio Pavez Canessa]]; 16 sociedades de papel que vendían facturas falsas a cambio de comisión.
2. **Clan Galaz**: atribuido a [[Juan Victor Galaz Rojas]]; falsas exportaciones de teléfonos para obtener devoluciones de IVA exportador (14 sociedades, $11.594 millones).
3. **Clan Barraza**: atribuido a [[Olga Paz Barraza Quezada]]; devoluciones del impuesto específico al diésel por $2.489 millones.
4. **Clan Croxatto**: atribuido a [[Osvaldo Mario Luis Sacco Croxatto]]; seis empresas proveedoras de facturas falsas ($422,7 millones).
5. **Clan Nexus** y 6. **Clan Barriga & Polanco**: redes de rebaja de IVA mediante facturas falsas ($849 millones y más de $2.000 millones).

En diciembre de 2023 la PDI ejecutó allanamientos simultáneos, deteniendo a 55 imputados e incautando relojes, joyas y vehículos de alta gama ([[Formalizacion-Megafraude-Operacion-Tributos-2023]]).

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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [SII confirma que 55 empresarios detenidos concretaron el mayor fraude de la historia contra el fisco](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml) | BioBioChile | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml) |
| [Megafraude tributario: clan Pavez Canessa vendía facturas falsas](https://www.latercera.com/nacional/noticia/megafraude-tributario-clan-de-pavez-canessa-vendia-facturas-falsas-y-contaba-con-un-notario-suplente-en-la-organizacion/552EKQIRDRFKBNGSSO2I3L2N3I/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/megafraude-tributario-clan-de-pavez-canessa-vendia-facturas-falsas-y-contaba-con-un-notario-suplente-en-la-organizacion/552EKQIRDRFKBNGSSO2I3L2N3I/) |
| [Caso Tributos: Fiscalía pide prisión preventiva para 26 empresarios](https://cooperativa.cl/noticias/pais/judicial/denuncias-de-corrupcion/caso-tributos-fiscalia-pide-prision-preventiva-para-26-empresarios/2023-12-18/164214.html) | Cooperativa | `secundaria` | 2023-12-18 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/denuncias-de-corrupcion/caso-tributos-fiscalia-pide-prision-preventiva-para-26-empresarios/2023-12-18/164214.html) |
