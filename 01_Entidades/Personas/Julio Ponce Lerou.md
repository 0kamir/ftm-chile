---
tipo_nodo: persona
rut: ""
aliases:
  - "Julio Ponce"
rol_principal: "Ex Presidente y Controlador de las Sociedades Cascada y de SQM S.A."
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Multa histórica ejecutoriada por la Corte Suprema (75.000 UF) en Caso Cascadas"
vinculos_familiares:
  - "[[Augusto Pinochet Ugarte]]"
  - "[[Lucia Hiriart Rodriguez]]"
tags:
  - entidad/persona
  - caso-cascadas
  - caso-sqm
  - condenado
  - familia-pinochet-hiriart
---

# Julio Ponce Lerou

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Sociedad de Inversiones Pampa Calichera SA]] / [[SQM SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Ex yerno de [[Augusto Pinochet Ugarte]] y [[Lucia Hiriart Rodriguez]])*
- **Situación Procesal**: `= this.situacion_procesal`
- **Sanción Judicial Ejecutoriada**: `= this.medida_cautelar`

## Síntesis
Ingeniero forestal, ex yerno de [[Augusto Pinochet Ugarte]] y [[Lucia Hiriart Rodriguez]], y controlador histórico de [[SQM SA]] a través de [[Sociedad de Inversiones Pampa Calichera SA]] tras las privatizaciones de fines de los años ochenta. En el [[Caso Cascadas]] fue sancionado por la [[Comision para el Mercado Financiero]] ([[Carlos Pavez Tolosa]]) mediante la [[Resolucion-SVS-CasoCascadas-2014]] —confirmada en última instancia por la [[Corte Suprema de Chile]]— como ideólogo y beneficiario de un esquema de compraventas bursátiles trianguladas con títulos de [[SQM SA]] (gerenciada por su hombre de confianza [[Patricio Contesse Gonzalez]]) que generó perjuicios registrados e infracciones por **$24.500.000.000 CLP** ([[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]]).

## Montos Operados como Firmante de Origen
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

dv.header(4, `Monto Total Operado (firmante_origen): ${formattedTotal}`);
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
