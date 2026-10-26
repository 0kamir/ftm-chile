---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía Regional de Antofagasta / Juzgado de Garantía de Antofagasta"
fiscal_a_cargo: "Juan Castro Bekios / Cristian Aguilar"
estado_judicial: formalizada
delito_principal: "[[Fraude al Fisco]]"
historial_correcciones:
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
  - "https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/"
  - "https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html"
  - "https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/"
  - "https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html"
tags:
  - causa
  - caso-convenios
  - antofagasta
---

# Caso Convenios (Arista Democracia Viva)

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal`

## Resumen Ejecutivo
Investigación penal iniciada de oficio en junio de 2023 por la Fiscalía Regional de Antofagasta a raíz de la suscripción de tres convenios por trato directo entre la [[Seremi MINVU Antofagasta]] (encabezada por [[Carlos Contreras Gutierrez]]) y la [[Fundacion Democracia Viva]] (presidida por [[Daniel Andrade Schwarze]]), ambos militantes del partido [[Revolucion Democratica]].

El monto total transferido bajo el Programa de Asentamientos Precarios alcanzó los **$426.000.000 CLP**, fraccionados en tres resoluciones exentas para eludir el trámite de Toma de Razón ante la Contraloría General de la República. El Consejo de Defensa del Estado (CDE) presentó querella criminal por el delito de fraude al fisco reiterado.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Firmante Origen",
  firmante_destino AS "Firmante Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Entidades e Imputados Clave en la Arista
- **Órgano Público Emisor**: [[Seremi MINVU Antofagasta]]
- **Entidad Privada Receptora**: [[Fundacion Democracia Viva]]
- **Partido Político Relacionado**: [[Revolucion Democratica]]
- **Funcionarios / Particulares Formalizados**:
  - [[Carlos Contreras Gutierrez]] (Ex Seremi MINVU Antofagasta)
  - [[Daniel Andrade Schwarze]] (Representante Legal de Democracia Viva)
- **Evidencia Documental Base**: [[Resolucion-Exenta-MINVU-Antofagasta-2022]]

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
| [Formalización de Daniel Andrade y Carlos Contreras: delitos y convenios Minvu Antofagasta](https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) | CNN Chile | `secundaria` | 2023-12-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) |
| [Contraloría publica informe sobre Democracia Viva y faltas a la probidad](https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) | Emol | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) |
| [Formalización de Camila Polizzi (Fundación En Ti) en Caso Convenios](https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) | CNN Chile | `secundaria` | 2023-11-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) |
| [Alberto Larraín fue formalizado por la arista Biobío del caso ProCultura](https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) | Cooperativa | `secundaria` | 2026-08-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) |
