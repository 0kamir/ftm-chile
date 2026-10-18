---
tipo_nodo: persona
rut: "12.918.430-2"
aliases:
  - "Marcelo Campos"
  - "Marcelo Campos Henríquez"
rol_principal: "Ex Administrador Municipal y Asesor Jurídico de la Municipalidad de Chillán"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena efectiva por cohecho y lavado de activos (TOP de Chillán)"
tags:
  - entidad/persona
  - caso-luminarias-led
  - condenado
  - funcionario-municipal
---

# Marcelo Campos Henriquez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Chillan]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Abogado y exdirectivo de la [[Municipalidad de Chillan]]. Fue condenado en juicio oral por el Tribunal de Juicio Oral en lo Penal de Chillán ([[Sentencia-TOP-Chillan-Luminarias-2023]]) en el [[Caso Luminarias LED]] por los delitos de [[Cohecho]] pasivo y [[Lavado de Activos]], tras acreditarse que recibió sobornos de [[Itelecom Holding Chile SpA]] ([[Leon Marcelo Lefort Hernandez]]) para asegurar la adjudicación del contrato de recambio de alumbrado público por **$3.200.000.000 CLP** ([[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]).

## Auditoría Contable: Montos Asociados como Firmante/Destinatario
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && (
    p.firmante_destino.path === dv.current().file.path ||
    String(p.firmante_destino).includes(dv.current().file.name)
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

dv.header(4, `Monto Total Licitación Asociada (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Empresa Origen", "Pagador", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
