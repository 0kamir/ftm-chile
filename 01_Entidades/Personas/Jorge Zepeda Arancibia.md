---
tipo_nodo: persona
rut: ""
aliases:
  - "Jorge Zepeda"
  - "Ministro Jorge Zepeda Arancibia"
rol_principal: "Ex Ministro de la Corte de Apelaciones de Santiago y Ministro en Visita Extraordinario del Caso Colonia Dignidad"
afiliacion_politica: "Independiente"
situacion_procesal: testigo_clave
medida_cautelar: "Sin medidas cautelares (Magistrado instructor designado por la Corte Suprema)"
tags:
  - entidad/persona
  - poder-judicial
  - caso-colonia-dignidad
---

# Jorge Zepeda Arancibia

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Magistrado del Poder Judicial designado por la [[Corte Suprema de Chile]] como Ministro en Visita extraordinario con dedicación exclusiva para instruir los cuadernos penales, patrimoniales, de asociación ilícita, control de armas y derechos humanos del [[Caso Colonia Dignidad]] (Rol `2.182-1998` y acumulados). Bajo su dirección se ejecutó la captura internacional de [[Paul Schafer Schneider]] en marzo de 2005, el hallazgo e incautación de los arsenales subterráneos de guerra en el predio de [[Sociedad Benefactora y Educacional Dignidad]] en junio de 2005 ([[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]]), los embargos patrimoniales junto al [[Servicio Impuestos Internos]] sobre el holding *Villa Baviera / Cerro Florido S.A.* ([[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]]) y el procesamiento de la jerarquía liderada por Schäfer y [[Hartmut Hopp Miottel]], cuyas condenas fueron confirmadas por la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-ColoniaDignidad-2013]].

## Causas y Nexos Instruidos Judicialmente
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Actuación",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto Registrado (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_destino), this.file.name) OR contains(string(firmante_origen), this.file.name)
SORT fecha ASC
```
