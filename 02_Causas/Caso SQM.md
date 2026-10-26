---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2015
tribunal_o_fiscalia: "Fiscalía Regional de Valparaíso / 8° Juzgado de Garantía de Santiago / 3° TOP de Santiago"
fiscal_a_cargo: "Claudia Perivancich / Pablo Gómez"
estado_judicial: absuelta_nulidad_pendiente
delito_principal: "[[Cohecho]]"
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
tags:
  - causa
  - caso-sqm
  - financiamiento-politico
---

# Caso SQM

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (junto a [[Delito Tributario]])

## Resumen Ejecutivo
Macrocausa sobre financiamiento irregular de la política iniciada en 2015 como arista del [[Caso Penta]], a partir de querellas del [[Servicio Impuestos Internos]] ([[Querella-SII-Boletas-SQM-2015]]) por boletas y facturas que la Fiscalía estimó ideológicamente falsas, emitidas a [[SQM SA]] por personas vinculadas a partidos de distintos sectores. La propia SQM reconoció ante la SEC y el Departamento de Justicia de EE.UU. pagos indebidos por unos US$ 14,75 millones. La causa tuvo una decena de condenas en procedimientos abreviados, más de 60 sobreseimientos y un centenar de suspensiones condicionales.

La hipótesis acusatoria contra [[Pablo Longueira Montes]] y [[Patricio Contesse Gonzalez]] por [[Cohecho]] vinculado a la Ley de Royalty Minero de 2010 ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]) **no fue acreditada en juicio**. El 22 de octubre de 2025 el 3° Tribunal de Juicio Oral en lo Penal de Santiago absolvió, por mayoría, a los ocho acusados que llegaron a juicio, entre ellos [[Pablo Longueira Montes]] y [[Patricio Contesse Gonzalez]]: no dio por acreditada más allá de toda duda razonable la falsedad ideológica de las boletas y facturas, y constató una vulneración del derecho a ser juzgado en un plazo razonable. La Fiscalía, el [[Servicio Impuestos Internos]] y el CDE presentaron recursos de nulidad, revisados por la Corte de Apelaciones de Santiago el 6 de octubre de 2026 y pendientes de resolución. Las absoluciones están vigentes y rige la presunción de inocencia.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Pagador / Emisor",
  firmante_destino AS "Receptor Político",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Fiscalía presenta recurso de nulidad contra fallo del caso SQM](https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) | Emol | `secundaria` | 2026-09-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) |
| [Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio](https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) | BioBioChile | `secundaria` | 2026-10-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) |
