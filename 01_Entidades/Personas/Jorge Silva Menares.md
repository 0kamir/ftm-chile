---
tipo_nodo: persona
rut: ""
aliases:
  - "Jorge Silva"
rol_principal: "Ex Director de Obras Municipales (DOM) de la Municipalidad de Machalí"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada por cohecho reiterado e inhabilitación para cargos públicos"
estado_verificacion: verificado
fuentes:
  - "https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/"
  - "https://radio.uchile.cl/?p=478347"
  - "https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
tags:
  - entidad/persona
  - caso-caval
  - condenado
---

# Jorge Silva Menares

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Machali]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Ex Director de Obras Municipales de la [[Municipalidad de Machali]]. En el [[Caso Caval]] fue condenado en enero de 2018 por cohecho reiterado (818 días con remisión condicional) por recibir $55.030.792 del gestor inmobiliario Juan Díaz, vinculados a predios que luego compró [[Exportadora y de Gestion Caval Ltda]], a cambio de gestionar e informar favorablemente la modificación del uso de suelo en el Plan Regulador Intercomunal de Rancagua para los terrenos de Machalí ([[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]]). El socio de Caval [[Mauricio Valero Illanes]] fue absuelto del cargo de soborno ([[Sentencia-TOP-Rancagua-Caval-2018]]).

## Montos Recibidos como Firmante de Destino
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name));

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
| [Caso Caval: el sospechoso historial del destituido director de obras de Machalí](https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/) | CIPER Chile | `secundaria` | 2015-07-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/) |
| [Caso Caval: Tribunal condena a Natalia Compagnon por delito tributario](https://radio.uchile.cl/?p=478347) | Radio Universidad de Chile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://radio.uchile.cl/?p=478347) |
| [Caso Caval: 818 días remitidos y multa de 55 millones para segundo condenado](https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/) | Radio Agricultura | `secundaria` | 2018-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/) |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Natalia Compagnon fue condenada por delito tributario](https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
