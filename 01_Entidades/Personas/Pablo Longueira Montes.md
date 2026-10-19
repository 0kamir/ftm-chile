---
tipo_nodo: persona
rut: ""
aliases:
  - "Pablo Longueira"
  - "Juan Pablo Longueira Montes"
rol_principal: "Ex Senador de la República y Ex Ministro de Economía"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: absuelto
medida_cautelar: "Absuelto por el 3° TOP de Santiago (22-10-2025); recursos de nulidad de Fiscalía, SII y CDE pendientes"
estado_verificacion: verificado
fuentes:
  - url: "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
    titulo: "Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados"
    medio: "La Tercera"
    tipo: secundaria
    fecha: 2025-10-22
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
    titulo: "Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2026-10-06
    consultado: 2026-10-19
tags:
  - entidad/persona
  - caso-sqm
  - ex-senador
---

# Pablo Longueira Montes

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero civil, exsenador y expresidente de [[Union Democrata Independiente]]. En el [[Caso SQM]] la Fiscalía lo acusó de [[Cohecho]] pasivo por su intervención en la indicación sobre invariabilidad tributaria de la Ley de Royalty Minero de 2010 y por pagos de [[SQM SA]] a personas de su entorno ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]). El 22 de octubre de 2025 el 3° Tribunal de Juicio Oral en lo Penal de Santiago absolvió, por mayoría, a los ocho acusados que llegaron a juicio, entre ellos [[Pablo Longueira Montes]] y [[Patricio Contesse Gonzalez]]: no dio por acreditada más allá de toda duda razonable la falsedad ideológica de las boletas y facturas, y constató una vulneración del derecho a ser juzgado en un plazo razonable. La Fiscalía, el [[Servicio Impuestos Internos]] y el CDE presentaron recursos de nulidad, revisados por la Corte de Apelaciones de Santiago el 6 de octubre de 2026 y pendientes de resolución. Las absoluciones están vigentes y rige la presunción de inocencia.

## Auditoría Contable: Montos Imputados como Destinatario Político
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

dv.header(4, `Monto Total Asociado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Emisor", "Monto (CLP)", "Causa"],
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
