---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Empresas Ariztía S.A."
fecha_constitucion: 1960-03-15
objeto_social: "Crianza, faenamiento, elaboración y comercialización de aves, cecinas, quesos y productos agrícolas"
representante_legal: "Manuel Ariztía Ruiz"
tags:
  - entidad/privada
  - ariztia
  - colusion-pollos
---

# Empresas Ariztia SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Familia Ariztía, encabezada por [[Manuel Ariztia Ruiz]]

## Contexto en Investigaciones
Segunda mayor productora avícola de Chile. En el [[Caso Colusion de los Pollos]], el TDLC y la [[Corte Suprema de Chile]] determinaron que coordinó con [[Agrosuper SA]] y [[Agricola Don Pollo Limitada]] el reparto estricto de cuotas de mercado y volumen de aves producidas, sancionándola con la multa máxima de 30.000 UTA (alrededor de US$ 23 millones / $16.000 millones de pesos).

## Registros Reificados
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
