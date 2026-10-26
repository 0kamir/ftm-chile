---
tipo_nodo: persona
rut: ""
aliases:
  - "Marcelo Lefort"
  - "León Marcelo Lefort Hernández"
rol_principal: "Fundador y Ex Gerente General de Itelecom Holding Chile SpA"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Arresto domiciliario (sustituyó la prisión preventiva en julio de 2021)"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/politica/caso-luminarias-25-claves-para-entender-la-investigacion-por-sobornos-en-municipios/"
  - "https://www.eldinamo.cl/pais/2021/06/30/caso-luminarias-led-confirman-prision-preventiva-de-dueno-de-itelecom-acusado-de-soborno/"
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-casi-5-anos-de-presidio-dos-ex"
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-otros-tres-acusados-incluido-un-ex"
tags:
  - entidad/persona
  - caso-luminarias-led
  - condenado
  - empresario
---

# Leon Marcelo Lefort Hernandez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Itelecom Holding Chile SpA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Ingeniero y controlador de [[Itelecom Holding Chile SpA]]. Imputado en el [[Caso Luminarias LED]] por soborno a funcionarios de al menos 24 instituciones públicas, según la Fiscalía, incluida la licitación de la [[Municipalidad de Chillan]] ([[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]]). Según la Fiscalía de Ñuble, [[Leon Marcelo Lefort Hernandez]] fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]], quien habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]. A la fecha de la última verificación (2026-10-19) no se encontró sentencia: la causa registra formalizaciones, prisión preventiva luego sustituida por arresto domiciliario y una acusación contra 15 imputados. Rige la presunción de inocencia.

## Montos Operados como Firmante de Origen
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

dv.header(4, `Monto Total Operado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Destino", "Contraparte", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_destino,
    p.firmante_destino,
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
| [Caso Luminarias LED: condenan a casi 5 años de presidio a dos exconcejales de Iquique por fraude al fisco y cohecho](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-casi-5-anos-de-presidio-dos-ex) | Fiscalía de Chile | `primaria` | 2023-05-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-casi-5-anos-de-presidio-dos-ex) |
| [Caso Luminarias LED: condenan a otros tres acusados, incluido un exconcejal de Iquique](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-otros-tres-acusados-incluido-un-ex) | Fiscalía de Chile | `primaria` | 2023-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/caso-luminarias-led-condenan-otros-tres-acusados-incluido-un-ex) |
