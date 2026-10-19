---
tipo_nodo: vista_analitica
titulo: "Reporte de Auditoría Forense Automatizada (UTM, HHI, PageRank, Brandes y Topología)"
actualizacion_automatica: true
tags:
  - dashboard
  - auditoria-cgr
  - topologia
---

# Reporte de Auditoría Forense Automatizada (CGR / Ministerio Público)

- **Monto Global Investigado**: **$694.022.063.198 CLP** (Equivalente a **11.661.961.8 UTM**)
- **Total de Aristas Reificadas (`TRX`)**: **70**
- **Casos de Fraccionamiento bajo 5.000 UTM detectados**: **1**

---

## 1. Diagrama Topológico de Flujos Financieros Reificados (Mermaid)

```mermaid
flowchart LR
  classDef pub fill:#1b5e20,stroke:#81c784,color:#fff,stroke-width:2px;
  classDef priv fill:#e65100,stroke:#ffb74d,color:#fff,stroke-width:2px;
  classDef trx fill:#b71c1c,stroke:#ef9a9a,color:#fff,stroke-width:1.5px;
  classDef pers fill:#0d47a1,stroke:#64b5f6,color:#fff,stroke-width:1.5px;
  N1["Agencia Central de Inteligencia CIA y Escuela de las Americas"]:::pub --> N3("TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01<br/>$9.500.000.000"):::trx
  N3 --> N2["Empresa El Mercurio SAP"]:::priv
  N4(["Manuel Contreras Sepulveda"]):::pers -. "autoriza" .-> N3
  N3 -. "suscribe" .-> N5(["Agustin Edwards Eastman"]):::pers
  N1["Agencia Central de Inteligencia CIA y Escuela de las Americas"]:::pub --> N7("TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01<br/>$14.800.000.000"):::trx
  N7 --> N6["Comando de Apoyo a la Fuerza del Ejercito"]:::priv
  N5(["Agustin Edwards Eastman"]):::pers -. "autoriza" .-> N7
  N7 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N1["Agencia Central de Inteligencia CIA y Escuela de las Americas"]:::pub --> N10("TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01<br/>$2.100.000.000"):::trx
  N10 --> N9["Corte Suprema de Chile"]:::priv
  N4(["Manuel Contreras Sepulveda"]):::pers -. "autoriza" .-> N10
  N10 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N12("TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01<br/>$18.500.000.000"):::trx
  N12 --> N9["Corte Suprema de Chile"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N12
  N12 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N16("TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01<br/>$2.950.000.000"):::trx
  N16 --> N15["Valmoval Ltda"]:::priv
  N8(["Augusto Pinochet Ugarte"]):::pers -. "autoriza" .-> N16
  N16 -. "suscribe" .-> N17(["Augusto Pinochet Hiriart"]):::pers
  N18["Sociedad Benefactora y Educacional Dignidad"]:::pub --> N20("TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01<br/>$3.450.000.000"):::trx
  N20 --> N19["Servicio Impuestos Internos"]:::priv
  N21(["Paul Schafer Schneider"]):::pers -. "autoriza" .-> N20
  N20 -. "suscribe" .-> N22(["Jorge Zepeda Arancibia"]):::pers
  N23["Union Democrata Independiente"]:::pub --> N24("TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01<br/>$240.000.000"):::trx
  N24 --> N18["Sociedad Benefactora y Educacional Dignidad"]:::priv
  N25(["Hernan Larrain Fernandez"]):::pers -. "autoriza" .-> N24
  N24 -. "suscribe" .-> N26(["Hartmut Hopp Miottel"]):::pers
  N27["Empresas CMPC SA"]:::pub --> N29("TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01<br/>$0"):::trx
  N29 --> N28["SCA Chile SA"]:::priv
  N30(["Eliodoro Matte Larrain"]):::pers -. "autoriza" .-> N29
  N29 -. "suscribe" .-> N31(["Gabriel Ruiz-Tagle Serrano"]):::pers
  N32["Ministerio de Obras Publicas"]:::pub --> N34("TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01<br/>$1.253.000.000"):::trx
  N34 --> N33["Gestion Ambiental y Territorial SA"]:::priv
  N35(["Carlos Cruz Lorenzen"]):::pers -. "autoriza" .-> N34
  N34 -. "suscribe" .-> N36(["Hector Pena Veliz"]):::pers
  N37["Inversiones El Bosque Ltda"]:::pub --> N38("TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01<br/>$480.000.000"):::trx
  N38 --> N19["Servicio Impuestos Internos"]:::priv
  N39(["Claudio Spiniak Vilensky"]):::pers -. "autoriza" .-> N38
  N38 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N40["Renovacion Nacional"]:::pub --> N41("TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01<br/>$120.000.000"):::trx
  N41 --> N9["Corte Suprema de Chile"]:::priv
  N42(["Pia Guzman Mena"]):::pers -. "autoriza" .-> N41
  N41 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N44("TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01<br/>$15.800.000.000"):::trx
  N44 --> N43["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N8(["Augusto Pinochet Ugarte"]):::pers -. "autoriza" .-> N44
  N44 -. "suscribe" .-> N45(["Oscar Aitken Lavanchy"]):::pers
  N18["Sociedad Benefactora y Educacional Dignidad"]:::pub --> N46("TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01<br/>$0"):::trx
  N46 --> N9["Corte Suprema de Chile"]:::priv
  N21(["Paul Schafer Schneider"]):::pers -. "autoriza" .-> N46
  N46 -. "suscribe" .-> N22(["Jorge Zepeda Arancibia"]):::pers
  N43["Riggs Bank y Sociedades Offshore Ashburton"]:::pub --> N47("TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01<br/>$2.450.000.000"):::trx
  N47 --> N19["Servicio Impuestos Internos"]:::priv
  N48(["Lucia Hiriart Rodriguez"]):::pers -. "autoriza" .-> N47
  N47 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N50("TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01<br/>$5.300.000.000"):::trx
  N50 --> N49["Comision para el Mercado Financiero"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N50
  N50 -. "suscribe" .-> N51(["Carlos Pavez Tolosa"]):::pers
  N52["Quiroz y Asociados Consultores SpA"]:::pub --> N54("TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01<br/>$0"):::trx
  N54 --> N53["Asociacion de Productores Avicolas de Chile AG"]:::priv
  N55(["Jorge Quiroz Castro"]):::pers -. "autoriza" .-> N54
  N54 -. "suscribe" .-> N56(["Juan Miguel Ovalle Garces"]):::pers
  N57["Farmacias Salcobrand SA"]:::pub --> N59("TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01<br/>$0"):::trx
  N59 --> N58["Farmacias Cruz Verde SA"]:::priv
  N60(["Roberto Belloni Pechini"]):::pers -. "autoriza" .-> N59
  N59 -. "suscribe" .-> N61(["Guillermo Harding Alvarado"]):::pers
  N62["Agrosuper SA"]:::pub --> N63("TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01<br/>$0"):::trx
  N63 --> N53["Asociacion de Productores Avicolas de Chile AG"]:::priv
  N64(["Gonzalo Vial Vial"]):::pers -. "autoriza" .-> N63
  N63 -. "suscribe" .-> N56(["Juan Miguel Ovalle Garces"]):::pers
  N65["SQM SA"]:::pub --> N66("TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01<br/>$340.000.000"):::trx
  N66 --> N11["Bancard Inversiones Ltda"]:::priv
  N67(["Patricio Contesse Gonzalez"]):::pers -. "autoriza" .-> N66
  N66 -. "suscribe" .-> N68(["Santiago Valdes Gutierrez"]):::pers
  N52["Quiroz y Asociados Consultores SpA"]:::pub --> N69("TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01<br/>$0"):::trx
  N69 --> N57["Farmacias Salcobrand SA"]:::priv
  N55(["Jorge Quiroz Castro"]):::pers -. "autoriza" .-> N69
  N69 -. "suscribe" .-> N60(["Roberto Belloni Pechini"]):::pers
  N65["SQM SA"]:::pub --> N70("TRX-2010-08-19-Correo-Royalty-SQM-01<br/>$730.000.000"):::trx
  N70 --> N23["Union Democrata Independiente"]:::priv
  N67(["Patricio Contesse Gonzalez"]):::pers -. "autoriza" .-> N70
  N70 -. "suscribe" .-> N71(["Pablo Longueira Montes"]):::pers
  N72["KDM Empresas SA"]:::pub --> N74("TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01<br/>$186.500.000"):::trx
  N74 --> N73["Municipalidad de Maipu"]:::priv
  N75(["Fernando Leon Steffens"]):::pers -. "autoriza" .-> N74
  N74 -. "suscribe" .-> N76(["Marcelo Torres Ferrari"]):::pers
  N77["Andes Iron SpA"]:::pub --> N78("TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01<br/>$75.500.000.000"):::trx
  N78 --> N11["Bancard Inversiones Ltda"]:::priv
  N79(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N78
  N78 -. "suscribe" .-> N13(["Sebastian Pinera Echenique"]):::pers
  N80["Empresas Penta SA"]:::pub --> N81("TRX-2011-03-10-Pagos-Penta-Wagner-01<br/>$42.000.000"):::trx
  N81 --> N19["Servicio Impuestos Internos"]:::priv
  N82(["Carlos Eugenio Lavin Garcia-Huidobro"]):::pers -. "autoriza" .-> N81
  N81 -. "suscribe" .-> N83(["Pablo Wagner San Martin"]):::pers
  N84["Sociedad de Inversiones Pampa Calichera SA"]:::pub --> N85("TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01<br/>$24.500.000.000"):::trx
  N85 --> N65["SQM SA"]:::priv
  N86(["Julio Ponce Lerou"]):::pers -. "autoriza" .-> N85
  N85 -. "suscribe" .-> N67(["Patricio Contesse Gonzalez"]):::pers
  N87["Municipalidad de Cerro Navia"]:::pub --> N88("TRX-2012-03-22-Fraude-Residuos-CerroNavia-01<br/>$1.120.000.000"):::trx
  N88 --> N72["KDM Empresas SA"]:::priv
  N89(["Luis Plaza Sanchez"]):::pers -. "autoriza" .-> N88
  N88 -. "suscribe" .-> N76(["Marcelo Torres Ferrari"]):::pers
  N90["Corpesca SA"]:::pub --> N92("TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01<br/>$233.000.000"):::trx
  N92 --> N91["Senado de la Republica de Chile"]:::priv
  N93(["Francisco Mujica Ortuzar"]):::pers -. "autoriza" .-> N92
  N92 -. "suscribe" .-> N94(["Jaime Orpis Bouchon"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N96("TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01<br/>$8.250.000.000"):::trx
  N96 --> N95["Contraloria General de la Republica"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N96
  N96 -. "suscribe" .-> N68(["Santiago Valdes Gutierrez"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N97("TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01<br/>$0"):::trx
  N97 --> N9["Corte Suprema de Chile"]:::priv
  N98(["Andres Velasco Branes"]):::pers -. "autoriza" .-> N97
  N97 -. "suscribe" .-> N98(["Andres Velasco Branes"]):::pers
  N80["Empresas Penta SA"]:::pub --> N99("TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01<br/>$1.260.000.000"):::trx
  N99 --> N23["Union Democrata Independiente"]:::priv
  N79(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N99
  N99 -. "suscribe" .-> N71(["Pablo Longueira Montes"]):::pers
  N80["Empresas Penta SA"]:::pub --> N100("TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01<br/>$156.000.000"):::trx
  N100 --> N23["Union Democrata Independiente"]:::priv
  N79(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N100
  N100 -. "suscribe" .-> N101(["Jovino Novoa Vasquez"]):::pers
  N102["Exportadora y de Gestion Caval Ltda"]:::pub --> N104("TRX-2014-02-18-Soborno-Caval-Machali-01<br/>$140.000.000"):::trx
  N104 --> N103["Municipalidad de Machali"]:::priv
  N105([""]):::pers -. "autoriza" .-> N104
  N104 -. "suscribe" .-> N106(["Jorge Silva Menares"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N108("TRX-2014-05-20-Facturas-LeyReservadaCobre-01<br/>$6.100.000.000"):::trx
  N108 --> N107["Frasim Ltda"]:::priv
  N109(["Juan Miguel Fuente-Alba Poblete"]):::pers -. "autoriza" .-> N108
  N108 -. "suscribe" .-> N110(["Jozo Santic Palomino"]):::pers
  N102["Exportadora y de Gestion Caval Ltda"]:::pub --> N111("TRX-2015-01-29-Facturas-Falsas-Caval-SII-01<br/>$2.500.000.000"):::trx
  N111 --> N19["Servicio Impuestos Internos"]:::priv
  N112(["Natalia Compagnon Soto"]):::pers -. "autoriza" .-> N111
  N111 -. "suscribe" .-> N112(["Natalia Compagnon Soto"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N113("TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01<br/>$0"):::trx
  N113 --> N9["Corte Suprema de Chile"]:::priv
  N114(["Eduardo Guendelman Israel"]):::pers -. "autoriza" .-> N113
  N113 -. "suscribe" .-> N114(["Eduardo Guendelman Israel"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N116("TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01<br/>$3.500.000.000"):::trx
  N116 --> N115["Unidad de Analisis Financiero"]:::priv
  N109(["Juan Miguel Fuente-Alba Poblete"]):::pers -. "autoriza" .-> N116
  N116 -. "suscribe" .-> N117(["Javier Cruz Tamburrino"]):::pers
  N62["Agrosuper SA"]:::pub --> N118("TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01<br/>$38.400.000.000"):::trx
  N118 --> N9["Corte Suprema de Chile"]:::priv
  N64(["Gonzalo Vial Vial"]):::pers -. "autoriza" .-> N118
  N118 -. "suscribe" .-> N119(["Manuel Ariztia Ruiz"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N120("TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01<br/>$0"):::trx
  N120 --> N9["Corte Suprema de Chile"]:::priv
  N121(["Andronico Luksic Craig"]):::pers -. "autoriza" .-> N120
  N120 -. "suscribe" .-> N121(["Andronico Luksic Craig"]):::pers
  N122["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N123("TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01<br/>$14.200.000.000"):::trx
  N123 --> N19["Servicio Impuestos Internos"]:::priv
  N124(["Gonzalo Delaveau Swett"]):::pers -. "autoriza" .-> N123
  N123 -. "suscribe" .-> N51(["Carlos Pavez Tolosa"]):::pers
  N122["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N125("TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01<br/>$19.500.000.000"):::trx
  N125 --> N115["Unidad de Analisis Financiero"]:::priv
  N5(["Agustin Edwards Eastman"]):::pers -. "autoriza" .-> N125
  N125 -. "suscribe" .-> N126(["Alfredo Ovalle Rodriguez"]):::pers
  N122["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N127("TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01<br/>$3.800.000.000"):::trx
  N127 --> N43["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N45(["Oscar Aitken Lavanchy"]):::pers -. "autoriza" .-> N127
  N127 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N128["Fundacion CEMA Chile"]:::pub --> N129("TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01<br/>$10.500.000.000"):::trx
  N129 --> N9["Corte Suprema de Chile"]:::priv
  N48(["Lucia Hiriart Rodriguez"]):::pers -. "autoriza" .-> N129
  N129 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N130["Direccion de Finanzas de Carabineros"]:::pub --> N131("TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01<br/>$28.348.928.198"):::trx
  N131 --> N130["Direccion de Finanzas de Carabineros"]:::priv
  N132(["Flavio Echeverria Cortez"]):::pers -. "autoriza" .-> N131
  N131 -. "suscribe" .-> N133(["Jaime Paz Meneses"]):::pers
  N27["Empresas CMPC SA"]:::pub --> N135("TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01<br/>$97.500.000.000"):::trx
  N135 --> N134["Servicio Nacional del Consumidor"]:::priv
  N30(["Eliodoro Matte Larrain"]):::pers -. "autoriza" .-> N135
  N135 -. "suscribe" .-> N31(["Gabriel Ruiz-Tagle Serrano"]):::pers
  N130["Direccion de Finanzas de Carabineros"]:::pub --> N136("TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01<br/>$1.450.000.000"):::trx
  N136 --> N115["Unidad de Analisis Financiero"]:::priv
  N132(["Flavio Echeverria Cortez"]):::pers -. "autoriza" .-> N136
  N136 -. "suscribe" .-> N117(["Javier Cruz Tamburrino"]):::pers
  N137["Direccion de Inteligencia Policial de Carabineros"]:::pub --> N138("TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01<br/>$0"):::trx
  N138 --> N9["Corte Suprema de Chile"]:::priv
  N139(["Gonzalo Blu Rodriguez"]):::pers -. "autoriza" .-> N138
  N138 -. "suscribe" .-> N140(["Alex Smith Leay"]):::pers
  N137["Direccion de Inteligencia Policial de Carabineros"]:::pub --> N141("TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01<br/>$25.000.000"):::trx
  N141 --> N137["Direccion de Inteligencia Policial de Carabineros"]:::priv
  N142(["Patricio Marin Lazo"]):::pers -. "autoriza" .-> N141
  N141 -. "suscribe" .-> N140(["Alex Smith Leay"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N143("TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01<br/>$0"):::trx
  N143 --> N137["Direccion de Inteligencia Policial de Carabineros"]:::priv
  N144(["Leonardo Osses Sandoval"]):::pers -. "autoriza" .-> N143
  N143 -. "suscribe" .-> N140(["Alex Smith Leay"]):::pers
  N145["Itelecom Holding Chile SpA"]:::pub --> N147("TRX-2019-05-14-Soborno-Luminarias-Chillan-01<br/>$37.000.000"):::trx
  N147 --> N146["Municipalidad de Chillan"]:::priv
  N148(["Leon Marcelo Lefort Hernandez"]):::pers -. "autoriza" .-> N147
  N147 -. "suscribe" .-> N149(["Marcelo Campos Henriquez"]):::pers
  N150["Factop SpA"]:::pub --> N151("TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01<br/>$190.000.000"):::trx
  N151 --> N91["Senado de la Republica de Chile"]:::priv
  N152(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N151
  N151 -. "suscribe" .-> N153(["Andres Chadwick Pinera"]):::pers
  N57["Farmacias Salcobrand SA"]:::pub --> N154("TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01<br/>$2.180.000.000"):::trx
  N154 --> N134["Servicio Nacional del Consumidor"]:::priv
  N60(["Roberto Belloni Pechini"]):::pers -. "autoriza" .-> N154
  N154 -. "suscribe" .-> N155(["Jose Codner Chijner"]):::pers
  N73["Municipalidad de Maipu"]:::pub --> N156("TRX-2020-12-15-Deficit-Maipu-Certificados-01<br/>$30.972.000.000"):::trx
  N156 --> N73["Municipalidad de Maipu"]:::priv
  N157(["Cathy Barriga Guerra"]):::pers -. "autoriza" .-> N156
  N156 -. "suscribe" .-> N157(["Cathy Barriga Guerra"]):::pers
  N158["Municipalidad de Vitacura"]:::pub --> N160("TRX-2021-04-15-Subvencion-VitaDeportes-01<br/>$759.000.000"):::trx
  N160 --> N159["Vita Deportes"]:::priv
  N161(["Raul Torrealba del Pedregal"]):::pers -. "autoriza" .-> N160
  N160 -. "suscribe" .-> N162(["Domingo Prieto Urrejola"]):::pers
  N163["Numen Publicidad SpA"]:::pub --> N164("TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01<br/>$0"):::trx
  N164 --> N40["Renovacion Nacional"]:::priv
  N165(["Fernando Cerimedo"]):::pers -. "autoriza" .-> N164
  N164 -. "suscribe" .-> N40(["Renovacion Nacional"]):::pers
  N166["Fundacion ProCultura"]:::pub --> N168("TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01<br/>$0"):::trx
  N168 --> N167["GORE Biobio"]:::priv
  N169(["Alberto Larrain Salas"]):::pers -. "autoriza" .-> N168
  N168 -. "suscribe" .-> N170(["Rodrigo Diaz Worner"]):::pers
  N171["Seremi MINVU Antofagasta"]:::pub --> N173("TRX-2022-10-03-Convenio-DV-01<br/>$200.000.000"):::trx
  N173 --> N172["Fundacion Democracia Viva"]:::priv
  N174(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N173
  N173 -. "suscribe" .-> N175(["Daniel Andrade Schwarze"]):::pers
  N171["Seremi MINVU Antofagasta"]:::pub --> N176("TRX-2022-10-19-Convenio-DV-02<br/>$170.000.000"):::trx
  N176 --> N172["Fundacion Democracia Viva"]:::priv
  N174(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N176
  N176 -. "suscribe" .-> N175(["Daniel Andrade Schwarze"]):::pers
  N171["Seremi MINVU Antofagasta"]:::pub --> N177("TRX-2022-10-28-Convenio-ProCultura-Antofagasta<br/>$500.000.000"):::trx
  N177 --> N166["Fundacion ProCultura"]:::priv
  N174(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N177
  N177 -. "suscribe" .-> N169(["Alberto Larrain Salas"]):::pers
  N150["Factop SpA"]:::pub --> N178("TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01<br/>$0"):::trx
  N178 --> N9["Corte Suprema de Chile"]:::priv
  N152(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N178
  N178 -. "suscribe" .-> N179(["Gabriel Zaliasnik Schilkrut"]):::pers
  N167["GORE Biobio"]:::pub --> N180("TRX-2022-11-18-Convenio-ProCultura-Biobio<br/>$2.553.000.000"):::trx
  N180 --> N166["Fundacion ProCultura"]:::priv
  N170(["Rodrigo Diaz Worner"]):::pers -. "autoriza" .-> N180
  N180 -. "suscribe" .-> N169(["Alberto Larrain Salas"]):::pers
  N171["Seremi MINVU Antofagasta"]:::pub --> N181("TRX-2022-11-29-Convenio-DV-03<br/>$56.000.000"):::trx
  N181 --> N172["Fundacion Democracia Viva"]:::priv
  N174(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N181
  N181 -. "suscribe" .-> N175(["Daniel Andrade Schwarze"]):::pers
  N167["GORE Biobio"]:::pub --> N183("TRX-2022-12-20-Convenio-EnTi-01<br/>$250.635.000"):::trx
  N183 --> N182["Fundacion En Ti"]:::priv
  N170(["Rodrigo Diaz Worner"]):::pers -. "autoriza" .-> N183
  N183 -. "suscribe" .-> N184(["Camila Polizzi Fonceca"]):::pers
  N185["Municipalidad de Santiago"]:::pub --> N187("TRX-2023-01-20-Compraventa-Clinica-SierraBella-01<br/>$0"):::trx
  N187 --> N186["Inmobiliaria San Valentino SpA"]:::priv
  N188(["Iraci Hassler Jacob"]):::pers -. "autoriza" .-> N187
  N187 -. "suscribe" .-> N189(["Felipe Sanchez Perez"]):::pers
  N150["Factop SpA"]:::pub --> N190("TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01<br/>$0"):::trx
  N190 --> N9["Corte Suprema de Chile"]:::priv
  N152(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N190
  N190 -. "suscribe" .-> N191(["Angela Vivanco Martinez"]):::pers
  N166["Fundacion ProCultura"]:::pub --> N192("TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01<br/>$315.000.000"):::trx
  N192 --> N19["Servicio Impuestos Internos"]:::priv
  N169(["Alberto Larrain Salas"]):::pers -. "autoriza" .-> N192
  N192 -. "suscribe" .-> N193(["Leonarda Villalobos Muth"]):::pers
  N150["Factop SpA"]:::pub --> N194("TRX-2023-06-22-Reunion-Audios-01<br/>$100.000.000"):::trx
  N194 --> N19["Servicio Impuestos Internos"]:::priv
  N152(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N194
  N194 -. "suscribe" .-> N193(["Leonarda Villalobos Muth"]):::pers
  N95["Contraloria General de la Republica"]:::pub --> N195("TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01<br/>$0"):::trx
  N195 --> N171["Seremi MINVU Antofagasta"]:::priv
  N196(["Jorge Bermudez Soto"]):::pers -. "autoriza" .-> N195
  N195 -. "suscribe" .-> N174(["Carlos Contreras Gutierrez"]):::pers
  N150["Factop SpA"]:::pub --> N197("TRX-2023-08-25-Reporte-ROS-Factop-UAF-01<br/>$480.000.000"):::trx
  N197 --> N115["Unidad de Analisis Financiero"]:::priv
  N152(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N197
  N197 -. "suscribe" .-> N117(["Javier Cruz Tamburrino"]):::pers
  N105[""]:::pub --> N198("TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01<br/>$240.000.000.000"):::trx
  N198 --> N19["Servicio Impuestos Internos"]:::priv
  N105([""]):::pers -. "autoriza" .-> N198
  N198 -. "suscribe" .-> N105([""]):::pers
  N91["Senado de la Republica de Chile"]:::pub --> N200("TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01<br/>$35.000.000"):::trx
  N200 --> N199["Camila Flores Oporto"]:::priv
  N91(["Senado de la Republica de Chile"]):::pers -. "autoriza" .-> N200
  N200 -. "suscribe" .-> N199(["Camila Flores Oporto"]):::pers
```

