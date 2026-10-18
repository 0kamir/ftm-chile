---
tipo_nodo: persona
rut: "2.341.892-4"
aliases:
  - "Lucía Hiriart"
  - "María Lucía Hiriart Rodríguez"
rol_principal: "Ex Presidenta Vitalicia de Fundación CEMA Chile y Cónyuge de Augusto Pinochet Ugarte"
afiliacion_politica: "Independiente (Cúpula Cívico-Militar)"
situacion_procesal: formalizado
medida_cautelar: "Fallecida en diciembre de 2021 (Procesada en Caso Riggs por delito tributario y malversación; obligada a restituir 108 inmuebles fiscales en Caso CEMA Chile y afectada por el comiso de la Corte Suprema en 2018)"
vinculos_familiares:
  - "[[Augusto Pinochet Ugarte]]"
  - "[[Augusto Pinochet Hiriart]]"
  - "[[Julio Ponce Lerou]]"
tags:
  - entidad/persona
  - caso-cema-chile
  - caso-riggs
  - clan-pinochet-hiriart
---

# Lucia Hiriart Rodriguez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Cónyuge de [[Augusto Pinochet Ugarte]], madre de [[Augusto Pinochet Hiriart]] y ex suegra de [[Julio Ponce Lerou]])*
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanción Patrimonial**: `= this.medida_cautelar`

## Síntesis Forense
Cónyuge de [[Augusto Pinochet Ugarte]] y presidenta a perpetuidad de la [[Fundacion CEMA Chile]] entre 1973 y agosto de 2016. Su participación se registra en dos grandes causas de corrupción patrimonial:
1. **[[Caso CEMA Chile]] (`Rol 34.125-2016`)**: Tras modificar los estatutos de [[Fundacion CEMA Chile]] antes del retorno a la democracia para asegurarse la presidencia vitalicia, encabezó la venta a privados de decenas de terrenos e inmuebles donados gratuitamente por el Fisco, SERVIU y municipalidades, desviando recursos y manteniendo más de un centenar de propiedades públicas bajo control privado hasta que la acción del Consejo de Defensa del Estado y de los tribunales obligó a la disolución de la entidad y a la restitución al Estado de **108 inmuebles y fondos líquidos** por más de **`$10.500.000.000 CLP`** ([[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] y [[Acuerdo-Judicial-Restitucion-CEMAChile-2019]]).
2. **[[Caso Riggs]] (`Rol 1.649-2004`)**: Fue procesada y detenida preventivamente en 2005 y 2007 por los Ministros en Visita [[Sergio Munoz Gajardo]] y Carlos Cerda tras las querellas del [[Servicio Impuestos Internos]] por complicidad en fraude tributario y malversación de caudales públicos asociados a las cuentas secretas de [[Riggs Bank y Sociedades Offshore Ashburton]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]]), quedando sujeta como heredera al comiso patrimonial dictado por la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-CasoRiggs-2018]].

## Auditoría Contable: Montos Imputados en Aristas Reificadas
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
