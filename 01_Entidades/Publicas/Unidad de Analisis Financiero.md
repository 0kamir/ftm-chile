---
tipo_nodo: entidad_publica
rut: "61.979.440-0"
categoria: Servicio Público Fiscalizador
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Ministerio de Hacienda"
autoridad_vinculada: "[[Javier Cruz Tamburrino]]"
tags:
  - entidad/publica
  - inteligencia-financiera
  - uaf
  - lavado-activos
---

# Unidad de Analisis Financiero

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Ex Director Vinculado en Reportes**: `= this.autoridad_vinculada`

## Contexto en Investigaciones Forenses
Servicio público descentralizado encargado de prevenir e impedir la utilización del sistema financiero y de otros sectores de la actividad económica para la comisión de los delitos de [[Lavado de Activos]] y financiamiento del terrorismo (Ley N° 19.913). En el grafo forense actúa como nodo articulador de inteligencia patrimonial al haber emitido los **Reportes de Operaciones Sospechosas (ROS)** que permitieron al Ministerio Público y al Consejo de Defensa del Estado trazabilizar:
1. El blanqueo de gastos reservados en el [[Caso Milicogate]] por parte de [[Juan Miguel Fuente-Alba Poblete]] ([[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]]).
2. La red de testaferros y adquisición de bienes raíces con caudales sustraídos de la [[Direccion de Finanzas de Carabineros]] en el [[Caso Pacogate]] por [[Flavio Echeverria Cortez]] ([[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]]).
3. Las alertas de operaciones de factoring ficticio de [[Factop SpA]] y [[Luis Hermosilla Osorio]] en el [[Caso Audios]].

## Historial de Nexos y Reportes de Inteligencia Financiera
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación Reportada",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen del Flujo",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
