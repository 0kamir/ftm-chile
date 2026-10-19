---
tipo_nodo: persona
rut: ""
aliases:
  - "Pablo Wagner"
rol_principal: "Ex Subsecretario de Minería (2010-2012) y Ex Ejecutivo de Empresas Penta"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Condenado por enriquecimiento ilícito y delitos tributarios (abreviado, 2018); absuelto de cohecho"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
    titulo: "Caso Penta: Tribunal desecha argumentos del CDE y absuelve a exsubsecretario Wagner por cohecho"
    medio: "Emol"
    tipo: secundaria
    fecha: 2018-07-06
    consultado: 2026-10-19
  - url: "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
    titulo: "Caso Penta deja condenas en juicios abreviados y suspensiones"
    medio: "T13"
    tipo: secundaria
    consultado: 2026-10-19
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
Ex Subsecretario de Minería y exejecutivo de [[Empresas Penta SA]]. En el [[Caso Penta]] recibió pagos bimensuales de `$3.000.000 CLP` (`$42.000.000 CLP` en total) de [[Empresas Penta SA]] mientras ejercía funciones públicas, documentados con boletas de terceros ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]). El 8° Juzgado de Garantía de Santiago (julio de 2018, procedimiento abreviado) lo **absolvió de cohecho** y lo condenó por enriquecimiento ilícito y delitos tributarios (pena remitida de dos años e inhabilitación para cargos públicos); la propia Fiscalía reconoció no haber acreditado que los pagos fueran a cambio de favores.

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
