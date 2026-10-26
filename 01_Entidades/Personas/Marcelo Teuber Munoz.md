---
tipo_nodo: persona
rut: ""
aliases:
  - "Marcelo Teuber"
  - "Marcelo Teuber Muñoz"
rol_principal: "Ex Coronel de Carabineros y Ex Jefe de la UIOE en La Araucanía"
afiliacion_politica: "Militar / Carabineros"
situacion_procesal: condenado
medida_cautelar: "Condenado a 3 años y un día más 100 días de presidio por el TOP de Temuco — sentencia no firme: recursos de nulidad pendientes (2026)"
estado_verificacion: verificado
fuentes:
  - "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml"
tags:
  - entidad/persona
  - caso-operacion-huracan
  - dipolcar
  - uioe
  - condenado
---

# Marcelo Teuber Munoz

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Inteligencia Policial de Carabineros]] / UIOE)
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Condena Ejecutoriada / Cautelar**: `= this.medida_cautelar`

## Síntesis
Coronel de Carabineros y jefe directo de la Unidad de Inteligencia Operativa Especializada (UIOE) en La Araucanía durante el desarrollo de la [[Caso Operacion Huracan]]. Estuvo a cargo de la coordinación territorial del operativo policial de detención y de visar administrativamente los oficios policiales remitidos a la Fiscalía de Temuco con base en la información fraudulenta provista por [[Alex Smith Leay]] y [[Leonardo Osses Sandoval]].

En el juicio oral ante el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]), fue sentenciado a penas que sumaron **3 años y un día más 100 días de presidio** por [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]], conmutadas a penas sustitutivas.

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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [El 'profesor' Smith condenado a 12 años de cárcel por montaje en Operación Huracán](https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) | El Dínamo | `secundaria` | 2026-04-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) |
| [Profesor Smith y otros 3 condenados en Operación Huracán presentan recurso para anular sentencia](https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) | BioBioChile | `secundaria` | 2026-05-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) |
