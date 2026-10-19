---
tipo_nodo: persona
rut: ""
aliases:
  - "Álex Smith"
  - "Álex Smith Leay"
  - "El Profesor"
rol_principal: "Creador Civil del Software Antorcha y Asesor de Inteligencia de la UIOE / DIPOLCAR"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condenado a 12 años de presidio efectivo por el TOP de Temuco (Falsificación de instrumento público y obstrucción a la investigación) — sentencia no firme: recursos de nulidad pendientes (2026)"
tags:
  - entidad/persona
  - caso-operacion-huracan
  - dipolcar
  - condenado
---

# Alex Smith Leay

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Condena Ejecutoriada / Cautelar**: `= this.medida_cautelar`

## Síntesis
Contratado a honorarios por la [[Direccion de Inteligencia Policial de Carabineros]] bajo el alias de *«El Profesor»*. Fue el ideólogo del supuesto software espía «Antorcha» y «Tubicación», herramientas ficticias que según la plana mayor de Carabineros interceptaban conversaciones de mensajería cifrada. 

En el juicio oral del [[Caso Operacion Huracan]], el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]) acreditó que Smith fabricó y proveyó los archivos de texto falsos (`.txt`) que fueron implantados manualmente en los teléfonos incautados a comuneros mapuche ([[TRX-2017-09-23-Detenciones-OperacionHuracan-01]]), cobrando honorarios y gastos reservados ([[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]]). Fue sentenciado a la pena más alta del caso: **12 años de presidio efectivo** como autor reiterado de [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]].

## Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Imputado / Percibido: ${formattedTotal}`);
dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Monto (CLP)", "Delito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.delito_imputado
  ])
);
```
