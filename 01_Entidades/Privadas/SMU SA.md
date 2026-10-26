---
tipo_nodo: entidad_privada
rut: "76.000.008-6"
razon_social: "SMU S.A."
fecha_constitucion: 2007-12-01
objeto_social: "Operación de supermercados y distribuidoras mayoristas (Unimarc, Mayorista 10, Alvi y Ok Market)"
representante_legal: "[[Alvaro Saieh Bendeck]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/"
  - "https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/"
  - "https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/"
tags:
  - entidad/privada
  - colusion-supermercados
  - retail
---

# SMU S.A.

## Perfil Societario y Rol en la Red
Holding supermercadista controlado por el grupo CorpGroup de [[Alvaro Saieh Bendeck]], operador de Unimarc, Mayorista 10 y Alvi. En el [[Caso Colusion de los Supermercados]], la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Supermercados-2020]]) condenó a **SMU S.A.** a una multa de **6.876 UTA** (~US$ 4,9 millones) a beneficio fiscal por su participación en la colusión *hub-and-spoke* del mercado de carne de pollo fresca junto a [[Cencosud SA]] y [[Walmart Chile SA]] ([[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]]).

## Flujos Financieros de Salida (Pagos / Contratos Emitidos)
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción",
  fecha AS "Fecha",
  entidad_destino AS "Destinatario",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa Judicial"
FROM "03_Hechos_y_Nexos"
WHERE entidad_origen = this.file.link
SORT fecha ASC
```

## Flujos Financieros de Entrada (Pagos / Adjudicaciones Recibidas)
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Pagador / Origen",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa Judicial"
FROM "03_Hechos_y_Nexos"
WHERE entidad_destino = this.file.link
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema condena a Cencosud, SMU y Walmart por colusión en el mercado de la carne de pollo fresca y duplica multa a US$ 21 millones](https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2020-04-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) |
| [Sentencia N° 167/2019 TDLC: Requerimiento de la FNE en contra de Cencosud S.A., SMU S.A. y Walmart Chile S.A.](https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) | Tribunal de Defensa de la Libre Competencia (TDLC) | `primaria` | 2019-02-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) |
| [Caso Supermercados: Hub-and-Spoke y programas de cumplimiento](https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) | CentroCompetencia (CeCo UAI) | `secundaria` | 2020-04-20 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) |
