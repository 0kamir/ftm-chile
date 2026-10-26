---
tipo_nodo: nexo_transaccion
fecha: 2022-11-15
tipo_nexo: coordinacion_mensajeria
monto_clp: 0
monto_origen: sin_monto
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Gabriel Zaliasnik Schilkrut]]"
causa_vinculada: "[[Caso Audios]]"
delito_imputado: "[[Trafico de Influencias]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
  - "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
  - "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
  - "https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/"
tags:
  - nexo/coordinacion
  - caso-audios
  - nombramientos-judiciales
  - trafico-influencias
---

# TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01

## Ficha de Arista Reificada (Coordinación Extraprocesal sobre Nombramientos y Gestiones Judiciales)
- **Fecha del Hito**: `= this.fecha` *(Noviembre de 2022 / Período 2022–2023)*
- **Tipo de Registro**: `= this.tipo_nexo` *(Intercambios de mensajería y consultas extrajudiciales periciadas en el teléfono de Hermosilla)*
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Nexo de influencia no monetizado directamente)*
- **Entidad / Ámbito de Origen**: `= this.entidad_origen`
- **Órgano Jurisdiccional de Destino**: `= this.entidad_destino`
- **Operador Emisor / Consultor**: `= this.firmante_origen`
- **Litigante Contraparte**: `= this.firmante_destino`
- **Causa Penal Vinculada**: `= this.causa_vinculada`
- **Delito Imputado en Indagatoria**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción del Nexo
En la arista judicial del [[Caso Audios]] investigada por la Fiscalía Regional de Valparaíso (Fiscal Claudia Perivancich), se indagan los intercambios de comunicaciones y testimonios relativos a la coordinación entre [[Luis Hermosilla Osorio]] y [[Gabriel Zaliasnik Schilkrut]]. 

En su declaración formal ante el Ministerio Público, Hermosilla reconoció que mantenía conversaciones habituales con Zaliasnik sobre los candidatos más idóneos para asumir cargos en las Cortes de Apelaciones y en la [[Corte Suprema de Chile]], destacando las redes de influencia de Zaliasnik en el máximo tribunal. Adicionalmente, los mensajes extraídos por la policía dieron cuenta de solicitudes de colaboración en tramitaciones de causas penales y medidas cautelares en favor de clientes del estudio de Zaliasnik, motivando la asignación formal de su calidad de imputado bajo hipótesis de [[Trafico de Influencias]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Cinco claves para comprender el caso Audios](https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) | Emol | `secundaria` | 2024-08-21 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) |
| [“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF](https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) | CIPER Chile | `secundaria` | 2023-11-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) |
| [Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho](https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) | El Dínamo | `secundaria` | 2024-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) |
| [Caso Audios: Luis Hermosilla será formalizado por la arista Parque Capital](https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) |
