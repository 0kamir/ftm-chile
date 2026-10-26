---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2011
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Occidente / 9° Juzgado de Garantía de Santiago / TOP Santiago"
fiscal_a_cargo: "José Luis Pérez Calaf / Tufit Bufadel Godoy"
estado_judicial: cerrada_con_condena
delito_principal: "[[Cohecho]]"
estado_verificacion: verificado
fuentes:
  - "https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf"
  - "https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/"
tags:
  - causa
  - corrupcion-municipal
  - licitacion-basura
  - caso-basura
---

# Caso Basura

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscales Investigadores**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Fraude al Fisco]] y [[Lavado de Activos]])

## Síntesis de la Causa
Investigación penal de alta complejidad desarrollada por la Fiscalía Regional Metropolitana Occidente ([[Acusacion-Fiscalia-Occidente-CasoBasura-2017]]) que indagó una red transversal de corrupción municipal en torno a la adjudicación de multimillonarios contratos de recolección, transporte y disposición final de residuos domiciliarios en favor del consorcio [[KDM Empresas SA]] (representado por [[Fernando Leon Steffens]]). El caso articuló a concejales, alcaldes y administradores municipales en la [[Municipalidad de Maipu]] y la [[Municipalidad de Cerro Navia]], destacando la actuación de [[Marcelo Torres Ferrari]] y del exalcalde [[Luis Plaza Sanchez]] (ambos militantes de [[Renovacion Nacional]]) en las operaciones [[TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01]] y [[TRX-2012-03-22-Contratos-Residuos-CerroNavia-01]].

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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Comunicado Fiscalía Occidente: condenas Caso Basura arista Cerro Navia](https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf) | Fiscalía Regional Metropolitana Occidente (vía El Mostrador) | `primaria` | 2025-06-03 | [Wayback ↺](https://web.archive.org/web/*/https://media-front.elmostrador.cl/2025/06/20250603-COMUNICADO-CASO-BASURA.pdf) |
| [Ex concejal RN de Maipú es condenado por lavado de activos y cohecho en caso Basura](https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/) | El Dínamo | `secundaria` | 2022-07-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2022/07/28/ex-concejal-rn-de-maipu-es-condenado-por-lavado-de-activos-y-cohecho-en-caso-basura/) |
