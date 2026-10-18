---
tipo_nodo: entidad_privada
rut: "96.522.000-3"
razon_social: "Agrosuper S.A."
fecha_constitucion: 1955-08-10
objeto_social: "Producción, procesamiento, faenamiento, distribución y exportación de productos cárnicos (pollo, cerdo, pavo y salmón)"
representante_legal: "José Guzmán Vial"
tags:
  - entidad/privada
  - agrosuper
  - alimentos
  - colusion-pollos
---

# Agrosuper SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Familia Vial, fundada por [[Gonzalo Vial Vial]]

## Contexto en Investigaciones Forenses
Holding agroindustrial y el mayor productor de alimentos cárnicos de Chile. En el [[Caso Colusion de los Pollos]], fue condenada por el Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-139-Colusion-Pollos-2014]]) y la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Pollos-2015]]) por liderar un cartel oligopólico junto a [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]], coordinado a través de la [[Asociacion de Productores Avicolas de Chile AG]] para fijar cuotas de producción entre 1994 y 2011. La Corte Suprema le impuso la multa máxima legal de 30.000 UTA (aproximadamente US$ 23 millones / $16.000 millones de pesos).

## Auditoría Contable: Registros Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito Imputado"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
