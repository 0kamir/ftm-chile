---
tipo_nodo: entidad_publica
rut: ""
categoria: GORE
region: "Biobío (VIII Región)"
superior_jerarquico: "Gobierno Regional del Biobío (Autónomo)"
tags:
  - entidad/publica
  - gore
  - biobio
---

# GORE Biobio

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Gobierno Regional del Biobío, encabezado durante el período investigado por el Gobernador Regional [[Rodrigo Diaz Worner]]. En el marco del [[Caso Convenios]] (Arista "Caso Lencería"), autorizó mediante la [[Resolucion-GORE-Biobio-EnTi-2022]] el traspaso directo de **$250.635.000 CLP** ([[TRX-2022-12-20-Convenio-EnTi-01]]) hacia la [[Fundacion En Ti]], gestionada de facto por [[Camila Polizzi Fonceca]].

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Convenio",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Firmante Público",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
