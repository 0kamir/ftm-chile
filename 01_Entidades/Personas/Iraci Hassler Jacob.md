---
tipo_nodo: persona
rut: ""
aliases:
  - "Irací Hassler"
rol_principal: "Ex Alcaldesa de la Municipalidad de Santiago (2021-2024)"
afiliacion_politica: "[[Partido Comunista de Chile]]"
situacion_procesal: imputado
medida_cautelar: "Investigación penal desformalizada y sumario de Contraloría por compraventa de Clínica Sierra Bella"
tags:
  - entidad/persona
  - caso-sierra-bella
  - partido-comunista
---

# Iraci Hassler Jacob

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Santiago]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Estado Procesal**: `= this.medida_cautelar`

## Síntesis Forense
Economista, militante del [[Partido Comunista de Chile]] y ex Alcaldesa de la [[Municipalidad de Santiago]]. En el [[Caso Sierra Bella]], impulsó la compra, aprobada por el concejo municipal, de la ex Clínica Sierra Bella con [[Inmobiliaria San Valentino SpA]] ([[Felipe Sanchez Perez]]) por **$8.200.000.000 CLP** ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]), operación cuyos pagos fueron paralizados por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) mediante el [[Dictamen-CGR-SierraBella-2023]] al constatarse que el precio cuadruplicaba el avalúo fiscal y el valor de compra previa sin justificación técnica verificable. La municipalidad finalmente no perseveró en la compra; la investigación penal no tiene formalizaciones conocidas.

## Auditoría Contable: Montos Suscritos como Firmante de Origen
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

dv.header(4, `Monto Total Suscrito (firmante_origen): ${formattedTotal}`);
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
