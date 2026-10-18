---
tipo_nodo: persona
rut: "6.371.420-8"
aliases:
  - "Patricio Contesse"
  - "Patricio Contesse González"
rol_principal: "Ex Gerente General de SQM S.A. (1990-2015)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Arraigo nacional y firma periódica (acusado en juicio oral)"
tags:
  - entidad/persona
  - caso-sqm
  - ejecutivo
---

# Patricio Contesse Gonzalez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[SQM SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero forestal y ex gerente general de [[SQM SA]] durante 25 años. En el [[Caso SQM]] fue acusado por el Ministerio Público y el [[Servicio Impuestos Internos]] ([[Querella-SII-Boletas-SQM-2015]]) por [[Delito Tributario]] reiterado y [[Cohecho]] activo (soborno) en relación con los pagos autorizados desde el centro de costos de la gerencia general a personas vinculadas a [[Pablo Longueira Montes]] y la tramitación del Royalty Minero ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]).

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
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Contraparte", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
