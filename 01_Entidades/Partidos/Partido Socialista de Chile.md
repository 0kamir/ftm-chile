---
tipo_nodo: partido_politico
rut: ""
sigla: "PS"
fecha_fundacion: "1933-04-19"
coalicion: "Socialismo Democrático (ex Concertación)"
estado_registro: "Vigente"
estado_verificacion: verificado
fuentes:
  - "https://www.servel.cl/partidos-politicos/partidos-constituidos/"
  - "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
  - "https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html"
  - "https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html"
  - "https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/"
  - "https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/"
tags:
  - entidad/partido
  - socialismo-democratico
  - caso-mop-gate
---

# Partido Socialista de Chile

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

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
| [Registro de Partidos Políticos Constituidos — Servicio Electoral de Chile](https://www.servel.cl/partidos-politicos/partidos-constituidos/) | Servel | `primaria` | 2024-01-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.servel.cl/partidos-politicos/partidos-constituidos/) |
| [Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas](https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html) | Emol | `secundaria` | 2016-06-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html) |
| [Caso MOP-Gate: ex ministro Carlos Cruz condenado a tres años de pena remitida](https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html) | Emol | `secundaria` | 2010-07-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html) |
| [Corte de Apelaciones ratificó condenas en el caso MOP-Gate](https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html) | Cooperativa | `secundaria` | 2014-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html) |
| [Fraude al fisco: el delito por el cual Jorge Quiroz fue condenado y luego absuelto por la Suprema](https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/) | El Mostrador | `secundaria` | 2026-06-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/) |
| [Libertad vigilada, millonaria multa y adiós a casa en La Reina: la condena al exalcalde de San Ramón](https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/) | El Mostrador | `secundaria` | 2025-07-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2025/07/04/libertad-vigilada-millonaria-multa-y-adios-a-casa-en-la-reina-la-condena-al-exalcalde-de-san-ramon/) |
