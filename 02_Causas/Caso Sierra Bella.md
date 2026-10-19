---
tipo_nodo: causa_judicial
ruc: "2300094812-3"
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía Metropolitana Centro Norte (fiscal Patricio Cooper, luego fiscal regional de Coquimbo) / Contraloría General de la República"
fiscal_a_cargo: "Patricio Cooper Monti"
estado_judicial: sobreseida_con_nueva_querella
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.ciperchile.cl/2023/03/09/compra-de-clinica-sierra-bella-fiscalia-pide-documentos-a-seremi-de-salud-impuestos-internos-y-conservador-de-bienes/"
    titulo: "Compra de clínica Sierra Bella: Fiscalía pide documentos"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2023-03-09
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/especial/bbcl-investiga/noticias/de-pasillo/2023/04/13/amp/golpe-a-hassler-contraloria-objeta-polemica-compra-de-clinica-sierra-bella-y-deja-operacion-en-vilo.shtml"
    titulo: "Contraloría objeta polémica compra de clínica Sierra Bella"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2023-04-13
    consultado: 2026-10-19
  - url: "https://www.emol.com/noticias/Nacional/2023/04/14/1092228/cronologia-compra-sierra-bella-santiago.html"
    titulo: "Cronología de la compra de Sierra Bella"
    medio: "Emol"
    tipo: secundaria
    fecha: 2023-04-14
    consultado: 2026-10-19
  - url: "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
    titulo: "Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella"
    medio: "24 Horas"
    tipo: secundaria
    fecha: 2025-05-26
    consultado: 2026-10-19
  - url: "https://www.latercera.com/nacional/noticia/sierra-bella-ningun-querellante-pidio-reapertura-y-se-cierra-el-telon-del-caso-para-iraci-hassler/"
    titulo: "Sierra Bella: ningún querellante pidió reapertura y se cierra el telón del caso para Irací Hassler"
    medio: "La Tercera"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.elmostrador.cl/noticias/pais/2026/06/04/tribunal-admite-querella-de-santiago-contra-iraci-hassler-por-fraude-al-fisco/"
    titulo: "Tribunal admite querella de Santiago contra Irací Hassler por fraude al fisco"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2026-06-04
    consultado: 2026-10-19
  - url: "https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2026/06/05/desbordes-tras-querella-contra-hassler-por-caso-sierra-bella-el-informe-de-contraloria-es-muy-duro.shtml"
    titulo: "Desbordes tras querella contra Hassler por caso Sierra Bella: 'El informe de Contraloría es muy duro'"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2026-06-05
    consultado: 2026-10-19
tags:
  - causa
  - sobreprecio-inmobiliario
  - caso-sierra-bella
---

# Caso Sierra Bella

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal Investigador**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal`

## Síntesis Forense de la Causa
Investigación penal y administrativa originada por el intento de adquisición mediante trato directo de la ex Clínica Sierra Bella por parte de la [[Municipalidad de Santiago]] —encabezada por la alcaldesa [[Iraci Hassler Jacob]] ([[Partido Comunista de Chile]])— a la sociedad [[Inmobiliaria San Valentino SpA]] (representada por [[Felipe Sanchez Perez]]) por un precio de **$8.200.000.000 CLP**, cuadruplicando el valor comercial y de adquisición previa del inmueble ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]). La operación fue objetada y frenada por la [[Contraloria General de la Republica]] bajo la dirección del Contralor [[Jorge Bermudez Soto]] mediante el [[Dictamen-CGR-SierraBella-2023]], tras objetar la Contraloría una diferencia de más de cuatro veces entre el precio pactado y el valor al que se habían adquirido los inmuebles.

## Transacciones y Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Desarrollo Judicial Posterior
En mayo de 2025 la Fiscalía decidió no perseverar y la causa quedó con sobreseimiento definitivo, confirmado por la Corte Suprema; Hassler nunca fue formalizada. En mayo de 2026 un sumario de la Contraloría dio por acreditada su responsabilidad administrativa en la compra. En junio de 2026 el 7° Juzgado de Garantía de Santiago declaró admisible una nueva querella de la Municipalidad de Santiago por fraude al fisco, que el Ministerio Público debe evaluar; Hassler sostiene que se trata de hechos ya juzgados y querelló por denuncia calumniosa contra el alcalde Mario Desbordes, acción que el tribunal también admitió. Rige la presunción de inocencia.

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
