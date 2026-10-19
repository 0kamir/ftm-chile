---
tipo_nodo: persona
rut: ""
aliases:
  - "Ángela Vivanco"
  - "Ángela Vivanco Martínez"
rol_principal: "Ex Ministra de la Corte Suprema de Chile (2018-2024)"
afiliacion_politica: "Independiente (Ex RN)"
situacion_procesal: formalizado
medida_cautelar: "Sujeta a investigación penal y destituida por cuaderno de remoción"
tags:
  - entidad/persona
  - caso-audios
  - poder-judicial
---

# Angela Vivanco Martinez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Corte Suprema de Chile]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Abogada y exministra de la [[Corte Suprema de Chile]]. En la arista judicial del [[Caso Audios]], el Ministerio Público investiga las comunicaciones y gestiones sostenidas con el abogado [[Luis Hermosilla Osorio]] ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) relativas a nombramientos judiciales y consultas sobre causas radicadas en la Tercera Sala, tipificadas bajo hipótesis de [[Trafico de Influencias]], [[Negociacion Incompatible]] y [[Cohecho]].

## Auditoría de Nexos como Destinataria
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && (
    p.firmante_destino.path === dv.current().file.path ||
    String(p.firmante_destino).includes(dv.current().file.name)
  ));

dv.table(
  ["Nexo / Gestión", "Fecha", "Tipo Nexo", "Origen", "Operador Origen", "Delito Imputado", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.firmante_origen,
    p.delito_imputado,
    p.causa_vinculada
  ])
);
```
