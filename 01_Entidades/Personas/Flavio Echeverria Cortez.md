---
tipo_nodo: persona
rut: "8.419.320-8"
aliases:
  - "Flavio Echeverría"
  - "General Flavio Echeverría Cortez"
rol_principal: "Ex General y Jefe de la Dirección de Finanzas de Carabineros"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Cumplimiento de condena efectiva (17 años de presidio mayor)"
tags:
  - entidad/persona
  - caso-pacogate
  - condenado
---

# Flavio Echeverria Cortez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Finanzas de Carabineros]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ex General de Intendencia y jefe de la [[Direccion de Finanzas de Carabineros]]. Fue condenado como líder de la asociación ilícita del [[Caso Pacogate]] por delitos reiterados de [[Malversacion de Caudales Publicos]] y [[Lavado de Activos]] por un monto acreditado en juicio oral de **$28.348.928.198 CLP** ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]), ejecutado junto a oficiales subordinados como [[Jaime Paz Meneses]] según consta en [[Sentencia-TOP-Santiago-Pacogate-2021]].

## Auditoría Contable: Montos Defraudados como Autorizador de Origen
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

dv.header(4, `Monto Total Condenado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Órgano Afectado", "Co-Imputado", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
