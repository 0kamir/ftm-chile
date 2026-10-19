---
tipo_nodo: causa_judicial
ruc: "2300094812-3"
año_inicio: 2023
tribunal_o_fiscalia: "Fiscalía Regional de Coquimbo / 7° Juzgado de Garantía de Santiago / Contraloría General de la República"
fiscal_a_cargo: "Patricio Cooper Monti"
estado_judicial: en_investigacion
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
alertas_verificacion:
  - "La municipalidad no perseveró en la compra tras el informe de Contraloría. Verificar si TRX-2023-01-20-Compraventa-Clinica-SierraBella-01 registra un pago que no ocurrió, y la fiscalía a cargo (el vault dice Coquimbo)."
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
