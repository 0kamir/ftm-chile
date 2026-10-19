---
tipo_nodo: partido_politico
rut: ""
sigla: "PC"
fecha_fundacion: "1912-06-04"
coalicion: "Apruebo Dignidad / Unidad por Chile"
estado_registro: "Vigente"
tags:
  - entidad/partido
  - apruebo-dignidad
  - caso-sierra-bella
---

# Partido Comunista de Chile

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Militantes y Autoridades Vinculadas en el Vault
```dataview
TABLE WITHOUT ID
  file.link AS "Persona",
  rol_principal AS "Rol Principal",
  situacion_procesal AS "Situación Procesal",
  medida_cautelar AS "Medida Cautelar"
FROM "01_Entidades/Personas"
WHERE contains(string(afiliacion_politica), this.file.name)
```
