---
tipo_nodo: persona
rut: ""
aliases:
  - "Carlos Contreras"
  - "Carlos Contreras Gutiérrez"
rol_principal: "Ex Seremi MINVU Región de Antofagasta"
afiliacion_politica: "[[Revolucion Democratica]]"
situacion_procesal: formalizado
medida_cautelar: "Arresto domiciliario total y arraigo nacional (previa prisión preventiva)"
tags:
  - entidad/persona
  - caso-convenios
  - funcionario-publico
---

# Carlos Contreras Gutierrez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut` (RUT de referencia)
- **Rol Principal**: `= this.rol_principal` ([[Seremi MINVU Antofagasta]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Ex Secretario Regional Ministerial de Vivienda y Urbanismo en la Región de Antofagasta ([[Seremi MINVU Antofagasta]]) y exmilitante de [[Revolucion Democratica]]. Fue formalizado por el Ministerio Público en el marco del [[Caso Convenios]] por delitos reiterados de fraude al fisco tras autorizar convenios de transferencia directa ([[TRX-2022-10-03-Convenio-DV-01]]) a favor de la [[Fundacion Democracia Viva]], representada por [[Daniel Andrade Schwarze]], mediante la [[Resolucion-Exenta-MINVU-Antofagasta-2022]].

## Montos Autorizados como Firmante de Origen
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
dv.paragraph(`Calculado automáticamente sobre **${pages.length}** transacción(es) reificada(s) en \`03_Hechos_y_Nexos/\`.`);

dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Firmante Destino", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
