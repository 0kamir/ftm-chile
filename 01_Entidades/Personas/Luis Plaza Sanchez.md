---
tipo_nodo: persona
rut: ""
aliases:
  - "Luis Plaza"
rol_principal: "Ex Alcalde de la Municipalidad de Cerro Navia (2008-2016)"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: condenado
medida_cautelar: "Condenado a 3 años y 1 día por fraude al fisco reiterado, con inhabilitación perpetua para derechos políticos (arista Cerro Navia, dic-2024)"
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/nacional/noticia/a-13-anos-de-que-se-iniciara-el-caso-condenan-a-exalcalde-luis-plaza-rn-por-fraude-al-fisco-en-ultima-arista-del-emblematico-caso-basura/TGWT6RCHCJHEBP5MVQXK2VL2AE/"
  - "https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf"
  - "https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/"
tags:
  - entidad/persona
  - caso-basura
  - renovacion-nacional
---

# Luis Plaza Sanchez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Cerro Navia]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Estado Procesal**: `= this.medida_cautelar`

## Síntesis
Ex Alcalde de la [[Municipalidad de Cerro Navia]] y militante de [[Renovacion Nacional]]. En el [[Caso Basura]] ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]), fue formalizado y acusado por la Fiscalía Regional Metropolitana Occidente junto a su entonces administrador municipal [[Marcelo Torres Ferrari]] por el delito de [[Fraude al Fisco]] en contrataciones y licitaciones municipales de aseo y servicios conexos a la red de [[KDM Empresas SA]] por **$1.120.000.000 CLP** ([[TRX-2012-03-22-Contratos-Residuos-CerroNavia-01]]).

## Montos Autorizados como Firmante de Origen
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name));

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
| [A 13 años de que se iniciara el caso, condenan a exalcalde Luis Plaza por fraude al fisco en última arista del Caso Basura](https://www.latercera.com/nacional/noticia/a-13-anos-de-que-se-iniciara-el-caso-condenan-a-exalcalde-luis-plaza-rn-por-fraude-al-fisco-en-ultima-arista-del-emblematico-caso-basura/TGWT6RCHCJHEBP5MVQXK2VL2AE/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/a-13-anos-de-que-se-iniciara-el-caso-condenan-a-exalcalde-luis-plaza-rn-por-fraude-al-fisco-en-ultima-arista-del-emblematico-caso-basura/TGWT6RCHCJHEBP5MVQXK2VL2AE/) |
| [Comunicado Fiscalía Occidente: condenas Caso Basura arista Cerro Navia](https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf) | Fiscalía Regional Metropolitana Occidente (vía El Mostrador) | `primaria` | 2025-06-03 | [Wayback ↺](https://web.archive.org/web/*/https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf) |
| [Ex concejal RN de Maipú es condenado por lavado de activos y cohecho en caso Basura](https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/) | El Dínamo | `secundaria` | 2022-07-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/) |
