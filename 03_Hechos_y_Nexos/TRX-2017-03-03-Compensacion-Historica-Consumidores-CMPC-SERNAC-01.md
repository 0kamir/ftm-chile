---
tipo_nodo: nexo_transaccion
fecha: 2017-03-03
tipo_nexo: compensacion_reparatoria
monto_clp: 97500000000
entidad_origen: "[[Empresas CMPC SA]]"
entidad_destino: "[[Servicio Nacional del Consumidor]]"
firmante_origen: "[[Eliodoro Matte Larrain]]"
firmante_destino: "[[Gabriel Ruiz-Tagle Serrano]]"
causa_vinculada: "[[Caso Colusion del Papel Tissue]]"
delito_imputado: "[[Colusion y Atentado a la Libre Competencia]]"
evidencia_soporte: "[[Acuerdo-Compensatorio-SERNAC-CMPC-Tissue-2017]]"
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

## Descripción Forense de la Operación
En marzo de 2017, tras las negociaciones en la mesa tripartita del Procedimiento Voluntario Colectivo conducido por el [[Servicio Nacional del Consumidor]] junto a las asociaciones de consumidores (Conadecus y Odecu), [[Empresas CMPC SA]] depositó en una cuenta fiduciaria de BancoEstado la suma de **`$97.500.000.000 CLP`** para resarcir el daño económico provocado por 13 años de colusión en productos de primera necesidad. El fondo financió el pago universal de **$7.000 CLP** a más de 13 millones de chilenos mayores de 18 años a partir de agosto de 2018.
