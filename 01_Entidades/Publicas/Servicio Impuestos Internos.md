---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Metropolitana de Santiago"
superior_jerarquico: "Ministerio de Hacienda"
tags:
  - entidad/publica
  - sii
  - caso-audios
---

# Servicio Impuestos Internos

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Órgano fiscalizador tributario dependiente del Ministerio de Hacienda. En el marco del [[Caso Audios]], la Fiscalía Metropolitana Oriente investiga pagos ilícitos y entregas de información reservada coordinadas por [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] a favor del factoring [[Factop SpA]], documentadas en el nexo [[TRX-2023-06-22-Reunion-Audios-01]] y la evidencia [[Audio-Reunion-Edificio-Alonso-2023]].

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_origen AS "Operador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
