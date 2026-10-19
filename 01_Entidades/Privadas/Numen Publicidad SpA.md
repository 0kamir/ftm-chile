---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Numen Publicidad SpA"
fecha_constitucion: 2020-07-15
objeto_social: "Servicios de publicidad, comunicación estratégica, marketing digital, análisis de redes sociales y sondeos de opinión"
representante_legal: "[[Fernando Cerimedo]]"
tags:
  - entidad/privada
  - agencia-digital
  - numen
  - redes-sociales
  - cerimedo
---

# Numen Publicidad SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador / Fundador**: [[Fernando Cerimedo]] (junto a socios locales chilenos)

## Contexto en Investigaciones y Electorales
Filial chilena de la agencia de marketing digital fundada por el estratega argentino [[Fernando Cerimedo]]. La entidad operó en Chile realizando sondeos de opinión pública digital y coordinando campañas de difusión y posicionamiento en redes sociales durante los ciclos electorales de 2020 a 2022.

En el marco del [[Caso Operaciones Digitales e Injerencia Electoral]], la sociedad y sus cuentas bancarias e infraestructura informática han sido objeto de oficios del Congreso y requerimientos de la Fiscalía Centro Norte para verificar la trazabilidad de fondos, la ausencia de facturación en las rendiciones de partidos ante el Servel y la eventual prestación de servicios mediante redes automatizadas en la campaña del Plebiscito de 2022.

## Registros Reificados
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
