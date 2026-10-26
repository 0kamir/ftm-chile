---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2009-11-18-Facturas-Bancard-SQM-2009-01"
fecha: 2009-11-18
tipo_nexo: factura_falsa
monto_clp: 340000000
monto_origen: acusacion
metodo_adjudicacion: no_aplica
entidad_origen: "[[SQM SA]]"
entidad_destino: "[[Bancard Inversiones Ltda]]"
firmante_origen: "[[Patricio Contesse Gonzalez]]"
firmante_destino: "[[Santiago Valdes Gutierrez]]"
delito_imputado: "[[Delito Tributario]]"
causa_vinculada: "[[Caso SQM]]"
evidencia_soporte: "[[Querella-SII-Boletas-SQM-2015]]"
historial_correcciones:
  - "Hecho no adjudicado: investigación cerrada por prescripción (2019)."
estado_verificacion: parcial
fuentes:
  - "https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/"
  - "https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
  - "https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
tags:
  - nexo/factura-falsa
  - caso-sqm
  - financiamiento-politico
  - bancard
---

# TRX-2009-11-18-Facturas-Bancard-SQM-2009-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$340.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen (Pagadora)**: `= this.entidad_origen`
- **Entidad de Destino (Emisora)**: `= this.entidad_destino` (y empresas proveedoras de campaña como *Vox Populi* / *Administradora Bancorp*)
- **Ejecutivo Autorizador en Origen**: `= this.firmante_origen`
- **Ejecutivo / Administrador Electoral en Destino**: `= this.firmante_destino` (en beneficio de la campaña presidencial de [[Sebastian Pinera Echenique]] y [[Renovacion Nacional]])
- **Delito Imputado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Pago de [[SQM SA]] a Bancorp, sociedad del grupo [[Bancard Inversiones Ltda]], por **$340.000.000 CLP** mediante 16 facturas (2009-2010) que la Fiscalía presumió ideológicamente falsas por no existir servicios que las justificaran. En 2015 SQM rectificó esos pagos ante el [[Servicio Impuestos Internos]]. [[Santiago Valdes Gutierrez]] sostuvo que la asesoría sí se prestó. En 2019 la Corte de Apelaciones sobreseyó a [[Santiago Valdes Gutierrez]] por prescripción (habían transcurrido más de cinco años desde los hechos al abrirse la investigación); no existe sentencia que declare falsas las facturas. Rige la presunción de inocencia.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Fiscalía reconstruye los pasos de Manuel Guerra: así se selló la salida del administrador electoral de Piñera del caso Penta](https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) | CIPER Chile | `secundaria` | 2024-11-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) |
| [Facturas de SQM aterrizan en campaña de Piñera: pagos de 2009 suman $103 millones](https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) | The Clinic | `secundaria` | 2017-09-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
| [Fiscalía presenta recurso de nulidad contra fallo del caso SQM](https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) | Emol | `secundaria` | 2026-09-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) |
| [Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio](https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) | BioBioChile | `secundaria` | 2026-10-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) |
