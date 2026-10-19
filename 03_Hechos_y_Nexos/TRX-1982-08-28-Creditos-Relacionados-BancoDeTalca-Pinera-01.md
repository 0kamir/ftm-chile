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
estado_verificacion: parcial
fuentes:
  - url: "https://www.emol.com/noticias/nacional/2009/07/27/368966/pinera-y-caso-banco-de-talca-fui-victima-de-un-acto-injusto-ilegal-y-arbitrario.html"
    titulo: "Piñera y caso Banco de Talca: 'Fui víctima de un acto injusto, ilegal y arbitrario'"
    medio: "Emol"
    tipo: secundaria
    fecha: 2009-07-27
    consultado: 2026-10-19
  - url: "https://eldesconcierto.cl/2017/02/27/del-banco-talca-exalmar-5-momentos-pinera-se-vio-complicado-la-justicia"
    titulo: "Del Banco de Talca a Exalmar: 5 momentos en que Piñera se vio complicado con la justicia"
    medio: "El Desconcierto"
    tipo: secundaria
    fecha: 2017-02-27
    consultado: 2026-10-19
historial_correcciones:
  - "2026-10-19: monto_clp $18.500.000.000 llevado a 0; la cifra no aparece en ninguna fuente verificable."
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
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
