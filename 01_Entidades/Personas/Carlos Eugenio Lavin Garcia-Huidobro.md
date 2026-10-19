---
tipo_nodo: persona
rut: ""
aliases:
  - "Carlos Eugenio Lavín"
rol_principal: "Cofundador y Controlador de Empresas Penta S.A."
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Condena cumplida en libertad vigilada, multa fiscal y clases de ética empresarial"
vinculos_familiares:
  - "[[Cathy Barriga Guerra]]"
tags:
  - entidad/persona
  - caso-penta
  - condenado
  - clan-lavin-barriga
---

# Carlos Eugenio Lavin Garcia-Huidobro

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Empresas Penta SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Tío político por afinidad extendida de [[Cathy Barriga Guerra]], a través de su primo hermano Joaquín Lavín Infante y su sobrino Joaquín Lavín León)*
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Cofundador y controlador de [[Empresas Penta SA]] junto a [[Carlos Alberto Delano Abbott]]. Condenado en el [[Caso Penta]] ([[Sentencia-8Juzgado-Garantia-Penta-2018]]) por delitos tributarios reiterados tras articular pagos irregulares a campañas de la [[Union Democrata Independiente]] ([[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]]) y pagos periódicos al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]). La Fiscalía retiró la imputación de soborno en el procedimiento abreviado de 2018.

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
