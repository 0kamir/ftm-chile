---
tipo_nodo: persona
rut: "9.624.180-1"
aliases:
  - "Jaime Paz"
  - "Coronel Jaime Paz Meneses"
rol_principal: "Ex Coronel de Intendencia de Carabineros"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Cumplimiento de condena efectiva (presidio mayor)"
tags:
  - entidad/persona
  - caso-pacogate
  - condenado
---

# Jaime Paz Meneses

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Finanzas de Carabineros]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ex Coronel de Intendencia en la [[Direccion de Finanzas de Carabineros]]. Condenado por sentencia firme ([[Sentencia-TOP-Santiago-Pacogate-2021]]) en el [[Caso Pacogate]] por [[Malversacion de Caudales Publicos]], [[Lavado de Activos]] y asociación ilícita, tras operar junto a [[Flavio Echeverria Cortez]] el mecanismo de nóminas adulteradas que sustrajo **$28.348.928.198 CLP** ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]).

## Auditoría Contable: Montos Operados como Firmante de Destino
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

dv.header(4, `Monto Total Condenado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Órgano Afectado", "Jefe Cúpula", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
