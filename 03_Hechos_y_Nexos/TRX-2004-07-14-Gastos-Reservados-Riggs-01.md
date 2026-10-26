---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2004-07-14-Gastos-Reservados-Riggs-01"
fecha: 2004-07-14
tipo_nexo: desviacion_fondos
monto_clp: 15800000000
monto_origen: sentencia
metodo_adjudicacion: no_aplica
entidad_origen: "[[Comando de Apoyo a la Fuerza del Ejercito]]"
entidad_destino: "[[Riggs Bank y Sociedades Offshore Ashburton]]"
firmante_origen: "[[Augusto Pinochet Ugarte]]"
firmante_destino: "[[Oscar Aitken Lavanchy]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
causa_vinculada: "[[Caso Riggs]]"
evidencia_soporte: "[[Sentencia-Corte-Suprema-CasoRiggs-2018]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
tags:
  - nexo/desviacion-fondos
  - caso-riggs
  - gastos-reservados
  - offshore
---

# TRX-2004-07-14-Gastos-Reservados-Riggs-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha` (fecha de destape por el Senado de EE.UU.; flujos ejecutados entre 1981 y 2004)
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$15.800.000.000 CLP` (`= this.monto_clp` — equivalente a los **US$ 17,86 millones** de origen ilícito acreditados por el peritaje de la Universidad de Chile)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen` (Partidas de Gastos Reservados de la Comandancia en Jefe del Ejército y Casa Militar)
- **Entidad de Destino**: `= this.entidad_destino`
- **Ordenador del Desvío en Origen**: `= this.firmante_origen`
- **Estructurador / Albacea en Destino**: `= this.firmante_destino` (junto al Ministro Instructor [[Sergio Munoz Gajardo]] y la [[Corte Suprema de Chile]])
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]] y uso de pasaportes falsos)
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Sustracción y desvío sistemático de caudales públicos provenientes de las partidas de gastos reservados de la Comandancia en Jefe del Ejército ([[Comando de Apoyo a la Fuerza del Ejercito]]) y de la Presidencia de la República bajo el mando de [[Augusto Pinochet Ugarte]], canalizados a través de valijas diplomáticas, agregadurías militares y transferencias del Banco Riggs hacia más de **125 cuentas bancarias secretas**, depósitos a plazo y sociedades *offshore* (*Ashburton Company Ltd.*, *Althorp Investment Co.*) administradas con la intervención de [[Oscar Aitken Lavanchy]] bajo nombres falsos (*"Daniel López"*). El peritaje de la Universidad de Chile en el [[Caso Riggs]], instruido inicialmente por [[Sergio Munoz Gajardo]], determinó que **US$ 17,86 millones** (`$15.800.000.000 CLP`) carecían de justificación lícita, culminando en la condena por [[Malversacion de Caudales Publicos]] y el comiso definitivo ordenado por la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-CasoRiggs-2018]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
