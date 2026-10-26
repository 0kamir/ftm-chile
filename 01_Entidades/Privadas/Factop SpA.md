---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Factop SpA"
fecha_constitucion: "2016-08-10"
objeto_social: "Operaciones de factoring, descuento de documentos y servicios financieros"
representante_legal: "[[Luis Hermosilla Osorio]]"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
  - "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
  - "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
  - "https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/"
  - "https://www.diarioconstitucional.cl/2026/03/10/corte-suprema-confirma-condena-contra-exdirector-de-la-pdi-hector-espinosa-por-malversacion-de-gastos-reservados-y-lavado-de-activos/"
  - "https://www.ciperchile.cl/2021/10/07/los-depositos-en-efectivo-que-acorralan-al-exdirector-de-la-pdi-hector-espinosa/"
tags:
  - entidad/privada
  - factoring
  - caso-audios
---

# Factop SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante / Asesor Legal en la Operación**: `= this.representante_legal`

## Contexto y Societario
Sociedad de factoring investigada en el [[Caso Audios]] por emisión de facturas ideológicamente falsas, [[Lavado de Activos]] y [[Cohecho]]. En la reunión registrada en [[Audio-Reunion-Edificio-Alonso-2023]], sus asesores legales [[Luis Hermosilla Osorio]] y [[Leonarda Villalobos Muth]] habrían estructurado, según la Fiscalía, un fondo para sobornos [[TRX-2023-06-22-Reunion-Audios-01]] dirigido a funcionarios del [[Servicio Impuestos Internos]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Operador Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Cinco claves para comprender el caso Audios](https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) | Emol | `secundaria` | 2024-08-21 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) |
| [“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF](https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) | CIPER Chile | `secundaria` | 2023-11-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) |
| [Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho](https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) | El Dínamo | `secundaria` | 2024-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) |
| [Caso Audios: Luis Hermosilla será formalizado por la arista Parque Capital](https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-audios-luis-hermosilla-sera-formalizado-en-enero-por-la-arista-de-parque-capital/) |
| [Corte Suprema confirma condena contra exdirector de la PDI Héctor Espinosa por malversación de gastos reservados y lavado de activos](https://www.diarioconstitucional.cl/2026/03/10/corte-suprema-confirma-condena-contra-exdirector-de-la-pdi-hector-espinosa-por-malversacion-de-gastos-reservados-y-lavado-de-activos/) | Diario Constitucional / Poder Judicial | `secundaria` | 2026-03-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.diarioconstitucional.cl/2026/03/10/corte-suprema-confirma-condena-contra-exdirector-de-la-pdi-hector-espinosa-por-malversacion-de-gastos-reservados-y-lavado-de-activos/) |
| [Los depósitos en efectivo que acorralan al exdirector de la PDI Héctor Espinosa](https://www.ciperchile.cl/2021/10/07/los-depositos-en-efectivo-que-acorralan-al-exdirector-de-la-pdi-hector-espinosa/) | CIPER Chile | `secundaria` | 2021-10-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2021/10/07/los-depositos-en-efectivo-que-acorralan-al-exdirector-de-la-pdi-hector-espinosa/) |
