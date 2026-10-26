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
  - "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
  - "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
  - "https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/"
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
  - "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
  - "https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/"
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

## Síntesis
Ex Subsecretario de Minería y exejecutivo de [[Empresas Penta SA]]. En el [[Caso Penta]] recibió pagos bimensuales de `$3.000.000 CLP` (`$42.000.000 CLP` en total) de [[Empresas Penta SA]] mientras ejercía funciones públicas, documentados con boletas de terceros ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]). El 8° Juzgado de Garantía de Santiago (julio de 2018, procedimiento abreviado) lo **absolvió de cohecho** y lo condenó por enriquecimiento ilícito y delitos tributarios (pena remitida de dos años e inhabilitación para cargos públicos); la propia Fiscalía reconoció no haber acreditado que los pagos fueran a cambio de favores.

## Montos Recibidos como Firmante de Destino
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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Penta: Tribunal desecha argumentos del CDE y absuelve a exsubsecretario Wagner por cohecho](https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) | Emol | `secundaria` | 2018-07-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) |
| [Caso Penta deja condenas en juicios abreviados y suspensiones](https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) | T13 | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) |
| [Délano y Lavín terminaron clases de ética](https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) |
| [Lavín y Délano comenzaron las clases de ética tras condena del caso Penta](https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) | 24 Horas | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) |
| [Cartas: 'Good bye' a las clases de ética](https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) | CIPER Chile | `secundaria` | 2024-06-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) |
| [Fiscalía cierra investigación por el caso Dominga y solicita sobreseimiento definitivo](https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/) | La Tercera | `secundaria` | 2024-01-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/) |
