---
tipo_nodo: partido_politico
rut: ""
sigla: "RD"
fecha_fundacion: "2012-01-07"
coalicion: "Frente Amplio"
estado_registro: "Fusionado en Partido Frente Amplio (2024)"
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
  - "https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/"
  - "https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html"
  - "https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/"
  - "https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml"
tags:
  - entidad/partido
  - frente-amplio
---

# Revolucion Democratica

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Rol en el Análisis de Redes (Caso Convenios)
Partido político al cual pertenecían tanto el autorizador público [[Carlos Contreras Gutierrez]] (ex jefe de gabinete parlamentario y ex titular de la [[Seremi MINVU Antofagasta]]) como el receptor privado [[Daniel Andrade Schwarze]] (presidente de la [[Fundacion Democracia Viva]]). Tras el estallido del [[Caso Convenios]], el Tribunal Supremo de la colectividad cursó la expulsión de ambos militantes.

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
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
| [Formalización de Daniel Andrade y Carlos Contreras: delitos y convenios Minvu Antofagasta](https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) | CNN Chile | `secundaria` | 2023-12-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) |
| [Contraloría publica informe sobre Democracia Viva y faltas a la probidad](https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) | Emol | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) |
| [Formalización de Camila Polizzi (Fundación En Ti) en Caso Convenios](https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) | CNN Chile | `secundaria` | 2023-11-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) |
| [Alberto Larraín fue formalizado por la arista Biobío del caso ProCultura](https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) | Cooperativa | `secundaria` | 2026-08-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) |
| [Caso Democracia Viva: contratos evitaron revisión de Contraloría al ser pagados de forma parcializada](https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) | BioBioChile | `secundaria` | 2023-06-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) |
