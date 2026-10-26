---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Exportadora y de Gestión Caval Limitada"
fecha_constitucion: "2012-02-03"
objeto_social: "Asesorías comerciales, gestión inmobiliaria, inversiones y consultoría estratégica"
representante_legal: "[[Mauricio Valero Illanes]]"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
  - "https://www.elciudadano.com/?p=524007"
  - "https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/"
  - "https://radio.uchile.cl/?p=478347"
tags:
  - entidad/privada
  - gestion-inmobiliaria
  - caso-caval
---

# Exportadora y de Gestion Caval Ltda

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Socio Administrador**: `= this.representante_legal` (junto a [[Natalia Compagnon Soto]])

## Contexto y Societario
Sociedad de responsabilidad limitada constituida en febrero de 2012 en partes iguales (50% cada uno) por [[Natalia Compagnon Soto]] y [[Mauricio Valero Illanes]] con un capital inicial de apenas `$6.000.000 CLP`. En el [[Caso Caval]], obtuvo un crédito bancario por `$6.500.000.000 CLP` para comprar y revender tres predios en la comuna de Machalí con una plusvalía proyectada superior a `$2.500.000.000 CLP`, operación por la que fue acusada de soborno al Director de Obras de la [[Municipalidad de Machali]] [[Jorge Silva Menares]] ([[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]]) y de delitos tributarios ([[TRX-2015-01-29-Facturas-Caval-SII-01]]). La sociedad fue absuelta en julio de 2018; solo [[Natalia Compagnon Soto]] fue condenada, por delito tributario ([[Sentencia-TOP-Rancagua-Caval-2018]]).

## Historial de Nexos y Transacciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Natalia Compagnon fue condenada por delito tributario](https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
| [Mauricio Valero fue absuelto](https://www.elciudadano.com/?p=524007) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=524007) |
| [Caso Caval: el sospechoso historial del destituido director de obras de Machalí](https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/) | CIPER Chile | `secundaria` | 2015-07-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/) |
| [Caso Caval: Tribunal condena a Natalia Compagnon por delito tributario](https://radio.uchile.cl/?p=478347) | Radio Universidad de Chile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://radio.uchile.cl/?p=478347) |
