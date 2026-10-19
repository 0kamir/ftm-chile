---
tipo_nodo: persona
rut: ""
aliases:
  - "Camila Polizzi"
  - "Camila Polizzi Fonceca"
rol_principal: "Gestora y Administradora de Convenio Fundación En Ti"
afiliacion_politica: "Independiente (Ex candidata Alcaldesa y Diputada)"
situacion_procesal: formalizado
medida_cautelar: "Arresto domiciliario total y arraigo nacional"
tags:
  - entidad/persona
  - caso-convenios
  - biobio
---

# Camila Polizzi Fonceca

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Fundacion En Ti]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Imputada en la arista regional del [[Caso Convenios]] en el Biobío por estafa, falsificación de documento oficial, usurpación de identidad y [[Lavado de Activos]] / [[Fraude al Fisco]]. Gestionó la adjudicación del convenio [[TRX-2022-12-20-Convenio-EnTi-01]] con el [[GORE Biobio]] (encabezado por [[Rodrigo Diaz Worner]]) utilizando la personalidad jurídica de [[Fundacion En Ti]] por **$250.635.000 CLP** según consta en la [[Resolucion-GORE-Biobio-EnTi-2022]].

## Auditoría Contable: Montos Recibidos como Firmante de Destino
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

dv.header(4, `Monto Total Suscrito (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Firmante Origen", "Monto (CLP)", "Causa"],
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
