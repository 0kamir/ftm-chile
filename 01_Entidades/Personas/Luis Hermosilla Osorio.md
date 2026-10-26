---
tipo_nodo: persona
rut: ""
aliases:
  - "Luis Hermosilla"
  - "Luis Hermosilla Osorio"
rol_principal: "Abogado Penalista y Asesor Legal"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva / Arresto domiciliario total"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
  - "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
  - "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
  - "https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/"
  - "https://www.diarioconstitucional.cl/2026/03/10/corte-suprema-confirma-condena-contra-exdirector-de-la-pdi-hector-espinosa-por-malversacion-de-gastos-reservados-y-lavado-de-activos/"
  - "https://www.ciperchile.cl/2021/10/07/los-depositos-en-efectivo-que-acorralan-al-exdirector-de-la-pdi-hector-espinosa/"
tags:
  - entidad/persona
  - caso-audios
  - abogado
---

# Luis Hermosilla Osorio

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Abogado penalista formalizado en el [[Caso Audios]] por delitos reiterados de [[Cohecho]], [[Lavado de Activos]] y delitos tributarios. En la reunión grabada en [[Audio-Reunion-Edificio-Alonso-2023]], según la acusación, habría coordinado junto a [[Leonarda Villalobos Muth]] un esquema de pagos ([[TRX-2023-06-22-Reunion-Audios-01]]) desde operaciones vinculadas a [[Factop SpA]] hacia funcionarios del [[Servicio Impuestos Internos]]. Asimismo, encabezó la defensa en la Acusación Constitucional de diciembre de 2019 de su socio de oficina y exministro del Interior [[Andres Chadwick Pinera]] (primo de [[Sebastian Pinera Echenique]]), transfiriéndole más de **`$190.000.000 CLP`** desde fondos originados en [[Factop SpA]] ([[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]) y articulando gestiones de [[Trafico de Influencias]] ante la [[Corte Suprema de Chile]] con [[Angela Vivanco Martinez]] ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) y coordinaciones en nombramientos judiciales con el penalista [[Gabriel Zaliasnik Schilkrut]] ([[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]]).

## Montos Operados como Firmante/Operador de Origen
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
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Contraparte", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
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
| [Cinco claves para comprender el caso Audios](https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) | Emol | `secundaria` | 2024-08-21 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) |
| [“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF](https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) | CIPER Chile | `secundaria` | 2023-11-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) |
| [Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho](https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) | El Dínamo | `secundaria` | 2024-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) |
| [Caso Audios: Luis Hermosilla será formalizado por la arista Parque Capital](https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) |
| [Corte Suprema confirma condena contra exdirector de la PDI Héctor Espinosa por malversación de gastos reservados y lavado de activos](https://www.diarioconstitucional.cl/2026/03/10/corte-suprema-confirma-condena-contra-exdirector-de-la-pdi-hector-espinosa-por-malversacion-de-gastos-reservados-y-lavado-de-activos/) | Diario Constitucional / Poder Judicial | `secundaria` | 2026-03-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.diarioconstitucional.cl/2026/03/10/corte-suprema-confirma-condena-contra-exdirector-de-la-pdi-hector-espinosa-por-malversacion-de-gastos-reservados-y-lavado-de-activos/) |
| [Los depósitos en efectivo que acorralan al exdirector de la PDI Héctor Espinosa](https://www.ciperchile.cl/2021/10/07/los-depositos-en-efectivo-que-acorralan-al-exdirector-de-la-pdi-hector-espinosa/) | CIPER Chile | `secundaria` | 2021-10-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2021/10/07/los-depositos-en-efectivo-que-acorralan-al-exdirector-de-la-pdi-hector-espinosa/) |
