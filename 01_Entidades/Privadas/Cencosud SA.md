---
tipo_nodo: entidad_privada
rut: "93.834.000-5"
razon_social: "Cencosud S.A."
fecha_constitucion: 1978-11-10
objeto_social: "Operación de hipermercados, supermercados (Jumbo, Santa Isabel), tiendas por departamento, mejoramiento del hogar y centros comerciales"
representante_legal: "[[Horst Paulmann Kemna]]"
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

# Cencosud S.A.

## Perfil Societario y Rol en la Red
Holding minorista fundado y controlado históricamente por [[Horst Paulmann Kemna]], operador de las cadenas de supermercados Jumbo y Santa Isabel. En el [[Caso Colusion de los Supermercados]], la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Supermercados-2020]]) condenó a **Cencosud S.A.** al pago de **11.532 UTA** (~US$ 8,2 millones) a beneficio fiscal tras acreditar su participación en la coordinación *hub-and-spoke* con [[Walmart Chile SA]] y [[SMU SA]] para no vender carne de pollo fresca bajo el costo de lista mayorista fijado junto a los proveedores avícolas ([[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]]).

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
