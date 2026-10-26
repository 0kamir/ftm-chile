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
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml"
  - "https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/"
  - "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
  - "https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml"
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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude](https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) | El Mostrador | `secundaria` | 2026-04-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) |
| [Pacogate: postergan juicio oral de 31 imputados](https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) | BioBioChile | `secundaria` | 2021-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) |
| [Pacogate: las claves de la investigación](https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) | The Clinic | `secundaria` | 2017-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) |
| [El 'profesor' Smith condenado a 12 años de cárcel por montaje en Operación Huracán](https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) | El Dínamo | `secundaria` | 2026-04-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/) |
| [Profesor Smith y otros 3 condenados en Operación Huracán presentan recurso para anular sentencia](https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) | BioBioChile | `secundaria` | 2026-05-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/region-de-la-araucania/2026/05/04/profesor-smith-y-otros-3-condenados-en-operacion-huracan-presentan-recurso-para-anular-sentencia.shtml) |
