---
tipo_nodo: persona
rut: "8.492.310-9"
aliases:
  - "Fernando León"
rol_principal: "Ex Gerente General de KDM Empresas S.A. / Demarco S.A."
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Acusación por soborno reiterado a autoridades municipales en licitaciones de residuos"
tags:
  - entidad/persona
  - caso-basura
---

# Fernando Leon Steffens

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[KDM Empresas SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Estado Procesal**: `= this.medida_cautelar`

## Síntesis Forense
Ejecutivo principal y representante de [[KDM Empresas SA]] (consorcio Demarco S.A. / Starco S.A.). En el [[Caso Basura]] ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]), la Fiscalía Regional Metropolitana Occidente le imputó haber autorizado el desvío de fondos societarios mediante sociedades pantalla para pagar coimas a concejales de la [[Municipalidad de Maipu]] articulados por [[Marcelo Torres Ferrari]], asegurando la adjudicación de la licitación de recolección de residuos domiciliarios por **$18.500.000.000 CLP** ([[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]]).

## Auditoría Contable: Montos Autorizados como Firmante de Origen
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
