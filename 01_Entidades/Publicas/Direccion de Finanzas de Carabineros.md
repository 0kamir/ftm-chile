---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Carabineros de Chile / Ministerio del Interior y Seguridad Pública"
tags:
  - entidad/publica
  - carabineros
  - caso-pacogate
---

# Direccion de Finanzas de Carabineros

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones Forenses
Repartición encargada de la administración presupuestaria y pago de remuneraciones de Carabineros de Chile (Dirección de Finanzas / Intendencia). En el [[Caso Pacogate]], fue el epicentro del desfalco de **$28.348.928.198 CLP** ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]) atribuido por la Fiscalía a una estructura encabezada por [[Flavio Echeverria Cortez]], con participación de oficiales como [[Jaime Paz Meneses]]. En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme. ([[Veredicto-TOP-Santiago-Pacogate-2026]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Desfalco",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Jefe Finanzas",
  firmante_destino AS "Operador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
