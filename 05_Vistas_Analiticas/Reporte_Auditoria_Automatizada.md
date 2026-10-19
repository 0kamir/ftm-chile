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

- **Monto Global Investigado**: **$725.998.563.198 CLP** (Equivalente a **12.187.433.0 UTM**)
- **Total de Aristas Reificadas (`TRX`)**: **71**
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
  N33["Gestion Ambiental y Territorial SA"]:::pub --> N37("TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01<br/>$450.000.000"):::trx
  N37 --> N19["Servicio Impuestos Internos"]:::priv
  N36(["Hector Pena Veliz"]):::pers -. "autoriza" .-> N37
  N37 -. "suscribe" .-> N35(["Carlos Cruz Lorenzen"]):::pers
  N38["Inversiones El Bosque Ltda"]:::pub --> N39("TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01<br/>$480.000.000"):::trx
  N39 --> N19["Servicio Impuestos Internos"]:::priv
  N40(["Claudio Spiniak Vilensky"]):::pers -. "autoriza" .-> N39
  N39 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N41["Renovacion Nacional"]:::pub --> N42("TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01<br/>$120.000.000"):::trx
  N42 --> N9["Corte Suprema de Chile"]:::priv
  N43(["Pia Guzman Mena"]):::pers -. "autoriza" .-> N42
  N42 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N45("TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01<br/>$15.800.000.000"):::trx
  N45 --> N44["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N8(["Augusto Pinochet Ugarte"]):::pers -. "autoriza" .-> N45
  N45 -. "suscribe" .-> N46(["Oscar Aitken Lavanchy"]):::pers
  N18["Sociedad Benefactora y Educacional Dignidad"]:::pub --> N47("TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01<br/>$1.850.000.000"):::trx
  N47 --> N9["Corte Suprema de Chile"]:::priv
  N21(["Paul Schafer Schneider"]):::pers -. "autoriza" .-> N47
  N47 -. "suscribe" .-> N22(["Jorge Zepeda Arancibia"]):::pers
  N44["Riggs Bank y Sociedades Offshore Ashburton"]:::pub --> N48("TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01<br/>$2.450.000.000"):::trx
  N48 --> N19["Servicio Impuestos Internos"]:::priv
  N49(["Lucia Hiriart Rodriguez"]):::pers -. "autoriza" .-> N48
  N48 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N51("TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01<br/>$5.300.000.000"):::trx
  N51 --> N50["Comision para el Mercado Financiero"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N51
  N51 -. "suscribe" .-> N52(["Carlos Pavez Tolosa"]):::pers
  N53["Quiroz y Asociados Consultores SpA"]:::pub --> N55("TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01<br/>$0"):::trx
  N55 --> N54["Asociacion de Productores Avicolas de Chile AG"]:::priv
  N56(["Jorge Quiroz Castro"]):::pers -. "autoriza" .-> N55
  N55 -. "suscribe" .-> N57(["Juan Miguel Ovalle Garces"]):::pers
  N58["Farmacias Salcobrand SA"]:::pub --> N60("TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01<br/>$0"):::trx
  N60 --> N59["Farmacias Cruz Verde SA"]:::priv
  N61(["Roberto Belloni Pechini"]):::pers -. "autoriza" .-> N60
  N60 -. "suscribe" .-> N62(["Guillermo Harding Alvarado"]):::pers
  N63["Agrosuper SA"]:::pub --> N64("TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01<br/>$0"):::trx
  N64 --> N54["Asociacion de Productores Avicolas de Chile AG"]:::priv
  N65(["Gonzalo Vial Vial"]):::pers -. "autoriza" .-> N64
  N64 -. "suscribe" .-> N57(["Juan Miguel Ovalle Garces"]):::pers
  N66["SQM SA"]:::pub --> N67("TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01<br/>$340.000.000"):::trx
  N67 --> N11["Bancard Inversiones Ltda"]:::priv
  N68(["Patricio Contesse Gonzalez"]):::pers -. "autoriza" .-> N67
  N67 -. "suscribe" .-> N69(["Santiago Valdes Gutierrez"]):::pers
  N53["Quiroz y Asociados Consultores SpA"]:::pub --> N70("TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01<br/>$0"):::trx
  N70 --> N58["Farmacias Salcobrand SA"]:::priv
  N56(["Jorge Quiroz Castro"]):::pers -. "autoriza" .-> N70
  N70 -. "suscribe" .-> N61(["Roberto Belloni Pechini"]):::pers
  N66["SQM SA"]:::pub --> N71("TRX-2010-08-19-Correo-Royalty-SQM-01<br/>$730.000.000"):::trx
  N71 --> N23["Union Democrata Independiente"]:::priv
  N68(["Patricio Contesse Gonzalez"]):::pers -. "autoriza" .-> N71
  N71 -. "suscribe" .-> N72(["Pablo Longueira Montes"]):::pers
  N73["KDM Empresas SA"]:::pub --> N75("TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01<br/>$18.500.000.000"):::trx
  N75 --> N74["Municipalidad de Maipu"]:::priv
  N76(["Fernando Leon Steffens"]):::pers -. "autoriza" .-> N75
  N75 -. "suscribe" .-> N77(["Marcelo Torres Ferrari"]):::pers
  N78["Andes Iron SpA"]:::pub --> N79("TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01<br/>$75.500.000.000"):::trx
  N79 --> N11["Bancard Inversiones Ltda"]:::priv
  N80(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N79
  N79 -. "suscribe" .-> N13(["Sebastian Pinera Echenique"]):::pers
  N81["Empresas Penta SA"]:::pub --> N82("TRX-2011-03-10-Pagos-Penta-Wagner-01<br/>$42.000.000"):::trx
  N82 --> N19["Servicio Impuestos Internos"]:::priv
  N83(["Carlos Eugenio Lavin Garcia-Huidobro"]):::pers -. "autoriza" .-> N82
  N82 -. "suscribe" .-> N84(["Pablo Wagner San Martin"]):::pers
  N85["Sociedad de Inversiones Pampa Calichera SA"]:::pub --> N86("TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01<br/>$24.500.000.000"):::trx
  N86 --> N66["SQM SA"]:::priv
  N87(["Julio Ponce Lerou"]):::pers -. "autoriza" .-> N86
  N86 -. "suscribe" .-> N68(["Patricio Contesse Gonzalez"]):::pers
  N88["Municipalidad de Cerro Navia"]:::pub --> N89("TRX-2012-03-22-Fraude-Residuos-CerroNavia-01<br/>$1.120.000.000"):::trx
  N89 --> N73["KDM Empresas SA"]:::priv
  N90(["Luis Plaza Sanchez"]):::pers -. "autoriza" .-> N89
  N89 -. "suscribe" .-> N77(["Marcelo Torres Ferrari"]):::pers
  N91["Corpesca SA"]:::pub --> N93("TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01<br/>$233.000.000"):::trx
  N93 --> N92["Senado de la Republica de Chile"]:::priv
  N94(["Francisco Mujica Ortuzar"]):::pers -. "autoriza" .-> N93
  N93 -. "suscribe" .-> N95(["Jaime Orpis Bouchon"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N97("TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01<br/>$8.250.000.000"):::trx
  N97 --> N96["Contraloria General de la Republica"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N97
  N97 -. "suscribe" .-> N69(["Santiago Valdes Gutierrez"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N98("TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01<br/>$0"):::trx
  N98 --> N9["Corte Suprema de Chile"]:::priv
  N99(["Andres Velasco Branes"]):::pers -. "autoriza" .-> N98
  N98 -. "suscribe" .-> N99(["Andres Velasco Branes"]):::pers
  N81["Empresas Penta SA"]:::pub --> N100("TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01<br/>$1.260.000.000"):::trx
  N100 --> N23["Union Democrata Independiente"]:::priv
  N80(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N100
  N100 -. "suscribe" .-> N72(["Pablo Longueira Montes"]):::pers
  N81["Empresas Penta SA"]:::pub --> N101("TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01<br/>$156.000.000"):::trx
  N101 --> N23["Union Democrata Independiente"]:::priv
  N80(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N101
  N101 -. "suscribe" .-> N102(["Jovino Novoa Vasquez"]):::pers
  N103["Exportadora y de Gestion Caval Ltda"]:::pub --> N105("TRX-2014-02-18-Soborno-Caval-Machali-01<br/>$140.000.000"):::trx
  N105 --> N104["Municipalidad de Machali"]:::priv
  N106([""]):::pers -. "autoriza" .-> N105
  N105 -. "suscribe" .-> N107(["Jorge Silva Menares"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N109("TRX-2014-05-20-Facturas-LeyReservadaCobre-01<br/>$6.100.000.000"):::trx
  N109 --> N108["Frasim Ltda"]:::priv
  N110(["Juan Miguel Fuente-Alba Poblete"]):::pers -. "autoriza" .-> N109
  N109 -. "suscribe" .-> N111(["Jozo Santic Palomino"]):::pers
  N103["Exportadora y de Gestion Caval Ltda"]:::pub --> N112("TRX-2015-01-29-Facturas-Falsas-Caval-SII-01<br/>$2.500.000.000"):::trx
  N112 --> N19["Servicio Impuestos Internos"]:::priv
  N113(["Natalia Compagnon Soto"]):::pers -. "autoriza" .-> N112
  N112 -. "suscribe" .-> N113(["Natalia Compagnon Soto"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N114("TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01<br/>$0"):::trx
  N114 --> N9["Corte Suprema de Chile"]:::priv
  N115(["Eduardo Guendelman Israel"]):::pers -. "autoriza" .-> N114
  N114 -. "suscribe" .-> N115(["Eduardo Guendelman Israel"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N117("TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01<br/>$3.500.000.000"):::trx
  N117 --> N116["Unidad de Analisis Financiero"]:::priv
  N110(["Juan Miguel Fuente-Alba Poblete"]):::pers -. "autoriza" .-> N117
  N117 -. "suscribe" .-> N118(["Javier Cruz Tamburrino"]):::pers
  N63["Agrosuper SA"]:::pub --> N119("TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01<br/>$38.400.000.000"):::trx
  N119 --> N9["Corte Suprema de Chile"]:::priv
  N65(["Gonzalo Vial Vial"]):::pers -. "autoriza" .-> N119
  N119 -. "suscribe" .-> N120(["Manuel Ariztia Ruiz"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N121("TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01<br/>$0"):::trx
  N121 --> N9["Corte Suprema de Chile"]:::priv
  N122(["Andronico Luksic Craig"]):::pers -. "autoriza" .-> N121
  N121 -. "suscribe" .-> N122(["Andronico Luksic Craig"]):::pers
  N123["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N124("TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01<br/>$14.200.000.000"):::trx
  N124 --> N19["Servicio Impuestos Internos"]:::priv
  N125(["Gonzalo Delaveau Swett"]):::pers -. "autoriza" .-> N124
  N124 -. "suscribe" .-> N52(["Carlos Pavez Tolosa"]):::pers
  N123["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N126("TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01<br/>$19.500.000.000"):::trx
  N126 --> N116["Unidad de Analisis Financiero"]:::priv
  N5(["Agustin Edwards Eastman"]):::pers -. "autoriza" .-> N126
  N126 -. "suscribe" .-> N127(["Alfredo Ovalle Rodriguez"]):::pers
  N123["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N128("TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01<br/>$3.800.000.000"):::trx
  N128 --> N44["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N46(["Oscar Aitken Lavanchy"]):::pers -. "autoriza" .-> N128
  N128 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N129["Fundacion CEMA Chile"]:::pub --> N130("TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01<br/>$10.500.000.000"):::trx
  N130 --> N9["Corte Suprema de Chile"]:::priv
  N49(["Lucia Hiriart Rodriguez"]):::pers -. "autoriza" .-> N130
  N130 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N131["Direccion de Finanzas de Carabineros"]:::pub --> N132("TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01<br/>$28.348.928.198"):::trx
  N132 --> N131["Direccion de Finanzas de Carabineros"]:::priv
  N133(["Flavio Echeverria Cortez"]):::pers -. "autoriza" .-> N132
  N132 -. "suscribe" .-> N134(["Jaime Paz Meneses"]):::pers
  N27["Empresas CMPC SA"]:::pub --> N136("TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01<br/>$97.500.000.000"):::trx
  N136 --> N135["Servicio Nacional del Consumidor"]:::priv
  N30(["Eliodoro Matte Larrain"]):::pers -. "autoriza" .-> N136
  N136 -. "suscribe" .-> N31(["Gabriel Ruiz-Tagle Serrano"]):::pers
  N131["Direccion de Finanzas de Carabineros"]:::pub --> N137("TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01<br/>$1.450.000.000"):::trx
  N137 --> N116["Unidad de Analisis Financiero"]:::priv
  N133(["Flavio Echeverria Cortez"]):::pers -. "autoriza" .-> N137
  N137 -. "suscribe" .-> N118(["Javier Cruz Tamburrino"]):::pers
  N138["Direccion de Inteligencia Policial de Carabineros"]:::pub --> N139("TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01<br/>$0"):::trx
  N139 --> N9["Corte Suprema de Chile"]:::priv
  N140(["Gonzalo Blu Rodriguez"]):::pers -. "autoriza" .-> N139
  N139 -. "suscribe" .-> N141(["Alex Smith Leay"]):::pers
  N138["Direccion de Inteligencia Policial de Carabineros"]:::pub --> N142("TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01<br/>$25.000.000"):::trx
  N142 --> N138["Direccion de Inteligencia Policial de Carabineros"]:::priv
  N143(["Patricio Marin Lazo"]):::pers -. "autoriza" .-> N142
  N142 -. "suscribe" .-> N141(["Alex Smith Leay"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N144("TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01<br/>$0"):::trx
  N144 --> N138["Direccion de Inteligencia Policial de Carabineros"]:::priv
  N145(["Leonardo Osses Sandoval"]):::pers -. "autoriza" .-> N144
  N144 -. "suscribe" .-> N141(["Alex Smith Leay"]):::pers
  N146["Itelecom Holding Chile SpA"]:::pub --> N148("TRX-2019-05-14-Soborno-Luminarias-Chillan-01<br/>$3.200.000.000"):::trx
  N148 --> N147["Municipalidad de Chillan"]:::priv
  N149(["Leon Marcelo Lefort Hernandez"]):::pers -. "autoriza" .-> N148
  N148 -. "suscribe" .-> N150(["Marcelo Campos Henriquez"]):::pers
  N151["Factop SpA"]:::pub --> N152("TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01<br/>$190.000.000"):::trx
  N152 --> N92["Senado de la Republica de Chile"]:::priv
  N153(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N152
  N152 -. "suscribe" .-> N154(["Andres Chadwick Pinera"]):::pers
  N58["Farmacias Salcobrand SA"]:::pub --> N155("TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01<br/>$2.180.000.000"):::trx
  N155 --> N135["Servicio Nacional del Consumidor"]:::priv
  N61(["Roberto Belloni Pechini"]):::pers -. "autoriza" .-> N155
  N155 -. "suscribe" .-> N156(["Jose Codner Chijner"]):::pers
  N74["Municipalidad de Maipu"]:::pub --> N157("TRX-2020-12-15-Deficit-Maipu-Certificados-01<br/>$30.972.000.000"):::trx
  N157 --> N74["Municipalidad de Maipu"]:::priv
  N158(["Cathy Barriga Guerra"]):::pers -. "autoriza" .-> N157
  N157 -. "suscribe" .-> N158(["Cathy Barriga Guerra"]):::pers
  N159["Municipalidad de Vitacura"]:::pub --> N161("TRX-2021-04-15-Subvencion-VitaDeportes-01<br/>$759.000.000"):::trx
  N161 --> N160["Vita Deportes"]:::priv
  N162(["Raul Torrealba del Pedregal"]):::pers -. "autoriza" .-> N161
  N161 -. "suscribe" .-> N163(["Domingo Prieto Urrejola"]):::pers
  N164["Numen Publicidad SpA"]:::pub --> N165("TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01<br/>$0"):::trx
  N165 --> N41["Renovacion Nacional"]:::priv
  N166(["Fernando Cerimedo"]):::pers -. "autoriza" .-> N165
  N165 -. "suscribe" .-> N41(["Renovacion Nacional"]):::pers
  N167["Fundacion ProCultura"]:::pub --> N169("TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01<br/>$0"):::trx
  N169 --> N168["GORE Biobio"]:::priv
  N170(["Alberto Larrain Salas"]):::pers -. "autoriza" .-> N169
  N169 -. "suscribe" .-> N171(["Rodrigo Diaz Worner"]):::pers
  N172["Seremi MINVU Antofagasta"]:::pub --> N174("TRX-2022-10-03-Convenio-DV-01<br/>$200.000.000"):::trx
  N174 --> N173["Fundacion Democracia Viva"]:::priv
  N175(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N174
  N174 -. "suscribe" .-> N176(["Daniel Andrade Schwarze"]):::pers
  N172["Seremi MINVU Antofagasta"]:::pub --> N177("TRX-2022-10-19-Convenio-DV-02<br/>$170.000.000"):::trx
  N177 --> N173["Fundacion Democracia Viva"]:::priv
  N175(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N177
  N177 -. "suscribe" .-> N176(["Daniel Andrade Schwarze"]):::pers
  N172["Seremi MINVU Antofagasta"]:::pub --> N178("TRX-2022-10-28-Convenio-ProCultura-Antofagasta<br/>$500.000.000"):::trx
  N178 --> N167["Fundacion ProCultura"]:::priv
  N175(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N178
  N178 -. "suscribe" .-> N170(["Alberto Larrain Salas"]):::pers
  N151["Factop SpA"]:::pub --> N179("TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01<br/>$0"):::trx
  N179 --> N9["Corte Suprema de Chile"]:::priv
  N153(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N179
  N179 -. "suscribe" .-> N180(["Gabriel Zaliasnik Schilkrut"]):::pers
  N168["GORE Biobio"]:::pub --> N181("TRX-2022-11-18-Convenio-ProCultura-Biobio<br/>$2.553.000.000"):::trx
  N181 --> N167["Fundacion ProCultura"]:::priv
  N171(["Rodrigo Diaz Worner"]):::pers -. "autoriza" .-> N181
  N181 -. "suscribe" .-> N170(["Alberto Larrain Salas"]):::pers
  N172["Seremi MINVU Antofagasta"]:::pub --> N182("TRX-2022-11-29-Convenio-DV-03<br/>$56.000.000"):::trx
  N182 --> N173["Fundacion Democracia Viva"]:::priv
  N175(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N182
  N182 -. "suscribe" .-> N176(["Daniel Andrade Schwarze"]):::pers
  N168["GORE Biobio"]:::pub --> N184("TRX-2022-12-20-Convenio-EnTi-01<br/>$250.635.000"):::trx
  N184 --> N183["Fundacion En Ti"]:::priv
  N171(["Rodrigo Diaz Worner"]):::pers -. "autoriza" .-> N184
  N184 -. "suscribe" .-> N185(["Camila Polizzi Fonceca"]):::pers
  N186["Municipalidad de Santiago"]:::pub --> N188("TRX-2023-01-20-Compraventa-Clinica-SierraBella-01<br/>$8.200.000.000"):::trx
  N188 --> N187["Inmobiliaria San Valentino SpA"]:::priv
  N189(["Iraci Hassler Jacob"]):::pers -. "autoriza" .-> N188
  N188 -. "suscribe" .-> N190(["Felipe Sanchez Perez"]):::pers
  N151["Factop SpA"]:::pub --> N191("TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01<br/>$0"):::trx
  N191 --> N9["Corte Suprema de Chile"]:::priv
  N153(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N191
  N191 -. "suscribe" .-> N192(["Angela Vivanco Martinez"]):::pers
  N167["Fundacion ProCultura"]:::pub --> N193("TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01<br/>$315.000.000"):::trx
  N193 --> N19["Servicio Impuestos Internos"]:::priv
  N170(["Alberto Larrain Salas"]):::pers -. "autoriza" .-> N193
  N193 -. "suscribe" .-> N194(["Leonarda Villalobos Muth"]):::pers
  N151["Factop SpA"]:::pub --> N195("TRX-2023-06-22-Reunion-Audios-01<br/>$100.000.000"):::trx
  N195 --> N19["Servicio Impuestos Internos"]:::priv
  N153(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N195
  N195 -. "suscribe" .-> N194(["Leonarda Villalobos Muth"]):::pers
  N96["Contraloria General de la Republica"]:::pub --> N196("TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01<br/>$0"):::trx
  N196 --> N172["Seremi MINVU Antofagasta"]:::priv
  N197(["Jorge Bermudez Soto"]):::pers -. "autoriza" .-> N196
  N196 -. "suscribe" .-> N175(["Carlos Contreras Gutierrez"]):::pers
  N151["Factop SpA"]:::pub --> N198("TRX-2023-08-25-Reporte-ROS-Factop-UAF-01<br/>$480.000.000"):::trx
  N198 --> N116["Unidad de Analisis Financiero"]:::priv
  N153(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N198
  N198 -. "suscribe" .-> N118(["Javier Cruz Tamburrino"]):::pers
  N106[""]:::pub --> N199("TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01<br/>$240.000.000.000"):::trx
  N199 --> N19["Servicio Impuestos Internos"]:::priv
  N106([""]):::pers -. "autoriza" .-> N199
  N199 -. "suscribe" .-> N106([""]):::pers
  N92["Senado de la Republica de Chile"]:::pub --> N201("TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01<br/>$35.000.000"):::trx
  N201 --> N200["Camila Flores Oporto"]:::priv
  N92(["Senado de la Republica de Chile"]):::pers -. "autoriza" .-> N201
  N201 -. "suscribe" .-> N200(["Camila Flores Oporto"]):::pers
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
| [[KDM Empresas SA]] | 1 | $18.500.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Fundacion CEMA Chile]] | 1 | $10.500.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Municipalidad de Santiago]] | 1 | $8.200.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Sociedad Benefactora y Educacional Dignidad]] | 2 | $5.300.000.000 | **5456** | Alta Concentración / Captura (> 2.500) |
| [[Itelecom Holding Chile SpA]] | 1 | $3.200.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
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
| [[Gestion Ambiental y Territorial SA]] | 1 | $450.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Fundacion ProCultura]] | 1 | $315.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Union Democrata Independiente]] | 1 | $240.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Corpesca SA]] | 1 | $233.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Renovacion Nacional]] | 1 | $120.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Senado de la Republica de Chile]] | 1 | $35.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |
| [[Direccion de Inteligencia Policial de Carabineros]] | 1 | $25.000.000 | **10000** | Alta Concentración / Captura (> 2.500) |

---

## 4. Ranking de Nodos Puente (*Betweenness Centrality* & *PageRank Forense*)

| Posición | Nodo / Entidad | Tipo de Nodo | Intermediación (Brandes) | PageRank Forense | Rol Topológico |
| :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | [[Corte Suprema de Chile]] | `entidad_publica` | `0.4155` | `0.0281` | Conector Interregional / Puente Crítico |
| 2 | [[Servicio Impuestos Internos]] | `entidad_publica` | `0.2881` | `0.0199` | Conector Interregional / Puente Crítico |
| 3 | [[Sergio Munoz Gajardo]] | `persona` | `0.0983` | `0.0082` | Conector Interregional / Puente Crítico |
| 4 | [[Augusto Pinochet Ugarte]] | `persona` | `0.0978` | `0.0089` | Conector Interregional / Puente Crítico |
| 5 | [[Bancard Inversiones Ltda]] | `entidad_privada` | `0.0866` | `0.0081` | Conector Interregional / Puente Crítico |
| 6 | [[Agrosuper SA]] | `entidad_privada` | `0.0810` | `0.0044` | Conector Interregional / Puente Crítico |
| 7 | [[Gonzalo Vial Vial]] | `persona` | `0.0810` | `0.0044` | Conector Interregional / Puente Crítico |
| 8 | [[Asociacion de Productores Avicolas de Chile AG]] | `entidad_privada` | `0.0708` | `0.0045` | Conector Interregional / Puente Crítico |
| 9 | [[Juan Miguel Ovalle Garces]] | `persona` | `0.0708` | `0.0045` | Conector Interregional / Puente Crítico |
| 10 | [[Factop SpA]] | `entidad_privada` | `0.0627` | `0.0071` | Conector Interregional / Puente Crítico |

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
| [[TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01]] | 2002-04-12 | `factura_falsa` | [[Gestion Ambiental y Territorial SA]] | [[Servicio Impuestos Internos]] | $450.000.000 | 7394.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]] | 2003-10-15 | `desviacion_fondos` | [[Inversiones El Bosque Ltda]] | [[Servicio Impuestos Internos]] | $480.000.000 | 7887.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | 2003-11-05 | `gestion_influencia` | [[Renovacion Nacional]] | [[Corte Suprema de Chile]] | $120.000.000 | 1972.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]] | 2004-07-14 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | $15.800.000.000 | 259642.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | 2005-06-14 | `desviacion_fondos` | [[Sociedad Benefactora y Educacional Dignidad]] | [[Corte Suprema de Chile]] | $1.850.000.000 | 30401.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | 2005-08-10 | `desviacion_fondos` | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[Servicio Impuestos Internos]] | $2.450.000.000 | 40261.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | 2006-07-24 | `gestion_influencia` | [[Bancard Inversiones Ltda]] | [[Comision para el Mercado Financiero]] | $5.300.000.000 | 87095.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]] | 2007-04-10 | `consulta_terceros` | [[Quiroz y Asociados Consultores SpA]] | [[Asociacion de Productores Avicolas de Chile AG]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]] | 2007-11-01 | `acuerdo_colusorio` | [[Farmacias Salcobrand SA]] | [[Farmacias Cruz Verde SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]] | 2008-01-15 | `acuerdo_colusorio` | [[Agrosuper SA]] | [[Asociacion de Productores Avicolas de Chile AG]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | 2009-11-18 | `factura_falsa` | [[SQM SA]] | [[Bancard Inversiones Ltda]] | $340.000.000 | 5587.2 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]] | 2010-06-15 | `peritaje_forense` | [[Quiroz y Asociados Consultores SpA]] | [[Farmacias Salcobrand SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | 2010-08-19 | `cohecho` | [[SQM SA]] | [[Union Democrata Independiente]] | $730.000.000 | 19588.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]] | 2010-11-15 | `cohecho_soborno` | [[KDM Empresas SA]] | [[Municipalidad de Maipu]] | $18.500.000.000 | 304011.3 UTM | Afecto (>= 5.000 UTM) |
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
| [[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]] | 2019-05-14 | `cohecho` | [[Itelecom Holding Chile SpA]] | [[Municipalidad de Chillan]] | $3.200.000.000 | 52585.7 UTM | Afecto (>= 5.000 UTM) |
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
| [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]] | 2023-01-20 | `trato_directo` | [[Municipalidad de Santiago]] | [[Inmobiliaria San Valentino SpA]] | $8.200.000.000 | 134751.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | 2023-02-09 | `llamada` | [[Factop SpA]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | 2023-05-10 | `factura_falsa` | [[Fundacion ProCultura]] | [[Servicio Impuestos Internos]] | $315.000.000 | 5176.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2023-06-22-Reunion-Audios-01]] | 2023-06-22 | `cohecho` | [[Factop SpA]] | [[Servicio Impuestos Internos]] | $100.000.000 | 1580.7 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | 2023-06-29 | `resolucion_administrativa` | [[Contraloria General de la Republica]] | [[Seremi MINVU Antofagasta]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | 2023-08-25 | `factura_falsa` | [[Factop SpA]] | [[Unidad de Analisis Financiero]] | $480.000.000 | 7887.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01]] | 2023-12-14 | `factura_falsa` | [[]] | [[Servicio Impuestos Internos]] | $240.000.000.000 | 3943930.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]] | 2025-10-15 | `desviacion_fondos` | [[Senado de la Republica de Chile]] | [[Camila Flores Oporto]] | $35.000.000 | 575.2 UTM | Exento (< 5.000 UTM) |
