---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "O'Higgins (VI Región)"
superior_jerarquico: "Concejo Municipal de Machalí (Autónoma)"
autoridad_vinculada: "[[Jorge Silva Menares]]"
estado_verificacion: verificado
fuentes:
  - "https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/"
  - "https://radio.uchile.cl/?p=478347"
  - "https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
tags:
  - entidad/publica
  - municipalidad
  - caso-caval
---

# Municipalidad de Machali

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Funcionario Investigado (DOM)**: `= this.autoridad_vinculada`

## Contexto y Administrativo
Corporación edilicia de la Región de O'Higgins cuya Dirección de Obras Municipales (DOM), encabezada por [[Jorge Silva Menares]], intervino técnicamente en los informes favorables para el cambio de uso de suelo de rural a urbano de los 44 hectáreas de predios adquiridos por [[Exportadora y de Gestion Caval Ltda]] ([[Natalia Compagnon Soto]] y [[Mauricio Valero Illanes]]), con pagos por los que su director de obras fue condenado por cohecho en el [[Caso Caval]] (los socios de Caval fueron absueltos del soborno) ([[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]], [[Sentencia-TOP-Rancagua-Caval-2018]]).

## Historial de Nexos y Transacciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Caval: el sospechoso historial del destituido director de obras de Machalí](https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/) | CIPER Chile | `secundaria` | 2015-07-08 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2015/07/08/caso-caval-el-sospechoso-historial-del-destituido-director-de-obras-de-machali/) |
| [Caso Caval: Tribunal condena a Natalia Compagnon por delito tributario](https://radio.uchile.cl/?p=478347) | Radio Universidad de Chile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://radio.uchile.cl/?p=478347) |
| [Caso Caval: 818 días remitidos y multa de 55 millones para segundo condenado](https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/) | Radio Agricultura | `secundaria` | 2018-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.radioagricultura.cl/noticias/nacional/caso-caval-818-dias-remitidos-y-multa-de-55-millones-para-segundo-condenado_20180128/) |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Natalia Compagnon fue condenada por delito tributario](https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/natalia-compagnon-fue-condenada-por-delito-tributario/) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
