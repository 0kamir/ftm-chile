---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Inversiones y Centro de Eventos El Bosque Limitada (Go Fitness)"
fecha_constitucion: 1998-04-14
objeto_social: "Inversiones inmobiliarias, administración de centros deportivos, gimnasios, estética y eventos"
representante_legal: "[[Claudio Spiniak Vilensky]]"
tags:
  - entidad/privada
  - caso-spiniak
  - sociedad-pantalla
---

# Inversiones El Bosque Ltda

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`

## Contexto en Investigaciones
Sociedad instrumental controlada por [[Claudio Spiniak Vilensky]] a través de la cual operaba el gimnasio *Go Fitness* en calle El Bosque Norte (Las Condes) y propiedades en El Arrayán. En el marco del [[Caso Spiniak]], el [[Servicio Impuestos Internos]] y la instrucción judicial del ministro [[Sergio Munoz Gajardo]] auditaron el uso de la sociedad para encubrir egresos ilícitos, gastos rechazados y evasión tributaria ([[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]]), documentados en [[Sentencia-Corte-Suprema-CasoSpiniak-2008]].

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte / Fiscalizador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
