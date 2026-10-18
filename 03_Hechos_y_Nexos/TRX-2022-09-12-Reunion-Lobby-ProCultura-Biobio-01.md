---
tipo_nodo: nexo_transaccion
fecha: 2022-09-12
tipo_nexo: reunion_lobby
monto_clp: 0
entidad_origen: "[[Fundacion ProCultura]]"
entidad_destino: "[[GORE Biobio]]"
firmante_origen: "[[Alberto Larrain Salas]]"
firmante_destino: "[[Rodrigo Diaz Worner]]"
causa_vinculada: "[[Caso Convenios]]"
delito_imputado: "[[Trafico de Influencias]]"
evidencia_soporte: "[[Registro-Audiencia-InfoLobby-Biobio-2022]]"
tags:
  - nexo/transaccion
  - reunion-lobby
  - caso-convenios
  - ley-del-lobby
---

# TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01

## Ficha de Arista Reificada (Audiencia Ley N° 20.730 / Reunión Pre-Adjudicación)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Audiencia previa sin traspaso monetario en el acto)*
- **Entidad Solicitante (Origen)**: `= this.entidad_origen`
- **Entidad Pública (Destino)**: `= this.entidad_destino`
- **Sujeto Activo de Lobby**: `= this.firmante_origen`
- **Sujeto Pasivo (Autoridad)**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito / Hipótesis Investigada**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Reunión y gestión previa celebrada el 12 de septiembre de 2022 entre el director ejecutivo de [[Fundacion ProCultura]], [[Alberto Larrain Salas]], y el Gobernador Regional del [[GORE Biobio]], [[Rodrigo Diaz Worner]], documentada en [[Registro-Audiencia-InfoLobby-Biobio-2022]].

Exactamente **67 días después** de esta reunión (el 18 de noviembre de 2022), el [[GORE Biobio]] adjudicó por trato directo el convenio [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] por **$2.553.000.000 CLP** a favor de [[Fundacion ProCultura]], activando la alerta forense de **Lobby Pre-Adjudicación (`< 90 días`)**.
