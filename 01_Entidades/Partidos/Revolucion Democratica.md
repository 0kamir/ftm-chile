---
tipo_nodo: partido_politico
rut: ""
sigla: "RD"
fecha_fundacion: "2012-01-07"
coalicion: "Frente Amplio"
estado_registro: "Fusionado en Partido Frente Amplio (2024)"
tags:
  - entidad/partido
  - frente-amplio
---

# Revolucion Democratica

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Rol en el Análisis de Redes (Caso Convenios)
Partido político al cual pertenecían tanto el autorizador público [[Carlos Contreras Gutierrez]] (ex jefe de gabinete parlamentario y ex titular de la [[Seremi MINVU Antofagasta]]) como el receptor privado [[Daniel Andrade Schwarze]] (presidente de la [[Fundacion Democracia Viva]]). Tras el estallido del [[Caso Convenios]], el Tribunal Supremo de la colectividad cursó la expulsión de ambos militantes.

## Militantes y Exmilitantes Registrados en el Vault
```dataview
TABLE WITHOUT ID
  file.link AS "Persona",
  rol_principal AS "Rol Principal",
  situacion_procesal AS "Situación Procesal",
  medida_cautelar AS "Medida Cautelar"
FROM "01_Entidades/Personas"
WHERE contains(string(afiliacion_politica), this.file.name)
```
