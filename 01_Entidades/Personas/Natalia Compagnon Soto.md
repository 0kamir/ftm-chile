---
tipo_nodo: persona
rut: "15.324.810-9"
aliases:
  - "Natalia Compagnon"
rol_principal: "Socia Cofundadora de Exportadora y de Gestión Caval Ltda."
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada a pena remitida y multa por delitos tributarios (TOP Rancagua)"
tags:
  - entidad/persona
  - caso-caval
  - condenado
---

# Natalia Compagnon Soto

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Exportadora y de Gestion Caval Ltda]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Socia cofundadora del 50% de [[Exportadora y de Gestion Caval Ltda]] junto a [[Mauricio Valero Illanes]]. Fue condenada por el Tribunal de Juicio Oral en lo Penal de Rancagua en el [[Caso Caval]] ([[Sentencia-TOP-Rancagua-Caval-2018]]) como autora de delitos tributarios previstos en el artículo 97 N° 4 del Código Tributario por declaraciones maliciosamente falsas y contabilización de facturas ideológicamente falsas ante el [[Servicio Impuestos Internos]] ([[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]]).

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
