---
tipo_nodo: nexo_transaccion
fecha: 2019-05-14
tipo_nexo: cohecho
monto_clp: 3200000000
entidad_origen: "[[Itelecom Holding Chile SpA]]"
entidad_destino: "[[Municipalidad de Chillan]]"
firmante_origen: "[[Leon Marcelo Lefort Hernandez]]"
firmante_destino: "[[Marcelo Campos Henriquez]]"
causa_vinculada: "[[Caso Luminarias LED]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Sentencia-TOP-Chillan-Luminarias-2023]]"
tags:
  - nexo/transaccion
  - cohecho
  - caso-luminarias-led
---

# TRX-2019-05-14-Soborno-Luminarias-Chillan-01

## Ficha de Arista Reificada (Licitación Municipal Manipulada por Soborno)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto del Contrato Adjudicado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Empresa Oferente / Sobornante**: `= this.entidad_origen`
- **Municipio Licitante**: `= this.entidad_destino`
- **Controlador Privado**: `= this.firmante_origen`
- **Directivo Municipal Receptor**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Condenado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]])
- **Evidencia / Sentencia Firme**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Adjudicación fraudulenta de la licitación pública de recambio de luminarias a tecnología LED en la [[Municipalidad de Chillan]] por **$3.200.000.000 CLP** a favor de [[Itelecom Holding Chile SpA]] ([[Leon Marcelo Lefort Hernandez]]), obtenida mediante el pago de sobornos a [[Marcelo Campos Henriquez]] (integrante de la comisión evaluadora y administrador municipal), sancionada penalmente en [[Sentencia-TOP-Chillan-Luminarias-2023]] dentro del [[Caso Luminarias LED]].
