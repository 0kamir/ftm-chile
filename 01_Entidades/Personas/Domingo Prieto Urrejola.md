---
tipo_nodo: persona
rut: ""
aliases:
  - "Domingo Prieto"
  - "Domingo Prieto Urrejola"
rol_principal: "Ex Presidente y Representante Legal de Vita Deportes"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Firma mensual y arraigo nacional (colaboración sustancial)"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/?p=152080"
  - "https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/"
  - "https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html"
tags:
  - entidad/persona
  - caso-vitacura
---

# Domingo Prieto Urrejola

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Vita Deportes]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Exdirectivo de los programas "Vita" y representante legal de [[Vita Deportes]]. Su testimonio y autodenuncia ante la Fiscalía ([[Declaracion-Judicial-Prieto-Vitacura-2021]]) destapó el mecanismo de desvío de subvenciones desde la [[Municipalidad de Vitacura]] ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]) hacia el entonces alcalde [[Raul Torrealba del Pedregal]] en el [[Caso Vitacura]].

## Montos Recibidos como Firmante de Destino
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && (
    p.firmante_destino.path === dv.current().file.path ||
    String(p.firmante_destino).includes(dv.current().file.name)
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

dv.header(4, `Monto Total Recibido (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Firmante Origen", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Audiencia de formalización de Raúl Torrealba](https://www.ex-ante.cl/?p=152080) | Ex-Ante | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/?p=152080) |
| [Fiscalía formalizará a exalcalde Raúl Torrealba por fraude al fisco y asociación ilícita](https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) | La Tercera | `secundaria` | 2023-05-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) |
| [Formalizan a exalcalde Raúl Torrealba](https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) | Pauta | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) |
