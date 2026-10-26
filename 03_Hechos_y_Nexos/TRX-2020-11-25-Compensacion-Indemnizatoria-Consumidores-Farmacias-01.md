---
tipo_nodo: nexo_transaccion
fecha: 2020-11-25
tipo_nexo: compensacion_reparatoria
monto_clp: 2180000000
monto_origen: sentencia
entidad_origen: "[[Farmacias Salcobrand SA]]"
entidad_destino: "[[Servicio Nacional del Consumidor]]"
firmante_origen: "[[Roberto Belloni Pechini]]"
firmante_destino: "[[Jose Codner Chijner]]"
causa_vinculada: "[[Caso Colusion de las Farmacias]]"
delito_imputado: "[[Colusion y Atentado a la Libre Competencia]]"
evidencia_soporte: "[[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]"
estado_verificacion: verificado
fuentes:
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
tags:
  - nexo/transaccion
  - compensacion-consumidores
  - colusion-farmacias
  - sernac
---

# TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01

## Ficha de Arista Reificada (Indemnización Judicial Civil Masiva por Sobreprecios en Medicamentos)
- **Fecha de Liquidación**: `= this.fecha` *(Noviembre de 2020)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto Reparatorio Liquidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Más de $2.180.000.000 CLP fijados en sentencia civil por demanda colectiva del SERNAC)*
- **Cadena Obligada al Pago**: `= this.entidad_origen`
- **Órgano Receptor Garante**: `= this.entidad_destino`
- **Ejecutivo Responsable**: `= this.firmante_origen`
- **Controlador Farmacéutico Histórico**: `= this.firmante_destino`
- **Causa Asociada**: `= this.causa_vinculada`
- **Delito / Infracción Subyacente**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción de la Operación
En el marco de la demanda colectiva interpuesta por el [[Servicio Nacional del Consumidor]] (SERNAC) y las asociaciones de consumidores contra las cadenas coludidas, el 10° Juzgado Civil de Santiago y la Corte de Apelaciones ordenaron a [[Farmacias Salcobrand SA]] y [[Farmacias Cruz Verde SA]] pagar una indemnización compensatoria superior a **`$2.180.000.000 CLP`** destinada a resarcir a los miles de pacientes afectados por el sobreprecio ilícito en los 222 medicamentos del cartel farmacéutico.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Fallo Corte Suprema Rol 2578-2012 (caso Farmacias)](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema rechaza reclamo de farmacias sobre multas](https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) | The Clinic | `secundaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
