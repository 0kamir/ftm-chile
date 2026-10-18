---
tipo_nodo: persona
rut: "7.584.210-4"
aliases:
  - "Luis Plaza"
rol_principal: "Ex Alcalde de la Municipalidad de Cerro Navia (2008-2016)"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: formalizado
medida_cautelar: "Acusación fiscal por fraude al fisco reiterado en contratos municipales (Caso Basura)"
tags:
  - entidad/persona
  - caso-basura
  - renovacion-nacional
---

# Luis Plaza Sanchez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Cerro Navia]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Estado Procesal**: `= this.medida_cautelar`

## Síntesis Forense
Ex Alcalde de la [[Municipalidad de Cerro Navia]] y militante de [[Renovacion Nacional]]. En el [[Caso Basura]] ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]), fue formalizado y acusado por la Fiscalía Regional Metropolitana Occidente junto a su entonces administrador municipal [[Marcelo Torres Ferrari]] por el delito de [[Fraude al Fisco]] en contrataciones y licitaciones municipales de aseo y servicios conexos a la red de [[KDM Empresas SA]] por **$1.120.000.000 CLP** ([[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]]).

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
