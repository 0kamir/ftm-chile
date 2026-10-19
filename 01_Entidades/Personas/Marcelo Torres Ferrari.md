---
tipo_nodo: persona
rut: ""
aliases:
  - "Marcelo Torres"
rol_principal: "Ex Concejal de Maipú y Ex Administrador Municipal de Cerro Navia"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: condenado
medida_cautelar: "Condenado por cohecho y lavado de activos (arista Maipú, 2022) y por fraude al fisco reiterado (arista Cerro Navia, dic-2024)"
estado_verificacion: verificado
fuentes:
  - url: "https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/"
    titulo: "Ex concejal RN de Maipú es condenado por lavado de activos y cohecho en caso Basura"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2022-07-28
    consultado: 2026-10-19
  - url: "https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf"
    titulo: "Comunicado Fiscalía Occidente: condenas Caso Basura arista Cerro Navia"
    medio: "Fiscalía Regional Metropolitana Occidente (vía El Mostrador)"
    tipo: primaria
    fecha: 2025-06-03
    consultado: 2026-10-19
tags:
  - entidad/persona
  - caso-basura
  - broker-municipal
---

# Marcelo Torres Ferrari

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Municipalidad de Maipu]] / [[Municipalidad de Cerro Navia]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Estado Procesal**: `= this.medida_cautelar`

## Síntesis Forense
Ex Concejal de la [[Municipalidad de Maipu]] y ex Administrador Municipal de la [[Municipalidad de Cerro Navia]] (bajo la gestión de [[Luis Plaza Sanchez]]), militante de [[Renovacion Nacional]]. En el [[Caso Basura]] ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]) fue sindicado por el Ministerio Público como el principal nodo articulador inter-municipal que recibió pagos ilícitos de [[KDM Empresas SA]] ([[Fernando Leon Steffens]]) para asegurar votos en el Concejo Municipal de Maipú en la licitación de basura por **$18.500.000.000 CLP** ([[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]]) y operar contrataciones irregulares en Cerro Navia por **$1.120.000.000 CLP** ([[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]]).

## Auditoría Contable: Montos Operados como Firmante de Destino
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

dv.header(4, `Monto Total Articulado (firmante_destino): ${formattedTotal}`);
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
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
