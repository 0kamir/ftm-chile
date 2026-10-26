---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Metropolitana de Santiago"
superior_jerarquico: "Ministerio de Hacienda"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
  - "https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html"
  - "https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html"
  - "https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html"
  - "https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz"
tags:
  - entidad/publica
  - sii
  - caso-audios
---

# Servicio Impuestos Internos

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Órgano fiscalizador tributario dependiente del Ministerio de Hacienda. En el marco del [[Caso Audios]], la Fiscalía Metropolitana Oriente investiga pagos ilícitos y entregas de información reservada coordinadas por [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] a favor del factoring [[Factop SpA]], documentadas en el nexo [[TRX-2023-06-22-Reunion-Audios-01]] y la evidencia [[Audio-Reunion-Edificio-Alonso-2023]].

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_origen AS "Operador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad](https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) | El Mostrador | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) |
| [Seis ex jerarcas de Colonia Dignidad fueron condenados a prisión por la Corte Suprema](https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) | Cooperativa | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) |
| [Falleció Claudio Spiniak, empresario condenado por liderar una red de pedofilia](https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) | Cooperativa | `secundaria` | 2026-03-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) |
| [Claudio Spiniak fue condenado a cinco años y un día de cárcel](https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) | Cooperativa | `secundaria` | 2006-08-10 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) |
| [Muere Claudio Spiniak](https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) | Emol | `secundaria` | 2026-03-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) |
| [Jovino Novoa, caso Spiniak e investigación del juez Sergio Muñoz](https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) | Pauta | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) |
