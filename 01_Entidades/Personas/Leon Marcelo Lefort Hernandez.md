---
tipo_nodo: persona
rut: "10.394.820-7"
aliases:
  - "Marcelo Lefort"
  - "León Marcelo Lefort Hernández"
rol_principal: "Fundador y Ex Gerente General de Itelecom Holding Chile SpA"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Arresto domiciliario (sustituyó la prisión preventiva en julio de 2021)"
tags:
  - entidad/persona
  - caso-luminarias-led
  - condenado
  - empresario
---

# Leon Marcelo Lefort Hernandez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Itelecom Holding Chile SpA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero y controlador de [[Itelecom Holding Chile SpA]]. Imputado en el [[Caso Luminarias LED]] por soborno a funcionarios de al menos 24 instituciones públicas, según la Fiscalía, incluida la licitación de la [[Municipalidad de Chillan]] ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]). Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

## Auditoría Contable: Montos Operados como Firmante de Origen
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

dv.header(4, `Monto Total Operado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Destino", "Contraparte", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_destino,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
