---
tipo_nodo: persona
rut: ""
aliases:
  - "Gabriel Ruiz-Tagle"
  - "Gabriel Ruiz-Tagle Serrano"
rol_principal: "Fundador y Ex Controlador de PISA (SCA Chile), Ex Ministro del Deporte y Ex Presidente de Blanco y Negro S.A."
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Sancionado por la CMF con multa e inhabilitación por uso de información privilegiada; artífice inicial del Cartel del Papel Tissue"
tags:
  - entidad/persona
  - ex-ministro
  - udi
  - caso-colusion-tissue
---

# Gabriel Ruiz-Tagle Serrano

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Empresario y dirigente político de la [[Union Democrata Independiente]]. Se desempeñó como Subsecretario y posteriormente Ministro del Deporte durante el primer gobierno de [[Sebastian Pinera Echenique]] (2010–2014) y presidente de Blanco y Negro S.A. (Colo-Colo). 

En el ámbito de libre competencia, fue el fundador y controlador de *Papeles Industriales S.A.* (PISA, hoy [[SCA Chile SA]]). En el [[Caso Colusion del Papel Tissue]], las investigaciones de la [[Fiscalia Nacional Economica]] y el Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-160-Colusion-Tissue-2017]]) acreditaron que en el año 2000 sostuvo reuniones clandestinas en el Club de Golf Las Brisas de Chicureo con ejecutivos de [[Empresas CMPC SA]] para poner fin a la «guerra de precios» y acordar el reparto de cuotas de mercado del papel higiénico y servilletas ([[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]). Posteriormente, en 2019 fue sancionado por la [[Comision para el Mercado Financiero]] con una multa de 7.500 UF y 5 años de inhabilitación directiva por uso de información privilegiada en la venta de acciones de Blanco y Negro.

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
