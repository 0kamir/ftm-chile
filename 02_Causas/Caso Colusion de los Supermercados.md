---
tipo_nodo: causa_judicial
ruc: "C-304-16 (TDLC) / Rol 9361-2019 (CS)"
año_inicio: 2016
tribunal_o_fiscalia: "Tribunal de Defensa de la Libre Competencia / Corte Suprema / Fiscalía Nacional Económica"
fiscal_a_cargo: "Felipe Irarrázabal Philippi / Ricardo Riesco Eyzaguirre (Fiscal Nacional Económico)"
estado_judicial: cerrada
delito_principal: "[[Colusion y Atentado a la Libre Competencia]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/"
  - "https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/"
  - "https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/"
tags:
  - causa
  - colusion-supermercados
  - libre-competencia
  - hub-and-spoke
---

# Caso Colusión de los Supermercados

## Ficha Procesal
- **Rol / RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal / Investigador a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Ilícito Principal**: `= this.delito_principal`

## Resumen Ejecutivo
El **Caso Colusión de los Supermercados** (Rol C-304-16 ante el Tribunal de Defensa de la Libre Competencia y Rol N° 9.361-2019 ante la [[Corte Suprema de Chile]]) se originó en enero de 2016 tras el requerimiento interpuesto por la [[Fiscalia Nacional Economica]] (FNE) contra las tres principales cadenas supermercadistas del país —[[Cencosud SA]] (Jumbo y Santa Isabel), [[Walmart Chile SA]] (Líder, Ekono y Superbodega Acuenta) y [[SMU SA]] (Unimarc, Mayorista 10 y Alvi)— por haber participado entre 2008 y 2011 en un acuerdo o práctica concertada destinada a fijar precios mínimos de venta al público de la carne de pollo fresca (esquema *hub-and-spoke* articulado a través de los proveedores avícolas [[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]], sancionados previamente en el [[Caso Colusion de los Pollos]]).

Mediante la [[Sentencia-Corte-Suprema-Colusion-Supermercados-2020]] del **8 de abril de 2020**, la Tercera Sala de la [[Corte Suprema de Chile]] confirmó la responsabilidad infraccional establecida en la Sentencia N° 167/2019 del Tribunal de Defensa de la Libre Competencia, rechazó las defensas basadas en programas de cumplimiento (*compliance*) ineficaces y **duplicó las multas a beneficio fiscal**, imponiendo una sanción conjunta de **29.568 Unidades Tributarias Anuales (UTA)** (aproximadamente **US$ 21 millones** / **$18.300.000.000 CLP**): **11.532 UTA** a [[Cencosud SA]], **11.160 UTA** a [[Walmart Chile SA]] y **6.876 UTA** a [[SMU SA]] ([[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]]).

## Vínculos Clave en la Bóveda
- **Supermercados Condenados:** [[Cencosud SA]] (vinculada a [[Horst Paulmann Kemna]]), [[Walmart Chile SA]] (vinculada a [[Enrique Ostale Brito]]) y [[SMU SA]] (vinculada a [[Alvaro Saieh Bendeck]]).
- **Proveedores *Hub* Relacionados:** [[Agrosuper SA]], [[Empresas Ariztia SA]], [[Agricola Don Pollo Limitada]] ([[Caso Colusion de los Pollos]]).
- **Hechos y Nexos:** [[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]].
- **Evidencia Documental:** [[Sentencia-Corte-Suprema-Colusion-Supermercados-2020]].

## Transacciones y Hechos Registrados en esta Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción / Hecho",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  monto_clp AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE causa_vinculada = this.file.link
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema condena a Cencosud, SMU y Walmart por colusión en el mercado de la carne de pollo fresca y duplica multa a US$ 21 millones](https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2020-04-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) |
| [Sentencia N° 167/2019 TDLC: Requerimiento de la FNE en contra de Cencosud S.A., SMU S.A. y Walmart Chile S.A.](https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) | Tribunal de Defensa de la Libre Competencia (TDLC) | `primaria` | 2019-02-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) |
| [Caso Supermercados: Hub-and-Spoke y programas de cumplimiento](https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) | CentroCompetencia (CeCo UAI) | `secundaria` | 2020-04-20 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) |
