---
tipo_nodo: persona
rut: ""
aliases:
  - "Jorge Quiroz"
  - "Jorge Quiroz Castro"
rol_principal: "Economista, Socio Principal de Quiroz & Asociados y Ex Asesor Económico Presidencial"
afiliacion_politica: "Independiente / Cercano a Partido Republicano"
situacion_procesal: testigo_y_perito
medida_cautelar: "Sin imputación penal ni sanción personal (actuación como consultor técnico y perito económico privado)"
estado_verificacion: verificado
fuentes:
  - "https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf"
  - "https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/"
  - "https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/"
  - "https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/"
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
tags:
  - entidad/persona
  - economista
  - perito-economico
  - consultoria-libre-competencia
  - colusion-pollos
  - colusion-farmacias
---

# Jorge Quiroz Castro

> [!NOTE] Disclaimer Jurídico y Procesal
> **Jorge Quiroz Castro no fue imputado penalmente, formalizado ni sancionado individualmente** por la Fiscalía Nacional Económica (FNE), el Ministerio Público ni los tribunales de libre competencia (TDLC y Corte Suprema). Su intervención en los procesos antimonopolio y de libre competencia descritos se circunscribió estrictamente al **ejercicio profesional de la consultoría económica privada y peritaje técnico** a través de su firma [[Quiroz y Asociados Consultores SpA]], contratada por empresas requeridas o asociaciones gremiales para aportar estudios econométricos, defensas de competencia o modelamientos de mercado.

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal` *(Perito técnico / Consultor económico)*
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis y Actuaciones
Economista de la Universidad de Chile y Ph.D. en Economía por la Universidad de Duke. Es socio principal de la consultora [[Quiroz y Asociados Consultores SpA]], firma especializada en análisis macroeconómico, regulación y libre competencia. En el ámbito público y político, ejerció como coordinador del programa económico de la candidatura presidencial de José Antonio Kast en las elecciones de 2021.

Su vinculación con causas de libre competencia en Chile se originó a partir de estudios económicos y peritajes encargados por empresas o gremios posteriormente sancionados:

1. **Modelo de Estimación en el [[Caso Colusion de los Pollos]]**: La firma de Quiroz elaboró para la [[Asociacion de Productores Avicolas de Chile AG]] (APA) un modelo econométrico de estimación de demanda y proyecciones de consumo de carne avícola ([[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]]). De acuerdo con el fallo del Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-139-Colusion-Pollos-2014]]), las empresas [[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]] utilizaron estas proyecciones globales como el insumo técnico base a partir del cual calculaban y se asignaban las cuotas físicas de faenamiento y producción anual. Quiroz ha declarado públicamente que el encargo técnico correspondió a proyecciones macroeconómicas y de demanda habituales, rechazando haber participado en la articulación o conocimiento de pactos colusorios entre competidores.
2. **Peritaje de Defensa en el [[Caso Colusion de las Farmacias]]**: Durante el juicio ante el TDLC (Rol C-184-08), actuó como perito económico en defensa de [[Farmacias Salcobrand SA]] ([[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]]). En sus informes técnicos y declaraciones testimoniales, sostuvo que las alzas concertadas de precios constituían un fenómeno de paralelismo consciente o dinámicas competitivas normales de mercado sin perjuicio ilícito. Dicha tesis fue finalmente desestimada por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) y por la [[Corte Suprema de Chile]], que condenaron a la cadena al acreditarse coordinación horizontal y uso de intermediarios.
3. **Otros Procesos ante el TDLC**: Su consultora evacuó informes económicos de parte para empresas en otros requerimientos antimonopolio, incluyendo el mercado del asfalto (defensa de Enap y Asfaltos Chilenos) y el transporte marítimo de automóviles (navieras).

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
| [Sentencia TDLC N° 139/2014](https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) | TDLC / FNE | `primaria` | 2014-09-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/wp-content/uploads/2016/03/Sentencia_139-_2014.pdf) |
| [TDLC condenó a Agrosuper, Ariztía y Don Pollo por colusión](https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/) | Fiscalía Nacional Económica | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/tdlc-condeno-a-agrosuper-ariztia-y-don-pollo-por-colusion-y-ordeno-disolver-el-gremio-que-las-reune/) |
| [FNE presenta requerimiento por colusión en la producción y comercialización de carne de pollo](https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) | Fiscalía Nacional Económica | `primaria` | 2011-12-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/fiscalia-nacional-economica-presenta-requerimiento-por-colusion-en-la-produccion-y-comercializacion-de-carne-de-pollo-en-el-pais/) |
| [Corte Suprema confirma multas por colusión contra Agrosuper, Ariztía y Don Pollo](https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/) | Fiscalía Nacional Económica | `primaria` | 2015-10-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-confirma-multas-por-colusion-contra-agrosuper-ariztia-y-don-pollo-y-endurece-sancion-contra-el-gremio-que-las-reune/) |
| [Sentencia TDLC N° 119/2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-01-31 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
