---
tipo_nodo: nexo_transaccion
fecha: 2017-03-03
tipo_nexo: compensacion_reparatoria
monto_clp: 97500000000
monto_origen: resolucion_administrativa
entidad_origen: "[[Empresas CMPC SA]]"
entidad_destino: "[[Servicio Nacional del Consumidor]]"
firmante_origen: "[[Eliodoro Matte Larrain]]"
firmante_destino: "[[Gabriel Ruiz-Tagle Serrano]]"
causa_vinculada: "[[Caso Colusion del Papel Tissue]]"
delito_imputado: "[[Colusion y Atentado a la Libre Competencia]]"
evidencia_soporte: "[[Acuerdo-Compensatorio-SERNAC-CMPC-Tissue-2017]]"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html"
  - "https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html"
  - "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml"
tags:
  - nexo/transaccion
  - compensacion-historica
  - colusion-tissue
  - siete-lucas-confort
  - sernac
---

# TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01

## Ficha de Arista Reificada (Fondo Compensatorio Extrajudicial Masivo a Consumidores)
- **Fecha del Acuerdo**: `= this.fecha` *(Marzo de 2017; pago materializado en 2018)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto Reparatorio Histórico (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(US$ 150 millones / $97.500.000.000 CLP en restitución patrimonial)*
- **Entidad Pagadora**: `= this.entidad_origen`
- **Órgano Receptor Garante**: `= this.entidad_destino`
- **Líder Corporativo de la Matriz**: `= this.firmante_origen`
- **Controlador Histórico Competidor**: `= this.firmante_destino`
- **Causa Asociada**: `= this.causa_vinculada`
- **Delito / Infracción Subyacente**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción de la Operación
En marzo de 2017, tras las negociaciones en la mesa tripartita del Procedimiento Voluntario Colectivo conducido por el [[Servicio Nacional del Consumidor]] junto a las asociaciones de consumidores (Conadecus y Odecu), [[Empresas CMPC SA]] depositó en una cuenta fiduciaria de BancoEstado la suma de **`$97.500.000.000 CLP`** para resarcir el daño económico provocado por 13 años de colusión en productos de primera necesidad. El fondo financió el pago universal de **$7.000 CLP** a más de 13 millones de chilenos mayores de 18 años a partir de agosto de 2018.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Acuerdo por colusión tissue: CMPC pagará US$150 millones para compensar a consumidores](https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) | Emol | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) |
| [CMPC pagará compensación de 150 millones de dólares: por consumidor serán 7.000 pesos](https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) | Cooperativa | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) |
| [TDLC dicta sentencia en caso Tissue: multa a SCA y exime a CMPC](https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) | Emol | `secundaria` | 2017-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) |
| [Suprema condena a CMPC y SCA por colusión](https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) | Emol | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) |
| [CMPC tendrá que pagar una millonaria multa por la colusión del papel](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) | BioBioChile | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) |
