---
tipo_nodo: persona
rut: "7.014.892-7"
aliases:
  - "Luis Hermosilla"
  - "Luis Hermosilla Osorio"
rol_principal: "Abogado Penalista y Asesor Legal"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva / Arresto domiciliario total"
tags:
  - entidad/persona
  - caso-audios
  - abogado
---

# Luis Hermosilla Osorio

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Abogado penalista formalizado en el [[Caso Audios]] por delitos reiterados de [[Cohecho]], [[Lavado de Activos]] y delitos tributarios. En la reunión grabada en [[Audio-Reunion-Edificio-Alonso-2023]], coordinó junto a [[Leonarda Villalobos Muth]] el esquema de pagos ilícitos [[TRX-2023-06-22-Reunion-Audios-01]] desde operaciones vinculadas a [[Factop SpA]] hacia funcionarios del [[Servicio Impuestos Internos]]. Asimismo, encabezó la defensa en la Acusación Constitucional de diciembre de 2019 de su socio de oficina y exministro del Interior [[Andres Chadwick Pinera]] (primo de [[Sebastian Pinera Echenique]]), transfiriéndole más de **`$190.000.000 CLP`** desde fondos originados en [[Factop SpA]] ([[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]) y articulando gestiones de [[Trafico de Influencias]] ante la [[Corte Suprema de Chile]] con [[Angela Vivanco Martinez]] ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) y coordinaciones en nombramientos judiciales con el penalista [[Gabriel Zaliasnik Schilkrut]] ([[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]]).

## Auditoría Contable: Montos Operados como Firmante/Operador de Origen
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && (
    p.firmante_origen.path === dv.current().file.path ||
    String(p.firmante_origen).includes(dv.current().file.name)
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

dv.header(4, `Monto Total Operado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Contraparte", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
