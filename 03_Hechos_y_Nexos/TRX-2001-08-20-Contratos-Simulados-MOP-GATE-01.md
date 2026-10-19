---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01"
fecha: 2001-08-20
tipo_nexo: trato_directo
monto_clp: 1253000000
metodo_adjudicacion: licitacion_privada
entidad_origen: "[[Ministerio de Obras Publicas]]"
entidad_destino: "[[Gestion Ambiental y Territorial SA]]"
firmante_origen: "[[Carlos Cruz Lorenzen]]"
firmante_destino: "[[Hector Pena Veliz]]"
delito_imputado: "[[Fraude al Fisco]]"
causa_vinculada: "[[Caso MOP-Gate]]"
evidencia_soporte: "[[Sentencia-Corte-Suprema-MOPGate-2016]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
    titulo: "Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas"
    medio: "Emol"
    tipo: secundaria
    fecha: 2016-06-29
    consultado: 2026-10-19
  - url: "https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html"
    titulo: "Corte de Apelaciones ratificó condenas en el caso MOP-Gate"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2014-08-12
    consultado: 2026-10-19
  - url: "https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/"
    titulo: "Fraude al fisco: el delito por el cual Jorge Quiroz fue condenado y luego absuelto por la Suprema"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-06-09
    consultado: 2026-10-19
historial_correcciones:
  - "Verificado el 2026-10-19: perjuicio judicialmente acreditado de $1.253 millones en la causa principal (El Mostrador, 2026)."
tags:
  - nexo/fraude-fisco
  - sobresueldos
  - caso-mop-gate
---

# TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$1.253.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Autoridad Firmante de Origen**: `= this.firmante_origen`
- **Representante Receptor**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Suscripción y pago de contratos de asesoría ambiental, territorial y de gestión en el [[Ministerio de Obras Publicas]] autorizados bajo la administración de [[Carlos Cruz Lorenzen]] en favor de la consultora [[Gestion Ambiental y Territorial SA]] (GATE), de propiedad de [[Hector Pena Veliz]], cuyo monto fue deliberadamente abultado en `$1.253.000.000 CLP` para desviar caudales públicos hacia el pago de sobresueldos de funcionarios y directivos ministeriales.

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
