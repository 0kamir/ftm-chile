---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Carabineros de Chile / Ministerio del Interior y Seguridad Pública"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/"
  - "https://en.wikipedia.org/wiki/Pacogate"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml"
  - "https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/"
tags:
  - entidad/publica
  - carabineros
  - caso-pacogate
---

# Direccion de Finanzas de Carabineros

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Repartición encargada de la administración presupuestaria y pago de remuneraciones de Carabineros de Chile (Dirección de Finanzas / Intendencia). En el [[Caso Pacogate]], fue el epicentro del desfalco de **$28.348.928.198 CLP** ([[TRX-2016-11-10-Fondos-Direccion-Finanzas-Carabineros-01]]) atribuido por la Fiscalía a una estructura encabezada por [[Flavio Echeverria Cortez]], con participación de oficiales como [[Jaime Paz Meneses]]. En abril de 2026 el Tribunal de Juicio Oral en lo Penal de Santiago dictó veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos; **descartó la asociación ilícita** y las penas se fijarán en la sentencia (anunciada por la prensa para febrero de 2027). El veredicto no está firme. ([[Veredicto-TOP-Santiago-Pacogate-2026]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Desfalco",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Jefe Finanzas",
  firmante_destino AS "Operador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Pacogate: rechazan prisión preventiva para los 25 condenados por megafraude](https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) | El Mostrador | `secundaria` | 2026-04-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/04/15/caso-pacogate-rechazan-prision-preventiva-para-los-25-condenados-por-megafraude/) |
| [Pacogate](https://en.wikipedia.org/wiki/Pacogate) | Wikipedia | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://en.wikipedia.org/wiki/Pacogate) |
| [Pacogate: postergan juicio oral de 31 imputados](https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) | BioBioChile | `secundaria` | 2021-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2021/05/10/pacogate-postergan-juicio-oral-de-31-imputados-por-fraude-en-carabineros-hasta-el-20-de-septiembre.shtml) |
| [Pacogate: las claves de la investigación](https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) | The Clinic | `secundaria` | 2017-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/04/04/pacogate-las-claves-la-investigacion-millonario-fraude-carabineros/) |
