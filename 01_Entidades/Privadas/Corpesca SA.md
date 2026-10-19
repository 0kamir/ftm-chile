---
tipo_nodo: entidad_privada
rut: "96.893.820-7"
razon_social: "Corpesca S.A."
fecha_constitucion: "1999-11-05"
objeto_social: "Pesca industrial extractiva, producción de harina y aceite de pescado"
representante_legal: "[[Francisco Mujica Ortuzar]]"
estado_verificacion: parcial
fuentes:
  - url: "https://snifa.sma.gob.cl/General/Descargar/1104217912"
    titulo: "Expediente de fiscalización con RUT de Corpesca S.A."
    medio: "Superintendencia del Medio Ambiente"
    tipo: primaria
    consultado: 2026-10-19
tags:
  - entidad/privada
  - pesquera
  - caso-corpesca
  - persona-juridica-condenada
---

# Corpesca SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Gerente General en Período Condenado**: `= this.representante_legal`

## Contexto Forense y Societario
Empresa pesquera industrial condenada penalmente como persona jurídica (bajo la Ley N° 20.393) en el [[Caso Corpesca]] ([[Sentencia-3TOP-Santiago-Corpesca-2021]]) al pago de 10.000 UTM y publicación de extracto de la sentencia por el delito de [[Cohecho]] activo (soborno), tras financiar con **$233.000.000 CLP** ([[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]]) al entonces senador [[Jaime Orpis Bouchon]] en el [[Senado de la Republica de Chile]].

## Historial de Nexos y Pagos Investigados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Ejecutivo",
  firmante_destino AS "Parlamentario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
