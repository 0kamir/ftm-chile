---
tipo_nodo: persona
rut: ""
aliases:
  - "Mauricio Valero"
rol_principal: "Socio Administrador de Exportadora y de Gestión Caval Ltda."
afiliacion_politica: "Independiente"
situacion_procesal: absuelto
medida_cautelar: "Absuelto por el TOP de Rancagua (julio de 2018)"
estado_verificacion: verificado
fuentes:
  - url: "https://radio.uchile.cl/?p=478347"
    titulo: "Caso Caval: Tribunal condena a Natalia Compagnon por delito tributario"
    medio: "Radio Universidad de Chile"
    tipo: secundaria
    fecha: 2018-07-11
    consultado: 2026-10-19
  - url: "https://www.elciudadano.com/?p=524007"
    titulo: "Mauricio Valero fue absuelto"
    medio: "El Ciudadano"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - entidad/persona
  - caso-caval
  - condenado
---

# Mauricio Valero Illanes

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Exportadora y de Gestion Caval Ltda]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Socio administrador del 50% de [[Exportadora y de Gestion Caval Ltda]] junto a [[Natalia Compagnon Soto]]. En el [[Caso Caval]] fue acusado de soborno y delitos tributarios, pero el Tribunal de Juicio Oral en lo Penal de Rancagua lo **absolvió** en julio de 2018, al igual que a la sociedad ([[Sentencia-TOP-Rancagua-Caval-2018]]). Rige la presunción de inocencia.

## Auditoría Contable: Montos Operados como Firmante
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

dv.header(4, `Monto Total Operado en Nexos: ${formattedTotal}`);
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

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
