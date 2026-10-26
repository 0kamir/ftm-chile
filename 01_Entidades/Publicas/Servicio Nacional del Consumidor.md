---
tipo_nodo: entidad_publica
rut: ""
categoria: Servicio Público Descentralizado
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Ministerio de Economía, Fomento y Turismo"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html"
  - "https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html"
  - "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml"
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
tags:
  - entidad/publica
  - sernac
  - proteccion-consumidor
---

# Servicio Nacional del Consumidor

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Servicio estatal encargado de velar por el cumplimiento de la Ley N° 19.496 sobre Protección de los Derechos de los Consumidores. En el [[Caso Colusion del Papel Tissue]], encabezó la mesa de negociación extrajudicial y el Procedimiento Voluntario Colectivo que concluyó en el histórico acuerdo compensatorio de **$97.500.000.000 CLP** pagados por [[Empresas CMPC SA]] a más de 13 millones de chilenos ([[Acuerdo-Compensatorio-SERNAC-CMPC-Tissue-2017]]).

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
| [Acuerdo por colusión tissue: CMPC pagará US$150 millones para compensar a consumidores](https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) | Emol | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) |
| [CMPC pagará compensación de 150 millones de dólares: por consumidor serán 7.000 pesos](https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) | Cooperativa | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) |
| [TDLC dicta sentencia en caso Tissue: multa a SCA y exime a CMPC](https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) | Emol | `secundaria` | 2017-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) |
| [Suprema condena a CMPC y SCA por colusión](https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) | Emol | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) |
| [CMPC tendrá que pagar una millonaria multa por la colusión del papel](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) | BioBioChile | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) |
| [Fallo Corte Suprema Rol 2578-2012 (caso Farmacias)](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
