---
tipo_nodo: nexo_transaccion
fecha: 2022-10-19
tipo_nexo: convenio_directo
monto_clp: 170000000
monto_origen: resolucion_administrativa
entidad_origen: "[[Seremi MINVU Antofagasta]]"
entidad_destino: "[[Fundacion Democracia Viva]]"
firmante_origen: "[[Carlos Contreras Gutierrez]]"
firmante_destino: "[[Daniel Andrade Schwarze]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Resolucion-Exenta-MINVU-Antofagasta-2022]]"
tags:
  - nexo/transaccion
  - convenio-directo
  - caso-convenios
  - fraccionamiento-cgr
---

# TRX-2022-10-19-Convenio-DV-02

## Ficha de Arista Reificada (Transacción / Hecho — Convenio II de III)
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
**Segundo convenio de transferencia directa** ($170.000.000 CLP, equivalente a ~2.818 UTM de octubre de 2022) para intervención en el Campamento EcuaChilePe (Antofagasta), firmado apenas 16 días después de [[TRX-2022-10-03-Convenio-DV-01]] entre [[Carlos Contreras Gutierrez]] ([[Seremi MINVU Antofagasta]]) y [[Daniel Andrade Schwarze]] ([[Fundacion Democracia Viva]]).

Con esta segunda cuota, el monto acumulado transferido a la fundación alcanzó los **$370.000.000 CLP** (~6.135 UTM), superando en los hechos el umbral de 5.000 UTM de Toma de Razón de Contraloría mediante fraccionamiento administrativo respaldado en [[Resolucion-Exenta-MINVU-Antofagasta-2022]] e investigado en [[Caso Convenios]].
