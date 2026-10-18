---
tipo_nodo: causa_judicial
ruc: "0300148920-1"
año_inicio: 2003
tribunal_o_fiscalia: "3° Juzgado del Crimen de Santiago / Ministra en Visita Gloria Ana Chevesich / Corte Suprema"
fiscal_a_cargo: "Gloria Ana Chevesich Ruiz (Ministra en Visita Extraordinaria)"
estado_judicial: cerrada_con_condena
delito_principal: "[[Fraude al Fisco]]"
tags:
  - causa
  - sobresueldos
  - caso-mop-gate
---

# Caso MOP-Gate

## Ficha Procesal y Judicial
- **RUC / Rol**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Ministra en Visita**: `= this.tribunal_o_fiscalia`
- **Magistrada Instructora**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Delito Tributario]])

## Síntesis Forense de la Causa
Investigación judicial instruida por la Ministra en Visita Extraordinaria Gloria Ana Chevesich Ruiz y ratificada por la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-MOPGate-2016]]) que desarticuló una red de triangulación de fondos públicos en el [[Ministerio de Obras Publicas]] encabezada por su entonces titular [[Carlos Cruz Lorenzen]] (militante del [[Partido Socialista de Chile]]). El esquema operaba mediante el abultamiento artificial de contratos de asesoría e ingeniería adjudicados a la consultora [[Gestion Ambiental y Territorial SA]] (GESCAM S.A., representada por [[Roberto Lewin Valdivieso]]), cuyos excedentes retornaban para financiar sobresueldos de altos directivos ministeriales ([[TRX-2001-08-20-Contratos-Simulados-MOP-GESCAM-01]]) respaldados con facturación ideológicamente falsa ante el [[Servicio Impuestos Internos]] ([[TRX-2002-04-12-Facturas-Triangulacion-GESCAM-SII-01]]).

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
