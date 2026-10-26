---
tipo_nodo: entidad_publica
rut: ""
categoria: Municipio
region: "Metropolitana de Santiago"
superior_jerarquico: "Concejo Municipal de Maipú (Autónoma)"
estado_verificacion: verificado
fuentes:
  - "https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/"
  - "https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf"
  - "https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/"
  - "https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/"
  - "https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/"
  - "https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html"
tags:
  - entidad/publica
  - municipio
  - maipu
---

# Municipalidad de Maipu

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Corporación edilicia de la Región Metropolitana. Durante la administración 2016–2021 encabezada por [[Cathy Barriga Guerra]], se implementó una modificación en la estructura de control presupuestario que permitió comprometer gastos sin respaldo financiero real por **$30.972.000.000 CLP** ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]), según acreditó el [[Informe-Contraloria-Municipalidad-Maipu-2021]] en el marco del [[Caso Municipalidad de Maipu]].

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Autoridad Municipal",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Ex concejal RN de Maipú es condenado por lavado de activos y cohecho en caso Basura](https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/) | El Dínamo | `secundaria` | 2022-07-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/) |
| [Comunicado Fiscalía Occidente Caso Basura](https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf) | Fiscalía Regional Metropolitana Occidente (vía El Mostrador) | `primaria` | 2025-06-03 | [Wayback ↺](https://web.archive.org/web/*/https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf) |
| [Expediente Cathy Barriga: las pruebas clave](https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/) |
| [Formalización de Cathy Barriga: qué delitos le imputan](https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) | CNN Chile | `secundaria` | 2024-01-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) |
| [Exalcaldesa Cathy Barriga será formalizada en enero de 2024](https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) | El Mostrador | `secundaria` | 2023-11-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) |
| [Caso Maipú: Fiscalía Oriente reformalizará a Cathy Barriga](https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) | Meganoticias | `secundaria` | 2024-08-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) |
