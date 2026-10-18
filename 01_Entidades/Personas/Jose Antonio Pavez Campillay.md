---
tipo_nodo: persona
rut: "13.845.921-7"
aliases:
  - "Jose Pavez Campillay"
  - "Jose Antonio Pavez Campillay"
rol_principal: "Líder del Clan Pavez y Principal Imputado en la Operación Tributos (Megafraude SII)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva en Capitán Yáber por asociación ilícita, fraude tributario y lavado de activos"
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - clan-pavez
---

# Jose Antonio Pavez Campillay

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Empresario chileno identificado por la Fiscalía Metropolitana Occidente y la PDI como el líder operativo e ideólogo del clan criminal más cuantioso del [[Caso Megafraude Tributario Operacion Tributos]]. A través de un entramado societario de más de 30 empresas pantalla, entre ellas [[Inversiones y Asesorias Pavez SpA]] y [[Comercializadora y Exportadora Global SpA]], coordinó la emisión y venta masiva de facturas ideológicamente falsas y la solicitud fraudulenta de devolución de IVA exportador ante el [[Servicio Impuestos Internos]], causando un perjuicio fiscal directo estimado en más de $56.000 millones de pesos imputables a su grupo directo.

Fue detenido el 14 de diciembre de 2023 en un allanamiento ejecutado por la Brigada de Lavado de Activos (BRILAC) de la PDI, incautándosele vehículos de alta gama, propiedades y cuentas bancarias. Quedó sujeto a la medida cautelar de prisión preventiva decretada por el 1° Juzgado de Garantía de Santiago.

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
