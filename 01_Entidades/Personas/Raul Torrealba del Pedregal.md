---
tipo_nodo: persona
rut: ""
aliases:
  - "Raúl Torrealba"
  - "El Tronco"
rol_principal: "Ex Alcalde de la Municipalidad de Vitacura (1996-2021)"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: formalizado
medida_cautelar: "Arresto domiciliario total y arraigo nacional (previa prisión preventiva)"
tags:
  - entidad/persona
  - caso-vitacura
  - alcalde
---

# Raul Torrealba del Pedregal

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Vitacura]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Exalcalde de la [[Municipalidad de Vitacura]] y exmilitante histórico de [[Renovacion Nacional]]. Fue formalizado en el [[Caso Vitacura]] por 29 delitos de [[Fraude al Fisco]] / [[Malversacion de Caudales Publicos]], asociación ilícita, delitos tributarios y [[Lavado de Activos]], tras acreditarse mediante la autodenuncia de [[Domingo Prieto Urrejola]] ([[Declaracion-Judicial-Prieto-Vitacura-2021]]) el desvío sistemático de subvenciones municipales otorgadas a [[Vita Deportes]] ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]).

## Auditoría Contable: Montos Autorizados como Firmante de Origen
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
