---
tipo_nodo: persona
rut: ""
aliases:
  - "Augusto Pinochet"
  - "Daniel López"
  - "José Ramón Ugarte"
rol_principal: "Ex Comandante en Jefe del Ejército de Chile y Jefe de la Junta Militar (1973–1990)"
afiliacion_politica: "Militar / Dictadura Cívico-Militar (Respaldado políticamente por UDI y RN)"
situacion_procesal: formalizado
medida_cautelar: "Fallecido en diciembre de 2006 bajo arresto domiciliario y desafuero; patrimonio ilícito comisado por sentencia definitiva de la Corte Suprema en 2018"
vinculos_familiares:
  - "[[Lucia Hiriart Rodriguez]]"
  - "[[Augusto Pinochet Hiriart]]"
  - "[[Julio Ponce Lerou]]"
tags:
  - entidad/persona
  - caso-riggs
  - caso-pinocheques
  - ejercito
  - familia-pinochet-hiriart
---

# Augusto Pinochet Ugarte

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Cónyuge de [[Lucia Hiriart Rodriguez]], padre de [[Augusto Pinochet Hiriart]] y ex suegro de [[Julio Ponce Lerou]])*
- **Situación Procesal**: `= this.situacion_procesal` (Desaforado y procesado en vida por malversación de caudales públicos, fraude tributario y uso de pasaportes falsos; sobreseído por fallecimiento en 2006, con condena patrimonial de comiso sobre su sucesión en 2018)
- **Medida Cautelar / Sanción Patrimonial**: `= this.medida_cautelar`

## Síntesis
General de Ejército que encabezó el régimen militar entre 1973 y 1990 y permaneció como Comandante en Jefe del Ejército hasta marzo de 1998 y senador vitalicio en el [[Senado de la Republica de Chile]] hasta 2002. En el mapa de corrupción patrimonial del Estado chileno constituye el eje articulador de dos macro-causas:
1. **[[Caso Pinocheques]] (1989–1995)**: Bajo su mando directo en el Ejército ([[Comando de Apoyo a la Fuerza del Ejercito]]), FAMAE giró en enero de 1989 tres cheques por cerca de US$ 3 millones (`$2.950.000.000 CLP` actualizados) a su hijo [[Augusto Pinochet Hiriart]] por la compra de la fábrica quebrada [[Valmoval Ltda]] ([[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]]). Para impedir el avance judicial y contralor de la causa, ordenó los acuartelamientos militares conocidos como *"Ejercicio de Enlace"* (1990) y *"Boinazo"* (1993).
2. **[[Caso Riggs]] (2004–2018)**: La investigación del Senado de EE.UU. y del Ministro en Visita [[Sergio Munoz Gajardo]] descubrió que mantuvo más de **125 cuentas bancarias secretas** y sociedades *offshore* en [[Riggs Bank y Sociedades Offshore Ashburton]], estructuradas junto a su albacea [[Oscar Aitken Lavanchy]] bajo nombres falsos como *"Daniel López"*, desviando gastos reservados del Ejército y de la Presidencia por **US$ 17,86 millones** sin justificación lícita ([[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]]) y evadiendo impuestos ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]]). En agosto de 2018, la [[Corte Suprema de Chile]] ordenó el comiso definitivo a favor del Fisco de sus cuentas y 24 propiedades ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]). Adicionalmente, en el ámbito familiar y societario se vincula con su cónyuge [[Lucia Hiriart Rodriguez]] ([[Caso CEMA Chile]]) y su ex yerno [[Julio Ponce Lerou]] ([[Caso Cascadas]] y [[Caso SQM]]).

## Montos Imputados en Aristas Reificadas
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

dv.header(4, `Monto Total Asociado en Aristas Reificadas: ${formattedTotal}`);
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
