---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Valparaíso (V Región) / Nacional"
superior_jerarquico: "Congreso Nacional de Chile (Poder Legislativo)"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html"
  - "https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html"
  - "https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/"
  - "https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/"
tags:
  - entidad/publica
  - senado
  - poder-legislativo
---

# Senado de la Republica de Chile

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria` *(Corporación del Poder Legislativo)*
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Cámara alta del Congreso Nacional. En el [[Caso Corpesca]], el tribunal acreditó mediante la [[Sentencia-3TOP-Santiago-Corpesca-2021]] que el entonces integrante de la Comisión de Intereses Marítimos, Pesca y Acuicultura del Senado, [[Jaime Orpis Bouchon]] ([[Union Democrata Independiente]]), actuó bajo mandato e instrucciones financieras de [[Corpesca SA]] ([[Francisco Mujica Ortuzar]]) a cambio de pagos por **$233.000.000 CLP** ([[TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Cohecho",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen Privado",
  firmante_destino AS "Senador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Corpesca: Jaime Orpis fue condenado por fraude al Fisco y cohecho](https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html) | Cooperativa | `secundaria` | 2020-12-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html) |
| [Ex senador Jaime Orpis irá a la cárcel por fraude al Fisco y cohecho](https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html) | Cooperativa | `secundaria` | 2021-04-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html) |
| [Corte confirmó la pena de cárcel para el ex senador Jaime Orpis](https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html) | Cooperativa | `secundaria` | 2022-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html) |
| [Cinco claves para comprender el caso Audios](https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) | Emol | `secundaria` | 2024-08-21 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2024/08/21/1140151/cinco-claves-comprender-caso-audios.html) |
| [“Aquí estamos haciendo una huevá que es delito”: el audio en el que Luis Hermosilla menciona pagos a funcionarios del SII y la CMF](https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) | CIPER Chile | `secundaria` | 2023-11-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2023/11/14/aqui-estamos-haciendo-una-hueva-que-es-delito-el-audio-en-el-que-luis-hermosilla-menciona-pagos-a-funcionarios-del-sii-y-la-cmf/) |
| [Caso Audios: Fiscalía pide formalizar a Luis Hermosilla por lavado de activos y cohecho](https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) | El Dínamo | `secundaria` | 2024-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/08/12/caso-audios-fiscalia-pide-formalizar-a-luis-hermosilla-por-lavado-de-activos-y-cohecho/) |
