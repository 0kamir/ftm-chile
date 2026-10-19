---
tipo_nodo: nexo_transaccion
fecha: 2020-12-15
tipo_nexo: transferencia
monto_clp: 30972000000
monto_origen: resolucion_administrativa
entidad_origen: "[[Municipalidad de Maipu]]"
entidad_destino: "[[Municipalidad de Maipu]]"
firmante_origen: "[[Cathy Barriga Guerra]]"
firmante_destino: "[[Cathy Barriga Guerra]]"
causa_vinculada: "[[Caso Municipalidad de Maipu]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Informe-Contraloria-Municipalidad-Maipu-2021]]"
tags:
  - nexo/transaccion
  - fraude-municipal
  - caso-maipu
---

# TRX-2020-12-15-Deficit-Maipu-Certificados-01

## Ficha de Arista Reificada (Defraudación Presupuestaria y Certificados Ideológicamente Falsos)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad Afectada**: `= this.entidad_destino`
- **Autoridad Imputada**: `= this.firmante_origen`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Déficit presupuestario, que la Fiscalía imputa como fraude al fisco, en la [[Municipalidad de Maipu]] bajo la administración de [[Cathy Barriga Guerra]] por **$30.972.000.000 CLP**, atribuido por la acusación a la emisión de Certificados de Disponibilidad Presupuestaria (CDP) sin respaldo contable, ocultamiento de pasivos devengados y desvío de fondos de uso exclusivo (como recursos de la sanitaria municipal SMAPA), según consta en el [[Informe-Contraloria-Municipalidad-Maipu-2021]] y la formalización del [[Caso Municipalidad de Maipu]].
