---
tipo_nodo: causa_judicial
ruc: "0400164900-4"
año_inicio: 2004
tribunal_o_fiscalia: "Corte de Apelaciones de Santiago / Corte Suprema de Chile (Causa Rol 1.649-2004 y Casación Rol 16.865-2017)"
fiscal_a_cargo: "Ministros en Visita Sergio Muñoz Gajardo, Carlos Cerda Fernández y Manuel Antonio Valderrama Rebolledo"
estado_judicial: cerrada_con_condena
delito_principal: "[[Malversacion de Caudales Publicos]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
    titulo: "Caso Riggs fue cerrado por la Corte Suprema tras 14 años"
    medio: "CNN Chile"
    tipo: secundaria
    fecha: 2018-08-24
    consultado: 2026-10-19
  - url: "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
    titulo: "Ordenan decomiso de bienes de Pinochet"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2018-08-25
    consultado: 2026-10-19
historial_correcciones:
  - "La CS condenó a tres exmilitares (Vergara, Mac Lean, Castillo) por malversación de US$ 6,47 millones y ordenó comiso de US$ 1,62 millones. Pinochet murió (2006) sin condena."
tags:
  - causa
  - caso-riggs
  - offshore
  - ejercito
  - gastos-reservados
---

# Caso Riggs

## Ficha Procesal y Judicial
- **RUC / Rol Judicial**: `= this.ruc` (Causa Rol N° `1.649-2004` / Sentencia Corte Suprema Rol N° `16.865-2017`)
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Ministro Instructor**: `= this.tribunal_o_fiscalia`
- **Magistrados a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Delito Tributario]], [[Lavado de Activos]], estafa al Fisco y uso malicioso de pasaportes e instrumentos públicos falsos)

## Síntesis Forense de la Causa
Macro-investigación penal, financiera y tributaria iniciada en julio de 2004 tras el informe del Subcomité Permanente de Investigaciones del Senado de los Estados Unidos que reveló que el **Riggs Bank** de Washington D.C. estructuró y ocultó una red de más de **125 cuentas bancarias secretas**, certificados de depósito a plazo y sociedades de papel *offshore* en Bahamas, Islas Vírgenes Británicas, Panamá y Gibraltar (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*), agrupadas bajo [[Riggs Bank y Sociedades Offshore Ashburton]], para esconder la fortuna ilícita de [[Augusto Pinochet Ugarte]] y su círculo familiar y jurídico integrado por [[Lucia Hiriart Rodriguez]], [[Augusto Pinochet Hiriart]] y su albacea [[Oscar Aitken Lavanchy]].

Los hallazgos periciales clave de la causa incluyen:
1. **Desvío Sistemático de Gastos Reservados y Uso de Identidades Falsas**: La instrucción del primer Ministro en Visita, [[Sergio Munoz Gajardo]], acreditó que [[Augusto Pinochet Ugarte]] abrió cuentas secretas utilizando pasaportes diplomáticos y cédulas chilenas ideológicamente falsas bajo heterónimos como *"Daniel López"* y *"José Ramón Ugarte"*, nutriéndolas con el desvío continuo de fondos públicos provenientes de los gastos reservados de la Presidencia de la República y de la Comandancia en Jefe del Ejército ([[Comando de Apoyo a la Fuerza del Ejercito]]) ([[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]]).
2. **Peritaje de la Universidad de Chile y Querellas del SII**: El peritaje contable de la Facultad de Economía y Negocios de la Universidad de Chile estableció que el patrimonio total acumulado ascendía a **US$ 21,32 millones**, de los cuales **US$ 17,86 millones** carecían de justificación económica lícita. Paralelamente, el [[Servicio Impuestos Internos]] presentó querellas criminales por declaraciones maliciosamente falsas e impuestos evadidos por más de **$2.450.000.000 CLP**, dando lugar al procesamiento de [[Lucia Hiriart Rodriguez]], [[Augusto Pinochet Hiriart]] y [[Oscar Aitken Lavanchy]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]]).
3. **Condena y Comiso Histórico de la Corte Suprema (2018)**: El 24 de agosto de 2018, la Segunda Sala Penal de la [[Corte Suprema de Chile]] dictó sentencia definitiva (Rol N° `16.865-2017`), revocando la prescripción de segunda instancia, condenando a tres exoficiales del Ejército (Gabriel Vergara Cifuentes, Juan Mac-Lean Vergara y Eugenio Castillo Cádiz) como autores de [[Malversacion de Caudales Publicos]] y decretando el **comiso definitivo a favor del Fisco de Chile de US$ 1.649.142 líquidos más 24 bienes raíces y vehículos** inscritos a nombre de Pinochet y sus sociedades pantalla ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).

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
