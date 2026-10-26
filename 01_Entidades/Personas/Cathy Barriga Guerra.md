---
tipo_nodo: persona
rut: ""
aliases:
  - "Cathy Barriga"
  - "Cathy Carolina Barriga Guerra"
rol_principal: "Ex Alcaldesa de la Municipalidad de Maipú (2016-2021)"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva / Arresto domiciliario total"
vinculos_familiares: []
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/"
  - "https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/"
  - "https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/"
  - "https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html"
tags:
  - entidad/persona
  - caso-maipu
  - alcaldesa
---

# Cathy Barriga Guerra

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Maipu]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Exalcaldesa de la [[Municipalidad de Maipu]] y ex Consejera Regional, electa en el cupo de [[Union Democrata Independiente]]. Fue formalizada por la Fiscalía Metropolitana Oriente en el [[Caso Municipalidad de Maipu]] por delitos reiterados de [[Fraude al Fisco]] y falsificación de instrumento público por un perjuicio patrimonial de **$30.972.000.000 CLP** ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]), según el [[Informe-Contraloria-Municipalidad-Maipu-2021]].

## Montos Imputados como Firmante de Origen
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

dv.header(4, `Monto Total Imputado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Monto (CLP)", "Delito", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.delito_imputado,
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Expediente Cathy Barriga: las pruebas clave](https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/) |
| [Formalización de Cathy Barriga: qué delitos le imputan](https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) | CNN Chile | `secundaria` | 2024-01-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) |
| [Exalcaldesa Cathy Barriga será formalizada en enero de 2024](https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) | El Mostrador | `secundaria` | 2023-11-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) |
| [Caso Maipú: Fiscalía Oriente reformalizará a Cathy Barriga](https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) | Meganoticias | `secundaria` | 2024-08-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) |
