---
tipo_nodo: persona
rut: "3.624.195-0"
aliases:
  - "Gonzalo Vial"
  - "Gonzalo Vial Vial"
rol_principal: "Fundador y Presidente Histórico de Agrosuper"
afiliacion_politica: "Independiente"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Condena civil y económica corporativa ratificada por la Corte Suprema de Chile"
tags:
  - entidad/persona
  - empresario
  - agrosuper
  - colusion-pollos
---

# Gonzalo Vial Vial

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Destacado empresario agroindustrial chileno, fundador y presidente del directorio de [[Agrosuper SA]]. Bajo su liderazgo empresarial, Agrosuper se consolidó como el gigante de la industria avícola, porcina y acuícola en Chile.

En el marco del [[Caso Colusion de los Pollos]], las investigaciones de la [[Fiscalia Nacional Economica]] y la [[Sentencia-TDLC-139-Colusion-Pollos-2014]] determinaron la activa participación de los directivos de Agrosuper en las reuniones de fijación y asignación de cuotas de producción avícola junto a [[Empresas Ariztia SA]] y la [[Asociacion de Productores Avicolas de Chile AG]], lo que conllevó la condena a su compañía con la multa máxima de 30.000 UTA fijada por la [[Corte Suprema de Chile]].

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
