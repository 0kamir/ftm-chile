---
tipo_nodo: persona
rut: "6.982.415-3"
aliases:
  - "Jorge Quiroz"
  - "Jorge Quiroz Castro"
rol_principal: "Economista, Socio Principal de Quiroz & Asociados y Ex Asesor Económico Presidencial"
afiliacion_politica: "Independiente / Cercano a Partido Republicano"
situacion_procesal: testigo_y_perito
medida_cautelar: "Sin imputación penal ni sanción personal (actuación como consultor técnico y perito económico privado)"
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

## Síntesis Forense y Actuaciones Periciales
Economista de la Universidad de Chile y Ph.D. en Economía por la Universidad de Duke. Es socio principal de la consultora [[Quiroz y Asociados Consultores SpA]], firma especializada en análisis macroeconómico, regulación y libre competencia. En el ámbito público y político, ejerció como coordinador del programa económico de la candidatura presidencial de José Antonio Kast en las elecciones de 2021.

Su vinculación con causas de libre competencia en Chile se originó a partir de estudios económicos y peritajes encargados por empresas o gremios posteriormente sancionados:

1. **Modelo de Estimación en el [[Caso Colusion de los Pollos]]**: La firma de Quiroz elaboró para la [[Asociacion de Productores Avicolas de Chile AG]] (APA) un modelo econométrico de estimación de demanda y proyecciones de consumo de carne avícola ([[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]]). De acuerdo con el fallo del Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-139-Colusion-Pollos-2014]]), las empresas [[Agrosuper SA]], [[Empresas Ariztia SA]] y [[Agricola Don Pollo Limitada]] utilizaron estas proyecciones globales como el insumo técnico base a partir del cual calculaban y se asignaban las cuotas físicas de faenamiento y producción anual. Quiroz ha declarado públicamente que el encargo técnico correspondió a proyecciones macroeconómicas y de demanda habituales, rechazando haber participado en la articulación o conocimiento de pactos colusorios entre competidores.
2. **Peritaje de Defensa en el [[Caso Colusion de las Farmacias]]**: Durante el juicio ante el TDLC (Rol C-184-08), actuó como perito económico en defensa de [[Farmacias Salcobrand SA]] ([[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]]). En sus informes técnicos y declaraciones testimoniales, sostuvo que las alzas concertadas de precios constituían un fenómeno de paralelismo consciente o dinámicas competitivas normales de mercado sin perjuicio ilícito. Dicha tesis pericial fue finalmente desestimada por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) y por la [[Corte Suprema de Chile]], que condenaron a la cadena al acreditarse coordinación horizontal y uso de intermediarios.
3. **Otros Procesos ante el TDLC**: Su consultora evacuó informes económicos de parte para empresas en otros requerimientos antimonopolio, incluyendo el mercado del asfalto (defensa de Enap y Asfaltos Chilenos) y el transporte marítimo de automóviles (navieras).

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
