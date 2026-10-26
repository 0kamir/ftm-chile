---
tipo_nodo: entidad_privada
rut: "81.201.000-K"
razon_social: "Walmart Chile S.A. (ex Distribución y Servicio D&S S.A.)"
fecha_constitucion: 1957-01-01
objeto_social: "Operación de supermercados e hipermercados (Líder, Express de Líder, Ekono y Superbodega Acuenta)"
representante_legal: "[[Enrique Ostale Brito]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/"
  - "https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/"
  - "https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/"
tags:
  - entidad/privada
  - colusion-supermercados
  - retail
---

# Walmart Chile S.A.

## Perfil Societario y Rol en la Red
Principal actor del mercado supermercadista chileno (continuador de D&S S.A.), dirigido ejecutivamente en el período por [[Enrique Ostale Brito]]. En el [[Caso Colusion de los Supermercados]], la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Supermercados-2020]]) desestimó la eximente/atenuante de su programa de cumplimiento corporativo y duplicó su sanción a **11.160 UTA** (~US$ 7,9 millones) por su participación en la fijación coordinada de precios mínimos de venta al público de carne de pollo fresca entre 2008 y 2011 ([[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]]).

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
| [Caso Supermercados: Hub-and-Spoke y programas de cumplimiento](https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) | CentroCompetencia (CeCo UAI) | `secundaria` | 2020-04-20 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) |
| [Sentencia N° 167/2019 TDLC: Requerimiento de la FNE en contra de Cencosud S.A., SMU S.A. y Walmart Chile S.A.](https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) | Tribunal de Defensa de la Libre Competencia (TDLC) | `primaria` | 2019-02-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) |
