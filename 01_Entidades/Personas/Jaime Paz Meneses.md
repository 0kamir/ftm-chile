---
tipo_nodo: persona
rut: ""
aliases:
  - "Jaime Paz"
  - "Coronel Jaime Paz Meneses"
rol_principal: "Ex Coronel de Intendencia de Carabineros"
afiliacion_politica: "Independiente"
situacion_procesal: acusado
medida_cautelar: "Acusado en juicio oral; veredicto de abril de 2026 condenó a 25 de 28 acusados (resultado individual no verificado); penas pendientes"
estado_verificacion: parcial
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
    titulo: "Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-04-15
    consultado: 2026-10-19
  - url: "https://en.wikipedia.org/wiki/Pacogate"
    titulo: "Pacogate"
    medio: "Wikipedia"
    tipo: secundaria
    consultado: 2026-10-19
alertas_verificacion:
  - "Verificar en la sentencia (feb-2027) si figura entre los condenados y su pena."
tags:
  - entidad/persona
  - caso-pacogate
  - condenado
---

# Jaime Paz Meneses

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Finanzas de Carabineros]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ex Coronel de Intendencia en la [[Direccion de Finanzas de Carabineros]], señalado como figura clave del esquema del [[Caso Pacogate]], que según la acusación habría sustraído **$28.348.928.198 CLP** mediante depósitos ficticios de remuneraciones ([[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]). En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme. Ver [[Veredicto-TOP-Santiago-Pacogate-2026]]. Rige la presunción de inocencia hasta sentencia firme.

## Auditoría Contable: Montos Operados como Firmante de Destino
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

dv.header(4, `Monto Total Condenado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Órgano Afectado", "Jefe Cúpula", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