---

## 2. Detección de Fraccionamiento Administrativo (Umbral Toma de Razón: 5.000 UTM)

| Órgano Público | Entidad Receptora | N° Cuotas | Suma Acumulada (CLP) | Suma en UTM | Aristas Fraccionadas |
| :--- | :--- | :---: | ---: | ---: | :--- |
| [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | 3 | **$426.000.000** | **7055.3 UTM** | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |

---

## 3. Índice de Concentración de Herfindahl-Hirschman (`HHI`) por Entidad Emisora

| Entidad Emisora | N° Receptores | Monto Total Emitido (CLP) | Índice HHI (0–10.000) | Diagnóstico de Concentración |
| :--- | :---: | ---: | ---: | :--- |
| [[]] | 1 | $240.000.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Empresas CMPC SA]] | 1 | $97.500.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Andes Iron SpA]] | 1 | $75.500.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Agrosuper SA]] | 1 | $38.400.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Mossack Fonseca y Sociedades Offshore Panama]] | 3 | $37.500.000.000 | **4241** | Alta Concentración / Captura (> 2.500) |
| [[Bancard Inversiones Ltda]] | 3 | $32.050.000.000 | **4268** | Alta Concentración / Captura (> 2.500) |
| [[Municipalidad de Maipu]] | 1 | $30.972.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Direccion de Finanzas de Carabineros]] | 2 | $29.798.928.198 | **9074** | Alta Concentración / Captura (> 2.500) |
| [[Comando de Apoyo a la Fuerza del Ejercito]] | 4 | $28.350.000.000 | **3830** | Alta Concentración / Captura (> 2.500) |
| [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | 3 | $26.400.000.000 | **4501** | Alta Concentración / Captura (> 2.500) |
| [[Sociedad de Inversiones Pampa Calichera SA]] | 1 | $24.500.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Fundacion CEMA Chile]] | 1 | $10.500.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Sociedad Benefactora y Educacional Dignidad]] | 1 | $3.450.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[GORE Biobio]] | 2 | $2.803.635.000 | **8372** | Alta Concentración / Captura (> 2.500) |
| [[Exportadora y de Gestion Caval Ltda]] | 2 | $2.640.000.000 | **8996** | Alta Concentración / Captura (> 2.500) |
| [[Riggs Bank y Sociedades Offshore Ashburton]] | 1 | $2.450.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Farmacias Salcobrand SA]] | 1 | $2.180.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Empresas Penta SA]] | 2 | $1.458.000.000 | **9440** | Alta Concentración / Captura (> 2.500) |
| [[Ministerio de Obras Publicas]] | 1 | $1.253.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Municipalidad de Cerro Navia]] | 1 | $1.120.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[SQM SA]] | 2 | $1.070.000.000 | **5664** | Alta Concentración / Captura (> 2.500) |
| [[Seremi MINVU Antofagasta]] | 2 | $926.000.000 | **5032** | Alta Concentración / Captura (> 2.500) |
| [[Factop SpA]] | 3 | $770.000.000 | **4664** | Alta Concentración / Captura (> 2.500) |
| [[Municipalidad de Vitacura]] | 1 | $759.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Inversiones El Bosque Ltda]] | 1 | $480.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Fundacion ProCultura]] | 1 | $315.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Union Democrata Independiente]] | 1 | $240.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Corpesca SA]] | 1 | $233.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[KDM Empresas SA]] | 1 | $186.500.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Renovacion Nacional]] | 1 | $120.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Itelecom Holding Chile SpA]] | 1 | $37.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Senado de la Republica de Chile]] | 1 | $35.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Direccion de Inteligencia Policial de Carabineros]] | 1 | $25.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |

