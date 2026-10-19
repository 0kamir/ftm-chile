---
tipo_nodo: persona
rut: ""
aliases:
  - "Cathy Barriga"
  - "Cathy Carolina Barriga Guerra"
rol_principal: "Ex Alcaldesa de la Municipalidad de Maipú (2016-2021)"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva / Arresto domiciliario total"
vinculos_familiares:
  - "[[Carlos Eugenio Lavin Garcia-Huidobro]]"
tags:
  - entidad/persona
  - caso-maipu
  - alcaldesa
  - clan-lavin-barriga
---

# Cathy Barriga Guerra

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Maipu]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Sobrina política por afinidad extendida de [[Carlos Eugenio Lavin Garcia-Huidobro]], en tanto cónyuge del diputado Joaquín Lavín León y nuera de Joaquín Lavín Infante)*
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Exalcaldesa de la [[Municipalidad de Maipu]] y ex Consejera Regional, electa en el cupo de [[Union Democrata Independiente]]. Fue formalizada por la Fiscalía Metropolitana Oriente en el [[Caso Municipalidad de Maipu]] por delitos reiterados de [[Fraude al Fisco]] y falsificación de instrumento público por un perjuicio patrimonial de **$30.972.000.000 CLP** ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]), acreditado en el [[Informe-Contraloria-Municipalidad-Maipu-2021]].

## Auditoría Contable: Montos Imputados como Firmante de Origen
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

dv.header(4, `Monto Total Imputado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Monto (CLP)", "Delito", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.delito_imputado,
    p.causa_vinculada
  ])
);
```
