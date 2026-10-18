---
tipo_nodo: persona
rut: "12.948.123-4"
aliases:
  - "Percy Marin"
  - "Percy Marin Vera"
rol_principal: "Ex Consejero Regional (CORE) de Valparaíso por Renovación Nacional"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: investigado
medida_cautelar: "Obligado por la Contraloría a restituir viáticos indebidos; allanado por la PDI por denuncia de difusión no consentida de registros íntimos"
tags:
  - entidad/persona
  - ex-core
  - rn
  - valparaiso
  - viaticos
  - percy-marin
---

# Percy Marin Vera

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medidas Cautelares / Sanciones Administrativas**: `= this.medida_cautelar`

## Síntesis Forense y Casos Vinculados
Dirigente político de [[Renovacion Nacional]] en la Región de Valparaíso, donde se desempeñó como consejero regional (CORE) y presidente del Consejo Regional. Exmarido de la senadora [[Camila Flores Oporto]].

1. **Sanción y Reparos de la Contraloría por Viáticos**: La Contraloría General de la República (CGR) determinó que percibió indebidamente millones de pesos por concepto de viáticos y asignaciones de combustible al fijar un domicilio particular ficticio alejado de la sede regional, obligándolo a reintegrar los fondos públicos mal percibidos.
2. **Denuncia Penal y Allanamiento por Difusión de Registros Íntimos**: En el marco del [[Caso Asignaciones Parlamentarias y Cuota Flores]], fue denunciado penalmente ante la Brigada del Cibercrimen de la Policía de Investigaciones (PDI) por la presunta extracción no autorizada y difusión masiva de registros audiovisuales privados de su expareja Camila Flores obtenidos desde cámaras de seguridad del domicilio común ([[TRX-2026-06-20-Extraccion-Difusion-Ilicita-Registros-Intimos-01]]), diligencia que motivó el allanamiento de su residencia por parte de la PDI ([[Denuncia-Cibercrimen-PDI-Registros-Intimos-2026]]).

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
