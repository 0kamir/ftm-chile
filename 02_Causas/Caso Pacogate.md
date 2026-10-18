---
tipo_nodo: causa_judicial
ruc: "1601012894-2"
año_inicio: 2016
tribunal_o_fiscalia: "Fiscalía Regional de Magallanes / 7° Juzgado de Garantía de Santiago / 4° TOP de Santiago"
fiscal_a_cargo: "Eugenio Campos Lucero"
estado_judicial: cerrada
delito_principal: "[[Malversacion de Caudales Publicos]]"
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
Mayor fraude fiscal institucional detectado en las Fuerzas de Orden y Seguridad de Chile. Entre 2006 y 2017, una organización criminal enquistada en la [[Direccion de Finanzas de Carabineros]] (Intendencia), liderada por el general (r) [[Flavio Echeverria Cortez]] y operada contablemente por oficiales como el coronel (r) [[Jaime Paz Meneses]], sustrajo **$28.348.928.198 CLP** ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]) mediante depósitos ficticios de remuneraciones y desahucios en cuentas corrientes de terceros ("cuentacorrentistas"). El 4° Tribunal de Juicio Oral en lo Penal de Santiago dictó condenas de hasta 17 años de presidio efectivo ([[Sentencia-TOP-Santiago-Pacogate-2021]]).

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
