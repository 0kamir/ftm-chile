---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01"
fecha: 2010-11-15
tipo_nexo: cohecho_soborno
monto_clp: 186500000
monto_origen: sentencia
metodo_adjudicacion: licitacion_publica
entidad_origen: "[[KDM Empresas SA]]"
entidad_destino: "[[Municipalidad de Maipu]]"
firmante_origen: "[[Fernando Leon Steffens]]"
firmante_destino: "[[Marcelo Torres Ferrari]]"
delito_imputado: "[[Cohecho]]"
causa_vinculada: "[[Caso Basura]]"
evidencia_soporte: "[[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/"
    titulo: "Ex concejal RN de Maipú es condenado por lavado de activos y cohecho en caso Basura"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2022-07-28
    consultado: 2026-10-19
historial_correcciones:
  - "monto_clp ajustado de $18.500 millones (valor de la licitación) a $186,5 millones (pagos de KDM acreditados por el tribunal) el 2026-10-19."
tags:
  - nexo/cohecho
  - licitacion-municipal
  - caso-basura
---

# TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto del Contrato Adjudicado (CLP)**: `$18.500.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad Concesionaria (Origen de Coimas)**: `= this.entidad_origen`
- **Corporación Edilicia (Destino)**: `= this.entidad_destino`
- **Ejecutivo Autorizador**: `= this.firmante_origen`
- **Concejal / Articulador Receptor**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Adjudicación de la licitación pública de recolección y transporte de residuos domiciliarios de la [[Municipalidad de Maipu]] en favor de la filial Demarco S.A. del consorcio [[KDM Empresas SA]] por un valor plurianual de `$18.500.000.000 CLP`, operación en la que la Fiscalía Regional Metropolitana Occidente imputó transferencias trianguladas desde el ejecutivo [[Fernando Leon Steffens]] (quien obtuvo una salida alternativa) hacia el entonces concejal [[Marcelo Torres Ferrari]] (condenado en 2022 por cohecho y lavado de activos; el tribunal dio por acreditados pagos de KDM por $186,5 millones) (militante de [[Renovacion Nacional]]) para asegurar la mayoría de votos en el Concejo Municipal.

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
