---
tipo_nodo: persona
rut: "6.418.923-9"
aliases:
  - "Claudio Spiniak"
rol_principal: "Empresario y Controlador de Inversiones El Bosque Ltda. (Gimnasio Go Fitness)"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena cumplida (12 años de presidio mayor en su grado medio ratificados por la Corte Suprema)"
tags:
  - entidad/persona
  - caso-spiniak
  - sector-privado
---

# Claudio Spiniak Vilensky

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Empresario propietario del centro de eventos y gimnasio *Go Fitness* en avenida El Bosque Norte (Las Condes), operado mediante [[Inversiones El Bosque Ltda]]. Detenido el 30 de septiembre de 2003 como cabecilla de la red investigada en el [[Caso Spiniak]], el [[Servicio Impuestos Internos]] y los peritajes contables ordenados por el ministro [[Sergio Munoz Gajardo]] auditaron el desvío de recursos societarios, gastos rechazados y ocultamiento patrimonial destinados a financiar la red ilícita ([[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]]). En 2008, la [[Corte Suprema de Chile]] elevó su condena definitiva a 12 años de presidio efectivo ([[Sentencia-Corte-Suprema-CasoSpiniak-2008]]).

## Auditoría Contable: Montos Imputados como Autorizador de Origen
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

dv.header(4, `Monto Total Asociado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
