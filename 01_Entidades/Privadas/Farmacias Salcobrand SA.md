---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Farmacias Salcobrand S.A. (Empresas SB)"
fecha_constitucion: 2000-04-10
objeto_social: "Explotación de farmacias, droguerías, perfumerías y comercialización de productos farmacéuticos"
representante_legal: "Matías Verdugo Correa"
tags:
  - entidad/privada
  - farmacias
  - salcobrand
  - colusion-farmacias
---

# Farmacias Salcobrand SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Grupo Controlador**: Empresas SB (familia Yarur Rey)

## Contexto en Investigaciones
Cadena de farmacias surgida de la fusión de Farmacias Salco y Farmacias Brand. En el [[Caso Colusion de las Farmacias]], su gerente general [[Roberto Belloni Pechini]] articuló junto a ejecutivos de [[Farmacias Cruz Verde SA]] y [[Farmacias Ahumada SA]] el mecanismo de alza coordinada de precios en medicamentos de uso crónico ([[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]), utilizando a laboratorios como agentes de control para evitar desviaciones en los valores de venta al público. 

Fue condenada por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) a una multa de **20.000 UTA** (confirmada por la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]) y obligada judicialmente en sede civil por demanda colectiva del [[Servicio Nacional del Consumidor]] a indemnizar a los consumidores con más de mil millones de pesos ([[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]).

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
