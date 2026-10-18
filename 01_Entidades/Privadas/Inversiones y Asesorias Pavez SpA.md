---
tipo_nodo: entidad_privada
rut: "77.123.456-9"
razon_social: "Inversiones y Asesorías Pavez SpA"
fecha_constitucion: 2018-04-12
objeto_social: "Inversiones de capital, asesorías tributarias, contables y financieras de empresas"
representante_legal: "[[Jose Antonio Pavez Campillay]]"
tags:
  - entidad/privada
  - megafraude-sii
  - operacion-tributos
  - empresa-fachada
---

# Inversiones y Asesorias Pavez SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador**: [[Jose Antonio Pavez Campillay]]

## Contexto en Investigaciones Forenses
Sociedad instrumental y matriz operativa utilizada por [[Jose Antonio Pavez Campillay]] y su contadora [[Ximena Jimenez Faras]] en el [[Caso Megafraude Tributario Operacion Tributos]]. Según la formalización del Ministerio Público y la querella del [[Servicio Impuestos Internos]], la sociedad actuó como nodo concentrador para la facturación falsa, canalización de fondos ilícitos procedentes de devoluciones tributarias espurias y distribución de comisiones ilegales a intermediarios.

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
