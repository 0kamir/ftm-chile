---
tipo_nodo: entidad_privada
rut: "76.987.654-5"
razon_social: "Comercializadora y Exportadora Global SpA"
fecha_constitucion: 2019-08-25
objeto_social: "Exportación e importación de insumos tecnológicos, materias primas y bienes de consumo"
representante_legal: "[[Jose Antonio Pavez Campillay]]"
tags:
  - entidad/privada
  - megafraude-sii
  - operacion-tributos
  - empresa-fantasma
  - iva-exportador
---

# Comercializadora y Exportadora Global SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador**: [[Jose Antonio Pavez Campillay]]

## Contexto en Investigaciones Forenses
Empresa fantasma creada y controlada por el Clan Pavez dentro del [[Caso Megafraude Tributario Operacion Tributos]]. Utilizada para simular operaciones de exportación de mercancías inexistentes o sobrevaloradas, solicitando fraudulentamente la devolución del IVA exportador ante el [[Servicio Impuestos Internos]] y canalizando los flujos hacia esquemas de [[Lavado de Activos]].

## Auditoría Contable: Registros Reificados
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
