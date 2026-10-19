---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01"
fecha: 2017-03-06
tipo_nexo: desviacion_fondos
monto_clp: 1450000000
monto_origen: acusacion
metodo_adjudicacion: no_aplica
entidad_origen: "[[Direccion de Finanzas de Carabineros]]"
entidad_destino: "[[Unidad de Analisis Financiero]]"
firmante_origen: "[[Flavio Echeverria Cortez]]"
firmante_destino: "[[Javier Cruz Tamburrino]]"
delito_imputado: "[[Lavado de Activos]]"
causa_vinculada: "[[Caso Pacogate]]"
evidencia_soporte: "[[Veredicto-TOP-Santiago-Pacogate-2026]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
    titulo: "Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-04-15
    consultado: 2026-10-19
tags:
  - nexo/lavado-activos
  - ros-uaf
  - caso-pacogate
---

# TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$1.450.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Órgano de Inteligencia Financiera (Destino ROS)**: `= this.entidad_destino`
- **Jefe de Finanzas Acusado**: `= this.firmante_origen`
- **Autoridad UAF Receptora / Reportante**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Malversacion de Caudales Publicos]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Presunta estructuración y estratificación de fondos sustraídos desde las cuentas institucionales de la [[Direccion de Finanzas de Carabineros]] por un subtotal trazabilizado en alertas bancarias de `$1.450.000.000 CLP` bajo el mando del General (r) [[Flavio Echeverria Cortez]] y [[Jaime Paz Meneses]], cuyas operaciones en efectivo y transferencias a testaferros activaron los Reportes de Operaciones Sospechosas (ROS) de la [[Unidad de Analisis Financiero]] encabezada por [[Javier Cruz Tamburrino]], antecedentes de la acusación por [[Lavado de Activos]] en el [[Caso Pacogate]]. En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme.

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
