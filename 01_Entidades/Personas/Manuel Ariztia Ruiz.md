---
tipo_nodo: persona
rut: ""
aliases:
  - "Manuel Ariztia"
  - "Manuel Ariztia Ruiz"
rol_principal: "Fundador y Presidente Histórico de Empresas Ariztía"
afiliacion_politica: "Independiente"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Condena civil y económica corporativa ratificada por la Corte Suprema de Chile"
tags:
  - entidad/persona
  - empresario
  - ariztia
  - colusion-pollos
---

# Manuel Ariztia Ruiz

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Empresario chileno del sector agropecuario, fundador y presidente de [[Empresas Ariztia SA]]. Su empresa fue una de las principales integrantes del cartel avícola sancionado en el [[Caso Colusion de los Pollos]].

De acuerdo con el requerimiento de la [[Fiscalia Nacional Economica]] y el fallo del Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-139-Colusion-Pollos-2014]]), Ariztía participó sistemáticamente en los acuerdos para coordinar los volúmenes de faenamiento y limitar la producción con el objetivo de controlar los precios internos, motivo por el cual la [[Corte Suprema de Chile]] le impuso la sanción económica máxima de 30.000 UTA.

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
