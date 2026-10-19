---
tipo_nodo: persona
rut: ""
aliases:
  - "Bruno Villalobos"
  - "Bruno Villalobos Krumm"
rol_principal: "Ex General Director de Carabineros de Chile (2015–2018)"
afiliacion_politica: "Militar / Carabineros"
situacion_procesal: formalizado
medida_cautelar: "Procesado y acusado en arista de malversación de gastos reservados en Carabineros"
tags:
  - entidad/persona
  - carabineros
  - caso-operacion-huracan
  - caso-pacogate
---

# Bruno Villalobos Krumm

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
General director de Carabineros entre agosto de 2015 y marzo de 2018. Su jefatura institucional coincidió con el destape de los dos mayores escándalos de la policía uniformada: el fraude en el [[Caso Pacogate]] y el montaje de inteligencia en la [[Caso Operacion Huracan]]. 

Durante la [[Caso Operacion Huracan]], respaldó la labor de la UIOE encabezada por el general [[Gonzalo Blu Rodriguez]], defendiendo la validez de los antecedentes presentados ante el Ministerio del Interior. En enero de 2018, al revelarse los peritajes de la PDI que desacreditaron el software «Antorcha», viajó al extranjero de vacaciones, lo que desató una fuerte controversia pública y culminó con su renuncia forzada el 12 de marzo de 2018. Paralelamente, fue procesado por la justicia militar y civil por la presunta malversación de más de `$600.000.000 CLP` en gastos reservados institucionales.

## Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Delito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    p.delito_imputado
  ])
);
```
