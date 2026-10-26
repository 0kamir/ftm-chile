---
tipo_nodo: persona
rut: ""
aliases:
  - "Natalia Compagnon"
rol_principal: "Socia Cofundadora de Exportadora y de Gestión Caval Ltda."
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada a pena remitida y multa por delitos tributarios (TOP Rancagua)"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
  - "https://www.elciudadano.com/?p=524007"
tags:
  - entidad/persona
  - caso-caval
  - condenado
---

# Natalia Compagnon Soto

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Exportadora y de Gestion Caval Ltda]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Socia cofundadora del 50% de [[Exportadora y de Gestion Caval Ltda]] junto a [[Mauricio Valero Illanes]]. Fue condenada por el Tribunal de Juicio Oral en lo Penal de Rancagua en el [[Caso Caval]] ([[Sentencia-TOP-Rancagua-Caval-2018]]) como autora de delitos tributarios previstos en el artículo 97 N° 4 del Código Tributario por declaraciones maliciosamente falsas y contabilización de facturas ideológicamente falsas ante el [[Servicio Impuestos Internos]] ([[TRX-2015-01-29-Facturas-Caval-SII-01]]).

## Montos Operados como Firmante
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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Natalia Compagnon fue condenada por delito tributario](https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
| [Mauricio Valero fue absuelto](https://www.elciudadano.com/?p=524007) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=524007) |
