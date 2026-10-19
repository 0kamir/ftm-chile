---
tipo_nodo: persona
rut: ""
aliases:
  - "Alberto Larraín"
  - "Alberto Larraín Salas"
rol_principal: "Cofundador y Director Ejecutivo de Fundación ProCultura"
afiliacion_politica: "Independiente (Ex DC / Cercano Frente Amplio)"
situacion_procesal: formalizado
medida_cautelar: "Arraigo nacional y firma mensual"
tags:
  - entidad/persona
  - caso-convenios
  - procultura
---

# Alberto Larrain Salas

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Fundacion ProCultura]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Médico psiquiatra y director ejecutivo de [[Fundacion ProCultura]]. En el marco del [[Caso Convenios]], suscribió convenios multirregionales tanto con la [[Seremi MINVU Antofagasta]] dirigida por [[Carlos Contreras Gutierrez]] ([[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]]) como con el [[GORE Biobio]] dirigido por [[Rodrigo Diaz Worner]] ([[TRX-2022-11-18-Convenio-ProCultura-Biobio]]), actuando como **conector interregional** en el grafo forense.

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
