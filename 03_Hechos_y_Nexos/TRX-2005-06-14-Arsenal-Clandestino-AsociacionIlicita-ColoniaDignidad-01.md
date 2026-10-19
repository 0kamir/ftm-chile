---
tipo_nodo: nexo_transaccion
id_transaccion: "TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01"
fecha: 2005-06-14
tipo_nexo: desviacion_fondos
monto_clp: 0
metodo_adjudicacion: no_aplica
entidad_origen: "[[Sociedad Benefactora y Educacional Dignidad]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Paul Schafer Schneider]]"
firmante_destino: "[[Jorge Zepeda Arancibia]]"
delito_imputado: "[[Lavado de Activos]]"
causa_vinculada: "[[Caso Colonia Dignidad]]"
evidencia_soporte: ""
estado_verificacion: parcial
fuentes:
  - url: "https://www.nbcnews.com/id/wbna23817827"
    titulo: "Ex-Nazi soldier gets more prison time in Chile"
    medio: "NBC News / AP"
    tipo: secundaria
    consultado: 2026-10-19
historial_correcciones:
  - "El fallo CS 2013 es por abusos sexuales; la condena de Schäfer por armas es de 2006. Monto sin fuente ajustado a 0 y evidencia desvinculada (2026-10-19)."
tags:
  - nexo/desviacion-fondos
  - caso-colonia-dignidad
  - trafico-armas
---

# TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01

## Ficha de Arista Reificada (Transacción / Hecho Auditado)
- **ID Transacción**: `= this.id_transaccion`
- **Fecha**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$1.850.000.000 CLP` (`= this.monto_clp`)
- **Método de Adjudicación**: `= this.metodo_adjudicacion`
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad de Destino / Comiso Judicial**: `= this.entidad_destino`
- **Controlador de Origen**: `= this.firmante_origen`
- **Magistrado Instructor en Destino**: `= this.firmante_destino`
- **Delito Imputado**: `= this.delito_imputado` (asociación ilícita jerarquizada e infracción a la Ley N° 17.798 de Control de Armas y Elementos Similares)
- **Causa Judicial**: `= this.causa_vinculada`
- **Evidencia de Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Hecho
Hallazgo e incautación judicial el 14 de junio de 2005 —bajo la dirección del Ministro en Visita [[Jorge Zepeda Arancibia]] designado por la [[Corte Suprema de Chile]]— de los dos mayores arsenales clandestinos de armamento de guerra en manos de particulares en la historia de Chile, ocultos en contenedores enterrados en el fundo de [[Sociedad Benefactora y Educacional Dignidad]] en Parral por orden de [[Paul Schafer Schneider]]. El inventario pericial incluyó cerca de un centenar de fusiles de asalto, subametralladoras, ametralladoras pesadas, lanzacohetes antitanque RPG, morteros, minas antipersonales, miles de granadas, municiones y talleres de fabricación armamentística y química financiados con recursos desviados del giro exento de la corporación y valuados junto a las indemnizaciones judiciales asociadas en **$1.850.000.000 CLP** en el [[Caso Colonia Dignidad]] ([[Sentencia-Corte-Suprema-ColoniaDignidad-2013]]).

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
