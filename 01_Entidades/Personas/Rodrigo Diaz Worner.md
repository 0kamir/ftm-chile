---
tipo_nodo: persona
rut: ""
aliases:
  - "Rodrigo Díaz"
  - "Rodrigo Díaz Wörner"
rol_principal: "Gobernador Regional del Biobío (2021-2025)"
afiliacion_politica: "Independiente (Ex DC)"
situacion_procesal: testigo
medida_cautelar: ""
tags:
  - entidad/persona
  - caso-convenios
  - gore-biobio
---

# Rodrigo Diaz Worner

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[GORE Biobio]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Máxima autoridad ejecutiva del [[GORE Biobio]] durante la suscripción del convenio [[TRX-2022-12-20-Convenio-EnTi-01]] con [[Fundacion En Ti]] (gestionada por [[Camila Polizzi Fonceca]]), respaldado en la [[Resolucion-GORE-Biobio-EnTi-2022]] e investigado en el [[Caso Convenios]].

## Montos Autorizados como Firmante de Origen
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

dv.header(4, `Monto Total Autorizado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Firmante Destino", "Monto (CLP)", "Causa"],
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
