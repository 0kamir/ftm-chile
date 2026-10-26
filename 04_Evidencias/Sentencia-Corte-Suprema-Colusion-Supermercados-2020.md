---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-CS-9361-2019"
tipo_documento: "Sentencia Judicial Ejecutoriada (Rol N° 9.361-2019 CS / Sentencia N° 167/2019 TDLC)"
fecha_emision: 2020-04-08
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Fiscalía Nacional Económica / Tribunal de Defensa de la Libre Competencia / Corte Suprema"
causa_vinculada: "[[Caso Colusion de los Supermercados]]"
nexo_respaldado: "[[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/"
  - "https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/"
tags:
  - evidencia/sentencia
  - colusion-supermercados
---

# Sentencia Corte Suprema y TDLC — Colusión de los Supermercados (2019-2020)

## Síntesis Documental
Fallo definitivo de la Tercera Sala de la [[Corte Suprema de Chile]] (Rol N° 9.361-2019, del 8 de abril de 2020) que conoció los recursos de reclamación contra la Sentencia N° 167/2019 del Tribunal de Defensa de la Libre Competencia en el [[Caso Colusion de los Supermercados]]. La Corte Suprema tuvo por acreditada la colusión tipo *hub-and-spoke* entre [[Cencosud SA]], [[Walmart Chile SA]] y [[SMU SA]] para fijar precios mínimos de reventa de carne de pollo fresca entre 2008 y 2011, duplicando las multas hasta un total de **29.568 UTA** (~US$ 21 millones / **$18.300.000.000 CLP**) y sentando jurisprudencia sobre los requisitos de seriedad, independencia y efectividad de los programas de *compliance* en libre competencia.

## Hechos y Transacciones Soportadas por esta Evidencia
```dataview
TABLE WITHOUT ID
  file.link AS "Transacción / Hecho",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  monto_clp AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE evidencia_soporte = this.file.link
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema condena a Cencosud, SMU y Walmart por colusión en el mercado de la carne de pollo fresca y duplica multa a US$ 21 millones](https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2020-04-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-condena-a-cencosud-smu-y-walmart-por-colusion-en-el-mercado-de-la-carne-de-pollo-fresca-y-duplica-multa-impuesta-por-el-tdlc-con-sancion-total-de-us-21-millones/) |
| [Sentencia N° 167/2019 TDLC: Requerimiento de la FNE en contra de Cencosud S.A., SMU S.A. y Walmart Chile S.A.](https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) | Tribunal de Defensa de la Libre Competencia (TDLC) | `primaria` | 2019-02-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.tdlc.cl/sentencia-167-2019-requerimiento-de-la-fiscalia-nacional-economica-en-contra-de-cencosud-s-a-y-otras/) |
