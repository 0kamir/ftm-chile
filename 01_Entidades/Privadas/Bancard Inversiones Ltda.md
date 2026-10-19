---
tipo_nodo: entidad_privada
rut: "96.582.410-3"
razon_social: "Bancard Inversiones Limitada / Bancard International Investment Inc. (BVI) / Inversiones Santa Cecilia S.A."
fecha_constitucion: 1989-11-14
objeto_social: "Family office, sociedades de inversión bursátil, capital privado y vehículos offshore en Islas Vírgenes Británicas y Luxemburgo"
representante_legal: "[[Sebastian Pinera Echenique]]"
tags:
  - entidad/privada
  - caso-dominga
  - caso-lan
  - caso-exalmar
  - caso-sqm
  - offshore
---

# Bancard Inversiones Ltda

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social / Holding**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador Principal**: `= this.representante_legal` (y gerente de finanzas [[Santiago Valdes Gutierrez]])

## Contexto en Investigaciones Forenses
Matriz de inversiones y *family office* del grupo de [[Sebastian Pinera Echenique]] y su familia (integrada por sus filiales chilenas *Inversiones Santa Cecilia S.A.*, *Inversiones Mediterráneo* y su brazo *offshore* en las Islas Vírgenes Británicas *Bancard International Investment Inc.*). Constituye el vehículo corporativo central en cuatro investigaciones forenses:
1. **[[Caso Minera Dominga Pandora Papers]]**: Suscribió el 10 de diciembre de 2010 en las Islas Vírgenes Británicas la venta de su participación en el proyecto Dominga a [[Andes Iron SpA]] ([[Carlos Alberto Delano Abbott]]) por **US$ 152 millones** (`$75.500.000.000 CLP`), condicionando la última cuota a que el gobierno de Piñera no declarara zona de exclusión ambiental en La Higuera ([[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]]).
2. **[[Caso LAN Informacion Privilegiada y Banco de Talca]]**: Ejecutó el 24 de julio de 2006 la compra de 3 millones de acciones de *LAN Airlines* por **`$5.300.000.000 CLP`** con información privilegiada conocida por [[Sebastian Pinera Echenique]] en sesión de directorio, sancionada por la [[Comision para el Mercado Financiero]] ([[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]]), además de adquirir "empresas zombis" con pérdidas arrastradas fiscalizadas por el [[Servicio Impuestos Internos]].
3. **[[Caso Exalmar y Fideicomiso Ciego]]**: Adquirió entre 2010 y 2013 el `9,18%` de la pesquera peruana *Exalmar S.A.* por **`$8.250.000.000 CLP`** mientras Chile litigaba con Perú ante la Corte Internacional de Justicia de La Haya ([[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]]).
4. **[[Caso SQM]]**: Bancorp, sociedad del grupo, emitió en 2009-2010 facturas a [[SQM SA]] por **`$340.000.000 CLP`** que la Fiscalía presumió ideológicamente falsas; SQM las rectificó ante el SII y la investigación terminó con el sobreseimiento por prescripción de [[Santiago Valdes Gutierrez]] en 2019 ([[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
