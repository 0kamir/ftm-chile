---
tipo_nodo: persona
rut: "7.192.450-5"
aliases:
  - "Pablo Longueira"
  - "Juan Pablo Longueira Montes"
rol_principal: "Ex Senador de la República y Ex Ministro de Economía"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: formalizado
medida_cautelar: "Sujeto a juicio oral (absuelto en primera instancia con recursos pendientes)"
tags:
  - entidad/persona
  - caso-sqm
  - ex-senador
---

# Pablo Longueira Montes

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero civil, exsenador y expresidente de [[Union Democrata Independiente]]. En el [[Caso SQM]] fue acusado por la Fiscalía por el delito de [[Cohecho]] pasivo tras detectarse el intercambio de correos electrónicos con el gerente general de [[SQM SA]], [[Patricio Contesse Gonzalez]], con la redacción de una indicación sobre invariabilidad tributaria en la Ley de Royalty Minero de 2010 y pagos por más de **$730.000.000 CLP** a fundaciones y emisores de boletas de su entorno ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]), documentados a partir de [[Querella-SII-Boletas-SQM-2015]].

## Auditoría Contable: Montos Imputados como Destinatario Político
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

dv.header(4, `Monto Total Asociado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Emisor", "Monto (CLP)", "Causa"],
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
