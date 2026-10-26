---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 1990
tribunal_o_fiscalia: "5° Juzgado del Crimen de Santiago / Corte de Apelaciones de Santiago / Comisión Investigadora Cámara de Diputados"
fiscal_a_cargo: "Ministro en Visita Alejandro Solís Muñoz / Consejo de Defensa del Estado"
estado_judicial: sobreseida
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html"
  - "https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html"
tags:
  - causa
  - caso-pinocheques
  - ejercito
  - fraude-fisco
---

# Caso Pinocheques

## Ficha Procesal y Judicial
- **RUC / Rol Judicial**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Instancia Investigadora**: `= this.tribunal_o_fiscalia`
- **Magistrado / Órgano Acusador**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` (Cerrada en julio de 1995 por instrucción presidencial al Consejo de Defensa del Estado invocando "razón de Estado" tras dos acuartelamientos militares)
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Negociacion Incompatible]] y [[Malversacion de Caudales Publicos]])

## Síntesis de la Causa
Investigación parlamentaria, contralora y penal originada por el pago en enero de 1989 de tres cheques girados por las Fábricas y Maestranzas del Ejército (FAMAE, dependiente de la estructura logística vinculada al [[Comando de Apoyo a la Fuerza del Ejercito]]) por un monto nominal de `$971.982.585 CLP` de la época (equivalentes a cerca de **US$ 3 millones**, valorizados en **`$2.950.000.000 CLP`**) a nombre directo de [[Augusto Pinochet Hiriart]], hijo mayor del entonces Comandante en Jefe del Ejército [[Augusto Pinochet Ugarte]], bajo el pretexto de adquirir la empresa metalúrgica y armera quebrada [[Valmoval Ltda]] (ex *Proyectos Integrados / Nihon PSP*) sin que mediara decreto supremo ni toma de razón de la [[Contraloria General de la Republica]] ([[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]]).

Cuando la Comisión Investigadora de la Cámara de Diputados (presidida por Jorge Schaulsohn) y el Consejo de Defensa del Estado avanzaron hacia el procesamiento de los responsables, [[Augusto Pinochet Ugarte]] ejecutó dos demostraciones de fuerza militar contra el poder civil:
1. **El "Ejercicio de Enlace" (19 de diciembre de 1990)**: Acuartelamiento sorpresivo de todas las unidades del Ejército en el país bajo el gobierno de Patricio Aylwin.
2. **El "Boinazo" (28 de mayo de 1993)**: Despliegue de comandos del Ejército con tenida de combate y armamento de guerra frente al Palacio de La Moneda al día siguiente de que el diario *La Nación* informara la reapertura judicial de los *Pinocheques*.

Finalmente, en julio de 1995, el gobierno de Eduardo Frei Ruiz-Tagle instruyó al Consejo de Defensa del Estado desistirse de las acciones penales ante la [[Corte Suprema de Chile]] invocando "razones de interés nacional". Una década más tarde, la investigación del [[Caso Riggs]] encabezada por el ministro [[Sergio Munoz Gajardo]] probó que parte de los fondos girados en los *Pinocheques* fueron depositados y triangulados en cuentas extranjeras controladas por [[Augusto Pinochet Ugarte]] en [[Riggs Bank y Sociedades Offshore Ashburton]] ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).

## Transacciones y Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Juez Valderrama sobreseyó arista de los 'Pinocheques' en caso Riggs](https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) | Cooperativa | `secundaria` | 2010-05-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) |
| [Frei descartó presiones militares para cerrar el caso de los 'pinocheques'](https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html) | Cooperativa | `secundaria` | 2004-12-07 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html) |
