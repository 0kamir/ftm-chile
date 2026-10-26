---
tipo_nodo: persona
rut: ""
aliases:
  - "Hernán Larraín"
rol_principal: "Ex Senador por el Maule Sur, Ex Presidente del Senado, Ex Presidente de la UDI y Ex Ministro de Justicia"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: testigo_clave
medida_cautelar: "Sin medidas cautelares penales (Reconoció públicamente en 2016 haber actuado en defensa política de Colonia Dignidad en los años 90)"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
  - "https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html"
tags:
  - entidad/persona
  - caso-colonia-dignidad
  - ex-senador
---

# Hernan Larrain Fernandez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Abogado, exsenador por la Circunscripción 11ª (Maule Sur, que incluye Parral), expresidente del [[Senado de la Republica de Chile]] (2004–2005), expresidente de la [[Union Democrata Independiente]] (2006–2008) y ex Ministro de Justicia y Derechos Humanos (2018–2022). En la arista político-institucional del [[Caso Colonia Dignidad]], durante la década de 1990 fue uno de los principales articuladores parlamentarios del denominado *"Grupo de Amigos de Colonia Dignidad"*, suscribiendo el requerimiento ante el Tribunal Constitucional en contra del Decreto Supremo N° 143 que canceló la personalidad jurídica de [[Sociedad Benefactora y Educacional Dignidad]] y cuestionando públicamente los allanamientos policiales ordenados para capturar a [[Paul Schafer Schneider]] en coordinación con la vocería de [[Hartmut Hopp Miottel]] ([[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]]). Tras las condenas definitivas de la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-ColoniaDignidad-2013]]), pidió perdón públicamente en 2016 por haber defendido al enclave.

## Nexos y Actuaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Gestión",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto Registrado (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad](https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) | El Mostrador | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) |
| [Seis ex jerarcas de Colonia Dignidad fueron condenados a prisión por la Corte Suprema](https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) | Cooperativa | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) |
