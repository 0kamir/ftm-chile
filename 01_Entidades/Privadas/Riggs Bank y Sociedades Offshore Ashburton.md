---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Riggs Bank N.A. & Estructuras Offshore (Ashburton Company Ltd. / Althorp Investment Co.)"
fecha_constitucion: 1994-03-22
objeto_social: "Banca privada internacional, fideicomisos offshore y vehículos de inversión en Bahamas, Islas Vírgenes Británicas y EE.UU."
representante_legal: "[[Oscar Aitken Lavanchy]]"
tags:
  - entidad/privada
  - caso-riggs
  - offshore
  - lavado-activos
---

# Riggs Bank y Sociedades Offshore Ashburton

## Ficha Societaria e Institucional
- **RUT Inversionista Extranjero / Referencial**: `= this.rut`
- **Razón Social / Red Fiduciaria**: `= this.razon_social`
- **Fecha de Constitución Red Offshore**: `= this.fecha_constitucion` (operativa entre 1985 y 2004)
- **Objeto Social**: `= this.objeto_social`
- **Estructurador / Apoderado Fiduciario**: `= this.representante_legal` (en beneficio de [[Augusto Pinochet Ugarte]] y [[Lucia Hiriart Rodriguez]])

## Contexto en Investigaciones Forenses
Complejo bancario y societario *offshore* con centro en el **Riggs Bank** de Washington D.C. y ramificaciones en Bahamas, Islas Vírgenes Británicas, Panamá y Gibraltar (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*, *Sonder S.A.*). En el [[Caso Riggs]], el Subcomité de Investigaciones del Senado de EE.UU. y el Ministro en Visita [[Sergio Munoz Gajardo]] acreditaron que esta estructura albergó más de **125 cuentas secretas** y certificados de depósito de [[Augusto Pinochet Ugarte]] (bajo identidades falsas como *"Daniel López"*), nutriéndose de la malversación de gastos reservados del Ejército ([[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]]) y evadiendo impuestos ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]]). En 2018, la [[Corte Suprema de Chile]] decretó el comiso definitivo de los saldos y bienes asociados a favor del Fisco ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
