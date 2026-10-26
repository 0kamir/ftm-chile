---
tipo_nodo: partido_politico
rut: ""
sigla: "RN"
fecha_fundacion: "1987-04-29"
coalicion: "Chile Vamos"
estado_registro: "Vigente"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html"
  - "https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html"
  - "https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html"
  - "https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz"
  - "https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/"
  - "https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/"
tags:
  - entidad/partido
  - chile-vamos
---

# Renovacion Nacional

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Rol en el Análisis de Redes
Partido político en el que militó históricamente el exalcalde de la [[Municipalidad de Vitacura]], [[Raul Torrealba del Pedregal]], hasta su renuncia tras la apertura del [[Caso Vitacura]].

Asimismo, en el marco del [[Caso Operaciones Digitales e Injerencia Electoral]], se documentó la presencia física del consultor digital [[Fernando Cerimedo]] en la sede central del partido durante la noche del 4 de septiembre de 2022 ([[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]), acreditada mediante la evidencia [[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]].

## Nexos y Operaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  delito_imputado AS "Delito / Infracción",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Militantes y Exmilitantes Registrados en el Vault
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
| [Falleció Claudio Spiniak, empresario condenado por liderar una red de pedofilia](https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) | Cooperativa | `secundaria` | 2026-03-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) |
| [Claudio Spiniak fue condenado a cinco años y un día de cárcel](https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) | Cooperativa | `secundaria` | 2006-08-10 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) |
| [Muere Claudio Spiniak](https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) | Emol | `secundaria` | 2026-03-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) |
| [Jovino Novoa, caso Spiniak e investigación del juez Sergio Muñoz](https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) | Pauta | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) |
| [El día que el 'rey de los trolls' llegó a la sede de RN](https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/) | The Clinic | `secundaria` | 2026-08-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/) |
| [Fiscalía Centro Norte abre investigación por presuntos delitos informáticos vinculados a Fernando Cerimedo](https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/) | CNN Chile | `secundaria` | 2026-09-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/) |
