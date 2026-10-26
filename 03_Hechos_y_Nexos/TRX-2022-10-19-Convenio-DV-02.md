---
tipo_nodo: nexo_transaccion
fecha: 2022-10-19
tipo_nexo: convenio_directo
monto_clp: 170000000
monto_origen: resolucion_administrativa
entidad_origen: "[[Seremi MINVU Antofagasta]]"
entidad_destino: "[[Fundacion Democracia Viva]]"
firmante_origen: "[[Carlos Contreras Gutierrez]]"
firmante_destino: "[[Daniel Andrade Schwarze]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-Exenta-MINVU-Antofagasta-2022]]"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml"
  - "https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/"
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
  - "https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/"
  - "https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html"
  - "https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/"
  - "https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html"
tags:
  - nexo/transaccion
  - convenio-directo
  - caso-convenios
  - fraccionamiento-cgr
---

# TRX-2022-10-19-Convenio-DV-02

## Ficha de Arista Reificada (Transacción / Hecho — Convenio II de III)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante de Origen**: `= this.firmante_origen`
- **Firmante de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción de la Operación
**Segundo convenio de transferencia directa** ($170.000.000 CLP, equivalente a ~2.818 UTM de octubre de 2022) para intervención en el Campamento EcuaChilePe (Antofagasta), firmado apenas 16 días después de [[TRX-2022-10-03-Convenio-DV-01]] entre [[Carlos Contreras Gutierrez]] ([[Seremi MINVU Antofagasta]]) y [[Daniel Andrade Schwarze]] ([[Fundacion Democracia Viva]]).

Con esta segunda cuota, el monto acumulado transferido a la fundación alcanzó los **$370.000.000 CLP** (~6.135 UTM), superando en los hechos el umbral de 5.000 UTM de Toma de Razón de Contraloría mediante fraccionamiento administrativo respaldado en [[Resolucion-Exenta-MINVU-Antofagasta-2022]] e investigado en [[Caso Convenios]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Democracia Viva: contratos evitaron revisión de Contraloría al ser pagados de forma parcializada](https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) | BioBioChile | `secundaria` | 2023-06-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) |
| [Tras informe sobre Democracia Viva, contralor afirma que hubo corrupción](https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) | La Tercera | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) |
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
| [Formalización de Daniel Andrade y Carlos Contreras: delitos y convenios Minvu Antofagasta](https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) | CNN Chile | `secundaria` | 2023-12-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) |
| [Contraloría publica informe sobre Democracia Viva y faltas a la probidad](https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) | Emol | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) |
| [Formalización de Camila Polizzi (Fundación En Ti) en Caso Convenios](https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) | CNN Chile | `secundaria` | 2023-11-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) |
| [Alberto Larraín fue formalizado por la arista Biobío del caso ProCultura](https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) | Cooperativa | `secundaria` | 2026-08-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) |
