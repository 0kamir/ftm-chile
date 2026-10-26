---
tipo_nodo: persona
rut: ""
aliases:
  - "Patricio Contesse"
  - "Patricio Contesse González"
rol_principal: "Ex Gerente General de SQM S.A. (1990-2015)"
afiliacion_politica: "Independiente"
situacion_procesal: absuelto
medida_cautelar: "Absuelto por el 3° TOP de Santiago (22-10-2025); recursos de nulidad de Fiscalía, SII y CDE pendientes"
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
  - "https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/"
  - "https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
tags:
  - entidad/persona
  - caso-sqm
  - ejecutivo
---

# Patricio Contesse Gonzalez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[SQM SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Ingeniero forestal y ex gerente general de [[SQM SA]]. En el [[Caso SQM]] la Fiscalía y el [[Servicio Impuestos Internos]] ([[Querella-SII-Boletas-SQM-2015]]) lo acusaron de [[Delito Tributario]] reiterado y soborno por pagos a personas vinculadas a [[Pablo Longueira Montes]] durante la tramitación del Royalty Minero ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]). El 22 de octubre de 2025 el 3° Tribunal de Juicio Oral en lo Penal de Santiago absolvió, por mayoría, a los ocho acusados que llegaron a juicio, entre ellos [[Pablo Longueira Montes]] y [[Patricio Contesse Gonzalez]]: no dio por acreditada más allá de toda duda razonable la falsedad ideológica de las boletas y facturas, y constató una vulneración del derecho a ser juzgado en un plazo razonable. La Fiscalía, el [[Servicio Impuestos Internos]] y el CDE presentaron recursos de nulidad, revisados por la Corte de Apelaciones de Santiago el 6 de octubre de 2026 y pendientes de resolución. Las absoluciones están vigentes y rige la presunción de inocencia.

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

dv.header(4, `Monto Total Autorizado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Contraparte", "Monto (CLP)", "Causa"],
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
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio](https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) | BioBioChile | `secundaria` | 2026-10-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml) |
| [Fiscalía reconstruye los pasos de Manuel Guerra: así se selló la salida del administrador electoral de Piñera del caso Penta](https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) | CIPER Chile | `secundaria` | 2024-11-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) |
| [Facturas de SQM aterrizan en campaña de Piñera: pagos de 2009 suman $103 millones](https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) | The Clinic | `secundaria` | 2017-09-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