---

## 4. Ranking de Nodos Puente (*Betweenness Centrality* & *PageRank Forense*)

| Posición | Nodo / Entidad | Tipo de Nodo | Intermediación (Brandes) | PageRank Forense | Rol Topológico |
| :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | [[Corte Suprema de Chile]] | `entidad_publica` | `0.4042` | `0.0283` | Conector Interregional / Puente Crítico |
| 2 | [[Servicio Impuestos Internos]] | `entidad_publica` | `0.2393` | `0.0177` | Conector Interregional / Puente Crítico |
| 3 | [[Augusto Pinochet Ugarte]] | `persona` | `0.0964` | `0.0089` | Conector Interregional / Puente Crítico |
| 4 | [[Sergio Munoz Gajardo]] | `persona` | `0.0868` | `0.0083` | Conector Interregional / Puente Crítico |
| 5 | [[Bancard Inversiones Ltda]] | `entidad_privada` | `0.0847` | `0.0081` | Conector Interregional / Puente Crítico |
| 6 | [[Agrosuper SA]] | `entidad_privada` | `0.0786` | `0.0044` | Conector Interregional / Puente Crítico |
| 7 | [[Gonzalo Vial Vial]] | `persona` | `0.0786` | `0.0044` | Conector Interregional / Puente Crítico |
| 8 | [[Asociacion de Productores Avicolas de Chile AG]] | `entidad_privada` | `0.0688` | `0.0045` | Conector Interregional / Puente Crítico |
| 9 | [[Juan Miguel Ovalle Garces]] | `persona` | `0.0688` | `0.0045` | Conector Interregional / Puente Crítico |
| 10 | [[Factop SpA]] | `entidad_privada` | `0.0607` | `0.0072` | Conector Interregional / Puente Crítico |

