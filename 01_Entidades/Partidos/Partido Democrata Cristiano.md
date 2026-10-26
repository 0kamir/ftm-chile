---
tipo_nodo: partido_politico
rut: ""
sigla: "PDC"
fecha_fundacion: "1957-07-28"
coalicion: "Centro Democrático (ex Concertación / Nueva Mayoría)"
estado_registro: "Vigente"
estado_verificacion: verificado
fuentes:
  - "https://www.servel.cl/partidos-politicos/partidos-constituidos/"
  - "https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/"
  - "https://www.biobiochile.cl/noticias/2013/07/16/victor-manuel-rebolledo-baja-candidatura-tras-criticas-por-su-condena-en-el-caso-coimas.shtml"
  - "https://www.cooperativa.cl/noticias/pais/judicial/suprema-ratifico-condena-de-tres-anos-por-fraude-contra-juan-pablo/2006-10-16/153132.html"
  - "https://www.cooperativa.cl/noticias/pais/organismos-del-estado/denuncias-de-corrupcion/ex-director-de-chiledeportes-de-valparaiso-fue-encontrado-culpable-de/2008-05-23/213737.html"
  - "https://www.biobiochile.cl/noticias/2015/01/24/cinco-casos-de-corrupcion-que-mancharon-la-politica-antes-de-penta-en-los-ultimos-15-anos.shtml"
tags:
  - entidad/partido
  - democracia-cristiana
  - caso-coimas
---

# Partido Demócrata Cristiano

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Contexto en Investigaciones Judiciales
Partido político histórico de la ex Concertación. En el [[Caso Coimas]], la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Caso-Coimas-2007]]) condenó en última instancia a sus entonces diputados [[Cristian Pareto Vergara]] y Jaime Jiménez Villavicencio (junto al exdiputado PPD [[Victor Manuel Rebolledo Gonzalez]]) a penas remitidas e inhabilitación perpetua para cargos públicos por [[Cohecho]] en la tramitación de permisos para plantas de revisión técnica en la Región de O'Higgins ([[TRX-2002-10-15-Sobornos-Plantas-Revision-Tecnica-Coimas-01]]).

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
| [Caso Coimas: Corte Suprema condena a tres exdiputados](https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/) | El Mostrador | `secundaria` | 2007-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/) |
| [Víctor Manuel Rebolledo y las condenas ejecutoriadas del Caso Coimas](https://www.biobiochile.cl/noticias/2013/07/16/victor-manuel-rebolledo-baja-candidatura-tras-criticas-por-su-condena-en-el-caso-coimas.shtml) | BioBioChile | `secundaria` | 2013-07-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/2013/07/16/victor-manuel-rebolledo-baja-candidatura-tras-criticas-por-su-condena-en-el-caso-coimas.shtml) |
| [Corte Suprema ratificó condena de tres años por fraude contra Juan Pablo Dávila](https://www.cooperativa.cl/noticias/pais/judicial/suprema-ratifico-condena-de-tres-anos-por-fraude-contra-juan-pablo/2006-10-16/153132.html) | Cooperativa | `secundaria` | 2006-10-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/judicial/suprema-ratifico-condena-de-tres-anos-por-fraude-contra-juan-pablo/2006-10-16/153132.html) |
| [Ex director de Chiledeportes de Valparaíso fue encontrado culpable de fraude al Fisco](https://www.cooperativa.cl/noticias/pais/organismos-del-estado/denuncias-de-corrupcion/ex-director-de-chiledeportes-de-valparaiso-fue-encontrado-culpable-de/2008-05-23/213737.html) | Cooperativa | `secundaria` | 2008-05-23 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/organismos-del-estado/denuncias-de-corrupcion/ex-director-de-chiledeportes-de-valparaiso-fue-encontrado-culpable-de/2008-05-23/213737.html) |
| [Casos de corrupción que mancharon la política antes de Penta: Chiledeportes y Publicam](https://www.biobiochile.cl/noticias/2015/01/24/cinco-casos-de-corrupcion-que-mancharon-la-politica-antes-de-penta-en-los-ultimos-15-anos.shtml) | BioBioChile | `secundaria` | 2015-01-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/2015/01/24/cinco-casos-de-corrupcion-que-mancharon-la-politica-antes-de-penta-en-los-ultimos-15-anos.shtml) |
