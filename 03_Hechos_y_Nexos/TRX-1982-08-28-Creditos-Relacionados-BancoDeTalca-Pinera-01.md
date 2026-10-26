---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01"
fecha: 1982-08-28
tipo_nexo: desviacion_fondos
monto_clp: 0
monto_origen: sin_monto
metodo_adjudicacion: trato_directo
entidad_origen: "[[Bancard Inversiones Ltda]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Sebastian Pinera Echenique]]"
firmante_destino: "[[Sergio Munoz Gajardo]]"
delito_imputado: "[[Negociacion Incompatible]]"
causa_vinculada: "[[Caso LAN Informacion Privilegiada y Banco de Talca]]"
evidencia_soporte: "[[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]]"
historial_correcciones:
  - "2026-10-19: monto_clp $18.500.000.000 llevado a 0; la cifra no aparece en ninguna fuente verificable."
estado_verificacion: parcial
fuentes:
  - "https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html"
  - "https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia"
  - "https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/"
  - "https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20121128/pags-amp/20121128154834.html"
tags:
  - nexo/desviacion-fondos
  - banco-de-talca
  - infraccion-bancaria
---

# TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$18.500.000.000 CLP` (`= this.monto_clp` — equivalente a los más de **US$ 38 millones** en créditos relacionados sin garantías reales otorgados en el *Banco de Talca*)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen` (Gerencia General del *Banco de Talca* / sociedades *Infinco*)
- **Entidad de Destino / Instancia Judicial**: `= this.entidad_destino`
- **Ejecutivo Ordenador en Origen**: `= this.firmante_origen`
- **Instancia / Magistrado Referencial en Destino**: `= this.firmante_destino` (y Ministro en Visita Luis Correa Bulo)
- **Delito Imputado**: `= this.delito_imputado` (estafa e infracción al artículo 84 de la Ley General de Bancos)
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho

> [!NOTE] Monto sin respaldo
> Las cifras en pesos mencionadas en esta nota no aparecen en ninguna fuente verificable y no se contabilizan en los totales del vault (antes: $18.500.000.000 CLP).

Otorgamiento sistemático de préstamos y créditos cruzados a sociedades de papel relacionadas con los propios directores y ejecutivos del *Banco de Talca* (donde [[Sebastian Pinera Echenique]] se desempeñaba como gerente general) por más de **US$ 38 millones** (`~85%` de las colocaciones totales del banco, valorizados en **$18.500.000.000 CLP**) sin respaldos ni garantías reales, lo que provocó la insolvencia e intervención estatal de la institución financiera. El 28 de agosto de 1982 el juez Luis Correa Bulo dictó encargatoria de reo y orden de detención contra [[Sebastian Pinera Echenique]], quien permaneció **24 días prófugo** hasta que la [[Corte Suprema de Chile]] acogió un recurso de amparo que anuló la orden de aprehensión ([[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]]).

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Piñera y caso Banco de Talca: 'Fui víctima de un acto injusto, ilegal y arbitrario'](https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html) | Emol | `secundaria` | 2009-07-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html) |
| [Del Banco de Talca a Exalmar: 5 momentos en que Piñera se vio complicado con la justicia](https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia) | El Desconcierto | `secundaria` | 2017-02-27 | [Wayback ↺](https://web.archive.org/web/*/https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia) |
| [El directorio de Lan que se transformó en la peor pesadilla de Piñera](https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/) | CIPER Chile | `secundaria` | 2009-09-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2009/09/29/el-directorio-de-lan-que-se-transformo-en-la-peor-pesadilla-de-pinera/) |
| [Piñera acusó motivos políticos en sanción de la SVS, aunque pagará la multa](https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html) | Cooperativa | `secundaria` | 2007-07-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html) |
| [Suprema ratificó multa contra dueños de LAN por comprar acciones con información privilegiada](https://www.cooperativa.cl/noticias/site/artic/20121128/pags-amp/20121128154834.html) | Cooperativa | `secundaria` | 2012-11-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20121128/pags-amp/20121128154834.html) |
