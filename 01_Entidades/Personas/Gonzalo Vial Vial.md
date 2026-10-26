---
tipo_nodo: persona
rut: ""
aliases:
  - "Gonzalo Vial"
  - "Gonzalo Vial Vial"
rol_principal: "Fundador y Presidente Histórico de Agrosuper"
afiliacion_politica: "Independiente"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Condena civil y económica corporativa ratificada por la Corte Suprema de Chile"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
  - "https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
  - "https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/wp-content/uploads/2015/10/secs_27_181-14.pdf"
  - "https://tdlc.cl/wp-content/uploads/sentencias/Sentencia_139_Corte_Suprema.pdf"
tags:
  - entidad/persona
  - empresario
  - agrosuper
  - colusion-pollos
---

# Gonzalo Vial Vial

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis
Destacado empresario agroindustrial chileno, fundador y presidente del directorio de [[Agrosuper SA]]. Bajo su liderazgo empresarial, Agrosuper se consolidó como el gigante de la industria avícola, porcina y acuícola en Chile.

En el marco del [[Caso Colusion de los Pollos]], las investigaciones de la [[Fiscalia Nacional Economica]] y la [[Sentencia-TDLC-139-Colusion-Pollos-2014]] determinaron la activa participación de los directivos de Agrosuper en las reuniones de fijación y asignación de cuotas de producción avícola junto a [[Empresas Ariztia SA]] y la [[Asociacion de Productores Avicolas de Chile AG]], lo que conllevó la condena a su compañía con la multa máxima de 30.000 UTA fijada por la [[Corte Suprema de Chile]].

## Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Delito", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    p.delito_imputado,
    p.causa_vinculada
  ])
);
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
