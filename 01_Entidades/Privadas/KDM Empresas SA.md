---
tipo_nodo: entidad_privada
rut: ""
razon_social: "KDM Empresas S.A. (Consorcio KDM / Demarco S.A. / Starco S.A.)"
fecha_constitucion: "1993-11-08"
objeto_social: "Recolección, transporte, tratamiento y disposición final de residuos sólidos domiciliarios e industriales"
representante_legal: "[[Fernando Leon Steffens]]"
estado_verificacion: verificado
fuentes:
  - "https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/"
  - "https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf"
  - "https://www.latercera.com/nacional/noticia/a-13-anos-de-que-se-iniciara-el-caso-condenan-a-exalcalde-luis-plaza-rn-por-fraude-al-fisco-en-ultima-arista-del-emblematico-caso-basura/TGWT6RCHCJHEBP5MVQXK2VL2AE/"
tags:
  - entidad/privada
  - concesionaria-residuos
  - caso-basura
---

# KDM Empresas SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Ejecutivo y Representante**: `= this.representante_legal`

## Contexto y Societario
Holding concesionario de recolección de basura y rellenos sanitarios (integrado por sus filiales Demarco S.A. y KDM Tratamiento S.A., filial del grupo Urbaser Danner). En el [[Caso Basura]] ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]), la Fiscalía Regional Metropolitana Occidente imputó que a través de su ejecutivo [[Fernando Leon Steffens]] y del operador municipal [[Marcelo Torres Ferrari]] se habrían canalizado sobornos para asegurar la adjudicación del contrato (el tribunal condenó en 2022 al exconcejal Marcelo Torres por pagos de KDM por $186,5 millones) de recolección de residuos de la [[Municipalidad de Maipu]] por **$18.500.000.000 CLP** ([[TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01]]) y contrataciones conexas en la [[Municipalidad de Cerro Navia]] bajo la alcaldía de [[Luis Plaza Sanchez]] ([[TRX-2012-03-22-Contratos-Residuos-CerroNavia-01]]).

## Historial de Licitaciones y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
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
| [Condenan a exalcalde Luis Plaza por fraude al fisco en última arista del Caso Basura](https://www.latercera.com/nacional/noticia/a-13-anos-de-que-se-iniciara-el-caso-condenan-a-exalcalde-luis-plaza-rn-por-fraude-al-fisco-en-ultima-arista-del-emblematico-caso-basura/TGWT6RCHCJHEBP5MVQXK2VL2AE/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/a-13-anos-de-que-se-iniciara-el-caso-condenan-a-exalcalde-luis-plaza-rn-por-fraude-al-fisco-en-ultima-arista-del-emblematico-caso-basura/TGWT6RCHCJHEBP5MVQXK2VL2AE/) |
