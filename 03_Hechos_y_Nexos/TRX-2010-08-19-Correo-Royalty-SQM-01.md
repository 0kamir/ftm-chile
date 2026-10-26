---
tipo_nodo: nexo_transaccion
fecha: 2010-08-19
tipo_nexo: cohecho
monto_clp: 730000000
monto_origen: acusacion
entidad_origen: "[[SQM SA]]"
entidad_destino: "[[Union Democrata Independiente]]"
firmante_origen: "[[Patricio Contesse Gonzalez]]"
firmante_destino: "[[Pablo Longueira Montes]]"
causa_vinculada: "[[Caso SQM]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Querella-SII-Boletas-SQM-2015]]"
historial_correcciones:
  - "Absolución en primera instancia (22-10-2025); monto de $730 millones corresponde a la acusación."
estado_verificacion: parcial
fuentes:
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
  - "https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html"
tags:
  - nexo/transaccion
  - cohecho
  - caso-sqm
  - captura-regulatoria
---

# TRX-2010-08-19-Correo-Royalty-SQM-01

## Ficha de Arista Reificada (Captura Regulatoria y Pagos vía Boletas Ideológicamente Falsas)
- **Fecha del Hecho Clave**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado Consolidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad / Entorno Político de Destino**: `= this.entidad_destino`
- **Ejecutivo Origen**: `= this.firmante_origen`
- **Autoridad Receptora**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción de la Operación
Según la acusación de la Fiscalía, la gerencia general de [[SQM SA]] ([[Patricio Contesse Gonzalez]]) envió el 19 de agosto de 2010 al entonces senador [[Pablo Longueira Montes]] una minuta para modificar el régimen de invariabilidad tributaria del Royalty Minero, y la empresa habría canalizado pagos por aproximadamente **$730.000.000 CLP** entre 2009 y 2015 a personas de su entorno mediante boletas y facturas ([[Querella-SII-Boletas-SQM-2015]]).

**Resultado judicial:** el 3° TOP de Santiago absolvió a ambos el 22-10-2025 al no dar por acreditados los hechos; hay recursos de nulidad pendientes. Este nexo registra una hipótesis acusatoria no acreditada, no un hecho probado.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio](https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) | BioBioChile | `secundaria` | 2026-10-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
| [Fiscalía presenta recurso de nulidad contra fallo del caso SQM](https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) | Emol | `secundaria` | 2026-09-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) |
