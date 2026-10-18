---
tipo_nodo: persona
rut: "10.642.810-7"
aliases:
  - "Pablo Wagner"
rol_principal: "Ex Subsecretario de Minería (2010-2012) y Ex Ejecutivo de Empresas Penta"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada por enriquecimiento ilícito y delitos tributarios"
tags:
  - entidad/persona
  - caso-penta
  - condenado
---

# Pablo Wagner San Martin

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ex Subsecretario de Minería y exejecutivo de [[Empresas Penta SA]]. En el marco del [[Caso Penta]], se acreditó que mientras ejercía funciones públicas recibió pagos bimensuales de `$3.000.000 CLP` (por un total de `$42.000.000 CLP`) provenientes de [[Empresas Penta SA]] autorizados por [[Carlos Eugenio Lavin Garcia-Huidobro]] y [[Carlos Alberto Delano Abbott]], ocultados mediante boletas de honorarios de terceros ante el [[Servicio Impuestos Internos]] ([[TRX-2011-03-10-Soborno-Penta-Wagner-01]]), siendo condenado conforme a [[Sentencia-8Juzgado-Garantia-Penta-2018]].

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
