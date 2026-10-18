---
tipo_nodo: entidad_privada
rut: "76.091.340-5"
razon_social: "Comercializadora e Importadora Frasim Limitada"
fecha_constitucion: "2008-04-15"
objeto_social: "Importación, comercialización de repuestos, insumos industriales y pertrechos"
representante_legal: "[[Jozo Santic Palomino]]"
tags:
  - entidad/privada
  - proveedor-militar
  - caso-milicogate
---

# Frasim Ltda

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Oficial Articulador en el CAF**: `= this.representante_legal`

## Contexto Forense y Societario
Sociedad proveedora utilizada en el [[Caso Milicogate]] para emitir facturas por servicios y suministros inexistentes pagados con fondos de la Ley Reservada del Cobre desde el [[Comando de Apoyo a la Fuerza del Ejercito]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]), en coordinación con el coronel (r) [[Jozo Santic Palomino]] y documentado en [[Auto-Procesamiento-Ministra-Rutherford-2019]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Repartición Militar",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
