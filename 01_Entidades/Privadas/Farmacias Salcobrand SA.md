---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Farmacias Salcobrand S.A. (Empresas SB)"
fecha_constitucion: 2000-04-10
objeto_social: "Explotación de farmacias, droguerías, perfumerías y comercialización de productos farmacéuticos"
representante_legal: "Matías Verdugo Correa"
estado_verificacion: verificado
fuentes:
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
  - "https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/"
tags:
  - entidad/privada
  - farmacias
  - salcobrand
  - colusion-farmacias
---

# Farmacias Salcobrand SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Grupo Controlador**: Empresas SB (familia Yarur Rey)

## Contexto en Investigaciones
Cadena de farmacias surgida de la fusión de Farmacias Salco y Farmacias Brand. En el [[Caso Colusion de las Farmacias]], su gerente general [[Roberto Belloni Pechini]] articuló junto a ejecutivos de [[Farmacias Cruz Verde SA]] y [[Farmacias Ahumada SA]] el mecanismo de alza coordinada de precios en medicamentos de uso crónico ([[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]), utilizando a laboratorios como agentes de control para evitar desviaciones en los valores de venta al público. 

Fue condenada por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) a una multa de **20.000 UTA** (confirmada por la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]) y obligada judicialmente en sede civil por demanda colectiva del [[Servicio Nacional del Consumidor]] a indemnizar a los consumidores con más de mil millones de pesos ([[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]).

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Sentencia TDLC N° 119/2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-01-31 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
| [Suprema rechaza reclamo de farmacias sobre multas](https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) | The Clinic | `secundaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) |
