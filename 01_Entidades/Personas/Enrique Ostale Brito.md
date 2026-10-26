---
tipo_nodo: persona
rut: ""
aliases:
  - "Enrique Ostalé"
  - "Enrique Ostale Brito"
rol_principal: "Ex Gerente General y Presidente del Directorio de Walmart Chile S.A. (ex D&S)"
afiliacion_politica: "Independiente"
situacion_procesal: ninguna
medida_cautelar: "Sanción corporativa aplicada a Walmart Chile S.A. por 11.160 UTA en sentencia de la Corte Suprema (Rol N° 9.361-2019)"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/"
  - "https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/"
  - "https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/"
tags:
  - entidad/persona
  - colusion-supermercados
---

# Enrique Ostalé Brito

## Reseña y Conexiones en la Red
Ejecutivo principal y presidente del directorio de [[Walmart Chile SA]] (ex D&S) durante la transición y operación del holding supermercadista en Chile. Vinculado como representante de la entidad sancionada por la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Supermercados-2020]]) con **11.160 UTA** en el [[Caso Colusion de los Supermercados]] ([[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]]). La sanción del D.L. N° 211 recayó sobre la persona jurídica [[Walmart Chile SA]]; **no consta ninguna sanción personal contra Enrique Ostale**.

## Sociedades y Entidades Representadas
```dataview
TABLE WITHOUT ID
  file.link AS "Entidad",
  rut AS "RUT",
  razon_social AS "Razón Social"
FROM "01_Entidades/Privadas"
WHERE representante_legal = this.file.link
```

## Participación en Flujos y Hechos
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción / Hecho",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE firmante_origen = this.file.link OR firmante_destino = this.file.link
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema condena a Cencosud, SMU y Walmart por colusión en el mercado de la carne de pollo fresca y duplica multa a US$ 21 millones](https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2020-04-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) |
| [Caso Supermercados: Hub-and-Spoke y programas de cumplimiento](https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) | CentroCompetencia (CeCo UAI) | `secundaria` | 2020-04-20 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/caso-supermercados-hub-and-spoke-y-programas-de-cumplimiento/) |
| [Sentencia N° 167/2019 TDLC: Requerimiento de la FNE en contra de Cencosud S.A., SMU S.A. y Walmart Chile S.A.](https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) | Tribunal de Defensa de la Libre Competencia (TDLC) | `primaria` | 2019-02-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) |
