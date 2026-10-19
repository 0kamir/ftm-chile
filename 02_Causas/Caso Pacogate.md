---
tipo_nodo: causa_judicial
ruc: "1601012894-2"
año_inicio: 2016
tribunal_o_fiscalia: "Fiscalía Regional de Magallanes / 7° Juzgado de Garantía de Santiago / 4° TOP de Santiago"
fiscal_a_cargo: "Eugenio Campos Lucero"
estado_judicial: veredicto_condenatorio_sin_sentencia
delito_principal: "[[Malversacion de Caudales Publicos]]"
estado_verificacion: desactualizado
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
    titulo: "Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-04-15
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml"
    titulo: "Pacogate: postergan juicio oral de 31 imputados"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2021-05-10
    consultado: 2026-10-19
  - url: "https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/"
    titulo: "Pacogate: las claves de la investigación"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2017-04-04
    consultado: 2026-10-19
alertas_verificacion:
  - "Veredicto del juicio oral: abril de 2026 (25 de 28 condenados; se descartó asociación ilícita). Las penas se conocerán en la sentencia (prensa: feb-2027). La evidencia 'Veredicto-TOP-Santiago-Pacogate-2026' no coincide con esa cronología."
tags:
  - causa
  - caso-pacogate
  - carabineros
---

# Caso Pacogate

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` *(Cúpula principal condenada por sentencia firme y ejecutoriada)*
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Lavado de Activos]] y asociación ilícita)

## Resumen Ejecutivo
Mayor fraude fiscal institucional detectado en las Fuerzas de Orden y Seguridad de Chile. Según la acusación, entre 2006 y 2017 funcionarios de la [[Direccion de Finanzas de Carabineros]] (Intendencia), con el general (r) [[Flavio Echeverria Cortez]] señalado como líder y oficiales como el coronel (r) [[Jaime Paz Meneses]], habrían sustraído **$28.348.928.198 CLP** ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]) mediante depósitos ficticios de remuneraciones y desahucios en cuentas corrientes de terceros ("cuentacorrentistas"). En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme. ([[Veredicto-TOP-Santiago-Pacogate-2026]]).

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Órgano Defraudado",
  firmante_origen AS "Jefe Cúpula",
  firmante_destino AS "Operador Financiero",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Sentencia / Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

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
