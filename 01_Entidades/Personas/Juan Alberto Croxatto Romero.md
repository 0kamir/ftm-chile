---
tipo_nodo: persona
rut: "12.489.371-2"
aliases:
  - "Juan Croxatto Romero"
  - "Juan Alberto Croxatto Romero"
rol_principal: "Líder del Clan Croxatto en la Operación Tributos (Megafraude SII)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Prisión preventiva por asociación ilícita, delitos tributarios y lavado de activos"
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - clan-croxatto
---

# Juan Alberto Croxatto Romero

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Imputado como cabecilla del "Clan Croxatto" dentro del [[Caso Megafraude Tributario Operacion Tributos]]. Su estructura delictiva operaba como un eslabón clave en la creación y administración de sociedades de papel destinadas a canalizar pagos y generar contratos ficticios de prestación de servicios, permitiendo a sus clientes deducir gastos falsos e inflar créditos de IVA.

Detenido en diciembre de 2023 por la Policía de Investigaciones de Chile en el marco de la mayor redada tributaria registrada en el país, fue formalizado ante el 1° Juzgado de Garantía de Santiago.

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
