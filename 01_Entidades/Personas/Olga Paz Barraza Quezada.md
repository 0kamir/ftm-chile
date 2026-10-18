---
tipo_nodo: persona
rut: "15.632.187-7"
aliases:
  - "Olga Barraza Quezada"
  - "Olga Paz Barraza Quezada"
rol_principal: "Líder del Clan Barraza en el Megafraude de la Operación Tributos"
afiliacion_politica: "Independiente"
situacion_procesal: formalizada
medida_cautelar: "Prisión preventiva por asociación ilícita, fraude tributario y lavado de activos"
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - clan-barraza
---

# Olga Paz Barraza Quezada

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Operadora comercial y líder del "Clan Barraza", articulación criminal formalizada en el marco del [[Caso Megafraude Tributario Operacion Tributos]]. Según la querella del [[Servicio Impuestos Internos]], su organización suministró facturación fraudulenta a empresas del rubro de la construcción, transporte y servicios en diversas regiones del país, captando comisiones porcentuales sobre el valor del IVA descontado ilegítimamente por los receptores.

Fue detenida en diciembre de 2023 por la BRILAC de la PDI y puesta en prisión preventiva por resolución del 1° Juzgado de Garantía de Santiago.

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
