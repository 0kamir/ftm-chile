---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2011-03-10-Pagos-Penta-Wagner-01"
fecha: 2011-03-10
tipo_nexo: transferencia
monto_clp: 42000000
monto_origen: sentencia
metodo_adjudicacion: no_aplica
entidad_origen: "[[Empresas Penta SA]]"
entidad_destino: "[[Servicio Impuestos Internos]]"
firmante_origen: "[[Carlos Eugenio Lavin Garcia-Huidobro]]"
firmante_destino: "[[Pablo Wagner San Martin]]"
delito_imputado: "[[Delito Tributario]]"
causa_vinculada: "[[Caso Penta]]"
evidencia_soporte: "[[Sentencia-8Juzgado-Garantia-Penta-2018]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
    titulo: "Caso Penta: Tribunal desecha argumentos del CDE y absuelve a exsubsecretario Wagner por cohecho"
    medio: "Emol"
    tipo: secundaria
    fecha: 2018-07-06
    consultado: 2026-10-19
  - url: "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
    titulo: "Caso Penta deja condenas en juicios abreviados y suspensiones"
    medio: "T13"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - nexo/cohecho
  - caso-penta
---

# TRX-2011-03-10-Pagos-Penta-Wagner-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$42.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad Fiscalizadora Defraudada**: `= this.entidad_destino`
- **Firmante / Autorizador de Origen**: `= this.firmante_origen`
- **Funcionario Público Receptor**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Pagos bimensuales de `$3.000.000 CLP` (totalizando `$42.000.000 CLP` entre 2010 y 2012) de [[Empresas Penta SA]] a [[Pablo Wagner San Martin]] mientras era Subsecretario de Minería, documentados con boletas de honorarios de terceros ante el [[Servicio Impuestos Internos]]. El 8° Juzgado de Garantía de Santiago (julio de 2018, procedimiento abreviado) absolvió a Wagner ** de cohecho** y lo condenó por enriquecimiento ilícito y delitos tributarios (pena remitida de dos años e inhabilitación para cargos públicos); la propia Fiscalía reconoció no haber acreditado que los pagos fueran a cambio de favores.

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
