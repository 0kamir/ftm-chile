---
tipo_nodo: partido_politico
rut: "65.012.340-9"
sigla: "RN"
fecha_fundacion: "1987-04-29"
coalicion: "Chile Vamos"
estado_registro: "Vigente"
tags:
  - entidad/partido
  - chile-vamos
---

# Renovacion Nacional

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Rol en el Análisis de Redes
Partido político en el que militó históricamente el exalcalde de la [[Municipalidad de Vitacura]], [[Raul Torrealba del Pedregal]], hasta su renuncia tras la apertura del [[Caso Vitacura]].

Asimismo, en el marco del [[Caso Operaciones Digitales e Injerencia Electoral]], se documentó la presencia física del consultor digital [[Fernando Cerimedo]] en la sede central del partido durante la noche del 4 de septiembre de 2022 ([[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]), acreditada mediante la evidencia [[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]].

## Nexos y Operaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  delito_imputado AS "Delito / Infracción",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

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
