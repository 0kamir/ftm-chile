---
tipo_nodo: persona
rut: ""
aliases:
  - "Jaime Orpis"
  - "Senador Jaime Orpis Bouchon"
rol_principal: "Ex Senador de la República (Circunscripción I, Tarapacá y Arica)"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Condena cumplida (5 años y 1 día de presidio efectivo por cohecho y fraude al fisco)"
tags:
  - entidad/persona
  - caso-corpesca
  - condenado
  - ex-senador
---

# Jaime Orpis Bouchon

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Senado de la Republica de Chile]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Abogado y exsenador de [[Union Democrata Independiente]]. Fue condenado por sentencia firme en el [[Caso Corpesca]] ([[Sentencia-3TOP-Santiago-Corpesca-2020]]) como autor de seis delitos de [[Fraude al Fisco]] y dos delitos de [[Cohecho]] pasivo tras recibir **$233.000.000 CLP** desde [[Corpesca SA]] (autorizados por [[Francisco Mujica Ortuzar]]) mediante boletas de honorarios ideológicamente falsas emitidas por terceros ([[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]]) mientras integraba comisiones legislativas en el [[Senado de la Republica de Chile]].

## Auditoría Contable: Montos Recibidos como Firmante/Destinatario
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
  ["Transacción / Nexo", "Fecha", "Empresa Pagadora", "Ejecutivo Origen", "Monto (CLP)", "Causa"],
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
