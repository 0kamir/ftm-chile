---
tipo_nodo: nexo_transaccion
fecha: 2023-06-22
tipo_nexo: cohecho
monto_clp: 100000000
monto_origen: acusacion
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Leonarda Villalobos Muth]]"
causa_vinculada: "[[Caso Audios]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
  - "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
  - "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
  - "https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/"
tags:
  - nexo/transaccion
  - cohecho
  - caso-audios
---

# TRX-2023-06-22-Reunion-Audios-01

## Ficha de Arista Reificada (Transacción / Hecho)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante / Operador de Origen**: `= this.firmante_origen`
- **Firmante / Operadora de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción de la Operación
Acuerdo y articulación financiera por un monto referencial de **$100.000.000 CLP** ("caja negra") presuntamente destinado, según la Fiscalía, al pago de sobornos a funcionarios públicos del [[Servicio Impuestos Internos]] y la CMF en beneficio de [[Factop SpA]]. El hecho quedó registrado en la grabación [[Audio-Reunion-Edificio-Alonso-2023]], en la que intervienen [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]], constituyendo la pieza probatoria basal del [[Caso Audios]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Cinco claves para comprender el caso Audios](https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) | Emol | `secundaria` | 2024-08-21 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) |
| [“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF](https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) | CIPER Chile | `secundaria` | 2023-11-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) |
| [Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho](https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) | El Dínamo | `secundaria` | 2024-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) |
| [Caso Audios: Luis Hermosilla será formalizado por la arista Parque Capital](https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) |
