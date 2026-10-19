---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2017
tribunal_o_fiscalia: "Tribunal de Juicio Oral en lo Penal de Temuco / Fiscalía Regional de Aysén y Fiscalía de La Araucanía"
fiscal_a_cargo: "Carlos Palma Guerra / Roberto Garrido Bedwell"
estado_judicial: cerrada_con_condena
delito_principal: "[[Falsificacion de Instrumento Publico]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
    titulo: "El 'profesor' Smith condenado a 12 años de cárcel por montaje en Operación Huracán"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2026-04-02
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml"
    titulo: "Profesor Smith y otros 3 condenados en Operación Huracán presentan recurso para anular sentencia"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2026-05-04
    consultado: 2026-10-19
tags:
  - causa
  - operacion-huracan
  - carabineros
  - dipolcar
  - uioe
  - montaje-estatal
  - condena-efectiva
---

# Caso Operacion Huracan

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio` (Operativo inicial en septiembre de 2017; causa contra Carabineros abierta en enero de 2018)
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscales a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` (Sentencia condenatoria firme dictada por el TOP de Temuco en 2024)
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Obstruccion a la Investigacion]], uso malicioso de instrumento público falso y asociación ilícita)

## Resumen Ejecutivo de la Causa
Investigación penal de máxima gravedad institucional que destapó la fabricación e implantación deliberada de pruebas falsas por parte de la [[Direccion de Inteligencia Policial de Carabineros]] (UIOE Temuco) para imputar a dirigentes mapuche bajo la Ley Antiterrorista en septiembre de 2017. 

La causa se articuló en tres momentos estructurales:
1. **La Farsa de «Antorcha» y Detenciones Ilegales (Septiembre 2017)**: La cúpula de inteligencia dirigida por el general [[Gonzalo Blu Rodriguez]], el excoronel [[Marcelo Teuber Munoz]] y el exmayor [[Patricio Marin Lazo]], con el respaldo del general director [[Bruno Villalobos Krumm]], orquestó la detención de 8 comuneros mapuche ([[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]]), afirmando haber interceptado sus celulares con el software «Antorcha» creado por [[Alex Smith Leay]], remunerado con gastos reservados institucionales ([[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]]).
2. **Descubrimiento del Montaje por Cibercrimen PDI (Enero 2018)**: Peritajes independientes de la Fiscalía y la Brigada del Cibercrimen de la PDI ([[Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018]]) acreditaron que «Antorcha» era inexistente y que el excapitán [[Leonardo Osses Sandoval]] y sus subalternos habían copiado manualmente archivos `.txt` en los teléfonos ya incautados ([[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]]). La Fiscalía sobreseyó definitivamente a los comuneros e imputó penalmente a la plana mayor policial.
3. **Condenas Históricas en Juicio Oral (2024)**: El Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]) condenó a **12 años de presidio efectivo** a [[Alex Smith Leay]], **10 años de presidio efectivo** a [[Leonardo Osses Sandoval]], **5 años de presidio** al general [[Gonzalo Blu Rodriguez]], **5 años de presidio** a [[Patricio Marin Lazo]] y penas menores a [[Marcelo Teuber Munoz]], consagrando judicialmente la existencia de un montaje estatal.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Receptor / Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

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
