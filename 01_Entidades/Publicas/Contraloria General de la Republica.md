---
tipo_nodo: entidad_publica
rut: ""
categoria: Órgano Contralor Constitucionalmente Autónomo
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Autonomía Constitucional"
autoridad_vinculada: "[[Jorge Bermudez Soto]]"
estado_verificacion: verificado
fuentes:
  - "https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/"
  - "https://www.df.cl/economia-y-politica/actualidad/sebastian-pinera-declaro-por-mas-de-dos-horas-en-fiscalia-por-caso-exalmar"
  - "https://www.cnnchile.com/pais/camara-de-diputados-aprobo-el-informe-de-la-comision-investigadora-del-caso_20171130/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml"
  - "https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/"
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
tags:
  - entidad/publica
  - contraloria
  - toma-de-razon
  - fiscalizacion
---

# Contraloria General de la Republica

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Contralor General (2015-2023)**: `= this.autoridad_vinculada`

## Contexto en Investigaciones
Órgano superior de fiscalización de la Administración del Estado. En el grafo interviene directamente tanto en la detección del fraccionamiento de convenios bajo las `5.000 UTM` en el [[Caso Convenios]] ([[Seremi MINVU Antofagasta]] / [[Fundacion Democracia Viva]]) como en el bloqueo y auditoría de la compraventa con sobreprecio de la ex Clínica Sierra Bella en la [[Municipalidad de Santiago]] ([[Caso Sierra Bella]], [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]], [[Dictamen-CGR-SierraBella-2023]]).

## Historial de Nexos y Fiscalizaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Acto Fiscalizado",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Registrada",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Pandora Papers: Piñera vendió Minera Dominga a Délano en Islas Vírgenes Británicas](https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/) | Radio Agricultura | `secundaria` | 2021-10-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/) |
| [Sebastián Piñera declaró por más de dos horas en Fiscalía por caso Exalmar](https://www.df.cl/economia-y-politica/actualidad/sebastian-pinera-declaro-por-mas-de-dos-horas-en-fiscalia-por-caso-exalmar) | Diario Financiero | `secundaria` | 2017-05-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/economia-y-politica/actualidad/sebastian-pinera-declaro-por-mas-de-dos-horas-en-fiscalia-por-caso-exalmar) |
| [Cámara de Diputados aprobó el informe de la comisión investigadora del caso](https://www.cnnchile.com/pais/camara-de-diputados-aprobo-el-informe-de-la-comision-investigadora-del-caso_20171130/) | CNN Chile | `secundaria` | 2017-11-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/camara-de-diputados-aprobo-el-informe-de-la-comision-investigadora-del-caso_20171130/) |
| [Caso Democracia Viva: contratos evitaron revisión de Contraloría al ser pagados de forma parcializada](https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) | BioBioChile | `secundaria` | 2023-06-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) |
| [Tras informe sobre Democracia Viva, contralor afirma que hubo corrupción](https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) | La Tercera | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) |
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
