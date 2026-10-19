---
tipo_nodo: causa_judicial
ruc: "15-CV-07433-LAP-SDNY"
año_inicio: 2024
tribunal_o_fiscalia: "Corte de Distrito de EE.UU. para el Distrito Sur de Nueva York (SDNY) / Departamento de Justicia (DOJ)"
fiscal_a_cargo: "Jueza Loretta Preska / Fiscalía Federal del Distrito Sur de Nueva York"
estado_judicial: descarte_procesal_sin_imputacion
delito_principal: "[[Trafico de Influencias]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.cnnchile.com/pais/cientifico-chileno-correos-jeffrey-epstein-eduardo-guendelman/"
    titulo: "Científico chileno en correos de Jeffrey Epstein (Eduardo Guendelman)"
    medio: "CNN Chile"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.justice.gov/epstein"
    titulo: "Epstein Library (archivos publicados por el DOJ)"
    medio: "U.S. Department of Justice"
    tipo: primaria
    fecha: 2026-01-30
    consultado: 2026-10-19
alertas_verificacion:
  - "ALTO RIESGO REPUTACIONAL: las fuentes indican menciones referenciales, sin imputación ni contacto directo acreditado con Velasco o Luksic. La publicación masiva del DOJ es de diciembre 2025 a enero 2026, no 2024 como dice la evidencia. Considerar retirar las aristas TRX de 'mención'."
tags:
  - causa
  - epstein-files
  - desclasificacion-doj
  - auditoria-osint
  - verificacion-judicial
---

# Caso Archivos Epstein Menciones Chile

## Ficha Procesal, Jurisdiccional y de Verificación OSINT
- **Expediente Judicial de Origen**: `= this.ruc` *(Civil Action No. 15-cv-07433-LAP, Virginia L. Giuffre v. Ghislaine Maxwell)*
- **Año de Desclasificación Masiva**: `= this.año_inicio`
- **Tribunal / Instancia de Desclasificación**: `= this.tribunal_o_fiscalia`
- **Autoridad Judicial Resolutiva**: `= this.fiscal_a_cargo`
- **Estado Procesal Respecto a Ciudadanos Chilenos**: `= this.estado_judicial` *(Sin imputaciones, querellas ni cargos penales; menciones estrictamente referenciales o académicas descartadas)*
- **Ámbito / Tipología Analizada**: `= this.delito_principal` *(Evaluación de redes de influencia internacional y donaciones)*

## Resumen Ejecutivo y Marco de Prevención contra Injurias
Investigación y auditoría documental originada por la desclasificación masiva de millones de páginas de expedientes judiciales, agendas y correos electrónicos ordenada por la jueza Loretta Preska del Tribunal Federal de Manhattan (SDNY) y el Departamento de Justicia de los Estados Unidos (DOJ) en el caso contra Jeffrey Epstein y Ghislaine Maxwell ([[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]).

En el marco de la metodología de inteligencia de fuentes abiertas (OSINT) y el estándar internacional contra la difamación (ICIJ, OCCRP y Sociedad Interamericana de Prensa), es imperativo distinguir entre **participación en una red delictual** versus **mención incidental o referencial en correspondencia de terceros**. 

Las investigaciones periciales de medios chilenos (*BioBioChile*, *La Tercera*, *El Mostrador*, *Interferencia*) sobre los documentos desclasificados acreditaron tres únicos casos relativos a Chile:

1. **[[Andronico Luksic Craig]] (`Mención Indirecta de Terceros / Sin Contacto Directo`)**:
   - En una cadena de correos entre el magnate portuario emiratí Sultan Ahmed bin Sulayem (presidente de *DP World*) y Jeffrey Epstein, Bin Sulayem adjuntó antecedentes curriculares de Luksic y consultó si lo conocía, con el fin de coordinar una reunión de negocios protocolar en Dubái.
   - **Resultado pericial**: No existe registro alguno de que Epstein haya respondido, ni de que haya existido reunión, llamada, correo o trato directo entre Luksic y Epstein ([[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]]). Luksic desmintió de forma categórica cualquier relación.

2. **[[Andres Velasco Branes]] (`Mención Referencial de Terceros / Comentario Social`)**:
   - En un correo enviado por el escritor británico Adrian Dannatt con el asunto *«Future President of Chile etc.»*, se alude a la trayectoria de Velasco en Harvard y a una eventual reunión social en Londres en 2013 en el marco de su precandidatura presidencial independiente.
   - **Resultado pericial**: Los archivos desclasificados no acreditan ninguna interacción, correo directo, aporte de campaña ni reunión entre Andrés Velasco y Epstein ([[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]]).

3. **[[Eduardo Guendelman Israel]] (`Intercambio Epistolar Académico / Donación Científica No Concretada`)**:
   - El físico teórico chileno-israelí (profesor emérito de la Universidad Ben-Gurión) mantuvo correspondencia directa con Epstein entre 2015 y 2019 solicitando patrocinio filantrópico para conferencias científicas y un centro de física teórica en Bahamas, en el contexto de las donaciones universitarias que Epstein realizaba a centros de Harvard y el MIT.
   - **Resultado pericial**: Los fondos solicitados nunca fueron otorgados ni transferidos ([[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]]), manteniéndose el intercambio en el plano científico sin vinculación delictual alguna.

4. **Bitácoras de Vuelo (*Flight Logs*)**:
   - En las bitácoras oficiales de pasajeros de las aeronaves privadas de Jeffrey Epstein no figura ninguna autoridad, parlamentario ni empresario chileno.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  firmante_origen AS "Sujeto Consultado / Mencionado",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
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
