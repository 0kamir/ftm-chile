---
tipo_nodo: persona
rut: ""
aliases:
  - "Camila Flores"
  - "Camila Flores Oporto"
rol_principal: "Senadora de la República (ex Diputada por el Distrito 6) y Dirigente de Renovación Nacional"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: investigada
medida_cautelar: "Sin formalización; sujeta a diligencias de entrada, registro e incautación de dispositivos por la URAC y OS9"
estado_verificacion: verificado
fuentes:
  - "https://www.ciperchile.cl/2026/05/06/fiscalia-ingresa-al-senado-por-investigacion-contra-camila-flores-por-posible-fraude-al-fisco/"
  - "https://www.emol.com/noticias/Nacional/2026/04/09/1196710/camila-flores-investigacion-fraude-fisco.html"
  - "https://www.diarioconstitucional.cl/2026/05/09/rn-remite-a-camila-flores-al-tribunal-supremo-en-medio-de-investigacion-por-presunto-fraude-al-fisco/"
tags:
  - entidad/persona
  - senadora
  - diputada
  - rn
  - cuota-flores
  - valparaiso
  - fraude-al-fisco
---

# Camila Flores Oporto

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal` *(Investigación penal desformalizada)*
- **Medidas Cautelares / Diligencias Judiciales**: `= this.medida_cautelar`

## Síntesis y Casos Vinculados
Abogada y dirigenta política del ala conservadora de [[Renovacion Nacional]]. Se desempeñó como diputada por el Distrito 6 de la Región de Valparaíso durante dos períodos legislativos (2018–2026), asumiendo posteriormente como senadora de la República.

En el marco del [[Caso Asignaciones Parlamentarias y Cuota Flores]], es investigada penalmente por la Unidad Regional Anticorrupción (URAC) de la Fiscalía de Valparaíso y el OS9 de Carabineros por presunto **fraude al Fisco reiterado**:

1. **Investigación "Cuota Flores"**: La fiscalía indaga el presunto cobro de aportes o devoluciones compulsivas en efectivo exigidas a asesores y trabajadores contratados con cargo a los fondos públicos de asignaciones del Congreso ([[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]). En abril de 2026, la policía allanó sus oficinas legislativas e incautó sus teléfonos y computadores portátiles bajo la orden judicial [[Orden-Entrada-Registro-Congreso-Caso-Flores-2026]].

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
| [Fiscalía ingresa al Senado por investigación contra Camila Flores](https://www.ciperchile.cl/2026/05/06/fiscalia-ingresa-al-senado-por-investigacion-contra-camila-flores-por-posible-fraude-al-fisco/) | CIPER Chile | `secundaria` | 2026-05-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2026/05/06/fiscalia-ingresa-al-senado-por-investigacion-contra-camila-flores-por-posible-fraude-al-fisco/) |
| [Camila Flores: investigación por fraude al fisco](https://www.emol.com/noticias/Nacional/2026/04/09/1196710/camila-flores-investigacion-fraude-fisco.html) | Emol | `secundaria` | 2026-04-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/04/09/1196710/camila-flores-investigacion-fraude-fisco.html) |
| [RN remite a Camila Flores al Tribunal Supremo](https://www.diarioconstitucional.cl/2026/05/09/rn-remite-a-camila-flores-al-tribunal-supremo-en-medio-de-investigacion-por-presunto-fraude-al-fisco/) | Diario Constitucional | `secundaria` | 2026-05-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.diarioconstitucional.cl/2026/05/09/rn-remite-a-camila-flores-al-tribunal-supremo-en-medio-de-investigacion-por-presunto-fraude-al-fisco/) |
