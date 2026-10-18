---
tipo_nodo: causa_judicial
ruc: "2300674512-K"
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía Regional de Antofagasta / Juzgado de Garantía de Antofagasta"
fiscal_a_cargo: "Juan Castro Bekios / Cristian Aguilar"
estado_judicial: formalizada
delito_principal: "[[Fraude al Fisco]]"
tags:
  - causa
  - caso-convenios
  - antofagasta
---

# Caso Convenios (Arista Democracia Viva)

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal`

## Resumen Ejecutivo
Investigación penal iniciada de oficio en junio de 2023 por la Fiscalía Regional de Antofagasta a raíz de la suscripción de tres convenios por trato directo entre la [[Seremi MINVU Antofagasta]] (encabezada por [[Carlos Contreras Gutierrez]]) y la [[Fundacion Democracia Viva]] (presidida por [[Daniel Andrade Schwarze]]), ambos militantes del partido [[Revolucion Democratica]].

El monto total transferido bajo el Programa de Asentamientos Precarios alcanzó los **$426.000.000 CLP**, fraccionados en tres resoluciones exentas para eludir el trámite de Toma de Razón ante la Contraloría General de la República. El Consejo de Defensa del Estado (CDE) presentó querella criminal por el delito de fraude al fisco reiterado.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Firmante Origen",
  firmante_destino AS "Firmante Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Entidades e Imputados Clave en la Arista
- **Órgano Público Emisor**: [[Seremi MINVU Antofagasta]]
- **Entidad Privada Receptora**: [[Fundacion Democracia Viva]]
- **Partido Político Relacionado**: [[Revolucion Democratica]]
- **Funcionarios / Particulares Formalizados**:
  - [[Carlos Contreras Gutierrez]] (Ex Seremi MINVU Antofagasta)
  - [[Daniel Andrade Schwarze]] (Representante Legal de Democracia Viva)
- **Evidencia Documental Base**: [[Resolucion-Exenta-MINVU-Antofagasta-2022]]
