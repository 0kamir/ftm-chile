---
tipo_nodo: partido_politico
rut: ""
sigla: "UDI"
fecha_fundacion: "1983-09-24"
coalicion: "Chile Vamos"
estado_registro: "Vigente"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
  - "https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html"
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
tags:
  - entidad/partido
  - chile-vamos
---

# Union Democrata Independiente

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Contexto en Investigaciones y Registro OSINT
Colectividad fundada en 1983 cuyos dirigentes históricos ("coroneles") y parlamentarios aparecen vinculados en múltiples causas estructurales de la bóveda: financiamiento ilegal de campañas en el [[Caso Penta]] ([[TRX-2013-07-15-Boletas-Penta-UDI-01]] y [[TRX-2013-09-20-Boletas-Penta-Novoa-01]]), la acusación por cohecho en el [[Caso SQM]] contra [[Pablo Longueira Montes]] (absuelto en 2025, con recursos de nulidad pendientes) y el [[Caso Corpesca]] ([[Jaime Orpis Bouchon]]), y red de protección parlamentaria en el [[Caso Colonia Dignidad]] ([[Hernan Larrain Fernandez]], [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]]). Asimismo, en el registro hemerográfico sobre la interna partidaria, consta la entrevista televisiva de agosto de 2017 de la excandidata a diputada UDI [[Loreto Letelier]] (*"Con las Manos en la Masa"*, Vía X), quien al recordar su etapa en la Juventud UDI describió las celebraciones en los *"retiros espirituales"* del partido en **Punta de Tralca**, donde dirigentes como [[Jovino Novoa Vasquez]] y Juan Antonio Coloma terminaban *"bailando arriba de las mesas"* con las corbatas en la cabeza, antes de ser pasada al Tribunal Supremo y marginada de la colectividad en septiembre de 2017.

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
| [Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad](https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) | El Mostrador | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) |
| [Seis ex jerarcas de Colonia Dignidad fueron condenados a prisión por la Corte Suprema](https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) | Cooperativa | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio](https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) | BioBioChile | `secundaria` | 2026-10-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
