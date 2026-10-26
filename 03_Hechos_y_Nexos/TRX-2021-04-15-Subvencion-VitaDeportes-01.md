---
tipo_nodo: nexo_transaccion
fecha: 2021-04-15
tipo_nexo: transferencia
monto_clp: 759000000
monto_origen: acusacion
entidad_origen: "[[Municipalidad de Vitacura]]"
entidad_destino: "[[Vita Deportes]]"
firmante_origen: "[[Raul Torrealba del Pedregal]]"
firmante_destino: "[[Domingo Prieto Urrejola]]"
causa_vinculada: "[[Caso Vitacura]]"
delito_imputado: "[[Malversacion de Caudales Publicos]]"
evidencia_soporte: "[[Declaracion-Judicial-Prieto-Vitacura-2021]]"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/?p=152080"
  - "https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/"
  - "https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html"
tags:
  - nexo/transaccion
  - transferencia
  - caso-vitacura
---

# TRX-2021-04-15-Subvencion-VitaDeportes-01

## Ficha de Arista Reificada (Transacción / Hecho)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino**: `= this.entidad_destino`
- **Firmante de Origen**: `= this.firmante_origen`
- **Firmante de Destino**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción de la Operación
Flujo de subvenciones municipales que, según la Fiscalía, habrían sido desviadas por **$759.000.000 CLP** desde la [[Municipalidad de Vitacura]] (bajo la alcaldía de [[Raul Torrealba del Pedregal]]) a través de [[Vita Deportes]] (representada por [[Domingo Prieto Urrejola]]), posteriormente retirados en efectivo y depositados en cuentas bancarias investigadas por [[Malversacion de Caudales Publicos]] y [[Lavado de Activos]] en el [[Caso Vitacura]], según consta en [[Declaracion-Judicial-Prieto-Vitacura-2021]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Audiencia de formalización de Raúl Torrealba](https://www.ex-ante.cl/?p=152080) | Ex-Ante | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/?p=152080) |
| [Fiscalía formalizará a exalcalde Raúl Torrealba por fraude al fisco y asociación ilícita](https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) | La Tercera | `secundaria` | 2023-05-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) |
| [Formalizan a exalcalde Raúl Torrealba](https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) | Pauta | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) |
