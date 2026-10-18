---
tipo_nodo: persona
rut: "4.918.234-1"
aliases:
  - "Paul Schäfer"
  - "Paul Schaefer"
rol_principal: "Fundador y Jerarca de Sociedad Benefactora y Educacional Dignidad (Colonia Dignidad / Villa Baviera)"
afiliacion_politica: "Independiente (Vinculado a aparatos de inteligencia DINA y redes políticas de extrema derecha)"
situacion_procesal: condenado
medida_cautelar: "Fallecido en prisión en 2010 (Cumpliendo condenas por 20 años de presidio mayor en su grado máximo y penas adicionales por Ley de Control de Armas y DD.HH.)"
tags:
  - entidad/persona
  - caso-colonia-dignidad
  - condenado
---

# Paul Schafer Schneider

## Perfil Biográfico e Institucional
- **RUT / Cédula Extranjería**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ciudadano alemán y fundador en 1961 de [[Sociedad Benefactora y Educacional Dignidad]] en la comuna de Parral. Como líder absoluto del enclave, dirigió el vaciamiento patrimonial de la corporación tras su disolución legal en 1991 para evadir al [[Servicio Impuestos Internos]] y al fisco ([[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]]), mantuvo el mayor arsenal clandestino privado de armas de guerra detectado en el país ([[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]]) y permaneció prófugo en la clandestinidad entre 1996 y marzo de 2005 hasta su captura en Tortuguitas (Argentina) por orden del Ministro en Visita [[Jorge Zepeda Arancibia]]. Fue condenado ejecutoriadamente en múltiples cuadernos del [[Caso Colonia Dignidad]] ratificados por la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-ColoniaDignidad-2013]]).

## Auditoría Contable: Montos Imputados como Controlador de Origen
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
