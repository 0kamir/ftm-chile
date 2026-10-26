---
tipo_nodo: entidad_publica
rut: ""
categoria: Policía
region: "Nacional / Macrozona Sur (UIOE Temuco)"
superior_jerarquico: "Carabineros de Chile / Ministerio del Interior y Seguridad Pública"
estado_verificacion: verificado
fuentes:
  - "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml"
tags:
  - entidad/publica
  - carabineros
  - dipolcar
  - uioe
  - caso-operacion-huracan
---

# Direccion de Inteligencia Policial de Carabineros

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
La Dirección de Inteligencia Policial de Carabineros (DIPOLCAR) y su Unidad de Inteligencia Operativa Especializada (UIOE) con base en Temuco fueron la estructura policial y de mando responsable del montaje de la [[Caso Operacion Huracan]], encabezada por el general [[Gonzalo Blu Rodriguez]], el excoronel [[Marcelo Teuber Munoz]], el exmayor [[Patricio Marin Lazo]], el excapitán [[Leonardo Osses Sandoval]] y el perito civil [[Alex Smith Leay]], bajo la jefatura institucional del general director [[Bruno Villalobos Krumm]]. La unidad fue clausurada tras descubrirse la implantación fraudulenta de supuestos chats de mensajería para incriminar a comuneros mapuche bajo la Ley Antiterrorista.

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [El 'profesor' Smith condenado a 12 años de cárcel](https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) | El Dínamo | `secundaria` | 2026-04-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) |
| [Profesor Smith y otros 3 condenados en Operación Huracán presentan recurso para anular sentencia](https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) | BioBioChile | `secundaria` | 2026-05-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) |
| [Huracán 2: formalización del creador de Antorcha y funcionario del Labocar](https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml) | BioBioChile | `secundaria` | 2018-02-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-los-rios/2018/02/19/amp/huracan-2-realizan-formalizacion-del-creador-de-antorcha-y-funcionario-del-labocar.shtml) |
| [SII confirma que 55 empresarios detenidos concretaron el mayor fraude](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml) | BioBioChile | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml) |
