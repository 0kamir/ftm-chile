---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2016
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Oriente / 4° Juzgado de Garantía de Santiago / Comisiones Investigadoras Cámara de Diputados"
fiscal_a_cargo: "Manuel Guerra Fuenzalida"
estado_judicial: sobreseida
delito_principal: "[[Negociacion Incompatible]]"
estado_verificacion: verificado
fuentes:
  - "https://www.df.cl/economia-y-politica/actualidad/sebastian-pinera-declaro-por-mas-de-dos-horas-en-fiscalia-por-caso-exalmar"
  - "https://www.cnnchile.com/pais/camara-de-diputados-aprobo-el-informe-de-la-comision-investigadora-del-caso_20171130/"
tags:
  - causa
  - caso-exalmar
  - fideicomiso-ciego
  - offshore
---

# Caso Exalmar y Fideicomiso Ciego

## Ficha Procesal y Parlamentaria
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio` (operaciones bursátiles y offshore ejecutadas entre noviembre de 2010 y febrero de 2013 durante el litigio en La Haya)
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con uso de información reservada del Estado y conflicto de interés regulatorio registrado por la [[Contraloria General de la Republica]])

## Síntesis de la Causa
Investigación penal del Ministerio Público y de dos Comisiones Especiales Investigadoras de la Cámara de Diputados sobre las inversiones transfronterizas no incluidas en el fideicomiso ciego voluntario de [[Sebastian Pinera Echenique]] mientras ejercía como Presidente de la República:

1. **Inversión Offshore en *Pesquera Exalmar S.A.* durante el Juicio en La Haya (`2010–2013`)**: Entre noviembre de 2010 y febrero de 2013 —mientras [[Sebastian Pinera Echenique]] conducía como Jefe de Estado la defensa soberana de Chile ante la Corte Internacional de Justicia de La Haya frente a la demanda marítima del Perú—, su *family office* [[Bancard Inversiones Ltda]] (*Bancard International Investment Inc.*, domiciliada en las Islas Vírgenes Británicas y gerenciada por [[Santiago Valdes Gutierrez]]) adquirió el **`9,18%` del capital accionario de la pesquera peruana *Exalmar S.A.*** por aproximadamente **US$ 16,5 millones** (`$8.250.000.000 CLP` en [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]]), empresa que, según los querellantes, se beneficiaría de los derechos de pesca en el triángulo marítimo adjudicado a Perú en el fallo de enero de 2014 ([[Contrato-Offshore-BVI-PandoraPapers-Dominga-2010]]).
2. **Arista Casino *Enjoy S.A.* y Decreto Supremo N° 77 (`2020–2021`)**: Fiscalización de la [[Contraloria General de la Republica]] y de la Comisión Investigadora parlamentaria por la dictación del Decreto Supremo N° 77 de Hacienda (enero de 2021) durante el segundo mandato de Piñera, que modificó las normas de concesiones de casinos y prorrogó plazos evitando la ejecución de boletas de garantía de *Enjoy S.A.* mientras administradoras vinculadas a los fideicomisos del mandatario mantenían exposición financiera en dicha compañía.

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
| [Sebastián Piñera declaró por más de dos horas en Fiscalía por caso Exalmar](https://www.df.cl/economia-y-politica/actualidad/sebastian-pinera-declaro-por-mas-de-dos-horas-en-fiscalia-por-caso-exalmar) | Diario Financiero | `secundaria` | 2017-05-12 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/economia-y-politica/actualidad/sebastian-pinera-declaro-por-mas-de-dos-horas-en-fiscalia-por-caso-exalmar) |
| [Cámara de Diputados aprobó el informe de la comisión investigadora del caso](https://www.cnnchile.com/pais/camara-de-diputados-aprobo-el-informe-de-la-comision-investigadora-del-caso_20171130/) | CNN Chile | `secundaria` | 2017-11-30 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/camara-de-diputados-aprobo-el-informe-de-la-comision-investigadora-del-caso_20171130/) |
