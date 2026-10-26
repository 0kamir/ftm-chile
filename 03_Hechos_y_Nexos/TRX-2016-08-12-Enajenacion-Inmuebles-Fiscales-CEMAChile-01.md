---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01"
fecha: 2016-08-12
tipo_nexo: desviacion_fondos
monto_clp: 0
monto_origen: sin_monto
metodo_adjudicacion: trato_directo
entidad_origen: "[[Fundacion CEMA Chile]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Lucia Hiriart Rodriguez]]"
firmante_destino: "[[Sergio Munoz Gajardo]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
causa_vinculada: "[[Caso CEMA Chile]]"
evidencia_soporte: "[[Disolucion-CDE-Fundacion-CEMAChile-2021]]"
historial_correcciones:
  - "2026-10-19: monto_clp $10.500.000.000 llevado a 0; la cifra no aparece en ninguna fuente verificable."
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html"
  - "https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/"
  - "https://www.theclinic.cl/2016/12/29/lo-que-declaro-lucia-hiriart-por-el-caso-cema-chile-por-mi-no-pasaba-ni-un-centavo/"
tags:
  - nexo/desviacion-fondos
  - caso-cema-chile
  - bienes-fiscales
---

# TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$10.500.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino / Restitución Judicial**: `= this.entidad_destino` (Poder Judicial y Consejo de Defensa del Estado en representación del Fisco de Chile)
- **Presidenta Vitalicia en Origen**: `= this.firmante_origen`
- **Magistrado / Instancia Judicial conexa**: `= this.firmante_destino` (y Ministro en Visita Guillermo de la Barra Dünner)
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Fraude al Fisco]] y distracción patrimonial de bienes públicos)
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho

> [!NOTE] Monto sin respaldo
> Las cifras en pesos mencionadas en esta nota no aparecen en ninguna fuente verificable y no se contabilizan en los totales del vault (antes: $10.500.000.000 CLP).

Apropiación estatutaria, venta comercial a terceros y posterior embargo y restitución forzosa al Fisco de Chile del patrimonio inmobiliario transferido gratuitamente por el Estado entre 1973 y 1990 a la [[Fundacion CEMA Chile]], presidida vitaliciamente por [[Lucia Hiriart Rodriguez]]. Tras las primeras pesquisas de desvíos de fondos de CEMA hacia la familia Pinochet detectadas por el ministro [[Sergio Munoz Gajardo]] en el [[Caso Riggs]], la reapertura judicial de 2016 en el [[Caso CEMA Chile]] investigó ventas inmobiliarias por más de `$8.900.000.000 CLP` y derivó en la disolución de la fundación vía CDE (2021) y el traspaso de sus bienes al Fisco y a fundaciones de beneficencia (según Emol, el Estado recuperó más de $18.000 millones; la cifra de $10.500 millones previa no tiene fuente) ([[Disolucion-CDE-Fundacion-CEMAChile-2021]]).

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Falleció Lucía Hiriart (menciona recuperación de bienes vía CDE)](https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html) | Emol | `secundaria` | 2021-12-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html) |
| [Caso CEMA Chile: querella por fraude al fisco](https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/) | The Clinic | `secundaria` | 2016-08-23 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/) |
| [Lo que declaró Lucía Hiriart por el caso CEMA Chile](https://www.theclinic.cl/2016/12/29/lo-que-declaro-lucia-hiriart-por-el-caso-cema-chile-por-mi-no-pasaba-ni-un-centavo/) | The Clinic | `secundaria` | 2016-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2016/12/29/lo-que-declaro-lucia-hiriart-por-el-caso-cema-chile-por-mi-no-pasaba-ni-un-centavo/) |
