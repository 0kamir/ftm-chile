---
tipo_nodo: partido_politico
rut: ""
sigla: "PC"
fecha_fundacion: "1912-06-04"
coalicion: "Apruebo Dignidad / Unidad por Chile"
estado_registro: "Vigente"
estado_verificacion: verificado
fuentes:
  - "https://www.servel.cl/partidos-politicos/partidos-constituidos/"
  - "https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/"
  - "https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml"
  - "https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html"
  - "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
  - "https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/"
tags:
  - entidad/partido
  - apruebo-dignidad
  - caso-sierra-bella
---

# Partido Comunista de Chile

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
| [Compra de clínica Sierra Bella: Fiscalía pide documentos](https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) | CIPER Chile | `secundaria` | 2023-03-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/) |
| [Contraloría objeta polémica compra de clínica Sierra Bella](https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) | BioBioChile | `secundaria` | 2023-04-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml) |
| [Cronología de la compra de Sierra Bella](https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) | Emol | `secundaria` | 2023-04-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html) |
| [Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella](https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) | 24 Horas | `secundaria` | 2025-05-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella) |
| [Sierra Bella: ningún querellante pidió reapertura y se cierra el telón del caso para Irací Hassler](https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/) |
