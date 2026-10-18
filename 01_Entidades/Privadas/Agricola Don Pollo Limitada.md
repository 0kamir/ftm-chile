---
tipo_nodo: entidad_privada
rut: "78.145.220-3"
razon_social: "Agrícola Don Pollo Limitada"
fecha_constitucion: 1982-10-18
objeto_social: "Explotación agropecuaria, producción, faenamiento y distribución de carne de ave"
representante_legal: "Ramón Covarrubias Matte"
tags:
  - entidad/privada
  - don-pollo
  - colusion-pollos
---

# Agricola Don Pollo Limitada

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador**: Familia Covarrubias

## Contexto en Investigaciones Forenses
Tercera compañía avícola del mercado chileno. En el [[Caso Colusion de los Pollos]], fue condenada por formar parte del cartel oligopólico que restringió la producción de pollo durante casi dos décadas bajo la coordinación de la [[Asociacion de Productores Avicolas de Chile AG]]. La [[Corte Suprema de Chile]] le impuso una multa de 12.000 UTA (aproximadamente US$ 9 millones / $6.400 millones de pesos).

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
