---
tipo_nodo: nexo_transaccion
fecha: 2000-05-15
tipo_nexo: acuerdo_colusorio
monto_clp: 0
entidad_origen: "[[Empresas CMPC SA]]"
entidad_destino: "[[SCA Chile SA]]"
firmante_origen: "[[Eliodoro Matte Larrain]]"
firmante_destino: "[[Gabriel Ruiz-Tagle Serrano]]"
causa_vinculada: "[[Caso Colusion del Papel Tissue]]"
delito_imputado: "[[Colusion y Atentado a la Libre Competencia]]"
evidencia_soporte: "[[Sentencia-TDLC-160-Colusion-Tissue-2017]]"
tags:
  - nexo/colusion
  - cartel-confort
  - libre-competencia
  - cmpc
  - pisa
---

# TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01

## Ficha de Arista Reificada (Concertación Ilícita de Cuotas de Mercado y Fijación de Precios)
- **Fecha de Inicio del Cartel**: `= this.fecha` *(Mayo de 2000)*
- **Tipo de Operación**: `= this.tipo_nexo` *(Pacto clandestino celebrado en reuniones en el Club de Golf Las Brisas de Chicureo)*
- **Monto Imputado Directo (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Daño económico derivado del sobreprecio cartelizado por más de 10 años)*
- **Empresa Instigadora**: `= this.entidad_origen`
- **Empresa Competidora Concertada**: `= this.entidad_destino`
- **Líder Corporativo de Origen**: `= this.firmante_origen`
- **Controlador Competidor Receptor**: `= this.firmante_destino`
- **Causa Sancionatoria**: `= this.causa_vinculada`
- **Infracción Acreditada**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
A mediados del año 2000, los máximos ejecutivos de [[Empresas CMPC SA]] (CMPC Tissue) y el fundador y controlador de PISA ([[SCA Chile SA]]), [[Gabriel Ruiz-Tagle Serrano]], acordaron poner fin a una guerra comercial de precios y dividirse artificialmente el mercado del papel higiénico y servilletas en Chile, congelando cuotas del 76% para CMPC y 24% para PISA. Para operar el cartel crearon cuentas de correo electrónico secretas con nombres falsos y teléfonos de prepago desechables, práctica que se extendió de manera ininterrumpida hasta fines de 2013, siendo sancionada por el TDLC ([[Sentencia-TDLC-160-Colusion-Tissue-2017]]) y la Corte Suprema ([[Sentencia-Corte-Suprema-Colusion-PapelTissue-2020]]).
