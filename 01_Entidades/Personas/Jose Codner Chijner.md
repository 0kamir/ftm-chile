---
tipo_nodo: persona
rut: ""
aliases:
  - "José Codner"
  - "José Codner Chijner"
rol_principal: "Fundador y Ex Controlador de Farmacias Ahumada S.A. (FASA)"
afiliacion_politica: "Independiente"
situacion_procesal: descarte_procesal_sin_imputacion
medida_cautelar: "Sin medidas cautelares vigentes; firmante del acuerdo conciliatorio de delación ante la FNE en marzo de 2009"
estado_verificacion: verificado
fuentes:
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
tags:
  - entidad/persona
  - empresario
  - farmacias
  - colusion-farmacias
---

# Jose Codner Chijner

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Farmacias Ahumada SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Hito Regulatorio**: `= this.medida_cautelar`

## Síntesis
Químico farmacéutico y empresario que transformó un modesto local en la cadena Farmacias Ahumada (FASA), expandiéndola a nivel nacional e internacional (Brasil, México y Perú). 

En el [[Caso Colusion de las Farmacias]], su administración participó en el cartel de alza de precios de 222 medicamentos entre diciembre de 2007 y marzo de 2008 junto a [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]] ([[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]). Ante la contundencia de las pruebas reunidas por la [[Fiscalia Nacional Economica]], en marzo de 2009 Codner y el directorio de FASA rompieron la defensa común del sector y firmaron un inédito acuerdo conciliatorio con la FNE ([[Acuerdo-Conciliatorio-FNE-FASA-2009]]), reconociendo la concertación de precios y pagando US$ 1 millón, lo que detonó una fuerte pugna interna entre los accionistas (incluido el grupo Falabella) y derivó en la venta de la cadena al consorcio mexicano Casa Saba en 2010.

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
| [Fallo Corte Suprema Rol 2578-2012 (caso Farmacias)](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema rechaza reclamo de farmacias sobre multas](https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) | The Clinic | `secundaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
