---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2023-08-25-Reporte-ROS-Factop-UAF-01"
fecha: 2023-08-25
tipo_nexo: factura_falsa
monto_clp: 0
monto_origen: sin_monto
metodo_adjudicacion: no_aplica
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Unidad de Analisis Financiero]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Javier Cruz Tamburrino]]"
delito_imputado: "[[Lavado de Activos]]"
causa_vinculada: "[[Caso Audios]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
historial_correcciones:
  - "2026-10-19: monto_clp $480.000.000 llevado a 0; la cifra no aparece en ninguna fuente verificable."
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
  - "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
  - "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
  - "https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/"
tags:
  - nexo/lavado-activos
  - ros-uaf
  - caso-audios
---

# TRX-2023-08-25-Reporte-ROS-Factop-UAF-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$480.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad Emisora (Origen)**: `= this.entidad_origen`
- **Órgano de Inteligencia Financiera (Destino)**: `= this.entidad_destino`
- **Operador Imputado**: `= this.firmante_origen`
- **Circuito de Trazabilidad UAF**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho

> [!NOTE] Monto sin respaldo
> Las cifras en pesos mencionadas en esta nota no aparecen en ninguna fuente verificable y no se contabilizan en los totales del vault (antes: $480.000.000 CLP).

Operaciones de descuento de facturas ideológicamente falsas y triangulación bancaria ejecutadas a través de [[Factop SpA]] en el circuito de [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] por `$480.000.000 CLP`, cuyos flujos activaron reportes de inteligencia patrimonial ante la [[Unidad de Analisis Financiero]] y la [[Comision para el Mercado Financiero]] en el [[Caso Audios]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Cinco claves para comprender el caso Audios](https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) | Emol | `secundaria` | 2024-08-21 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) |
| [“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF](https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) | CIPER Chile | `secundaria` | 2023-11-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) |
| [Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho](https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) | El Dínamo | `secundaria` | 2024-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) |
| [Caso Audios: Luis Hermosilla será formalizado por la arista Parque Capital](https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) |
