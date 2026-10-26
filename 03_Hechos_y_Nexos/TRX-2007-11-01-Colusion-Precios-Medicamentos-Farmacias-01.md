---
tipo_nodo: nexo_transaccion
fecha: 2007-11-01
tipo_nexo: acuerdo_colusorio
monto_clp: 0
monto_origen: sin_monto
entidad_origen: "[[Farmacias Salcobrand SA]]"
entidad_destino: "[[Farmacias Cruz Verde SA]]"
firmante_origen: "[[Roberto Belloni Pechini]]"
firmante_destino: "[[Guillermo Harding Alvarado]]"
causa_vinculada: "[[Caso Colusion de las Farmacias]]"
delito_imputado: "[[Colusion y Atentado a la Libre Competencia]]"
evidencia_soporte: "[[Sentencia-TDLC-119-Colusion-Farmacias-2012]]"
estado_verificacion: verificado
fuentes:
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
tags:
  - nexo/colusion
  - colusion-farmacias
  - cartel-medicamentos
  - libre-competencia
---

# TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01

## Ficha de Arista Reificada (Concertación Ilícita de Precios en 222 Medicamentos Críticos)
- **Fecha de Inicio de la Coordinación**: `= this.fecha` *(Noviembre de 2007; ejecución entre diciembre 2007 y marzo 2008)*
- **Tipo de Operación**: `= this.tipo_nexo` *(Mecanismo de alzas de precios concertadas y trianguladas con laboratorios proveedores)*
- **Monto Imputado Directo (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Perjuicio patrimonial masivo derivado de sobreprecios en salud básica)*
- **Cadena Coordinadora de Origen**: `= this.entidad_origen`
- **Cadena Concertada de Destino**: `= this.entidad_destino`
- **Operador Comercial de Origen**: `= this.firmante_origen`
- **Controlador Competidor Concertado**: `= this.firmante_destino`
- **Causa Sancionatoria**: `= this.causa_vinculada`
- **Infracción Acreditada**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Entre diciembre de 2007 y marzo de 2008, las gerencias comerciales de [[Farmacias Salcobrand SA]] (bajo el mando de [[Roberto Belloni Pechini]]), [[Farmacias Cruz Verde SA]] (controlada por [[Guillermo Harding Alvarado]]) y [[Farmacias Ahumada SA]] (controlada por [[Jose Codner Chijner]]) ejecutaron un esquema concertado para elevar de forma artificial y simultánea los precios al consumidor de 222 medicamentos esenciales para tratamientos crónicos. El cartel operó contactando a los laboratorios farmacéuticos para que actuaran como supervisores del cumplimiento de las listas de precios infladas, amenazando con paralizar compras a los laboratorios que vendieran a precios inferiores a alguna de las cadenas.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Sentencia TDLC N° 119/2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-01-31 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
