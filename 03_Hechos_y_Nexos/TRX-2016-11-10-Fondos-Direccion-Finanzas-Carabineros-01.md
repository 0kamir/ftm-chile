---
tipo_nodo: nexo_transaccion
fecha: 2016-11-10
tipo_nexo: transferencia
monto_clp: 28348928198
monto_origen: acusacion
entidad_origen: "[[Direccion de Finanzas de Carabineros]]"
entidad_destino: "[[Direccion de Finanzas de Carabineros]]"
firmante_origen: "[[Flavio Echeverria Cortez]]"
firmante_destino: "[[Jaime Paz Meneses]]"
causa_vinculada: "[[Caso Pacogate]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
evidencia_soporte: "[[Veredicto-TOP-Santiago-Pacogate-2026]]"
estado_verificacion: parcial
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
  - "https://en.wikipedia.org/wiki/Pacogate"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml"
  - "https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/"
tags:
  - nexo/transaccion
  - transferencia
  - caso-pacogate
---

# TRX-2016-11-10-Fondos-Direccion-Finanzas-Carabineros-01

## Ficha de Arista Reificada (Desfalco Consolidado en Intendencia de Carabineros)
- **Fecha de Corte**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Órgano Público Defraudado**: `= this.entidad_origen`
- **Jefe de Cúpula Condenado**: `= this.firmante_origen`
- **Operador Contable Condenado**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Condenado**: `= this.delito_imputado` (en concurso con [[Lavado de Activos]])
- **Evidencia / Sentencia Firme**: `= this.evidencia_soporte`

## Descripción de la Operación
Presunta sustracción sistemática de caudales públicos desde las cuentas institucionales de la [[Direccion de Finanzas de Carabineros]] por un total, según la acusación, de **$28.348.928.198 CLP**. La operación consistía en alterar las nóminas electrónicas de pago de remuneraciones y desahucios enviadas al Banco Estado para abonar sumas millonarias a cuentas particulares y luego distribuir el retorno en efectivo a la cúpula encabezada por [[Flavio Echeverria Cortez]] y [[Jaime Paz Meneses]], en el [[Caso Pacogate]]. En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude](https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) | El Mostrador | `secundaria` | 2026-04-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) |
| [Pacogate](https://en.wikipedia.org/wiki/Pacogate) | Wikipedia | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://en.wikipedia.org/wiki/Pacogate) |
| [Pacogate: postergan juicio oral de 31 imputados](https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) | BioBioChile | `secundaria` | 2021-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) |
| [Pacogate: las claves de la investigación](https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) | The Clinic | `secundaria` | 2017-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) |
