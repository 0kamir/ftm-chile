---
tipo_nodo: nexo_transaccion
fecha: 2011-06-09
tipo_nexo: transferencia
monto_clp: 68634000000
monto_origen: sentencia
entidad_origen: "[[Empresas La Polar SA]]"
entidad_destino: "[[Comision para el Mercado Financiero]]"
firmante_origen: "[[Pablo Alcalde Saavedra]]"
firmante_destino: "[[Julian Moreno de Pablo]]"
causa_vinculada: "[[Caso La Polar]]"
delito_imputado: "[[Lavado de Activos]]"
evidencia_soporte: "[[Sentencia-Condenatoria-y-Fallo-CS-LaPolar-2015]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales"
  - "https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf"
  - "https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/"
tags:
  - nexo/transaccion
  - caso-la-polar
  - mercado-de-valores
---

# TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01

## Ficha de Arista Reificada (Transacción / Hecho)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Acreditado por Sentencia (CLP)**: `$68.634.000.000 CLP` (equivalente a las **2.575.388 UF** de perjuicio acreditado y ratificado en condena solidaria por la [[Corte Suprema de Chile]])
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad Fiscalizadora / Mercado**: `= this.entidad_destino` (y compensaciones colectivas vía [[Servicio Nacional del Consumidor]])
- **Presidente / Ex Gerente General Condenado**: `= this.firmante_origen`
- **Gerente de Productos Financieros Condenado**: `= this.firmante_destino` (junto a [[Maria Isabel Farah Silva]])
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción de la Operación
Esquema masivo de reprogramaciones unilaterales sin consentimiento aplicado en la cartera de tarjetas de crédito de [[Empresas La Polar SA]] y ocultado en los estados financieros remitidos a la SVS (hoy [[Comision para el Mercado Financiero]]). El hecho derivó en las condenas penales firmes de [[Pablo Alcalde Saavedra]], [[Julian Moreno de Pablo]] y [[Maria Isabel Farah Silva]] por delitos de mercado de valores y [[Lavado de Activos]] ([[Sentencia-Condenatoria-y-Fallo-CS-LaPolar-2015]]), así como en la condena civil solidaria confirmada por la [[Corte Suprema de Chile]] por 2.575.388 UF (`$68.634.000.000 CLP`).

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [La Polar: Fiscalía Centro Norte obtiene condena de principales ejecutivos por delitos de mercado de valores y lavado de activos](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales) | Fiscalía de Chile | `primaria` | 2015-12-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales) |
| [Sentencia Judicial sobre Sanciones SVS en Caso La Polar](https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf) | Poder Judicial (vía CIPER Chile) | `primaria` | 2014-09-03 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf) |
| [Corte Suprema confirma condena contra ex ejecutivos de La Polar y ordena indemnizar a AFP por pérdidas en fondos de pensiones](https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/) | Diario Constitucional | `secundaria` | 2026-03-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/) |
