---
tipo_nodo: persona
rut: "11.984.210-7"
aliases:
  - "Ximena Jimenez"
  - "Ximena Jimenez Faras"
rol_principal: "Contadora, Operadora Financiera y Socia Operativa del Clan Pavez"
afiliacion_politica: "Independiente"
situacion_procesal: formalizada
medida_cautelar: "Prisión preventiva por asociación ilícita, delitos tributarios reiterados y lavado de activos"
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - clan-pavez
---

# Ximena Jimenez Faras

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Contadora y brazo operativo financiero de [[Jose Antonio Pavez Campillay]] en el [[Caso Megafraude Tributario Operacion Tributos]]. Según la formalización del Ministerio Público y las querellas del [[Servicio Impuestos Internos]], desempeñó un rol técnico determinante en la estructuración de balances ficticios, confección de declaraciones tributarias maliciosamente falsas (Formularios 29 y 22) y timbraje electrónico de facturas ideológicamente falsas para decenas de empresas fantasmas.

Fue detenida en los operativos simultáneos del 14 de diciembre de 2023 por la BRILAC de la PDI, quedando formalizada en el 1° Juzgado de Garantía de Santiago bajo prisión preventiva.

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
