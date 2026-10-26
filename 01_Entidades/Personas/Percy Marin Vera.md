---
tipo_nodo: persona
rut: ""
aliases:
  - "Percy Marin"
  - "Percy Marin Vera"
rol_principal: "Ex Consejero Regional (CORE) de Valparaíso por Renovación Nacional"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: ninguna
medida_cautelar: "Juicio de cuentas iniciado por la Contraloría (2020) por viáticos objetados; sin imputación penal conocida"
historial_correcciones:
  - "Se retiró la arista de registros íntimos (2026-10-19): asunto de vida privada sin formalización. RUT eliminado por no constar en fuente pública."
estado_verificacion: parcial
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2020/01/17/contraloria-iniciara-juicio-de-cuentas-contra-percy-marin-cifra-indagada-de-mas-de-9-millones.shtml"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2020/06/16/rn-solicita-sanciones-expulsion-al-consejero-regional-percy-marin.shtml"
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

## Síntesis y Casos Vinculados
Dirigente político de [[Renovacion Nacional]] en la Región de Valparaíso, donde fue consejero regional (CORE) y presidente del Consejo Regional.

**Reparo de la Contraloría por viáticos:** una auditoría de la Contraloría al Consejo Regional de Valparaíso objetó el cobro de más de $9 millones en viáticos y combustible por no acreditar su residencia, y en 2020 inició un juicio de cuentas para su restitución. Su defensa sostuvo que había pedido renunciar a los viáticos y que quedaban recursos pendientes. En junio de 2020 el Tribunal Regional de RN lo suspendió del partido. No se encontró información sobre el resultado final del juicio de cuentas.

## Registros Reificados
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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Contraloría iniciará juicio de cuentas contra Percy Marín: cifra indagada de más de 9 millones](https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2020/01/17/contraloria-iniciara-juicio-de-cuentas-contra-percy-marin-cifra-indagada-de-mas-de-9-millones.shtml) | BioBioChile | `secundaria` | 2020-01-17 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2020/01/17/contraloria-iniciara-juicio-de-cuentas-contra-percy-marin-cifra-indagada-de-mas-de-9-millones.shtml) |
| [RN solicita sanciones y expulsión al consejero regional Percy Marín](https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2020/06/16/rn-solicita-sanciones-expulsion-al-consejero-regional-percy-marin.shtml) | BioBioChile | `secundaria` | 2020-06-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2020/06/16/rn-solicita-sanciones-expulsion-al-consejero-regional-percy-marin.shtml) |
