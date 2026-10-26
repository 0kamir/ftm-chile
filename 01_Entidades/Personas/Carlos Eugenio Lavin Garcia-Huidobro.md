---
tipo_nodo: persona
rut: ""
aliases:
  - "Carlos Eugenio Lavín"
rol_principal: "Cofundador y Controlador de Empresas Penta S.A."
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Condena cumplida en libertad vigilada, multa fiscal y clases de ética empresarial"
vinculos_familiares: []
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
  - "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
  - "https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/"
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
  - "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
tags:
  - entidad/persona
  - caso-penta
  - condenado
---

# Carlos Eugenio Lavin Garcia-Huidobro

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Empresas Penta SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Cofundador y controlador de [[Empresas Penta SA]] junto a [[Carlos Alberto Delano Abbott]]. Condenado en el [[Caso Penta]] ([[Sentencia-8Juzgado-Garantia-Penta-2018]]) por delitos tributarios reiterados tras articular pagos irregulares a campañas de la [[Union Democrata Independiente]] ([[TRX-2013-07-15-Boletas-Penta-UDI-01]]) y pagos periódicos al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]). La Fiscalía retiró la imputación de soborno en el procedimiento abreviado de 2018.

## Montos Autorizados como Firmante de Origen
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

dv.header(4, `Monto Total Autorizado (firmante_origen): ${formattedTotal}`);
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
