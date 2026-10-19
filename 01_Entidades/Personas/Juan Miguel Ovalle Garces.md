---
tipo_nodo: persona
rut: ""
aliases:
  - "Juan Miguel Ovalle"
  - "Juan Miguel Ovalle Garces"
rol_principal: "Presidente Histórico de la Asociación de Productores Avícolas de Chile (APA)"
afiliacion_politica: "Independiente"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Condena civil y económica; disolución forzada de la entidad gremial que presidía"
tags:
  - entidad/persona
  - dirigente-gremial
  - apa
  - colusion-pollos
---

# Juan Miguel Ovalle Garces

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Dirigente gremial y médico veterinario que ejerció durante más de dos décadas como presidente ejecutivo de la [[Asociacion de Productores Avicolas de Chile AG]] (APA). 

En el marco del [[Caso Colusion de los Pollos]], la investigación de la [[Fiscalia Nacional Economica]] y los tribunales de justicia lo identificaron como el artífice técnico y coordinador cotidiano del cartel. Desde su posición en la APA, calculaba y distribuía las cuotas de producción entre [[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]], auditaba los despachos e intervenía ante eventuales desviaciones de los acuerdos de restricción de oferta, lo que culminó en la disolución judicial forzosa del gremio.

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
