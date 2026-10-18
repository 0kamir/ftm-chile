---
tipo_nodo: causa_judicial
ruc: "0600306114-2"
año_inicio: 2006
tribunal_o_fiscalia: "Superintendencia de Valores y Seguros (CMF) / Corte de Apelaciones de Santiago / Corte Suprema de Chile"
fiscal_a_cargo: "Superintendencia de Valores y Seguros (Resolución Exenta N° 306-2007) / Ministro Luis Correa Bulo (Causa Banco de Talca 1982)"
estado_judicial: cerrada_con_condena
delito_principal: "[[Negociacion Incompatible]]"
tags:
  - causa
  - caso-lan
  - banco-de-talca
  - informacion-privilegiada
  - mercado-valores
---

# Caso LAN Informacion Privilegiada y Banco de Talca

## Ficha Procesal y Regulatoria
- **RUC / Rol Administrativo**: `= this.ruc` (Resolución Exenta SVS N° `306` de 6 de julio de 2007 y Causa Criminal Banco de Talca de agosto de 1982)
- **Año de Inicio**: `= this.año_inicio` (con antecedente penal bancario en 1982 y fiscalizaciones SII sobre "empresas zombis" entre 2007 y 2015)
- **Órgano Sancionador / Tribunal**: `= this.tribunal_o_fiscalia`
- **Autoridad Instructora**: `= this.fiscal_a_cargo`
- **Estado Judicial / Administrativo**: `= this.estado_judicial` (Multa ejecutoriada y pagada de 11.470 UF ante la SVS/CMF por uso de información privilegiada en 2007; sobreseimiento por amparo de la Corte Suprema en Banco de Talca 1982)
- **Delito / Infracción Principal**: `= this.delito_principal` (infracción al artículo 165 de la Ley N° 18.045 de Mercado de Valores, infracción a la Ley General de Bancos y elusión tributaria fiscalizada por el [[Servicio Impuestos Internos]])

## Síntesis Forense de la Causa
Expediente regulatorio, bursátil, bancario y tributario que consolida las infracciones patrimoniales y financieras de [[Sebastian Pinera Echenique]] y su grupo empresarial [[Bancard Inversiones Ltda]] en el mercado de capitales chileno:

1. **Sanción por Uso de Información Privilegiada en *LAN Airlines* (`2006–2007`)**: El 24 de julio de 2006, tras participar en una sesión extraordinaria del directorio de *LAN Airlines S.A.* en la que se entregaron estados financieros reservados no divulgados al mercado ni a la [[Comision para el Mercado Financiero]] (entonces SVS), [[Sebastian Pinera Echenique]] instruyó a través de su vehículo *Inversiones Santa Cecilia S.A.* ([[Bancard Inversiones Ltda]]) la compra de **3.000.000 de acciones de LAN** por cerca de **US$ 9,8 millones** (`$5.300.000.000 CLP` en [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]]). Mediante la [[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]], la SVS lo sancionó con una **multa de 11.470 UF (~US$ 363.000)** por vulnerar el deber de abstención sobre información privilegiada.
2. **Caso *Banco de Talca* (`1982`)**: Durante su gestión como gerente general del *Banco de Talca*, se otorgaron créditos cruzados sin garantías reales a sociedades relacionadas de papel (*Infinco* y grupo Calaf-Danioni) por más de **US$ 38 millones** (`~85%` de la cartera del banco, equivalentes a **`$18.500.000.000 CLP`** en [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]]), provocando la intervención y liquidación de la entidad. El 28 de agosto de 1982 el juez Luis Correa Bulo dictó encargatoria de reo y orden de captura por estafa e infracción a la Ley General de Bancos contra [[Sebastian Pinera Echenique]], quien permaneció **24 días prófugo** hasta que la [[Corte Suprema de Chile]] acogió un recurso de amparo que dejó sin efecto la declaratoria de reo.
3. **Esquema de "Empresas Zombis" y Elusión ante el SII (`2007–2015`)**: Adquisición por parte de [[Bancard Inversiones Ltda]] (administrada por [[Santiago Valdes Gutierrez]]) de sociedades quebradas con pérdidas tributarias arrastradas para absorber utilidades y eludir el pago de impuestos ante el [[Servicio Impuestos Internos]].

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
