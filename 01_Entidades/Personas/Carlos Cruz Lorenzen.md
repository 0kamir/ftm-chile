---
tipo_nodo: persona
rut: ""
aliases:
  - "Carlos Cruz"
rol_principal: "Ex Ministro de Obras Públicas (2000-2002) y Ex Coordinador General de Concesiones"
afiliacion_politica: "[[Partido Socialista de Chile]]"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada de 3 años de pena remitida e indemnización fiscal por fraude al fisco"
tags:
  - entidad/persona
  - caso-mop-gate
  - condenado
---

# Carlos Cruz Lorenzen

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Ministerio de Obras Publicas]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Ex Ministro de Obras Públicas y militante del [[Partido Socialista de Chile]]. Fue condenado por la Ministra en Visita Gloria Ana Chevesich y ratificado por la [[Corte Suprema de Chile]] en el [[Caso MOP-Gate]] ([[Sentencia-Corte-Suprema-MOPGate-2016]]) como autor del delito reiterado de [[Fraude al Fisco]], tras articular junto a [[Hector Pena Veliz]] ([[Gestion Ambiental y Territorial SA]]) la suscripción de contratos abultados y simulados en el [[Ministerio de Obras Publicas]] por **$1.253.000.000 CLP** para financiar sobresueldos de directivos públicos ([[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]).

## Montos Autorizados como Firmante de Origen
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name));

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
  ["Transacción / Nexo", "Fecha", "Origen", "Destino", "Monto (CLP)", "Causa"],
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
