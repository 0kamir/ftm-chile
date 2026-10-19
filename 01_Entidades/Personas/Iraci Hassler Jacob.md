---
tipo_nodo: persona
rut: ""
aliases:
  - "Irací Hassler"
rol_principal: "Ex Alcaldesa de la Municipalidad de Santiago (2021-2024)"
afiliacion_politica: "[[Partido Comunista de Chile]]"
situacion_procesal: ninguna
medida_cautelar: "Sin cargos: la Fiscalía decidió no perseverar en la investigación (26-05-2025); nunca fue formalizado/a"
estado_verificacion: verificado
fuentes:
  - url: "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
    titulo: "Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella"
    medio: "24 Horas"
    tipo: secundaria
    fecha: 2025-05-26
    consultado: 2026-10-19
tags:
  - entidad/persona
  - caso-sierra-bella
  - partido-comunista
---

# Iraci Hassler Jacob

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Santiago]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Estado Procesal**: `= this.medida_cautelar`

## Síntesis Forense
Economista, militante del [[Partido Comunista de Chile]] y ex Alcaldesa de la [[Municipalidad de Santiago]]. En el [[Caso Sierra Bella]], impulsó la compra, aprobada por el concejo municipal, de la ex Clínica Sierra Bella con [[Inmobiliaria San Valentino SpA]] ([[Felipe Sanchez Perez]]) por **$8.200.000.000 CLP** ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]), operación cuyos pagos fueron paralizados por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) mediante el [[Dictamen-CGR-SierraBella-2023]] al constatarse que el precio cuadruplicaba el avalúo fiscal y el valor de compra previa sin justificación técnica verificable. La municipalidad finalmente no perseveró en la compra; en mayo de 2025 la Fiscalía decidió no perseverar en la investigación penal, sin formalizarla.

## Auditoría Contable: Montos Suscritos como Firmante de Origen
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Suscrito (firmante_origen): ${formattedTotal}`);
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
