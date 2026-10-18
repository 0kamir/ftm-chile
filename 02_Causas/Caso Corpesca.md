---
tipo_nodo: causa_judicial
ruc: "1300589410-8"
año_inicio: 2013
tribunal_o_fiscalia: "Fiscalía de Alta Complejidad Centro Norte / 3° TOP de Santiago"
fiscal_a_cargo: "Ximena Chong / Jaime Retamal"
estado_judicial: cerrada
delito_principal: "[[Cohecho]]"
tags:
  - causa
  - caso-corpesca
  - ley-de-pesca
  - congreso-nacional
---

# Caso Corpesca

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` *(Sentencia condenatoria firme y ejecutoriada)*
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Fraude al Fisco]] por asignaciones parlamentarias y responsabilidad penal de la persona jurídica Ley N° 20.393)

## Resumen Ejecutivo
Primera causa en la historia judicial chilena en que un parlamentario en ejercicio y una gran empresa fueron condenados en juicio oral por delitos de corrupción asociados a la tramitación de una ley de la República ("Ley de Pesca"). El 3° Tribunal de Juicio Oral en lo Penal de Santiago ([[Sentencia-3TOP-Santiago-Corpesca-2020]]) condenó al exsenador de [[Union Democrata Independiente]], [[Jaime Orpis Bouchon]], a 5 años y un día de presidio efectivo por [[Cohecho]] y [[Fraude al Fisco]] en el [[Senado de la Republica de Chile]], tras acreditarse que recibió **$233.000.000 CLP** ([[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]]) desde la pesquera [[Corpesca SA]], autorizados por su gerente general [[Francisco Mujica Ortuzar]], para representar los intereses de la compañía en las votaciones legislativas.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Empresa Sobornante",
  entidad_destino AS "Órgano Legislativo",
  firmante_origen AS "Ejecutivo Condenado",
  firmante_destino AS "Senador Condenado",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Sentencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
