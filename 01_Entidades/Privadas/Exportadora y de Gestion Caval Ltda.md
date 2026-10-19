---
tipo_nodo: entidad_privada
rut: "76.195.420-2"
razon_social: "Exportadora y de Gestión Caval Limitada"
fecha_constitucion: "2012-02-03"
objeto_social: "Asesorías comerciales, gestión inmobiliaria, inversiones y consultoría estratégica"
representante_legal: "[[Mauricio Valero Illanes]]"
tags:
  - entidad/privada
  - gestion-inmobiliaria
  - caso-caval
---

# Exportadora y de Gestion Caval Ltda

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Socio Administrador**: `= this.representante_legal` (junto a [[Natalia Compagnon Soto]])

## Contexto Forense y Societario
Sociedad de responsabilidad limitada constituida en febrero de 2012 en partes iguales (50% cada uno) por [[Natalia Compagnon Soto]] y [[Mauricio Valero Illanes]] con un capital inicial de apenas `$6.000.000 CLP`. En el [[Caso Caval]], obtuvo un crédito bancario por `$6.500.000.000 CLP` para comprar y revender tres predios en la comuna de Machalí con una plusvalía proyectada superior a `$2.500.000.000 CLP`, operación por la que fue acusada de soborno al Director de Obras de la [[Municipalidad de Machali]] [[Jorge Silva Menares]] ([[TRX-2014-02-18-Soborno-Caval-Machali-01]]) y de delitos tributarios ([[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]]). La sociedad fue absuelta en julio de 2018; solo [[Natalia Compagnon Soto]] fue condenada, por delito tributario ([[Sentencia-TOP-Rancagua-Caval-2018]]).

## Historial de Nexos y Transacciones Auditadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```
