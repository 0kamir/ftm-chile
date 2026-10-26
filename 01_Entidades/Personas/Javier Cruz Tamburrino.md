---
tipo_nodo: persona
rut: ""
aliases:
  - "Javier Cruz"
rol_principal: "Ex Director de la Unidad de Análisis Financiero (UAF)"
afiliacion_politica: "Independiente"
situacion_procesal: testigo_experto
medida_cautelar: "Sin medidas cautelares (Autoridad emisora de Reportes de Operaciones Sospechosas ROS)"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html"
  - "https://vlex.cl/vid/corte-marcial-revoca-condena-844999287"
  - "https://www.elciudadano.com/?p=683869"
  - "https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/"
  - "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
  - "https://en.wikipedia.org/wiki/Pacogate"
tags:
  - entidad/persona
  - uaf
  - fiscalizador
---

# Javier Cruz Tamburrino

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Unidad de Analisis Financiero]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Estado**: `= this.medida_cautelar`

## Síntesis
Abogado y ex Director de la [[Unidad de Analisis Financiero]] (UAF). Durante su gestión al frente de la unidad de inteligencia financiera del Estado se remitieron al Ministerio Público los Reportes de Operaciones Sospechosas (ROS) bancarias, automotrices e inmobiliarias que destaparon y documentaron los esquemas de [[Lavado de Activos]] de [[Juan Miguel Fuente-Alba Poblete]] en el [[Caso Milicogate]] ([[TRX-2015-08-14-GastosReservados-Ejercito-UAF-01]]) y del clan mafioso de intendencia encabezado por [[Flavio Echeverria Cortez]] en la [[Direccion de Finanzas de Carabineros]] en el [[Caso Pacogate]] ([[TRX-2017-03-06-Reportes-UAF-Carabineros-01]]), así como las alertas sobre [[Factop SpA]] y [[Luis Hermosilla Osorio]].

## Flujos Ilícitos Trazabilizados en Nexos UAF
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

dv.header(4, `Monto Total Trazabilizado en ROS UAF: ${formattedTotal}`);
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
| [Procesan a general (r) por defraudar al fisco con cerca de 1.800 millones](https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) | Cooperativa | `secundaria` | 2018-02-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) |
| [Corte Marcial revoca condena por fraude a general (r) Santic](https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) | vLex Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) |
| [Fraude en el Ejército: Corte Marcial disminuye condenas a cuatro uniformados](https://www.elciudadano.com/?p=683869) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=683869) |
| [Los documentos secretos del Milicogate](https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) | The Clinic | `secundaria` | 2015-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) |
| [Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude](https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) | El Mostrador | `secundaria` | 2026-04-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) |
| [Pacogate](https://en.wikipedia.org/wiki/Pacogate) | Wikipedia | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://en.wikipedia.org/wiki/Pacogate) |
