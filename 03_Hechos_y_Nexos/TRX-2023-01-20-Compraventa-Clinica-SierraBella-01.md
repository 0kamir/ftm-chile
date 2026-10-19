---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2023-01-20-Compraventa-Clinica-SierraBella-01"
fecha: 2023-01-20
tipo_nexo: trato_directo
monto_clp: 0
monto_origen: sin_monto
metodo_adjudicacion: trato_directo
entidad_origen: "[[Municipalidad de Santiago]]"
entidad_destino: "[[Inmobiliaria San Valentino SpA]]"
firmante_origen: "[[Iraci Hassler Jacob]]"
firmante_destino: "[[Felipe Sanchez Perez]]"
delito_imputado: "[[Fraude al Fisco]]"
causa_vinculada: "[[Caso Sierra Bella]]"
evidencia_soporte: "[[Dictamen-CGR-SierraBella-2023]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
    titulo: "Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella"
    medio: "24 Horas"
    tipo: secundaria
    fecha: 2025-05-26
    consultado: 2026-10-19
historial_correcciones:
  - "La compraventa no se concretó: $8.200 millones fue el precio acordado y no un pago; monto ajustado a 0 (2026-10-19)."
tags:
  - nexo/trato-directo
  - sobreprecio-inmobiliario
  - caso-sierra-bella
---

# TRX-2023-01-20-Compraventa-Clinica-SierraBella-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Pactado (CLP)**: `$8.200.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad Compradora (Origen)**: `= this.entidad_origen`
- **Sociedad Vendedora (Destino)**: `= this.entidad_destino`
- **Alcaldesa Firmante**: `= this.firmante_origen`
- **Representante Vendedor**: `= this.firmante_destino`
- **Delito Investigado**: `= this.delito_imputado`
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Suscripción de escritura pública de compraventa por trato directo entre la [[Municipalidad de Santiago]] —representada por [[Iraci Hassler Jacob]]— e [[Inmobiliaria San Valentino SpA]] —constituida el 5 de abril de 2022 y representada por [[Felipe Sanchez Perez]]— por un monto de `$8.200.000.000 CLP` para adquirir la ex Clínica Sierra Bella. La operación activa la alerta forense de **Constitución Reciente (`< 365 días`, `290 días`)** y fue objetada por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) en el [[Dictamen-CGR-SierraBella-2023]].

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
