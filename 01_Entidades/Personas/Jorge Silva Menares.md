---
tipo_nodo: persona
rut: "7.419.620-9"
aliases:
  - "Jorge Silva"
rol_principal: "Ex Director de Obras Municipales (DOM) de la Municipalidad de Machalí"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada por cohecho reiterado e inhabilitación para cargos públicos"
tags:
  - entidad/persona
  - caso-caval
  - condenado
---

# Jorge Silva Menares

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Machali]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ex Director de Obras Municipales de la [[Municipalidad de Machali]]. En el [[Caso Caval]] fue condenado en enero de 2018 por cohecho reiterado (818 días con remisión condicional) por recibir pagos vinculados a la operación de [[Exportadora y de Gestion Caval Ltda]] a cambio de gestionar e informar favorablemente la modificación del uso de suelo en el Plan Regulador Intercomunal de Rancagua para los terrenos de Machalí ([[TRX-2014-02-18-Soborno-Caval-Machali-01]]). El socio de Caval [[Mauricio Valero Illanes]] fue absuelto del cargo de soborno ([[Sentencia-TOP-Rancagua-Caval-2018]]).

## Auditoría Contable: Montos Recibidos como Firmante de Destino
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Recibido (firmante_destino): ${formattedTotal}`);
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
