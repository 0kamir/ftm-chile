---
tipo_nodo: entidad_privada
rut: "96.714.830-K"
razon_social: "Empresas Penta S.A."
fecha_constitucion: "1986-09-12"
objeto_social: "Holding financiero, inversiones previsionales, seguros, salud e inmobiliaria"
representante_legal: "[[Carlos Alberto Delano Abbott]]"
tags:
  - entidad/privada
  - holding-financiero
  - caso-penta
---

# Empresas Penta SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador y Representante**: `= this.representante_legal` (junto a [[Carlos Eugenio Lavin Garcia-Huidobro]])

## Contexto Forense y Societario
Holding financiero cuyos controladores [[Carlos Alberto Delano Abbott]] y [[Carlos Eugenio Lavin Garcia-Huidobro]] articularon en el [[Caso Penta]] un mecanismo de rebaja fraudulenta de base imponible ante el [[Servicio Impuestos Internos]] mediante la contabilización de boletas y facturas ideológicamente falsas para financiar campañas de la [[Union Democrata Independiente]] y de [[Pablo Longueira Montes]] ([[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]]), además de realizar pagos bimensuales (sin condena por cohecho: la imputación de soborno fue retirada en 2018) al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]), según [[Sentencia-8Juzgado-Garantia-Penta-2018]].

## Historial de Desembolsos y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Destinatario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
