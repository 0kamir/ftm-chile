---
tipo_nodo: entidad_privada
rut: "89.807.200-2"
razon_social: "Farmacias Cruz Verde S.A. (Socofar)"
fecha_constitucion: 1984-01-05
objeto_social: "Distribución, droguería, importación y venta al por menor de medicamentos e insumos médicos"
representante_legal: "Eduardo Castillo Castillo"
historial_correcciones:
  - "RUT corregido el 2026-10-19: el vault registraba 96.677.000-7, que no corresponde a la empresa; el RUT verificado es 89.807.200-2."
estado_verificacion: parcial
fuentes:
  - "https://www.portalchile.org/empresa/farmacias-cruz-verde-spa-89807200"
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
  - "https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/"
tags:
  - entidad/privada
  - farmacias
  - cruz-verde
  - colusion-farmacias
---

# Farmacias Cruz Verde SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Fundada por [[Guillermo Harding Alvarado]] (Grupo Socofar), posteriormente adquirida por la multinacional mexicana FEMSA

## Contexto en Investigaciones
Cadena de farmacias líder en cobertura a nivel nacional. En el [[Caso Colusion de las Farmacias]], coordinó junto a [[Farmacias Salcobrand SA]] y [[Farmacias Ahumada SA]] alzas simultáneas y concertadas de precios en 222 medicamentos entre diciembre de 2007 y marzo de 2008 mediante contactos triangulados con laboratorios proveedores farmacéuticos ([[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]). Fue condenada por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) y confirmada por la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]) a pagar la multa máxima de **20.000 UTA** (aproximadamente US$ 19 millones), y en sede civil al pago de compensaciones directas a los consumidores afectados ([[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]).

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
| [Registro de RUT: Farmacias Cruz Verde](https://www.portalchile.org/empresa/farmacias-cruz-verde-spa-89807200) | PortalChile (datos SII) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.portalchile.org/empresa/farmacias-cruz-verde-spa-89807200) |
| [Sentencia TDLC N° 119/2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-01-31 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
| [Suprema rechaza reclamo de farmacias sobre multas](https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) | The Clinic | `secundaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2012/09/07/suprema-le-hace-una-tapa-de-100-metros-a-farmacias-por-reclamo-sobre-multas-en-caso-colusion/) |
