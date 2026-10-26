---
tipo_nodo: entidad_publica
rut: ""
categoria: Servicio Público Autónomo
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Ministerio de Economía, Fomento y Turismo (Supervigilancia)"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html"
  - "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml"
  - "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
tags:
  - entidad/publica
  - fne
  - libre-competencia
  - carteles
---

# Fiscalia Nacional Economica

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Agencia pública descentralizada encargada de instruir investigaciones y perseguir infracciones contra la libre competencia (Decreto Ley N° 211). En el [[Caso Colusion del Papel Tissue]], desarticuló el cartel de más de una década entre [[Empresas CMPC SA]] y [[SCA Chile SA]], haciendo valer por primera vez en un caso de gran impacto masivo el mecanismo de delación compensada que derivó en la [[Sentencia-TDLC-160-Colusion-Tissue-2017]].

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
| [TDLC dicta sentencia en caso Tissue: multa a SCA y exime a CMPC](https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) | Emol | `secundaria` | 2017-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) |
| [Suprema condena a CMPC y SCA por colusión](https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) | Emol | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) |
| [CMPC tendrá que pagar una millonaria multa por la colusión del papel](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) | BioBioChile | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) |
| [FNE presenta requerimiento por colusión en la producción y comercialización de carne de pollo](https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) | Fiscalía Nacional Económica | `primaria` | 2011-12-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) |
| [Sentencia TDLC N° 119/2012 y fallo Corte Suprema Rol 2578-2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Sentencia TDLC N° 139/2014 (Rol C-236-2011)](https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) | TDLC / FNE | `primaria` | 2014-09-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) |
