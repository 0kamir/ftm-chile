---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2017-03-06-Reportes-UAF-Carabineros-01"
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
  - "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
  - "https://en.wikipedia.org/wiki/Pacogate"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml"
  - "https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/"
tags:
  - nexo/lavado-activos
  - ros-uaf
  - caso-pacogate
---

# TRX-2017-03-06-Reportes-UAF-Carabineros-01

## Ficha de Arista Reificada (Transacción / Hecho Registrado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Registrado (CLP)**: `$1.450.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Órgano de Inteligencia Financiera (Destino ROS)**: `= this.entidad_destino`
- **Jefe de Finanzas Acusado**: `= this.firmante_origen`
- **Autoridad UAF Receptora / Reportante**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Malversacion de Caudales Publicos]])
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción del Hecho
Presunta estructuración y estratificación de fondos sustraídos desde las cuentas institucionales de la [[Direccion de Finanzas de Carabineros]] por un subtotal trazabilizado en alertas bancarias de `$1.450.000.000 CLP` bajo el mando del General (r) [[Flavio Echeverria Cortez]] y [[Jaime Paz Meneses]], cuyas operaciones en efectivo y transferencias a testaferros activaron los Reportes de Operaciones Sospechosas (ROS) de la [[Unidad de Analisis Financiero]] encabezada por [[Javier Cruz Tamburrino]], antecedentes de la acusación por [[Lavado de Activos]] en el [[Caso Pacogate]]. En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme.

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude](https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) | El Mostrador | `secundaria` | 2026-04-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) |
| [Pacogate](https://en.wikipedia.org/wiki/Pacogate) | Wikipedia | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://en.wikipedia.org/wiki/Pacogate) |
| [Pacogate: postergan juicio oral de 31 imputados](https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) | BioBioChile | `secundaria` | 2021-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) |
| [Pacogate: las claves de la investigación](https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) | The Clinic | `secundaria` | 2017-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) |
