---
tipo_nodo: persona
rut: ""
aliases:
  - "Marcelo Teuber"
  - "Marcelo Teuber Muñoz"
rol_principal: "Ex Coronel de Carabineros y Ex Jefe de la UIOE en La Araucanía"
afiliacion_politica: "Militar / Carabineros"
situacion_procesal: condenado
medida_cautelar: "Condenado a 3 años y un día más 100 días de presidio por el TOP de Temuco"
tags:
  - entidad/persona
  - caso-operacion-huracan
  - dipolcar
  - uioe
  - condenado
---

# Marcelo Teuber Munoz

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Inteligencia Policial de Carabineros]] / UIOE)
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Condena Ejecutoriada / Cautelar**: `= this.medida_cautelar`

## Síntesis Forense
Coronel de Carabineros y jefe directo de la Unidad de Inteligencia Operativa Especializada (UIOE) en La Araucanía durante el desarrollo de la [[Caso Operacion Huracan]]. Estuvo a cargo de la coordinación territorial del operativo policial de detención y de visar administrativamente los oficios policiales remitidos a la Fiscalía de Temuco con base en la información fraudulenta provista por [[Alex Smith Leay]] y [[Leonardo Osses Sandoval]].

En el juicio oral ante el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2024]]), fue sentenciado a penas que sumaron **3 años y un día más 100 días de presidio** por [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]], conmutadas a penas sustitutivas.

## Auditoría Contable: Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Delito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    p.delito_imputado
  ])
);
```
