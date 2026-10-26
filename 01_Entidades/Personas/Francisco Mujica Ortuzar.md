---
tipo_nodo: persona
rut: ""
aliases:
  - "Francisco Mujica"
  - "Francisco Mujica Ortúzar"
rol_principal: "Ex Gerente General de Corpesca S.A. (1999-2013)"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condena ejecutoriada en procedimiento abreviado por soborno y delitos tributarios"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html"
tags:
  - entidad/persona
  - caso-corpesca
  - condenado
  - ejecutivo
---

# Francisco Mujica Ortuzar

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Corpesca SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Ingeniero comercial y ex gerente general de [[Corpesca SA]]. Fue condenado en el [[Caso Corpesca]] como autor de delitos reiterados de [[Cohecho]] activo (soborno) y [[Delito Tributario]], tras autorizar los pagos por **$233.000.000 CLP** al entonces senador [[Jaime Orpis Bouchon]] ([[TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01]]) para incidir en la discusión de la Ley de Pesca en el [[Senado de la Republica de Chile]], hechos refrendados en [[Sentencia-3TOP-Santiago-Corpesca-2021]].

## Montos Autorizados como Firmante de Origen
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

dv.header(4, `Monto Total Condenado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Empresa", "Destinatario", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Corpesca: Jaime Orpis fue condenado por fraude al Fisco y cohecho](https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html) | Cooperativa | `secundaria` | 2020-12-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html) |
| [Ex senador Jaime Orpis irá a la cárcel por fraude al Fisco y cohecho](https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html) | Cooperativa | `secundaria` | 2021-04-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html) |
| [Corte confirmó la pena de cárcel para el ex senador Jaime Orpis](https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html) | Cooperativa | `secundaria` | 2022-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html) |
