---
tipo_nodo: persona
rut: ""
aliases:
  - "Irací Hassler"
rol_principal: "Ex Alcaldesa de la Municipalidad de Santiago (2021-2024)"
afiliacion_politica: "[[Partido Comunista de Chile]]"
situacion_procesal: sobreseido
medida_cautelar: "Sobreseimiento definitivo (mayo de 2025, confirmado por la Corte Suprema); responsabilidad administrativa acreditada en sumario de Contraloría (mayo de 2026); nueva querella municipal admitida a trámite (junio de 2026), sin formalización"
estado_verificacion: verificado
fuentes:
  - url: "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
    titulo: "Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella"
    medio: "24 Horas"
    tipo: secundaria
    fecha: 2025-05-26
    consultado: 2026-10-19
  - url: "https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/"
    titulo: "Sierra Bella: ningún querellante pidió reapertura y se cierra el telón del caso para Irací Hassler"
    medio: "La Tercera"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/"
    titulo: "Tribunal admite querella de Santiago contra Irací Hassler por fraude al fisco"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-06-04
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml"
    titulo: "Desbordes tras querella contra Hassler por caso Sierra Bella: 'El informe de Contraloría es muy duro'"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2026-06-05
    consultado: 2026-10-19
  - url: "https://www.cnnchile.com/pais/mario-desbordes-tribunal-ratifica-admisibilidad-de-querella-de-iraci-hassler-en-su-contra-por-denuncia-calumniosa/"
    titulo: "Mario Desbordes: tribunal ratifica admisibilidad de querella de Irací Hassler en su contra por denuncia calumniosa"
    medio: "CNN Chile"
    tipo: secundaria
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
Economista, militante del [[Partido Comunista de Chile]] y ex Alcaldesa de la [[Municipalidad de Santiago]]. En el [[Caso Sierra Bella]], impulsó la compra, aprobada por el concejo municipal, de la ex Clínica Sierra Bella con [[Inmobiliaria San Valentino SpA]] ([[Felipe Sanchez Perez]]) por **$8.200.000.000 CLP** ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]), operación cuyos pagos fueron paralizados por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) mediante el [[Dictamen-CGR-SierraBella-2023]] al constatarse que el precio cuadruplicaba el avalúo fiscal y el valor de compra previa sin justificación técnica verificable. La municipalidad finalmente no perseveró en la compra. En mayo de 2025 la Fiscalía decidió no perseverar y la causa quedó con sobreseimiento definitivo, confirmado por la Corte Suprema; Hassler nunca fue formalizada. En mayo de 2026 un sumario de la Contraloría dio por acreditada su responsabilidad administrativa en la compra. En junio de 2026 el 7° Juzgado de Garantía de Santiago declaró admisible una nueva querella de la Municipalidad de Santiago por fraude al fisco, que el Ministerio Público debe evaluar; Hassler sostiene que se trata de hechos ya juzgados y querelló por denuncia calumniosa contra el alcalde Mario Desbordes, acción que el tribunal también admitió. Rige la presunción de inocencia.

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
