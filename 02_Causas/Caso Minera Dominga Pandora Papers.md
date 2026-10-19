---
tipo_nodo: causa_judicial
ruc: "2100912845-3"
año_inicio: 2021
tribunal_o_fiscalia: "Fiscalía Nacional / Fiscalía Regional de Valparaíso / 7° Juzgado de Garantía de Santiago / Cámara de Diputados"
fiscal_a_cargo: "Claudia Perivancich Hoyuelos (Fiscal Regional de Valparaíso) / Manuel Guerra Fuenzalida (Arista 2017)"
estado_judicial: sobreseida
delito_principal: "[[Cohecho]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/"
    titulo: "Fiscalía cierra investigación por el caso Dominga y solicita sobreseimiento definitivo"
    medio: "La Tercera"
    tipo: secundaria
    fecha: 2024-01-05
    consultado: 2026-10-19
  - url: "https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html"
    titulo: "Pandora Papers: venta de Minera Dominga en Islas Vírgenes"
    medio: "Meganoticias"
    tipo: secundaria
    fecha: 2021-10-05
    consultado: 2026-10-19
alertas_verificacion:
  - "Fiscalía pidió sobreseimiento definitivo en enero de 2024; no se confirmó la resolución del tribunal."
tags:
  - causa
  - caso-dominga
  - pandora-papers
  - offshore
  - conflicto-interes
---

# Caso Minera Dominga Pandora Papers

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc` (y arista previa `RUC 1700198420-K`)
- **Año de Inicio**: `= this.año_inicio` (Hechos ejecutados en diciembre de 2010; primera investigación en 2017 y reapertura penal tras los *Pandora Papers* de ICIJ en octubre de 2021)
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscales Investigadores**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` (Acusación constitucional aprobada por la Cámara de Diputados en noviembre de 2021 y rechazada por falta de quórum en el Senado; extinción de responsabilidad penal por fallecimiento del imputado en febrero de 2024)
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Negociacion Incompatible]] y [[Delito Tributario]])

## Síntesis Forense de la Causa
Investigación penal y constitucional desencadenada en octubre de 2021 por la filtración global **Pandora Papers** del Consorcio Internacional de Periodistas de Investigación (ICIJ), que reveló los contratos originales firmados el 10 de diciembre de 2010 en las Islas Vírgenes Británicas mediante los cuales el *family office* de la familia Piñera Morel, [[Bancard Inversiones Ltda]] (*Bancard International Investment Inc.* e *Inversiones Mediterráneo*), vendió su participación en el proyecto minero-portuario **Dominga** (comuna de La Higuera, Región de Coquimbo) a [[Andes Iron SpA]], sociedad controlada por [[Carlos Alberto Delano Abbott]] (socio fundador de [[Empresas Penta SA]] e íntimo amigo del entonces Presidente de la República [[Sebastian Pinera Echenique]]), por un total de **US$ 152 millones** (`$75.500.000.000 CLP` en [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]]).

Los elementos forenses centrales documentados en [[Contrato-Offshore-BVI-PandoraPapers-Dominga-2010]] son:
1. **Cláusula Condicional Supeditada a Decisión Presidencial**: El contrato suscrito en el paraíso fiscal de Islas Vírgenes Británicas por **US$ 138 millones** (más US$ 14 millones en Chile) estableció que el pago de la tercera y última cuota —por **US$ 9,9 millones**— quedaba expresamente condicionado a que el Gobierno de Chile (encabezado por [[Sebastian Pinera Echenique]]) **no declarara la zona de emplazamiento del proyecto (frente a la Reserva Nacional Pingüino de Humboldt / Punta de Choros) como un área de exclusión o parque nacional** que impidiera la construcción del puerto minero de [[Andes Iron SpA]].
2. **Omisión de Protección Ambiental y Arista Subsecretaría de Minería**: Durante el primer gobierno de Piñera no se decretó dicha zona de exclusión ambiental, habilitándose el cobro de la cuota final. Asimismo, el entonces Subsecretario de Minería era [[Pablo Wagner San Martin]], condenado en el [[Caso Penta]] por delitos tributarios y enriquecimiento ilícito (absuelto de cohecho); no se encontró fuente que acredite gestiones suyas a favor del proyecto.
3. **Acusación Constitucional (Noviembre 2021)**: El 9 de noviembre de 2021, la Cámara de Diputados aprobó la acusación constitucional contra [[Sebastian Pinera Echenique]] por infringir gravemente el principio de probidad constitucional y comprometer el honor de la Nación.

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
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
