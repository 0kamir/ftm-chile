---
tipo_nodo: persona
rut: "17.893.204-7"
aliases:
  - "Daniel Andrade"
  - "Daniel Andrade Schwarze"
rol_principal: "Presidente y Representante Legal de Fundación Democracia Viva"
afiliacion_politica: "[[Revolucion Democratica]]"
situacion_procesal: formalizado
medida_cautelar: "Arresto domiciliario total y arraigo nacional (previa prisión preventiva)"
tags:
  - entidad/persona
  - caso-convenios
  - representante-legal
---

# Daniel Andrade Schwarze

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut` (RUT de referencia forense)
- **Rol Principal**: `= this.rol_principal` ([[Fundacion Democracia Viva]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero civil y exdirigente estudiantil, militante de [[Revolucion Democratica]] hasta su expulsión en 2023. En su calidad de presidente y representante legal de la [[Fundacion Democracia Viva]], suscribió el convenio de transferencia directa [[TRX-2022-10-03-Convenio-DV-01]] con la [[Seremi MINVU Antofagasta]], dirigida por [[Carlos Contreras Gutierrez]], por un monto global de **$426.000.000 CLP** respaldado en la [[Resolucion-Exenta-MINVU-Antofagasta-2022]]. Se encuentra formalizado en la causa [[Caso Convenios]] por fraude al fisco reiterado.

## Auditoría Contable: Montos Recibidos como Firmante de Destino
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

dv.header(4, `Monto Total Suscrito (firmante_destino): ${formattedTotal}`);
dv.paragraph(`Calculado automáticamente sobre **${pages.length}** transacción(es) reificada(s) en \`03_Hechos_y_Nexos/\`.`);

dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Firmante Origen", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
