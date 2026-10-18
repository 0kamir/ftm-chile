---
tipo_nodo: persona
rut: "12.849.102-3"
aliases:
  - "Patricio Marín"
  - "Patricio Marín Lazo"
rol_principal: "Ex Mayor de Carabineros y Ex Jefe Operativo de la UIOE en La Araucanía"
afiliacion_politica: "Militar / Carabineros"
situacion_procesal: condenado
medida_cautelar: "Condenado a 5 años de presidio (libertad vigilada intensiva) por el TOP de Temuco"
tags:
  - entidad/persona
  - caso-operacion-huracan
  - dipolcar
  - uioe
  - condenado
---

# Patricio Marin Lazo

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Inteligencia Policial de Carabineros]] / UIOE)
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Condena Ejecutoriada / Cautelar**: `= this.medida_cautelar`

## Síntesis Forense
Mayor de Carabineros que se desempeñó como jefe de operaciones de la Unidad de Inteligencia Operativa Especializada (UIOE) en Temuco. Coordinó en terreno la ejecución de la [[Caso Operacion Huracan]], supervisó la incorporación de [[Alex Smith Leay]] a las labores de inteligencia y gestionó el pago de fondos reservados para financiar el supuesto software «Antorcha» ([[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]]).

Durante el juicio oral ([[Sentencia-TOP-Temuco-OperacionHuracan-2024]]), el tribunal acreditó su autoría en la remisión de informes falsificados dirigidos al Ministerio Público y a tribunales con el objeto de inducir detenciones y medidas cautelares ([[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]]), siendo sentenciado a **5 años de presidio** menor en su grado máximo por [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]].

## Auditoría Contable: Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Imputado / Autorizado: ${formattedTotal}`);
dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Monto (CLP)", "Delito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.delito_imputado
  ])
);
```