---

## 5. Desglose de Aristas Reificadas en Pesos Chilenos (CLP) y UTM

| Nexo (`TRX`) | Fecha | Tipo | Origen | Destino | Monto (CLP) | Equivalencia (UTM) | Toma de Razón Individual |
| :--- | :---: | :---: | :--- | :--- | ---: | ---: | :---: |
| [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]] | 1971-09-09 | `desviacion_fondos` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Empresa El Mercurio SAP]] | $9.500.000.000 | 156113.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]] | 1972-10-12 | `gestion_influencia` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | $14.800.000.000 | 243209.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | 1975-08-15 | `desviacion_fondos` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Corte Suprema de Chile]] | $2.100.000.000 | 34509.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | 1982-08-28 | `desviacion_fondos` | [[Bancard Inversiones Ltda]] | [[Corte Suprema de Chile]] | $18.500.000.000 | 304011.3 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | 1989-01-10 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Valmoval Ltda]] | $2.950.000.000 | 48477.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]] | 1991-01-31 | `desviacion_fondos` | [[Sociedad Benefactora y Educacional Dignidad]] | [[Servicio Impuestos Internos]] | $3.450.000.000 | 56694.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | 1996-06-12 | `gestion_influencia` | [[Union Democrata Independiente]] | [[Sociedad Benefactora y Educacional Dignidad]] | $240.000.000 | 3943.9 UTM | Exento (< 5.000 UTM) |
| [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]] | 2000-05-15 | `acuerdo_colusorio` | [[Empresas CMPC SA]] | [[SCA Chile SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]] | 2001-08-20 | `trato_directo` | [[Ministerio de Obras Publicas]] | [[Gestion Ambiental y Territorial SA]] | $1.253.000.000 | 20590.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]] | 2003-10-15 | `desviacion_fondos` | [[Inversiones El Bosque Ltda]] | [[Servicio Impuestos Internos]] | $480.000.000 | 7887.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | 2003-11-05 | `gestion_influencia` | [[Renovacion Nacional]] | [[Corte Suprema de Chile]] | $120.000.000 | 1972.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]] | 2004-07-14 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | $15.800.000.000 | 259642.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | 2005-06-14 | `desviacion_fondos` | [[Sociedad Benefactora y Educacional Dignidad]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | 2005-08-10 | `desviacion_fondos` | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[Servicio Impuestos Internos]] | $2.450.000.000 | 40261.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | 2006-07-24 | `gestion_influencia` | [[Bancard Inversiones Ltda]] | [[Comision para el Mercado Financiero]] | $5.300.000.000 | 87095.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]] | 2007-04-10 | `consulta_terceros` | [[Quiroz y Asociados Consultores SpA]] | [[Asociacion de Productores Avicolas de Chile AG]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]] | 2007-11-01 | `acuerdo_colusorio` | [[Farmacias Salcobrand SA]] | [[Farmacias Cruz Verde SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]] | 2008-01-15 | `acuerdo_colusorio` | [[Agrosuper SA]] | [[Asociacion de Productores Avicolas de Chile AG]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | 2009-11-18 | `factura_falsa` | [[SQM SA]] | [[Bancard Inversiones Ltda]] | $340.000.000 | 5587.2 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]] | 2010-06-15 | `peritaje_forense` | [[Quiroz y Asociados Consultores SpA]] | [[Farmacias Salcobrand SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | 2010-08-19 | `cohecho` | [[SQM SA]] | [[Union Democrata Independiente]] | $730.000.000 | 19588.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]] | 2010-11-15 | `cohecho_soborno` | [[KDM Empresas SA]] | [[Municipalidad de Maipu]] | $186.500.000 | 3064.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | 2010-12-10 | `trato_directo` | [[Andes Iron SpA]] | [[Bancard Inversiones Ltda]] | $75.500.000.000 | 1240694.8 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | 2011-03-10 | `transferencia` | [[Empresas Penta SA]] | [[Servicio Impuestos Internos]] | $42.000.000 | 690.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | 2011-12-19 | `desviacion_fondos` | [[Sociedad de Inversiones Pampa Calichera SA]] | [[SQM SA]] | $24.500.000.000 | 402609.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]] | 2012-03-22 | `trato_directo` | [[Municipalidad de Cerro Navia]] | [[KDM Empresas SA]] | $1.120.000.000 | 18405.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]] | 2012-07-11 | `cohecho` | [[Corpesca SA]] | [[Senado de la Republica de Chile]] | $233.000.000 | 3828.9 UTM | Exento (< 5.000 UTM) |
| [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | 2012-11-20 | `gestion_influencia` | [[Bancard Inversiones Ltda]] | [[Contraloria General de la Republica]] | $8.250.000.000 | 135572.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]] | 2013-05-20 | `correo_electronico` | [[Corte Suprema de Chile]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | 2013-07-15 | `factura_falsa` | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | $1.260.000.000 | 20705.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | 2013-09-20 | `factura_falsa` | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | $156.000.000 | 2563.6 UTM | Exento (< 5.000 UTM) |
| [[TRX-2014-02-18-Soborno-Caval-Machali-01]] | 2014-02-18 | `cohecho_soborno` | [[Exportadora y de Gestion Caval Ltda]] | [[Municipalidad de Machali]] | $140.000.000 | 2300.6 UTM | Exento (< 5.000 UTM) |
| [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]] | 2014-05-20 | `transferencia` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Frasim Ltda]] | $6.100.000.000 | 100241.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]] | 2015-01-29 | `factura_falsa` | [[Exportadora y de Gestion Caval Ltda]] | [[Servicio Impuestos Internos]] | $2.500.000.000 | 41082.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]] | 2015-08-10 | `solicitud_patrocinio` | [[Corte Suprema de Chile]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]] | 2015-08-14 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Unidad de Analisis Financiero]] | $3.500.000.000 | 57515.7 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]] | 2015-10-29 | `compensacion_reparatoria` | [[Agrosuper SA]] | [[Corte Suprema de Chile]] | $38.400.000.000 | 631028.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]] | 2015-11-14 | `consulta_terceros` | [[Corte Suprema de Chile]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | 2016-04-03 | `gestion_influencia` | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Servicio Impuestos Internos]] | $14.200.000.000 | 233349.2 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | 2016-04-05 | `desviacion_fondos` | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Unidad de Analisis Financiero]] | $19.500.000.000 | 320444.3 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | 2016-04-15 | `desviacion_fondos` | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | $3.800.000.000 | 62445.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | 2016-08-12 | `desviacion_fondos` | [[Fundacion CEMA Chile]] | [[Corte Suprema de Chile]] | $10.500.000.000 | 172547.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]] | 2016-11-10 | `transferencia` | [[Direccion de Finanzas de Carabineros]] | [[Direccion de Finanzas de Carabineros]] | $28.348.928.198 | 615064.3 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] | 2017-03-03 | `compensacion_reparatoria` | [[Empresas CMPC SA]] | [[Servicio Nacional del Consumidor]] | $97.500.000.000 | 1602221.7 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]] | 2017-03-06 | `desviacion_fondos` | [[Direccion de Finanzas de Carabineros]] | [[Unidad de Analisis Financiero]] | $1.450.000.000 | 23827.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]] | 2017-09-23 | `montaje_policial` | [[Direccion de Inteligencia Policial de Carabineros]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]] | 2017-10-15 | `desvio_fondos_reservados` | [[Direccion de Inteligencia Policial de Carabineros]] | [[Direccion de Inteligencia Policial de Carabineros]] | $25.000.000 | 410.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] | 2018-01-25 | `peritaje_forense` | [[Corte Suprema de Chile]] | [[Direccion de Inteligencia Policial de Carabineros]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]] | 2019-05-14 | `cohecho` | [[Itelecom Holding Chile SpA]] | [[Municipalidad de Chillan]] | $37.000.000 | 608.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | 2019-12-11 | `transferencia` | [[Factop SpA]] | [[Senado de la Republica de Chile]] | $190.000.000 | 3122.3 UTM | Exento (< 5.000 UTM) |
| [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]] | 2020-11-25 | `compensacion_reparatoria` | [[Farmacias Salcobrand SA]] | [[Servicio Nacional del Consumidor]] | $2.180.000.000 | 35824.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]] | 2020-12-15 | `transferencia` | [[Municipalidad de Maipu]] | [[Municipalidad de Maipu]] | $30.972.000.000 | 606949.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2021-04-15-Subvencion-VitaDeportes-01]] | 2021-04-15 | `transferencia` | [[Municipalidad de Vitacura]] | [[Vita Deportes]] | $759.000.000 | 14711.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]] | 2022-09-04 | `reunion_lobby` | [[Numen Publicidad SpA]] | [[Renovacion Nacional]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01]] | 2022-09-12 | `reunion_lobby` | [[Fundacion ProCultura]] | [[GORE Biobio]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-10-03-Convenio-DV-01]] | 2022-10-03 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | $200.000.000 | 3316.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-10-19-Convenio-DV-02]] | 2022-10-19 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | $170.000.000 | 2818.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | 2022-10-28 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion ProCultura]] | $500.000.000 | 8290.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | 2022-11-15 | `coordinacion_mensajeria` | [[Factop SpA]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | 2022-11-18 | `convenio_directo` | [[GORE Biobio]] | [[Fundacion ProCultura]] | $2.553.000.000 | 41953.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2022-11-29-Convenio-DV-03]] | 2022-11-29 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | $56.000.000 | 920.3 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-12-20-Convenio-EnTi-01]] | 2022-12-20 | `convenio_directo` | [[GORE Biobio]] | [[Fundacion En Ti]] | $250.635.000 | 4098.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]] | 2023-01-20 | `trato_directo` | [[Municipalidad de Santiago]] | [[Inmobiliaria San Valentino SpA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | 2023-02-09 | `llamada` | [[Factop SpA]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | 2023-05-10 | `factura_falsa` | [[Fundacion ProCultura]] | [[Servicio Impuestos Internos]] | $315.000.000 | 5176.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2023-06-22-Reunion-Audios-01]] | 2023-06-22 | `cohecho` | [[Factop SpA]] | [[Servicio Impuestos Internos]] | $100.000.000 | 1580.7 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | 2023-06-29 | `resolucion_administrativa` | [[Contraloria General de la Republica]] | [[Seremi MINVU Antofagasta]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | 2023-08-25 | `factura_falsa` | [[Factop SpA]] | [[Unidad de Analisis Financiero]] | $480.000.000 | 7887.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01]] | 2023-12-14 | `factura_falsa` | [[]] | [[Servicio Impuestos Internos]] | $240.000.000.000 | 3943930.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]] | 2025-10-15 | `desviacion_fondos` | [[Senado de la Republica de Chile]] | [[Camila Flores Oporto]] | $35.000.000 | 575.2 UTM | Exento (< 5.000 UTM) |
