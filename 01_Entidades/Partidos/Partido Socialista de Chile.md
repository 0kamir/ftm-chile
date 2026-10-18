---
tipo_nodo: partido_politico
rut: "65.014.320-5"
sigla: "PS"
fecha_fundacion: "1933-04-19"
coalicion: "Socialismo Democrático (ex Concertación)"
estado_registro: "Vigente"
tags:
  - entidad/partido
  - socialismo-democratico
  - caso-mop-gate
---

# Partido Socialista de Chile

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
