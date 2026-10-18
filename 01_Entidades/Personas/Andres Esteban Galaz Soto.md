---
tipo_nodo: persona
rut: "14.210.543-8"
aliases:
  - "Andres Galaz Soto"
  - "Andres Esteban Galaz Soto"
rol_principal: "Líder del Clan Galaz en el Megafraude de la Operación Tributos"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva por asociación ilícita, fraude tributario y lavado de activos"
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - clan-galaz
---

# Andres Esteban Galaz Soto

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Empresario imputado como cabecilla del "Clan Galaz", uno de los 7 grupos estructurados identificados en el [[Caso Megafraude Tributario Operacion Tributos]]. La Fiscalía le imputó la administración de múltiples sociedades de fachada empleadas para la intermediación y comercio clandestino de facturas falsas, facilitando a cientos de contribuyentes la evasión del IVA y del Impuesto a la Renta mediante maniobras de crédito fiscal ilegítimo.

Formalizado ante el 1° Juzgado de Garantía de Santiago tras el allanamiento masivo de diciembre de 2023, quedó sujeto a la medida cautelar de prisión preventiva.

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
