---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Quiroz y Asociados Consultores SpA"
fecha_constitucion: 1998-05-12
objeto_social: "Asesorías económicas, consultoría macroeconómica, estudios de mercado y libre competencia"
representante_legal: "[[Jorge Quiroz Castro]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
  - "https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
  - "https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/"
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
tags:
  - entidad/privada
  - consultoria
  - libre-competencia
  - peritaje-economico
---

# Quiroz y Asociados Consultores SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Socio Principal**: `= this.representante_legal`

## Contexto en Investigaciones y Regulatorias
Firma de consultoría económica y financiera fundada y encabezada por el economista [[Jorge Quiroz Castro]]. La consultora prestó servicios y estudios económicos para diversas empresas y asociaciones gremiales investigadas por la [[Fiscalia Nacional Economica]] y sometidas a proceso ante el Tribunal de Defensa de la Libre Competencia (TDLC).

Entre sus principales encargos documentados en expedientes de libre competencia se encuentran los modelos de demanda y proyección confeccionados para la [[Asociacion de Productores Avicolas de Chile AG]] ([[Caso Colusion de los Pollos]]) e informes económicos de defensa para [[Farmacias Salcobrand SA]] ([[Caso Colusion de las Farmacias]]).

## Registros Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito Imputado"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Sentencia TDLC N° 139/2014](https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) | TDLC / FNE | `primaria` | 2014-09-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) |
| [TDLC condenó a Agrosuper, Ariztía y Don Pollo por colusión](https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/) | Fiscalía Nacional Económica | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/) |
| [FNE presenta requerimiento por colusión en la producción y comercialización de carne de pollo](https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) | Fiscalía Nacional Económica | `primaria` | 2011-12-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) |
| [Corte Suprema confirma multas por colusión contra Agrosuper, Ariztía y Don Pollo](https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/) | Fiscalía Nacional Económica | `primaria` | 2015-10-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/) |
| [Sentencia TDLC N° 119/2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-01-31 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
