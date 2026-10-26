---
tipo_nodo: persona
rut: ""
aliases:
  - "Guillermo Harding"
  - "Guillermo Harding Alvarado"
rol_principal: "Fundador y Ex Controlador de Farmacias Cruz Verde y de Empresas Socofar"
afiliacion_politica: "Independiente"
situacion_procesal: descarte_procesal_sin_imputacion
medida_cautelar: "Empresa matriz multada con 20.000 UTA por la Corte Suprema y condenada a indemnización civil"
estado_verificacion: verificado
fuentes:
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
  - "https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/"
tags:
  - entidad/persona
  - empresario
  - farmacias
  - cruz-verde
  - colusion-farmacias
---

# Guillermo Harding Alvarado

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Farmacias Cruz Verde SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Sanción Corporativa**: `= this.medida_cautelar`

## Síntesis
Empresario chileno y farmacéutico de Valparaíso, fundador de Farmacias Cruz Verde y del holding distribuidor Socofar. Bajo su liderazgo, la compañía se transformó en la mayor cadena farmacéutica de Chile.

Durante el [[Caso Colusion de las Farmacias]], ejecutivos comerciales de [[Farmacias Cruz Verde SA]] coordinaron con [[Farmacias Salcobrand SA]] y [[Farmacias Ahumada SA]] el alza de precios de 222 medicamentos entre diciembre de 2007 y marzo de 2008 ([[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]). Pese a que Cruz Verde negó sistemáticamente los hechos tras la confesión de FASA, el Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) y la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]) condenaron a la empresa al pago de la multa máxima de **20.000 UTA** (cerca de US$ 19 millones). En 2015, Harding vendió el 60% de Socofar al grupo mexicano FEMSA por cerca de US$ 1.000 millones.

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
| [Sentencia TDLC N° 119/2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-01-31 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
| [Suprema rechaza reclamo de farmacias sobre multas](https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) | The Clinic | `secundaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) |
