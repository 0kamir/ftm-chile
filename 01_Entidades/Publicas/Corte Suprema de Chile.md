---
tipo_nodo: entidad_publica
rut: ""
categoria: Poder Judicial
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Corte Suprema de Justicia (Órgano Autónomo Constitucional)"
estado_verificacion: verificado
fuentes:
  - "https://irp.fas.org/cia/product/chile/index.html"
  - "https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile"
  - "https://nsarchive.gwu.edu/node/3113"
  - "https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash"
  - "https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html"
  - "https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia"
tags:
  - entidad/publica
  - poder-judicial
  - corte-suprema
---

# Corte Suprema de Chile

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Máximo tribunal de la República. En el [[Caso Colonia Dignidad]], designó al Ministro en Visita extraordinario [[Jorge Zepeda Arancibia]] para fragmentar la asociación ilícita encabezada por [[Paul Schafer Schneider]] e incautar los arsenales de guerra ocultos en Parral ([[TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01]]), confirmando las condenas definitivas en [[Sentencia-Corte-Suprema-ColoniaDignidad-2013]]. Asimismo, en noviembre de 2003, en el marco del [[Caso Spiniak]], el Pleno debió intervenir de urgencia tras la operación de extorsión con cámara oculta contra el juez Daniel Calvo Flores, removiéndolo de la investigación y designando como Ministro en Visita extraordinario a [[Sergio Munoz Gajardo]] ([[TRX-2003-11-05-Arista-Politica-Spiniak-01]]), quien instruyó la causa hasta la sentencia definitiva [[Sentencia-Corte-Suprema-CasoSpiniak-2008]]. Dos décadas más tarde, en las derivaciones del [[Caso Audios]], el peritaje del teléfono móvil de [[Luis Hermosilla Osorio]] reveló intercambios de mensajería y coordinaciones extraprocesales ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) con la entonces ministra de la Tercera Sala Constitucional [[Angela Vivanco Martinez]], lo que derivó en la apertura de un cuaderno de remoción y su destitución en 2024.

## Nexos y Gestiones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Gestión",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Externo",
  firmante_destino AS "Magistrado / Funcionario",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [CIA Activities in Chile (Informe Hinchey)](https://irp.fas.org/cia/product/chile/index.html) | CIA / FAS | `primaria` | 2000-09-18 | [Wayback ↺](https://web.archive.org/web/*/https://irp.fas.org/cia/product/chile/index.html) |
| [Hinchey Report on CIA Activities in Chile](https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile) | Transnational Institute | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile) |
| [Documentos desclasificados sobre Chile](https://nsarchive.gwu.edu/node/3113) | National Security Archive | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://nsarchive.gwu.edu/node/3113) |
| [Chile's journalists' union kicked out powerful media mogul over CIA propaganda cash](https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) | The World (PRI) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) |
| [Piñera y caso Banco de Talca: 'Fui víctima de un acto injusto, ilegal y arbitrario'](https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html) | Emol | `secundaria` | 2009-07-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html) |
| [Del Banco de Talca a Exalmar: 5 momentos en que Piñera se vio complicado con la justicia](https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia) | El Desconcierto | `secundaria` | 2017-02-27 | [Wayback ↺](https://web.archive.org/web/*/https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia) |
