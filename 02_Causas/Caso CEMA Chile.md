---
tipo_nodo: causa_judicial
ruc: "1600341250-8"
año_inicio: 2016
tribunal_o_fiscalia: "Corte de Apelaciones de Santiago / 34° Juzgado del Crimen de Santiago / Consejo de Defensa del Estado (Rol 34.125-2016)"
fiscal_a_cargo: "Ministro en Visita Guillermo de la Barra Dünner / Consejo de Defensa del Estado"
estado_judicial: cerrada_con_condena
delito_principal: "[[Malversacion de Caudales Publicos]]"
tags:
  - causa
  - caso-cema-chile
  - bienes-fiscales
  - fundaciones
---

# Caso CEMA Chile

## Ficha Procesal y Judicial
- **RUC / Rol Judicial**: `= this.ruc` (Causa Rol N° `34.125-2016` y demanda civil de disolución y restitución patrimonial del Consejo de Defensa del Estado)
- **Año de Inicio**: `= this.año_inicio` (reapertura por orden de la Corte de Apelaciones de Santiago tras hallazgos preliminares en el [[Caso Riggs]])
- **Tribunal / Ministro Instructor**: `= this.tribunal_o_fiscalia`
- **Magistrado / Órgano Acusador**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` (Cerrada con disolución de la fundación y restitución forzosa al Fisco de 108 inmuebles y la totalidad de sus activos líquidos en 2019)
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Fraude al Fisco]] y distracción indebida de activos públicos)

## Síntesis Forense de la Causa
Investigación penal y patrimonial sobre el apoderamiento, enajenación comercial y desvío de recursos derivados de más de **135 bienes raíces fiscales, municipales y del SERVIU** que fueron transferidos gratuitamente entre 1973 y 1990 a la [[Fundacion CEMA Chile]], entidad privada presidida a perpetuidad hasta agosto de 2016 por [[Lucia Hiriart Rodriguez]], cónyuge de [[Augusto Pinochet Ugarte]].

El mecanismo forense acreditado en la causa operó en tres fases:
1. **Privatización Estatutaria y Blindaje Vitalicio (1989–1990)**: Antes del término de la dictadura militar, el directorio encabezado por [[Lucia Hiriart Rodriguez]] modificó los estatutos de [[Fundacion CEMA Chile]] para desvincular su presidencia del cargo de Primera Dama de la República, asegurándole el control vitalicio del patrimonio inmobiliario donado por el Estado.
2. **Liquidación Inmobiliaria y Desvío de Fondos (1990–2016)**: Durante más de dos décadas, [[Fundacion CEMA Chile]] vendió a privados decenas de terrenos, sedes comunitarias y plazas públicas recibidas gratuitamente del Fisco, recaudando más de **`$8.900.000.000 CLP`**, además de sufragar gastos y asignaciones vinculadas a [[Lucia Hiriart Rodriguez]] y su entorno familiar (hechos pesquisados inicialmente por el Ministro en Visita [[Sergio Munoz Gajardo]] en las diligencias conexas del [[Caso Riggs]]).
3. **Embargo Judicial, Disolución y Restitución Histórica al Fisco (2016–2019)**: Tras el embargo decretado por el Ministro en Visita Guillermo de la Barra y la demanda del Consejo de Defensa del Estado ante los tribunales superiores ([[Corte Suprema de Chile]]), [[Lucia Hiriart Rodriguez]] renunció en agosto de 2016 y la fundación fue obligada a disolverse y restituir al Estado de Chile **108 inmuebles fiscales y municipales más sus fondos bancarios remanentes**, por un valor patrimonial auditado superior a **`$10.500.000.000 CLP`** ([[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] y [[Acuerdo-Judicial-Restitucion-CEMAChile-2019]]).

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
