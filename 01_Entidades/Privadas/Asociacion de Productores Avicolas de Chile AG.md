---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Asociación de Productores Avícolas de Chile A.G. (APA)"
fecha_constitucion: 1980-04-10
objeto_social: "Asociación gremial de representación, coordinación y fomento de la industria avícola chilena"
representante_legal: "[[Juan Miguel Ovalle Garces]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
  - "https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
  - "https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf"
  - "https://tdlc.cl/wp-content/uploads/sentencias/Sentencia_139_Corte_Suprema.pdf"
tags:
  - entidad/privada
  - apa
  - gremio
  - colusion-pollos
  - disuelta-por-sentencia
---

# Asociacion de Productores Avicolas de Chile AG

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal Histórico**: [[Juan Miguel Ovalle Garces]]
- **Estado Legal**: **Disuelta por Orden Judicial** ([[Sentencia-TDLC-139-Colusion-Pollos-2014]] ratificada por [[Sentencia-Corte-Suprema-Colusion-Pollos-2015]])

## Contexto en Investigaciones
Asociación gremial que agrupaba a las empresas productoras de carne de ave en Chile ([[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]]). En el [[Caso Colusion de los Pollos]], la FNE y los tribunales acreditaron que la APA funcionó como la secretaría técnica y órgano ejecutivo del cartel: proyectaba la demanda de pollo a nivel país, fijaba las cuotas de faenamiento para cada productor y realizaba auditorías de verificación para sancionar a quienes rompieran los acuerdos colusorios.

En una resolución sin precedentes en el derecho chileno de la competencia, el TDLC y la Corte Suprema ordenaron su **disolución forzada**, al haberse demostrado que su objeto real era facilitar y ejecutar conductas ilícitas contrarias a la libre competencia.

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
| [Sentencia Corte Suprema Rol 27.181-2014](https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf) | Corte Suprema (vía FNE) | `primaria` | 2015-10-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf) |
| [Sentencia 139 - Corte Suprema](https://tdlc.cl/wp-content/uploads/sentencias/Sentencia_139_Corte_Suprema.pdf) | TDLC | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://tdlc.cl/wp-content/uploads/sentencias/Sentencia_139_Corte_Suprema.pdf) |
