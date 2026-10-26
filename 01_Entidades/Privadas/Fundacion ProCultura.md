---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Fundación ProCultura"
fecha_constitucion: "2010-03-18"
objeto_social: "Promoción cultural, patrimonio, identidad territorial y proyectos comunitarios"
representante_legal: "[[Alberto Larrain Salas]]"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml"
  - "https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/"
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
  - "https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/"
  - "https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html"
  - "https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/"
tags:
  - entidad/privada
  - fundacion
  - caso-convenios
  - nodo-puente
---

# Fundacion ProCultura

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Director Ejecutivo**: `= this.representante_legal`

## Rol Topológico en la Red (Nodo Puente Multirregional)
En la arquitectura del grafo del [[Caso Convenios]], **Fundación ProCultura** opera como un **nodo puente de alta centralidad de intermediación (*Betweenness Centrality*)**: conecta simultáneamente a la [[Seremi MINVU Antofagasta]] (vía [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] por **$500.000.000 CLP**) y al [[GORE Biobio]] (vía [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] por **$2.553.000.000 CLP**), articulando en una misma red a autoridades de distintas regiones bajo la representación de [[Alberto Larrain Salas]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_origen AS "Autorizador Público",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Democracia Viva: contratos evitaron revisión de Contraloría al ser pagados de forma parcializada](https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) | BioBioChile | `secundaria` | 2023-06-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) |
| [Tras informe sobre Democracia Viva, contralor afirma que hubo corrupción](https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) | La Tercera | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) |
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
| [Formalización de Daniel Andrade y Carlos Contreras: delitos y convenios Minvu Antofagasta](https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) | CNN Chile | `secundaria` | 2023-12-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) |
| [Contraloría publica informe sobre Democracia Viva y faltas a la probidad](https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) | Emol | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) |
| [Formalización de Camila Polizzi (Fundación En Ti) en Caso Convenios](https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) | CNN Chile | `secundaria` | 2023-11-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) |
