---
tipo_nodo: persona
rut: ""
aliases:
  - "Santiago Valdés"
rol_principal: "Ex Gerente de Administración y Finanzas de Bancard y Administrador Electoral Campaña Presidencial 2009"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: sobreseido
medida_cautelar: "Sobreseído en 2019 por prescripción (Corte de Apelaciones de Santiago)"
estado_verificacion: verificado
fuentes:
  - "https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/"
  - "https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
  - "https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html"
tags:
  - entidad/persona
  - caso-sqm
  - caso-penta
  - caso-exalmar
  - bancard
---

# Santiago Valdes Gutierrez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Bancard Inversiones Ltda]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Ingeniero comercial, gerente de administración y finanzas de [[Bancard Inversiones Ltda]] y administrador electoral de la campaña presidencial de [[Sebastian Pinera Echenique]] en 2009. Fue formalizado en 2015 en el [[Caso Penta]] por delitos tributarios vinculados a facturas emitidas a [[SQM SA]] ([[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]]), que él sostuvo correspondían a asesorías efectivamente prestadas. En 2019 la Corte de Apelaciones sobreseyó a lo por prescripción (habían transcurrido más de cinco años desde los hechos al abrirse la investigación); no existe sentencia que declare falsas las facturas. Rige la presunción de inocencia.

Asimismo, participó en la ejecución de las inversiones *offshore* de *Bancard International Investment Inc.* en la pesquera peruana *Exalmar S.A.* en el [[Caso Exalmar y Fideicomiso Ciego]] ([[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]]).

## Montos Operados en Aristas Reificadas
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

dv.header(4, `Monto Total Asociado: ${formattedTotal}`);
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
| [Fiscalía reconstruye los pasos de Manuel Guerra: así se selló la salida del administrador electoral de Piñera del caso Penta](https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) | CIPER Chile | `secundaria` | 2024-11-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) |
| [Facturas de SQM aterrizan en campaña de Piñera: pagos de 2009 suman $103 millones](https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) | The Clinic | `secundaria` | 2017-09-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
| [Fiscalía presenta recurso de nulidad contra fallo del caso SQM](https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) | Emol | `secundaria` | 2026-09-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/09/04/1210579/fiscalia-nulidad-fallo-caso-sqm.html) |
