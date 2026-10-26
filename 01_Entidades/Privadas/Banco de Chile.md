---
tipo_nodo: entidad_privada
rut: "97.004.000-5"
razon_social: "Banco de Chile"
fecha_constitucion: 1893-10-28
objeto_social: "Institución bancaria, intermediación financiera, operaciones de crédito y servicios bancarios comerciales"
representante_legal: "Eduardo Ebensperger Orrego"
estado_verificacion: parcial
fuentes:
  - "https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTcwTwMDQwMDAtNQ-jTw/nombre-y-rut/BANCO-DE-CHILE-97004000-5"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
  - "https://www.elciudadano.com/?p=524007"
  - "https://www.fne.gob.cl/corte-suprema-acoge-parcialmente-reclamacion-de-la-fne-y-sanciona-a-todas-las-navieras-que-integraron-cartel-del-transporte-maritimo-de-vehiculos-hacia-chile-con-multas-totales-de-us-305-millones/"
  - "https://www.fne.gob.cl/fne-pide-a-la-corte-suprema-que-eleve-sanciones-contra-navieras-que-integraron-cartel-de-transporte-de-vehiculos-hacia-chile/"
tags:
  - entidad/privada
  - banco
  - quinenco
  - caso-caval
---

# Banco de Chile

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Grupo Controlador**: Quiñenco S.A. / Citigroup (LQ Inversiones Financieras S.A., vinculado a [[Andronico Luksic Craig]])

## Contexto en Investigaciones
Institución financiera chilena de relevancia sistémica. En el [[Caso Caval]], el banco concedió en febrero de 2014 un crédito por **$6.500.000.000 CLP** a [[Exportadora y de Gestion Caval Ltda]] para la compra de tres predios en Machalí, previa reunión sostenida en noviembre de 2013 entre el vicepresidente de la entidad [[Andronico Luksic Craig]], [[Natalia Compagnon Soto]] y Sebastián Dávalos Bachelet.

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Registro de RUT: Banco de Chile](https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTcwTwMDQwMDAtNQ-jTw/nombre-y-rut/BANCO-DE-CHILE-97004000-5) | Genealog (datos SII) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTcwTwMDQwMDAtNQ-jTw/nombre-y-rut/BANCO-DE-CHILE-97004000-5) |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
| [Mauricio Valero fue absuelto](https://www.elciudadano.com/?p=524007) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=524007) |
| [Corte Suprema acoge reclamación de la FNE y sanciona a todas las navieras que integraron cartel del transporte marítimo de vehículos hacia Chile con multas de US$ 30,5 millones](https://www.fne.gob.cl/corte-suprema-acoge-parcialmente-reclamacion-de-la-fne-y-sanciona-a-todas-las-navieras-que-integraron-cartel-del-transporte-maritimo-de-vehiculos-hacia-chile-con-multas-totales-de-us-305-millones/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2020-08-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-acoge-parcialmente-reclamacion-de-la-fne-y-sanciona-a-todas-las-navieras-que-integraron-cartel-del-transporte-maritimo-de-vehiculos-hacia-chile-con-multas-totales-de-us-305-millones/) |
| [FNE pide a la Corte Suprema que eleve sanciones contra navieras que integraron cartel de transporte de vehículos hacia Chile](https://www.fne.gob.cl/fne-pide-a-la-corte-suprema-que-eleve-sanciones-contra-navieras-que-integraron-cartel-de-transporte-de-vehiculos-hacia-chile/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2017-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/fne-pide-a-la-corte-suprema-que-eleve-sanciones-contra-navieras-que-integraron-cartel-de-transporte-de-vehiculos-hacia-chile/) |
