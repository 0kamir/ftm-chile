---
tipo_nodo: nexo_transaccion
fecha: 2022-12-20
tipo_nexo: convenio_directo
monto_clp: 250635000
entidad_origen: "[[GORE Biobio]]"
entidad_destino: "[[Fundacion En Ti]]"
firmante_origen: "[[Rodrigo Diaz Worner]]"
firmante_destino: "[[Camila Polizzi Fonceca]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-GORE-Biobio-EnTi-2022]]"
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

## Descripción Forense de la Operación
Transferencia directa del [[GORE Biobio]] hacia la [[Fundacion En Ti]] por **$250.635.000 CLP** para un programa de mejoramiento barrial en el sector norte de Concepción. La investigación penal de la Fiscalía Regional del Biobío en el [[Caso Convenios]] acreditó el desvío de fondos hacia sociedades instrumentales, gastos personales improcedentes y rendiciones con facturas ideológicamente falsas, en operaciones vinculadas a [[Camila Polizzi Fonceca]] y autorizadas bajo la administración de [[Rodrigo Diaz Worner]] mediante la [[Resolucion-GORE-Biobio-EnTi-2022]].
