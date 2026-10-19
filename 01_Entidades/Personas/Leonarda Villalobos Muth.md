---
tipo_nodo: persona
rut: ""
aliases:
  - "Leonarda Villalobos"
  - "María Leonarda Villalobos Muth"
rol_principal: "Abogada y Asesora Tributaria"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva"
tags:
  - entidad/persona
  - caso-audios
  - abogada
---

# Leonarda Villalobos Muth

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Abogada formalizada en el [[Caso Audios]] por [[Cohecho]], [[Lavado de Activos]] y delitos tributarios. Registró y participó en la reunión del edificio Alonso de Córdova ([[Audio-Reunion-Edificio-Alonso-2023]]) con [[Luis Hermosilla Osorio]], donde, según el audio difundido por CIPER, se mencionaron pagos por **$100.000.000 CLP** ([[TRX-2023-06-22-Reunion-Audios-01]]) desde el entorno de [[Factop SpA]] hacia funcionarios del [[Servicio Impuestos Internos]].

## Montos Canalizados como Firmante/Operadora de Destino
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && (
    p.firmante_destino.path === dv.current().file.path ||
    String(p.firmante_destino).includes(dv.current().file.name)
  ));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Canalizado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Operador Origen", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
