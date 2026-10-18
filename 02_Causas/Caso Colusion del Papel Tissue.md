---
tipo_nodo: causa_judicial
ruc: "ROL-C-299-15-TDLC"
año_inicio: 2015
tribunal_o_fiscalia: "Tribunal de Defensa de la Libre Competencia (TDLC) / Corte Suprema de Chile"
fiscal_a_cargo: "Felipe Irarrázabal Philippi (Fiscal Nacional Económico) / TDLC"
estado_judicial: cerrada_con_condena
delito_principal: "[[Colusion y Atentado a la Libre Competencia]]"
tags:
  - causa
  - libre-competencia
  - colusion-tissue
  - cartel-confort
  - cmpc
  - pisa
---

# Caso Colusion del Papel Tissue

## Ficha Procesal, Regulatoria y Sancionatoria
- **Rol de Causa / Expediente TDLC**: `= this.ruc` *(Sentencia N° 160/2017 y Recurso de Reclamación Rol 2.923-2018 ante Corte Suprema)*
- **Año de Requerimiento Público**: `= this.año_inicio` (Período colusorio acreditado: 2000–2015)
- **Tribunales Resolutivos**: `= this.tribunal_o_fiscalia`
- **Órgano Persecutor Especializado**: `= this.fiscal_a_cargo` (en coordinación con el [[Servicio Nacional del Consumidor]])
- **Estado Judicial**: `= this.estado_judicial` (Fallo definitivo ejecutoriado con multas históricas y compensación masiva)
- **Infracción / Delito Económico Principal**: `= this.delito_principal`

## Resumen Ejecutivo de la Causa
Investigación y condena histórica por colusión y formación de cartel empresarial en el mercado del papel tissue (papel higiénico, servilletas, pañuelos desechables y toallas de papel), protagonizado por las dos empresas dominantes que concentraban más del 90% del mercado chileno: [[Empresas CMPC SA]] (Grupo Matte) y [[SCA Chile SA]] (ex PISA, fundada por [[Gabriel Ruiz-Tagle Serrano]]).

La causa se articuló en tres hitos fundamentales:
1. **Pacto Clandestino de Precios y Cuotas de Mercado (2000–2015)**: A comienzos del año 2000, para frenar la competencia y la entrada de marcas propias de supermercados, ejecutivos de CMPC y PISA encabezados por [[Gabriel Ruiz-Tagle Serrano]] sostuvieron reuniones en el Club de Golf Las Brisas de Chicureo y en hoteles de Santiago, acordando congelar las participaciones de mercado (aproximadamente 76% para CMPC y 24% para PISA) y coordinar alzas periódicas de listas de precios ([[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]).
2. **Requerimiento FNE y Delación Compensada (Octubre 2015)**: La [[Fiscalia Nacional Economica]] presentó requerimiento tras acoger la autodenuncia de CMPC y luego la de SCA Chile. La revelación forzó la renuncia de [[Eliodoro Matte Larrain]] a la presidencia de CMPC en 2016 y conmocionó el debate económico del país.
3. **Compensación Universal y Multas de la Corte Suprema (2017–2020)**: En marzo de 2017, CMPC suscribió un acuerdo voluntario con el [[Servicio Nacional del Consumidor]] por el cual traspasó **`$97.500.000.000 CLP`** (US$ 150 millones) distribuidos en $7.000 CLP a cada chileno mayor de 18 años ([[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]]). En enero de 2020, la [[Corte Suprema de Chile]] revocó la exención de multa a CMPC al determinar que había coaccionado a su competidora, multando a ambas empresas con 20.000 UTA (cerca de US$ 15 millones cada una).

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Infracción / Delito",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```
