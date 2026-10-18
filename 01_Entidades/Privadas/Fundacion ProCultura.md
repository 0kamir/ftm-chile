---
tipo_nodo: entidad_privada
rut: "65.034.810-9"
razon_social: "Fundación ProCultura"
fecha_constitucion: "2010-03-18"
objeto_social: "Promoción cultural, patrimonio, identidad territorial y proyectos comunitarios"
representante_legal: "[[Alberto Larrain Salas]]"
tags:
  - entidad/privada
  - fundacion
  - caso-convenios
  - nodo-puente
---

# Fundacion ProCultura

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Director Ejecutivo**: `= this.representante_legal`

## Rol Topológico en la Red (Nodo Puente Multirregional)
En la arquitectura del grafo del [[Caso Convenios]], **Fundación ProCultura** opera como un **nodo puente de alta centralidad de intermediación (*Betweenness Centrality*)**: conecta simultáneamente a la [[Seremi MINVU Antofagasta]] (vía [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] por **$500.000.000 CLP**) y al [[GORE Biobio]] (vía [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] por **$2.553.000.000 CLP**), articulando en una misma red a autoridades de distintas regiones bajo la representación de [[Alberto Larrain Salas]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_origen AS "Autorizador Público",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
