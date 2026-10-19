---
tipo_nodo: persona
rut: ""
aliases:
  - "Augusto Pinochet Hiriart"
rol_principal: "Ex Oficial de Ejército y Empresario (Receptor de los Pinocheques en Caso Valmoval)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Sin medidas cautelares vigentes (Procesado en Caso Riggs y Caso recepción de vehículos robados; beneficiario del cierre por razón de Estado en Caso Pinocheques)"
vinculos_familiares:
  - "[[Augusto Pinochet Ugarte]]"
  - "[[Lucia Hiriart Rodriguez]]"
tags:
  - entidad/persona
  - caso-pinocheques
  - caso-riggs
  - clan-pinochet-hiriart
---

# Augusto Pinochet Hiriart

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Hijo mayor de [[Augusto Pinochet Ugarte]] y [[Lucia Hiriart Rodriguez]])*
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Hijo mayor de [[Augusto Pinochet Ugarte]] y [[Lucia Hiriart Rodriguez]]. En enero de 1989 recibió tres cheques girados directamente a su nombre por FAMAE / Ejército de Chile ([[Comando de Apoyo a la Fuerza del Ejercito]]) por cerca de US$ 3 millones (`$2.950.000.000 CLP` actualizados) por la compraventa de la empresa armera quebrada [[Valmoval Ltda]], operación que dio origen al [[Caso Pinocheques]] ([[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]]). Posteriormente, en el [[Caso Riggs]], el Ministro en Visita [[Sergio Munoz Gajardo]] y las querellas del [[Servicio Impuestos Internos]] investigaron un eventual flujo de esos recursos hacia cuentas en el extranjero (en 2010 el ministro Valderrama sobreseyó la arista Pinocheques al determinar que no llegaron a las cuentas de Pinochet Ugarte) vinculadas a [[Riggs Bank y Sociedades Offshore Ashburton]], siendo procesado en la arista tributaria y patrimonial ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).

## Auditoría Contable: Montos Imputados como Receptor Directo
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)) ||
              (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Asociado: ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
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
