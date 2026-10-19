---
tipo_nodo: persona
rut: ""
aliases:
  - "Leonardo Osses"
  - "Leonardo Osses Sandoval"
rol_principal: "Ex Capitán de Carabineros e Integrante Operativo de la UIOE en La Araucanía"
afiliacion_politica: "Militar / Carabineros"
situacion_procesal: condenado
medida_cautelar: "Condenado a 10 años de presidio efectivo por el TOP de Temuco (Falsificación de instrumento público y obstrucción a la investigación) — sentencia no firme: recursos de nulidad pendientes (2026)"
tags:
  - entidad/persona
  - caso-operacion-huracan
  - dipolcar
  - uioe
  - condenado
---

# Leonardo Osses Sandoval

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Inteligencia Policial de Carabineros]] / UIOE)
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Condena Ejecutoriada / Cautelar**: `= this.medida_cautelar`

## Síntesis Forense
Capitán de Carabineros y analista operativo de la Unidad de Inteligencia Operativa Especializada (UIOE) en Temuco. Trabajó en estrecho contacto con el civil [[Alex Smith Leay]], participando activamente en la redacción de los oficios policiales e implantación de conversaciones falsas en los teléfonos móviles incautados durante la [[Caso Operacion Huracan]]. 

En el juicio oral ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]), el tribunal acreditó que Osses remitió por correo electrónico borradores de los textos que luego aparecieron falsamente atribuidos a los comuneros mapuche ([[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]]), siendo sentenciado a **10 años de presidio efectivo** como autor de [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]].

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
