---
tipo_nodo: persona
rut: ""
aliases:
  - "Claudio Spiniak"
rol_principal: "Empresario y Controlador de Inversiones El Bosque Ltda. (Gimnasio Go Fitness)"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Fallecido en marzo de 2026; había cumplido su condena (12 años, ratificada por la Corte Suprema en 2008)"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html"
  - "https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html"
  - "https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html"
  - "https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz"
tags:
  - entidad/persona
  - caso-spiniak
  - sector-privado
---

# Claudio Spiniak Vilensky

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Empresario propietario del centro de eventos y gimnasio *Go Fitness* en avenida El Bosque Norte (Las Condes), operado mediante [[Inversiones El Bosque Ltda]]. Detenido el 30 de septiembre de 2003 como cabecilla de la red investigada en el [[Caso Spiniak]], el [[Servicio Impuestos Internos]] y los peritajes contables ordenados por el ministro [[Sergio Munoz Gajardo]] auditaron el desvío de recursos societarios, gastos rechazados y ocultamiento patrimonial destinados a financiar la red ilícita ([[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]]). En 2008, la [[Corte Suprema de Chile]] elevó su condena definitiva a 12 años de presidio efectivo ([[Sentencia-Corte-Suprema-CasoSpiniak-2008]]).

## Montos Imputados como Autorizador de Origen
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

dv.header(4, `Monto Total Asociado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
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
| [Falleció Claudio Spiniak, empresario condenado por liderar una red de pedofilia](https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) | Cooperativa | `secundaria` | 2026-03-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) |
| [Claudio Spiniak fue condenado a cinco años y un día de cárcel](https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) | Cooperativa | `secundaria` | 2006-08-10 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) |
| [Muere Claudio Spiniak](https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) | Emol | `secundaria` | 2026-03-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) |
| [Jovino Novoa, caso Spiniak e investigación del juez Sergio Muñoz](https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) | Pauta | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) |
