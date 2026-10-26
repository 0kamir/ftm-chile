---
tipo_nodo: partido_politico
rut: ""
sigla: "PPD"
fecha_fundacion: "1987-12-15"
coalicion: "Socialismo Democrático (ex Concertación / Nueva Mayoría)"
estado_registro: "Vigente"
estado_verificacion: verificado
fuentes:
  - "https://www.servel.cl/partidos-politicos/partidos-constituidos/"
  - "https://www.biobiochile.cl/especial/noticias/reportajes/reportajes-reportajes/2017/08/18/las-cuentas-pendientes-de-la-corporacion-ambientalista-que-triangulo-platas-al-ppd.shtml"
  - "https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/"
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
tags:
  - entidad/partido
  - socialismo-democratico
  - caso-sqm
  - caso-coimas
---

# Partido por la Democracia

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Contexto en Investigaciones Judiciales
Colectividad política involucrada en el [[Caso SQM]] —donde [[Patricio Rodrigo Salinas]], director de la ONG [[Corporacion Chile Ambiente]], fue condenado en juicio abreviado ([[Sentencia-Abreviada-SQM-ChileAmbiente-PPD-2017]]) tras reconocer facturas por servicios no prestados a [[SQM SA]] entre 2011 y 2012; según CIPER, esos fondos habrían llegado al partido ([[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]])—, así como en el [[Caso Coimas]] (condena firme de la [[Corte Suprema de Chile]] contra su exdiputado [[Victor Manuel Rebolledo Gonzalez]], [[Sentencia-Corte-Suprema-Caso-Coimas-2007]]).

## Militantes y Autoridades Vinculadas en el Vault
```dataview
TABLE WITHOUT ID
  file.link AS "Persona",
  rol_principal AS "Rol Principal",
  situacion_procesal AS "Situación Procesal",
  medida_cautelar AS "Medida Cautelar"
FROM "01_Entidades/Personas"
WHERE contains(string(afiliacion_politica), this.file.name)
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Partidos Políticos Constituidos](https://www.servel.cl/partidos-politicos/partidos-constituidos/) | Servicio Electoral de Chile (Servel) | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.servel.cl/partidos-politicos/partidos-constituidos/) |
| [Las cuentas pendientes de la corporación ambientalista que trianguló platas de SQM al PPD](https://www.biobiochile.cl/especial/noticias/reportajes/reportajes-reportajes/2017/08/18/las-cuentas-pendientes-de-la-corporacion-ambientalista-que-triangulo-platas-al-ppd.shtml) | BioBioChile | `secundaria` | 2017-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/especial/noticias/reportajes/reportajes-reportajes/2017/08/18/las-cuentas-pendientes-de-la-corporacion-ambientalista-que-triangulo-platas-al-ppd.shtml) |
| [Caso Coimas: Corte Suprema condena a tres exdiputados](https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/) | El Mostrador | `secundaria` | 2007-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/) |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
