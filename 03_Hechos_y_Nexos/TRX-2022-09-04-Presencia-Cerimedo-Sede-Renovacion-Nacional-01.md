---
tipo_nodo: nexo_transaccion
fecha: 2022-09-04
tipo_nexo: reunion_lobby
monto_clp: 0
monto_origen: sin_monto
entidad_origen: "[[Numen Publicidad SpA]]"
entidad_destino: "[[Renovacion Nacional]]"
firmante_origen: "[[Fernando Cerimedo]]"
firmante_destino: "[[Renovacion Nacional]]"
causa_vinculada: "[[Caso Operaciones Digitales e Injerencia Electoral]]"
delito_imputado: ""
evidencia_soporte: "[[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]]"
estado_verificacion: sin_fuente
fuentes: []
historial_correcciones:
  - "Se eliminó delito_imputado (2026-10-19): la presencia en una sede partidaria no es un delito imputado. RN afirma que Cerimedo nunca fue contratado."
tags:
  - nexo/transaccion
  - cerimedo
  - renovacion-nacional
  - rechazo-2022
  - reunion
---

# TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01

## Ficha de Arista Reificada (Presencia y Coordinación en Cuartel General de Campaña)
- **Fecha del Hito**: `= this.fecha` *(4 de septiembre de 2022)*
- **Tipo de Operación**: `= this.tipo_nexo`
- **Monto Monetario Directo Declarado**: `= this.monto_clp` *(Sin contrato ni facturación informada ante el Servel)*
- **Entidad Operadora Digital**: `= this.entidad_origen`
- **Partido Político Receptor / Anfitrión**: `= this.entidad_destino`
- **Consultor Estratégico**: `= this.firmante_origen`
- **Colectividad Política**: `= this.firmante_destino`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Delito / Infracción Investigada**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción de la Operación
Registro fotográfico, difundido por The Clinic, de la presencia del consultor político argentino [[Fernando Cerimedo]], titular de [[Numen Publicidad SpA]], en la sede central de [[Renovacion Nacional]] durante la jornada electoral y celebración de los resultados del Plebiscito Constitucional del 4 de septiembre de 2022. 

En dicha instancia, documentada en la [[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]] revelada por *The Clinic*, Cerimedo compartió dependencias con el entonces prosecretario del partido Manuel José Errázuriz y operadores de campaña. El hecho motivó requerimientos parlamentarios ante el Servel y la apertura de investigaciones de la Fiscalía Centro Norte respecto de la falta de rendición contable de servicios digitales extranjeros o aportes de campaña no declarados.

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
