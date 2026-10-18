---
tipo_nodo: persona
rut: "7.319.480-6"
aliases:
  - "Roberto Lewin"
rol_principal: "Gerente General y Controlador de Gestión Ambiental y Territorial S.A. (GESCAM)"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada a pena remitida y pago solidario de perjuicio fiscal"
tags:
  - entidad/persona
  - caso-mop-gate
  - condenado
---

# Roberto Lewin Valdivieso

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Gestion Ambiental y Territorial SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero y controlador de la consultora [[Gestion Ambiental y Territorial SA]] (GESCAM S.A.). Fue condenado en el [[Caso MOP-Gate]] ([[Sentencia-Corte-Suprema-MOPGate-2016]]) por su participación en el esquema de [[Fraude al Fisco]] articulado con el ex Ministro [[Carlos Cruz Lorenzen]] en el [[Ministerio de Obras Publicas]] ([[TRX-2001-08-20-Contratos-Simulados-MOP-GESCAM-01]]) y por la emisión de facturación ideológicamente falsa para triangular fondos ante el [[Servicio Impuestos Internos]] ([[TRX-2002-04-12-Facturas-Triangulacion-GESCAM-SII-01]]).

## Auditoría Contable: Montos Operados como Firmante
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Operado en Nexos: ${formattedTotal}`);
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
