---
tipo_nodo: persona
rut: ""
aliases:
  - "Juan Miguel Fuente-Alba"
  - "General Fuente-Alba"
rol_principal: "Ex Comandante en Jefe del Ejército de Chile (2010-2014)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Procesado por malversación de gastos reservados (Justicia Militar / Ordinaria)"
tags:
  - entidad/persona
  - caso-milicogate
  - ejercito
---

# Juan Miguel Fuente-Alba Poblete

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Comando de Apoyo a la Fuerza del Ejercito]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
General de Ejército (r) y Comandante en Jefe entre 2010 y 2014. Fue sometido a proceso por la Ministra en Visita Romy Rutherford ([[Procesamientos-Ministra-Rutherford-Milicogate]]) en el [[Caso Milicogate]] por [[Malversacion de Caudales Publicos]] de gastos reservados y juzgado en la justicia ordinaria por [[Lavado de Activos]]. Durante su período de mando operó asimismo el desfalco de la Ley Reservada del Cobre en el [[Comando de Apoyo a la Fuerza del Ejercito]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]).

## Auditoría Contable: Montos Asociados como Mando de Origen
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

dv.header(4, `Monto Total Asociado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Repartición", "Operador Destino", "Monto (CLP)", "Causa"],
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
