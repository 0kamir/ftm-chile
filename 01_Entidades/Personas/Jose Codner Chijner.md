---
tipo_nodo: persona
rut: "3.948.123-5"
aliases:
  - "José Codner"
  - "José Codner Chijner"
rol_principal: "Fundador y Ex Controlador de Farmacias Ahumada S.A. (FASA)"
afiliacion_politica: "Independiente"
situacion_procesal: descarte_procesal_sin_imputacion
medida_cautelar: "Sin medidas cautelares vigentes; firmante del acuerdo conciliatorio de delación ante la FNE en marzo de 2009"
tags:
  - entidad/persona
  - empresario
  - farmacias
  - colusion-farmacias
---

# Jose Codner Chijner

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Farmacias Ahumada SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Hito Regulatorio**: `= this.medida_cautelar`

## Síntesis Forense
Químico farmacéutico y empresario que transformó un modesto local en la cadena Farmacias Ahumada (FASA), expandiéndola a nivel nacional e internacional (Brasil, México y Perú). 

En el [[Caso Colusion de las Farmacias]], su administración participó en el cartel de alza de precios de 222 medicamentos entre diciembre de 2007 y marzo de 2008 junto a [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]] ([[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]). Ante la contundencia de las pruebas reunidas por la [[Fiscalia Nacional Economica]], en marzo de 2009 Codner y el directorio de FASA rompieron la defensa común del sector y firmaron un inédito acuerdo conciliatorio con la FNE ([[Acuerdo-Conciliatorio-FNE-FASA-2009]]), reconociendo la concertación de precios y pagando US$ 1 millón, lo que detonó una fuerte pugna interna entre los accionistas (incluido el grupo Falabella) y derivó en la venta de la cadena al consorcio mexicano Casa Saba en 2010.

## Auditoría Contable: Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Delito", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    p.delito_imputado,
    p.causa_vinculada
  ])
);
```
