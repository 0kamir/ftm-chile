---
tipo_nodo: nexo_transaccion
fecha: 2010-08-19
tipo_nexo: cohecho
monto_clp: 730000000
entidad_origen: "[[SQM SA]]"
entidad_destino: "[[Union Democrata Independiente]]"
firmante_origen: "[[Patricio Contesse Gonzalez]]"
firmante_destino: "[[Pablo Longueira Montes]]"
causa_vinculada: "[[Caso SQM]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Querella-SII-Boletas-SQM-2015]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
    titulo: "Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados"
    medio: "La Tercera"
    tipo: secundaria
    fecha: 2025-10-22
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/noticias/nacional/chile/2026/10/06/caso-sqm-corte-revisa-recursos-que-buscan-anular-absoluciones-y-repetir-el-juicio.shtml"
    titulo: "Caso SQM: Corte revisa recursos que buscan anular absoluciones y repetir el juicio"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2026-10-06
    consultado: 2026-10-19
historial_correcciones:
  - "Absolución en primera instancia (22-10-2025); monto de $730 millones corresponde a la acusación."
tags:
  - nexo/transaccion
  - cohecho
  - caso-sqm
  - captura-regulatoria
---

# TRX-2010-08-19-Correo-Royalty-SQM-01

## Ficha de Arista Reificada (Captura Regulatoria y Pagos vía Boletas Ideológicamente Falsas)
- **Fecha del Hecho Clave**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado Consolidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad / Entorno Político de Destino**: `= this.entidad_destino`
- **Ejecutivo Origen**: `= this.firmante_origen`
- **Autoridad Receptora**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Según la acusación de la Fiscalía, la gerencia general de [[SQM SA]] ([[Patricio Contesse Gonzalez]]) envió el 19 de agosto de 2010 al entonces senador [[Pablo Longueira Montes]] una minuta para modificar el régimen de invariabilidad tributaria del Royalty Minero, y la empresa habría canalizado pagos por aproximadamente **$730.000.000 CLP** entre 2009 y 2015 a personas de su entorno mediante boletas y facturas ([[Querella-SII-Boletas-SQM-2015]]).

**Resultado judicial:** el 3° TOP de Santiago absolvió a ambos el 22-10-2025 al no dar por acreditados los hechos; hay recursos de nulidad pendientes. Este nexo registra una hipótesis acusatoria no acreditada, no un hecho probado.

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
