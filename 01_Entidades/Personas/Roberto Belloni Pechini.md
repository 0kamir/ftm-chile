---
tipo_nodo: persona
rut: ""
aliases:
  - "Roberto Belloni"
  - "Roberto Belloni Pechini"
rol_principal: "Ex Gerente General Corporativo de Farmacias Salcobrand S.A."
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Formalizado penalmente por alteración fraudulenta de precios (absuelto en juicio penal por atipicidad previa a reforma Ley 20.945; condena ejecutoriada a la empresa por el TDLC)"
tags:
  - entidad/persona
  - ejecutivo
  - farmacias
  - salcobrand
  - colusion-farmacias
---

# Roberto Belloni Pechini

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Farmacias Salcobrand SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Marco Judicial**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero comercial que ejerció como gerente general de [[Farmacias Salcobrand SA]] durante el período del cartel. En el [[Caso Colusion de las Farmacias]], los correos electrónicos incautados por la [[Fiscalia Nacional Economica]] y periciados por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) demostraron que Belloni mantuvo contacto con gerentes de laboratorios internacionales para exigirles que forzaran a [[Farmacias Ahumada SA]] y [[Farmacias Cruz Verde SA]] a respetar los precios acordados, amenazando con represalias comerciales en caso de quiebres de precios ([[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]). 

En sede penal, fue formalizado junto a otros 9 ejecutivos por alteración fraudulenta de precios de medicamentos. Si bien el tribunal oral los absolvió en 2015 al considerar que la antigua norma del artículo 285 del Código Penal no describía con exactitud la colusión moderna entre cadenas, el fallo provocó un escándalo ciudadano transversal que motivó al Congreso a dictar la Ley N° 20.945 en 2016, reincorporando la pena de cárcel efectiva para los delitos de colusión.

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
