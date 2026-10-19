---
tipo_nodo: causa_judicial
ruc: "9600218200-5"
año_inicio: 1996
tribunal_o_fiscalia: "Corte de Apelaciones de Santiago / Corte Suprema de Chile (Ministro en Visita Extraordinario — Rol 2.182-1998 y acumulados)"
fiscal_a_cargo: "Ministro en Visita Jorge Zepeda Arancibia (y Ministro Hernán González García en etapa inicial)"
estado_judicial: cerrada_con_condena
delito_principal: "[[Lavado de Activos]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
    titulo: "Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad"
    medio: "El Mostrador"
    tipo: secundaria
    fecha: 2013-01-28
    consultado: 2026-10-19
  - url: "https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html"
    titulo: "Seis ex jerarcas de Colonia Dignidad fueron condenados a prisión por la Corte Suprema"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2013-01-28
    consultado: 2026-10-19
alertas_verificacion:
  - "El fallo CS de enero 2013 condenó por complicidad en abusos sexuales a menores; la condena de Schäfer por armas es de 2006. Revisar TRX-2005-06-14-Arsenal y la evidencia 'Sentencia-Corte-Suprema-ColoniaDignidad-2013'."
tags:
  - causa
  - caso-colonia-dignidad
  - asociacion-ilicita
  - derechos-humanos
---

# Caso Colonia Dignidad

## Ficha Procesal y Judicial
- **RUC / Rol Judicial**: `= this.ruc` (Causa Rol N° `2.182-1998` y cuadernos acumulados)
- **Año de Inicio**: `= this.año_inicio` (cancelación de personalidad jurídica en 1991; instrucción penal por fugas y abusos desde 1996)
- **Tribunal / Ministro Instructor**: `= this.tribunal_o_fiscalia`
- **Magistrado a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso real con asociación ilícita jerarquizada, [[Delito Tributario]], abuso sexual reiterado de menores, secuestro calificado, torturas e infracción a la Ley N° 17.798 de Control de Armas)

## Síntesis Forense de la Causa
Macro-proceso penal, tributario e institucional centrado en el enclave fundado en 1961 en Catillo (comuna de Parral, Región del Maule) bajo la fachada de la corporación sin fines de lucro [[Sociedad Benefactora y Educacional Dignidad]] (posteriormente rebautizada comercialmente como *Villa Baviera*), dirigida con control totalitario por [[Paul Schafer Schneider]] y su segundo al mando [[Hartmut Hopp Miottel]]. La investigación forense se estructura en tres grandes ejes de corrupción, captura estatal e ilicitud financiera:

1. **Arista Tributaria y de Vaciamiento Patrimonial (SII / Holding Villa Baviera)**: Tras la dictación del Decreto Supremo N° 143 del Ministerio de Justicia (31 de enero de 1991) que canceló la personalidad jurídica de [[Sociedad Benefactora y Educacional Dignidad]] por desviación de fines y violaciones sistemáticas a los derechos fundamentales, la jerarquía del enclave ejecutó un vaciamiento patrimonial masivo transfiriendo gratuitamente o a precios viles más de 17.000 hectáreas, plantas industriales de áridos, hospitales y activos financieros hacia un entramado de más de 15 sociedades anónimas cerradas (*Inmobiliaria e Inversiones Cerro Florido S.A.*, *Agrícola y Forestal Las Acacias S.A.*, entre otras) para burlar el traspaso legal de bienes al Estado y evadir impuestos ante el [[Servicio Impuestos Internos]] ([[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]]).
2. **Arista de Blindaje Político-Parlamentario y Obstrucción a la Justicia**: Durante la década de 1990, mientras [[Paul Schafer Schneider]] permanecía prófugo (1996–2005) de las órdenes de captura judicial por abuso sistemático de menores, operó una red de protección política, parlamentaria y judicial articulada en torno al denominado *"Grupo de Amigos de Colonia Dignidad"*, con participación destacada de parlamentarios de la [[Union Democrata Independiente]] encabezados por el senador de la circunscripción Maule Sur [[Hernan Larrain Fernandez]], quienes interpusieron requerimientos ante el Tribunal Constitucional contra la disolución de la corporación y denunciaron públicamente los operativos policiales de allanamiento ([[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]]).
3. **Arista de Asociación Ilícita, Tráfico de Armas de Guerra y Captura de Aparatos de Seguridad**: Tras la detención de [[Paul Schafer Schneider]] en Argentina en marzo de 2005, la instrucción del Ministro en Visita [[Jorge Zepeda Arancibia]] descubrió en junio de 2005 dos gigantescos arsenales subterráneos clandestinos con armamento de guerra, cohetes antitanque, explosivos y precursores químicos dentro del predio de [[Sociedad Benefactora y Educacional Dignidad]] ([[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]]), acreditando una asociación ilícita entre la jerarquía del enclave y agentes estatales que culminó en las condenas definitivas ratificadas por la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-ColoniaDignidad-2013]].

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
