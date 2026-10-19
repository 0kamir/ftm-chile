---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2003
tribunal_o_fiscalia: "3° Juzgado del Crimen de Santiago / Ministra en Visita Gloria Ana Chevesich / Corte Suprema"
fiscal_a_cargo: "Gloria Ana Chevesich Ruiz (Ministra en Visita Extraordinaria)"
estado_judicial: cerrada_con_condena
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
    titulo: "Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas"
    medio: "Emol"
    tipo: secundaria
    fecha: 2016-06-29
    consultado: 2026-10-19
  - url: "https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html"
    titulo: "Caso MOP-Gate: ex ministro Carlos Cruz condenado a tres años de pena remitida"
    medio: "Emol"
    tipo: secundaria
    fecha: 2010-07-01
    consultado: 2026-10-19
historial_correcciones:
  - "Corregido el 2026-10-19: la empresa es GATE y su dueño condenado es Héctor Peña Véliz; se retiró 'Roberto Lewin Valdivieso' por falta de fuente."
tags:
  - causa
  - sobresueldos
  - caso-mop-gate
---

# Caso MOP-Gate

## Ficha Procesal y Judicial
- **RUC / Rol**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Ministra en Visita**: `= this.tribunal_o_fiscalia`
- **Magistrada Instructora**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Delito Tributario]])

## Síntesis de la Causa
Investigación judicial instruida por la Ministra en Visita Extraordinaria Gloria Ana Chevesich Ruiz y ratificada por la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-MOPGate-2016]]) que desarticuló una red de triangulación de fondos públicos en el [[Ministerio de Obras Publicas]] encabezada por su entonces titular [[Carlos Cruz Lorenzen]] (militante del [[Partido Socialista de Chile]]). El esquema operaba mediante el abultamiento artificial de contratos de asesoría e ingeniería adjudicados a la consultora [[Gestion Ambiental y Territorial SA]] (GATE, de propiedad de [[Hector Pena Veliz]]), cuyos excedentes retornaban para financiar sobresueldos de altos directivos ministeriales ([[TRX-2001-08-20-Contratos-MOP-GATE-01]]).

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
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
