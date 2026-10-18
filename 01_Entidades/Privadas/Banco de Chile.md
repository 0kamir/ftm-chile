---
tipo_nodo: entidad_privada
rut: "97.004.000-5"
razon_social: "Banco de Chile"
fecha_constitucion: 1893-10-28
objeto_social: "Institución bancaria, intermediación financiera, operaciones de crédito y servicios bancarios comerciales"
representante_legal: "Eduardo Ebensperger Orrego"
tags:
  - entidad/privada
  - banco
  - quinenco
  - caso-caval
---

# Banco de Chile

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Grupo Controlador**: Quiñenco S.A. / Citigroup (LQ Inversiones Financieras S.A., vinculado a [[Andronico Luksic Craig]])

## Contexto en Investigaciones Forenses
Institución financiera chilena de relevancia sistémica. En el [[Caso Caval]], el banco concedió en febrero de 2014 un crédito por **$6.500.000.000 CLP** a [[Exportadora y de Gestion Caval Ltda]] para la compra de tres predios en Machalí, previa reunión sostenida en noviembre de 2013 entre el vicepresidente de la entidad [[Andronico Luksic Craig]], [[Natalia Compagnon Soto]] y Sebastián Dávalos Bachelet.

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
