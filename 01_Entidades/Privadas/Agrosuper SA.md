---
tipo_nodo: entidad_privada
rut: "76.129.263-3"
razon_social: "Agrosuper S.A."
fecha_constitucion: 1955-08-10
objeto_social: "Producción, procesamiento, faenamiento, distribución y exportación de productos cárnicos (pollo, cerdo, pavo y salmón)"
representante_legal: "José Guzmán Vial"
historial_correcciones:
  - "RUT corregido el 2026-10-19: el vault registraba 96.522.000-3, que no corresponde a la empresa; el RUT verificado es 76.129.263-3."
estado_verificacion: parcial
fuentes:
  - "https://www.agrosuper.com/inversionistas/wp-content/uploads/2023/02/Reporte-Integrado-Agrosuper-2024-v29_17_06.pdf"
  - "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
  - "https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
  - "https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf"
tags:
  - entidad/privada
  - agrosuper
  - alimentos
  - colusion-pollos
---

# Agrosuper SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Familia Vial, fundada por [[Gonzalo Vial Vial]]

## Contexto en Investigaciones
Holding agroindustrial y el mayor productor de alimentos cárnicos de Chile. En el [[Caso Colusion de los Pollos]], fue condenada por el Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-139-Colusion-Pollos-2014]]) y la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Pollos-2015]]) por liderar un cartel oligopólico junto a [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]], coordinado a través de la [[Asociacion de Productores Avicolas de Chile AG]] para fijar cuotas de producción entre 1994 y 2011. La Corte Suprema le impuso la multa máxima legal de 30.000 UTA (aproximadamente US$ 23 millones / $16.000 millones de pesos).

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
| [Reporte Integrado Agrosuper 2024 (identificación de la sociedad)](https://www.agrosuper.com/inversionistas/wp-content/uploads/2023/02/Reporte-Integrado-Agrosuper-2024-v29_17_06.pdf) | Agrosuper S.A. | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.agrosuper.com/inversionistas/wp-content/uploads/2023/02/Reporte-Integrado-Agrosuper-2024-v29_17_06.pdf) |
| [Sentencia TDLC N° 139/2014](https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) | TDLC / FNE | `primaria` | 2014-09-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) |
| [TDLC condenó a Agrosuper, Ariztía y Don Pollo por colusión](https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/) | Fiscalía Nacional Económica | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/) |
| [FNE presenta requerimiento por colusión en la producción y comercialización de carne de pollo](https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) | Fiscalía Nacional Económica | `primaria` | 2011-12-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) |
| [Corte Suprema confirma multas por colusión contra Agrosuper, Ariztía y Don Pollo](https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/) | Fiscalía Nacional Económica | `primaria` | 2015-10-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/) |
| [Sentencia Corte Suprema Rol 27.181-2014](https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf) | Corte Suprema (vía FNE) | `primaria` | 2015-10-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf) |
