---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01"
fecha: 2005-08-10
tipo_nexo: desviacion_fondos
monto_clp: 2450000000
monto_origen: acusacion
metodo_adjudicacion: no_aplica
entidad_origen: "[[Riggs Bank y Sociedades Offshore Ashburton]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Lucia Hiriart Rodriguez]]"
firmante_destino: "[[Sergio Munoz Gajardo]]"
delito_imputado: "[[Delito Tributario]]"
causa_vinculada: "[[Caso Riggs]]"
evidencia_soporte: "[[Sentencia-Corte-Suprema-CasoRiggs-2018]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
tags:
  - nexo/desviacion-fondos
  - caso-riggs
  - evasion-tributaria
---

# TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$2.450.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino / Querellante Fiscal**: `= this.entidad_destino`
- **Sujetos Procesados en Origen**: `= this.firmante_origen` (junto a [[Augusto Pinochet Ugarte]], [[Augusto Pinochet Hiriart]] y [[Oscar Aitken Lavanchy]])
- **Magistrado Instructor en Destino**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (artículo 97 N° 4 del Código Tributario — declaraciones maliciosamente incompletas o falsas)
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Auditoría tributaria y querellas criminales deducidas por el [[Servicio Impuestos Internos]] en el marco del [[Caso Riggs]] tras comprobarse la omisión maliciosa de rentas, intereses financieros e incrementos de patrimonio no declarados en las cuentas secretas y sociedades *offshore* de [[Riggs Bank y Sociedades Offshore Ashburton]] por un perjuicio fiscal tributario estimado en **$2.450.000.000 CLP**. A partir de estas querellas, el 10 de agosto de 2005 el Ministro en Visita [[Sergio Munoz Gajardo]] sometió a proceso y ordenó la detención de [[Lucia Hiriart Rodriguez]] y su hijo Marco Antonio Pinochet como cómplices de fraude tributario, sumándose a los procesamientos contra [[Augusto Pinochet Ugarte]], [[Augusto Pinochet Hiriart]] y [[Oscar Aitken Lavanchy]] ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
