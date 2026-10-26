---
tipo_nodo: nexo_transaccion
fecha: 2022-12-20
tipo_nexo: convenio_directo
monto_clp: 250635000
monto_origen: acusacion
entidad_origen: "[[GORE Biobio]]"
entidad_destino: "[[Fundacion En Ti]]"
firmante_origen: "[[Rodrigo Diaz Worner]]"
firmante_destino: "[[Camila Polizzi Fonceca]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-GORE-Biobio-EnTi-2022]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/"
  - "https://www.radioagricultura.cl/nacional/2023/08/07/caso-convenios-pdi-allana-gobierno-regional-del-biobio/"
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
  - "https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/"
  - "https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html"
  - "https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html"
tags:
  - nexo/transaccion
  - convenio-directo
  - caso-convenios
  - biobio
---

# TRX-2022-12-20-Convenio-EnTi-01

## Ficha de Arista Reificada (Transacción / Hecho)
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
Transferencia directa del [[GORE Biobio]] hacia la [[Fundacion En Ti]] por **$250.635.000 CLP** para un programa de mejoramiento barrial en el sector norte de Concepción. La investigación penal de la Fiscalía Regional del Biobío en el [[Caso Convenios]] sostiene que hubo desvío de fondos hacia sociedades instrumentales, gastos personales improcedentes y rendiciones con facturas ideológicamente falsas, en operaciones vinculadas a [[Camila Polizzi Fonceca]] y autorizadas bajo la administración de [[Rodrigo Diaz Worner]] mediante la [[Resolucion-GORE-Biobio-EnTi-2022]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Formalización de Camila Polizzi en Caso Convenios](https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) | CNN Chile | `secundaria` | 2023-11-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-camila-polizzi-convenios_20231129/) |
| [Caso Convenios: PDI allana Gobierno Regional del Biobío](https://www.radioagricultura.cl/nacional/2023/08/07/caso-convenios-pdi-allana-gobierno-regional-del-biobio/) | Radio Agricultura | `secundaria` | 2023-08-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.radioagricultura.cl/nacional/2023/08/07/caso-convenios-pdi-allana-gobierno-regional-del-biobio/) |
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
| [Formalización de Daniel Andrade y Carlos Contreras: delitos y convenios Minvu Antofagasta](https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) | CNN Chile | `secundaria` | 2023-12-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) |
| [Contraloría publica informe sobre Democracia Viva y faltas a la probidad](https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) | Emol | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) |
| [Alberto Larraín fue formalizado por la arista Biobío del caso ProCultura](https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) | Cooperativa | `secundaria` | 2026-08-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) |
