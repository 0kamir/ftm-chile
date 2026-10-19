---
tipo_nodo: nexo_transaccion
fecha: 2016-11-10
tipo_nexo: transferencia
monto_clp: 28348928198
entidad_origen: "[[Direccion de Finanzas de Carabineros]]"
entidad_destino: "[[Direccion de Finanzas de Carabineros]]"
firmante_origen: "[[Flavio Echeverria Cortez]]"
firmante_destino: "[[Jaime Paz Meneses]]"
causa_vinculada: "[[Caso Pacogate]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
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
  - nexo/transaccion
  - transferencia
  - caso-pacogate
---

# TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01

## Ficha de Arista Reificada (Desfalco Consolidado en Intendencia de Carabineros)
- **Fecha de Corte Pericial**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Órgano Público Defraudado**: `= this.entidad_origen`
- **Jefe de Cúpula Condenado**: `= this.firmante_origen`
- **Operador Contable Condenado**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Condenado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]])
- **Evidencia / Sentencia Firme**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Presunta sustracción sistemática de caudales públicos desde las cuentas institucionales de la [[Direccion de Finanzas de Carabineros]] por un total, según la acusación, de **$28.348.928.198 CLP**. La operación consistía en alterar las nóminas electrónicas de pago de remuneraciones y desahucios enviadas al Banco Estado para abonar sumas millonarias a cuentas particulares y luego distribuir el retorno en efectivo a la cúpula encabezada por [[Flavio Echeverria Cortez]] y [[Jaime Paz Meneses]], en el [[Caso Pacogate]]. En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme.

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
