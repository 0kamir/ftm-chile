---
tipo_nodo: persona
rut: "7.319.482-2"
aliases:
  - "Gonzalo Delaveau"
rol_principal: "Abogado Societario, Agente de Mossack Fonseca en Chile y Ex Presidente de Chile Transparente"
afiliacion_politica: "Independiente"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Renuncia forzada a la presidencia de Chile Transparente (4 de abril de 2016) y fiscalización tributaria del SII"
tags:
  - entidad/persona
  - panama-papers
  - offshore
  - conflicto-interes
---

# Gonzalo Delaveau Swett

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Mossack Fonseca y Sociedades Offshore Panama]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal / Institucional**: `= this.situacion_procesal`
- **Consecuencia Institucional**: `= this.medida_cautelar`

## Síntesis Forense
Abogado especialista en derecho corporativo y minero que ejercía como **Presidente de *Chile Transparente*** (el capítulo chileno de la organización anticorrupción *Transparencia Internacional*) cuando el 3 de abril de 2016 estalló el [[Caso Panama Papers Chile]]. Los documentos internos de [[Mossack Fonseca y Sociedades Offshore Panama]] revelaron que Delaveau no solo era uno de los principales estudios jurídicos intermediarios del bufete panameño en Santiago, sino que figuraba personalmente como director, apoderado y secretario de al menos **cinco sociedades *offshore* domiciliadas en Bahamas** (*Turnbrook Corporation*, *DKL Holdings*, *Westquarter Limited*, *Mining Press Holdings* y *Turnbrook Mining Ltd.*) que controlaban en Chile el proyecto minero *Andes Copper* ([[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] y [[Informe-ICIJ-SII-PanamaPapers-Chile-2016]]). Ante el conflicto de interés con su cargo al frente del organismo anticorrupción, debió presentar su renuncia indeclinable el 4 de abril de 2016.

## Auditoría Contable: Montos Asociados en Aristas Reificadas
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
