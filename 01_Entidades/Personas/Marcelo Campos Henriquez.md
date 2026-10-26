---
tipo_nodo: persona
rut: ""
aliases:
  - "Marcelo Campos"
  - "Marcelo Campos Henríquez"
rol_principal: "Ex Administrador Municipal y Asesor Jurídico de la Municipalidad de Chillán"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: ""
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
  - "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
tags:
  - entidad/persona
  - caso-luminarias-led
  - condenado
  - funcionario-municipal
---

# Marcelo Campos Henriquez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Chillan]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Abogado, exasesor jurídico de la [[Municipalidad de Chillan]] y juez de policía local. Imputado en el [[Caso Luminarias LED]] por [[Cohecho]] y [[Violacion de Secreto]] ([[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]]). Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

## Montos Asociados como Firmante/Destinatario
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

dv.header(4, `Monto Total Licitación Asociada (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Empresa Origen", "Pagador", "Monto (CLP)", "Causa"],
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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Luminarias: claves de la investigación por sobornos en municipios](https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) | Ex-Ante | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/) |
| [Caso Luminarias LED: confirman prisión preventiva de dueño de Itelecom](https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) | El Dínamo | `secundaria` | 2021-06-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/) |
