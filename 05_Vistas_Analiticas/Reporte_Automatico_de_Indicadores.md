---
tipo_nodo: vista_analitica
titulo: "Reporte de Revisión Automatizada (UTM, HHI, PageRank, Brandes y Topología)"
actualizacion_automatica: true
tags:
  - dashboard
  - auditoria-cgr
  - topologia
---

# Reporte Automático de Indicadores (montos, umbrales y centralidad)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.
>
> Los umbrales (por ejemplo, el de toma de razón de la Contraloría) se usan como señales para revisar documentos, no como determinación de una irregularidad.


- **Monto Global Investigado**: **$841.204.734.718 CLP** (Equivalente a **14.080.621.0 UTM**)
- **Total de Aristas Reificadas (`TRX`)**: **81**
- **Casos de Fraccionamiento bajo 5.000 UTM detectados**: **1**

---

## 1. Diagrama Topológico de Flujos Financieros Reificados (Mermaid)

```mermaid
flowchart LR
  classDef pub fill:#1b5e20,stroke:#81c784,color:#fff,stroke-width:2px;
  classDef priv fill:#e65100,stroke:#ffb74d,color:#fff,stroke-width:2px;
  classDef trx fill:#b71c1c,stroke:#ef9a9a,color:#fff,stroke-width:1.5px;
  classDef pers fill:#0d47a1,stroke:#64b5f6,color:#fff,stroke-width:1.5px;
  N1["Agencia Central de Inteligencia CIA y Escuela de las Americas"]:::pub --> N3("TRX-1971-09-09-Fondos-CIA-ElMercurio-01<br/>$0"):::trx
  N3 --> N2["Empresa El Mercurio SAP"]:::priv
  N4(["Manuel Contreras Sepulveda"]):::pers -. "autoriza" .-> N3
  N3 -. "suscribe" .-> N5(["Agustin Edwards Eastman"]):::pers
  N1["Agencia Central de Inteligencia CIA y Escuela de las Americas"]:::pub --> N7("TRX-1972-10-12-Fondos-CIA-Gremios-ParoCamioneros-01<br/>$0"):::trx
  N7 --> N6["Comando de Apoyo a la Fuerza del Ejercito"]:::priv
  N5(["Agustin Edwards Eastman"]):::pers -. "autoriza" .-> N7
  N7 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N1["Agencia Central de Inteligencia CIA y Escuela de las Americas"]:::pub --> N10("TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01<br/>$0"):::trx
  N10 --> N9["Corte Suprema de Chile"]:::priv
  N4(["Manuel Contreras Sepulveda"]):::pers -. "autoriza" .-> N10
  N10 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N12("TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01<br/>$0"):::trx
  N12 --> N9["Corte Suprema de Chile"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N12
  N12 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N16("TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01<br/>$2.950.000.000"):::trx
  N16 --> N15["Valmoval Ltda"]:::priv
  N8(["Augusto Pinochet Ugarte"]):::pers -. "autoriza" .-> N16
  N16 -. "suscribe" .-> N17(["Augusto Pinochet Hiriart"]):::pers
  N18["Sociedad Benefactora y Educacional Dignidad"]:::pub --> N20("TRX-1991-01-31-Movimientos-Patrimoniales-ColoniaDignidad-01<br/>$0"):::trx
  N20 --> N19["Servicio Impuestos Internos"]:::priv
  N21(["Paul Schafer Schneider"]):::pers -. "autoriza" .-> N20
  N20 -. "suscribe" .-> N22(["Jorge Zepeda Arancibia"]):::pers
  N23["Corporacion Nacional del Cobre de Chile"]:::pub --> N24("TRX-1994-01-21-Operaciones-Futuros-Codelco-Davilazo-01<br/>$98.580.000.000"):::trx
  N24 --> N19["Servicio Impuestos Internos"]:::priv
  N25(["Juan Pablo Davila Silva"]):::pers -. "autoriza" .-> N24
  N24 -. "suscribe" .-> N25(["Juan Pablo Davila Silva"]):::pers
  N26["Fuerza Aerea de Chile"]:::pub --> N28("TRX-1994-12-15-Comisiones-Compra-Aviones-Mirage-FACh-01<br/>$6.000.000.000"):::trx
  N28 --> N27["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N29(["Ramon Vega Hidalgo"]):::pers -. "autoriza" .-> N28
  N28 -. "suscribe" .-> N30(["Jaime Estay Viveros"]):::pers
  N31["Union Democrata Independiente"]:::pub --> N32("TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01<br/>$0"):::trx
  N32 --> N18["Sociedad Benefactora y Educacional Dignidad"]:::priv
  N33(["Hernan Larrain Fernandez"]):::pers -. "autoriza" .-> N32
  N32 -. "suscribe" .-> N34(["Hartmut Hopp Miottel"]):::pers
  N35["Empresas CMPC SA"]:::pub --> N37("TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01<br/>$0"):::trx
  N37 --> N36["SCA Chile SA"]:::priv
  N38(["Eliodoro Matte Larrain"]):::pers -. "autoriza" .-> N37
  N37 -. "suscribe" .-> N39(["Gabriel Ruiz-Tagle Serrano"]):::pers
  N40["Ministerio de Obras Publicas"]:::pub --> N42("TRX-2001-08-20-Contratos-MOP-GATE-01<br/>$1.253.000.000"):::trx
  N42 --> N41["Gestion Ambiental y Territorial SA"]:::priv
  N43(["Carlos Cruz Lorenzen"]):::pers -. "autoriza" .-> N42
  N42 -. "suscribe" .-> N44(["Hector Pena Veliz"]):::pers
  N45["Partido Democrata Cristiano"]:::pub --> N46("TRX-2002-10-15-Sobornos-Plantas-Revision-Tecnica-Coimas-01<br/>$20.000.000"):::trx
  N46 --> N40["Ministerio de Obras Publicas"]:::priv
  N47(["Cristian Pareto Vergara"]):::pers -. "autoriza" .-> N46
  N46 -. "suscribe" .-> N48(["Victor Manuel Rebolledo Gonzalez"]):::pers
  N49["Inversiones El Bosque Ltda"]:::pub --> N50("TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01<br/>$0"):::trx
  N50 --> N19["Servicio Impuestos Internos"]:::priv
  N51(["Claudio Spiniak Vilensky"]):::pers -. "autoriza" .-> N50
  N50 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N52["Renovacion Nacional"]:::pub --> N53("TRX-2003-11-05-Arista-Politica-Spiniak-01<br/>$0"):::trx
  N53 --> N9["Corte Suprema de Chile"]:::priv
  N54(["Pia Guzman Mena"]):::pers -. "autoriza" .-> N53
  N53 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N55("TRX-2004-07-14-Gastos-Reservados-Riggs-01<br/>$15.800.000.000"):::trx
  N55 --> N27["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N8(["Augusto Pinochet Ugarte"]):::pers -. "autoriza" .-> N55
  N55 -. "suscribe" .-> N56(["Oscar Aitken Lavanchy"]):::pers
  N18["Sociedad Benefactora y Educacional Dignidad"]:::pub --> N57("TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01<br/>$0"):::trx
  N57 --> N9["Corte Suprema de Chile"]:::priv
  N21(["Paul Schafer Schneider"]):::pers -. "autoriza" .-> N57
  N57 -. "suscribe" .-> N22(["Jorge Zepeda Arancibia"]):::pers
  N27["Riggs Bank y Sociedades Offshore Ashburton"]:::pub --> N58("TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01<br/>$2.450.000.000"):::trx
  N58 --> N19["Servicio Impuestos Internos"]:::priv
  N59(["Lucia Hiriart Rodriguez"]):::pers -. "autoriza" .-> N58
  N58 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N60["Instituto Nacional de Deportes Chiledeportes"]:::pub --> N62("TRX-2005-11-10-Desvio-Fondos-Chiledeportes-Publicam-01<br/>$417.000.000"):::trx
  N62 --> N61["Publicam Limitada"]:::priv
  N63([""]):::pers -. "autoriza" .-> N62
  N62 -. "suscribe" .-> N64(["Manuel Arancibia Morales"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N66("TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01<br/>$5.300.000.000"):::trx
  N66 --> N65["Comision para el Mercado Financiero"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N66
  N66 -. "suscribe" .-> N67(["Carlos Pavez Tolosa"]):::pers
  N68["Quiroz y Asociados Consultores SpA"]:::pub --> N70("TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01<br/>$0"):::trx
  N70 --> N69["Asociacion de Productores Avicolas de Chile AG"]:::priv
  N71(["Jorge Quiroz Castro"]):::pers -. "autoriza" .-> N70
  N70 -. "suscribe" .-> N72(["Juan Miguel Ovalle Garces"]):::pers
  N73["Farmacias Salcobrand SA"]:::pub --> N75("TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01<br/>$0"):::trx
  N75 --> N74["Farmacias Cruz Verde SA"]:::priv
  N76(["Roberto Belloni Pechini"]):::pers -. "autoriza" .-> N75
  N75 -. "suscribe" .-> N77(["Guillermo Harding Alvarado"]):::pers
  N78["Agrosuper SA"]:::pub --> N79("TRX-2008-01-15-Colusion-Cuotas-Produccion-Pollos-01<br/>$0"):::trx
  N79 --> N69["Asociacion de Productores Avicolas de Chile AG"]:::priv
  N80(["Gonzalo Vial Vial"]):::pers -. "autoriza" .-> N79
  N79 -. "suscribe" .-> N72(["Juan Miguel Ovalle Garces"]):::pers
  N81["SQM SA"]:::pub --> N82("TRX-2009-11-18-Facturas-Bancard-SQM-2009-01<br/>$340.000.000"):::trx
  N82 --> N11["Bancard Inversiones Ltda"]:::priv
  N83(["Patricio Contesse Gonzalez"]):::pers -. "autoriza" .-> N82
  N82 -. "suscribe" .-> N84(["Santiago Valdes Gutierrez"]):::pers
  N68["Quiroz y Asociados Consultores SpA"]:::pub --> N85("TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01<br/>$0"):::trx
  N85 --> N73["Farmacias Salcobrand SA"]:::priv
  N71(["Jorge Quiroz Castro"]):::pers -. "autoriza" .-> N85
  N85 -. "suscribe" .-> N76(["Roberto Belloni Pechini"]):::pers
  N81["SQM SA"]:::pub --> N86("TRX-2010-08-19-Correo-Royalty-SQM-01<br/>$730.000.000"):::trx
  N86 --> N31["Union Democrata Independiente"]:::priv
  N83(["Patricio Contesse Gonzalez"]):::pers -. "autoriza" .-> N86
  N86 -. "suscribe" .-> N87(["Pablo Longueira Montes"]):::pers
  N88["KDM Empresas SA"]:::pub --> N90("TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01<br/>$186.500.000"):::trx
  N90 --> N89["Municipalidad de Maipu"]:::priv
  N91(["Fernando Leon Steffens"]):::pers -. "autoriza" .-> N90
  N90 -. "suscribe" .-> N92(["Marcelo Torres Ferrari"]):::pers
  N93["Andes Iron SpA"]:::pub --> N94("TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01<br/>$75.500.000.000"):::trx
  N94 --> N11["Bancard Inversiones Ltda"]:::priv
  N95(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N94
  N94 -. "suscribe" .-> N13(["Sebastian Pinera Echenique"]):::pers
  N96["Empresas Penta SA"]:::pub --> N97("TRX-2011-03-10-Pagos-Penta-Wagner-01<br/>$42.000.000"):::trx
  N97 --> N19["Servicio Impuestos Internos"]:::priv
  N98(["Carlos Eugenio Lavin Garcia-Huidobro"]):::pers -. "autoriza" .-> N97
  N97 -. "suscribe" .-> N99(["Pablo Wagner San Martin"]):::pers
  N100["Universidad del Mar"]:::pub --> N102("TRX-2011-04-15-Sobornos-Acreditacion-UniversidadDelMar-CNA-01<br/>$105.000.000"):::trx
  N102 --> N101["Comision Nacional de Acreditacion"]:::priv
  N103(["Hector Zuniga Rogers"]):::pers -. "autoriza" .-> N102
  N102 -. "suscribe" .-> N104(["Luis Eugenio Diaz Corvalan"]):::pers
  N105["Empresas La Polar SA"]:::pub --> N106("TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01<br/>$68.634.000.000"):::trx
  N106 --> N65["Comision para el Mercado Financiero"]:::priv
  N107(["Pablo Alcalde Saavedra"]):::pers -. "autoriza" .-> N106
  N106 -. "suscribe" .-> N108(["Julian Moreno de Pablo"]):::pers
  N81["SQM SA"]:::pub --> N110("TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01<br/>$57.000.000"):::trx
  N110 --> N109["Partido por la Democracia"]:::priv
  N63([""]):::pers -. "autoriza" .-> N110
  N110 -. "suscribe" .-> N111(["Patricio Rodrigo Salinas"]):::pers
  N112["Sociedad de Inversiones Pampa Calichera SA"]:::pub --> N113("TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01<br/>$0"):::trx
  N113 --> N81["SQM SA"]:::priv
  N114(["Julio Ponce Lerou"]):::pers -. "autoriza" .-> N113
  N113 -. "suscribe" .-> N63([""]):::pers
  N115["Municipalidad de Cerro Navia"]:::pub --> N116("TRX-2012-03-22-Contratos-Residuos-CerroNavia-01<br/>$1.120.000.000"):::trx
  N116 --> N88["KDM Empresas SA"]:::priv
  N117(["Luis Plaza Sanchez"]):::pers -. "autoriza" .-> N116
  N116 -. "suscribe" .-> N92(["Marcelo Torres Ferrari"]):::pers
  N118["Corpesca SA"]:::pub --> N120("TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01<br/>$233.000.000"):::trx
  N120 --> N119["Senado de la Republica de Chile"]:::priv
  N121(["Francisco Mujica Ortuzar"]):::pers -. "autoriza" .-> N120
  N120 -. "suscribe" .-> N122(["Jaime Orpis Bouchon"]):::pers
  N11["Bancard Inversiones Ltda"]:::pub --> N124("TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01<br/>$8.250.000.000"):::trx
  N124 --> N123["Contraloria General de la Republica"]:::priv
  N13(["Sebastian Pinera Echenique"]):::pers -. "autoriza" .-> N124
  N124 -. "suscribe" .-> N84(["Santiago Valdes Gutierrez"]):::pers
  N96["Empresas Penta SA"]:::pub --> N125("TRX-2013-07-15-Boletas-Penta-UDI-01<br/>$1.260.000.000"):::trx
  N125 --> N31["Union Democrata Independiente"]:::priv
  N95(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N125
  N125 -. "suscribe" .-> N87(["Pablo Longueira Montes"]):::pers
  N96["Empresas Penta SA"]:::pub --> N126("TRX-2013-09-20-Boletas-Penta-Novoa-01<br/>$156.000.000"):::trx
  N126 --> N31["Union Democrata Independiente"]:::priv
  N95(["Carlos Alberto Delano Abbott"]):::pers -. "autoriza" .-> N126
  N126 -. "suscribe" .-> N127(["Jovino Novoa Vasquez"]):::pers
  N63[""]:::pub --> N129("TRX-2014-02-18-Pagos-DOM-Machali-Caval-01<br/>$55.030.792"):::trx
  N129 --> N128["Municipalidad de Machali"]:::priv
  N63([""]):::pers -. "autoriza" .-> N129
  N129 -. "suscribe" .-> N130(["Jorge Silva Menares"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N132("TRX-2014-05-20-Facturas-LeyReservadaCobre-01<br/>$6.100.000.000"):::trx
  N132 --> N131["Frasim Ltda"]:::priv
  N133(["Juan Miguel Fuente-Alba Poblete"]):::pers -. "autoriza" .-> N132
  N132 -. "suscribe" .-> N134(["Jozo Santic Palomino"]):::pers
  N135["PricewaterhouseCoopers Consultores Auditores SpA"]:::pub --> N136("TRX-2014-07-24-Sanciones-SVS-CS-Auditorias-PwC-LaPolar-Cascadas-01<br/>$2.100.000.000"):::trx
  N136 --> N105["Empresas La Polar SA"]:::priv
  N137(["Javier Gatica Menke"]):::pers -. "autoriza" .-> N136
  N136 -. "suscribe" .-> N63([""]):::pers
  N138["Exportadora y de Gestion Caval Ltda"]:::pub --> N139("TRX-2015-01-29-Facturas-Caval-SII-01<br/>$2.500.000.000"):::trx
  N139 --> N19["Servicio Impuestos Internos"]:::priv
  N140(["Natalia Compagnon Soto"]):::pers -. "autoriza" .-> N139
  N139 -. "suscribe" .-> N140(["Natalia Compagnon Soto"]):::pers
  N141["Empresas Pullman Bus SA"]:::pub --> N143("TRX-2015-04-20-Multas-Colusion-Buses-Interurbanos-01<br/>$898.000.000"):::trx
  N143 --> N142["Fiscalia Nacional Economica"]:::priv
  N144(["Pedro Farias Soto"]):::pers -. "autoriza" .-> N143
  N143 -. "suscribe" .-> N145(["Jesus Diez Gonzalez"]):::pers
  N6["Comando de Apoyo a la Fuerza del Ejercito"]:::pub --> N147("TRX-2015-08-14-GastosReservados-Ejercito-UAF-01<br/>$3.500.000.000"):::trx
  N147 --> N146["Unidad de Analisis Financiero"]:::priv
  N133(["Juan Miguel Fuente-Alba Poblete"]):::pers -. "autoriza" .-> N147
  N147 -. "suscribe" .-> N148(["Javier Cruz Tamburrino"]):::pers
  N149["Municipalidad de Antofagasta"]:::pub --> N151("TRX-2015-10-01-Asesoria-Main-CMDS-Antofagasta-01<br/>$23.722.228"):::trx
  N151 --> N150["Main Comunicacion Estrategica"]:::priv
  N152(["Karen Rojo Venegas"]):::pers -. "autoriza" .-> N151
  N151 -. "suscribe" .-> N153(["Jose Miguel Izquierdo Sanchez"]):::pers
  N78["Agrosuper SA"]:::pub --> N154("TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01<br/>$38.400.000.000"):::trx
  N154 --> N9["Corte Suprema de Chile"]:::priv
  N80(["Gonzalo Vial Vial"]):::pers -. "autoriza" .-> N154
  N154 -. "suscribe" .-> N155(["Manuel Ariztia Ruiz"]):::pers
  N156["AC Inversions SpA"]:::pub --> N157("TRX-2016-03-01-Estafa-Piramidal-Lavado-ACInversions-01<br/>$50.000.000.000"):::trx
  N157 --> N146["Unidad de Analisis Financiero"]:::priv
  N158(["Patricio Santos Hernandez"]):::pers -. "autoriza" .-> N157
  N157 -. "suscribe" .-> N158(["Patricio Santos Hernandez"]):::pers
  N159["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N160("TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01<br/>$0"):::trx
  N160 --> N19["Servicio Impuestos Internos"]:::priv
  N161(["Gonzalo Delaveau Swett"]):::pers -. "autoriza" .-> N160
  N160 -. "suscribe" .-> N67(["Carlos Pavez Tolosa"]):::pers
  N159["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N162("TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01<br/>$0"):::trx
  N162 --> N146["Unidad de Analisis Financiero"]:::priv
  N5(["Agustin Edwards Eastman"]):::pers -. "autoriza" .-> N162
  N162 -. "suscribe" .-> N163(["Alfredo Ovalle Rodriguez"]):::pers
  N159["Mossack Fonseca y Sociedades Offshore Panama"]:::pub --> N164("TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01<br/>$0"):::trx
  N164 --> N27["Riggs Bank y Sociedades Offshore Ashburton"]:::priv
  N56(["Oscar Aitken Lavanchy"]):::pers -. "autoriza" .-> N164
  N164 -. "suscribe" .-> N8(["Augusto Pinochet Ugarte"]):::pers
  N165["Fundacion CEMA Chile"]:::pub --> N166("TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01<br/>$0"):::trx
  N166 --> N9["Corte Suprema de Chile"]:::priv
  N59(["Lucia Hiriart Rodriguez"]):::pers -. "autoriza" .-> N166
  N166 -. "suscribe" .-> N14(["Sergio Munoz Gajardo"]):::pers
  N167["Direccion de Finanzas de Carabineros"]:::pub --> N168("TRX-2016-11-10-Fondos-Direccion-Finanzas-Carabineros-01<br/>$28.348.928.198"):::trx
  N168 --> N167["Direccion de Finanzas de Carabineros"]:::priv
  N169(["Flavio Echeverria Cortez"]):::pers -. "autoriza" .-> N168
  N168 -. "suscribe" .-> N170(["Jaime Paz Meneses"]):::pers
  N35["Empresas CMPC SA"]:::pub --> N172("TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01<br/>$97.500.000.000"):::trx
  N172 --> N171["Servicio Nacional del Consumidor"]:::priv
  N38(["Eliodoro Matte Larrain"]):::pers -. "autoriza" .-> N172
  N172 -. "suscribe" .-> N39(["Gabriel Ruiz-Tagle Serrano"]):::pers
  N167["Direccion de Finanzas de Carabineros"]:::pub --> N173("TRX-2017-03-06-Reportes-UAF-Carabineros-01<br/>$1.450.000.000"):::trx
  N173 --> N146["Unidad de Analisis Financiero"]:::priv
  N169(["Flavio Echeverria Cortez"]):::pers -. "autoriza" .-> N173
  N173 -. "suscribe" .-> N148(["Javier Cruz Tamburrino"]):::pers
  N174["Policia de Investigaciones de Chile"]:::pub --> N175("TRX-2017-05-15-Desvio-Gastos-Reservados-PDI-Espinosa-01<br/>$146.000.000"):::trx
  N175 --> N146["Unidad de Analisis Financiero"]:::priv
  N176(["Hector Espinosa Valenzuela"]):::pers -. "autoriza" .-> N175
  N175 -. "suscribe" .-> N176(["Hector Espinosa Valenzuela"]):::pers
  N177["Municipalidad de San Ramon"]:::pub --> N178("TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01<br/>$246.918.500"):::trx
  N178 --> N146["Unidad de Analisis Financiero"]:::priv
  N179(["Miguel Angel Aguilera Sanhueza"]):::pers -. "autoriza" .-> N178
  N178 -. "suscribe" .-> N179(["Miguel Angel Aguilera Sanhueza"]):::pers
  N180["Direccion de Inteligencia Policial de Carabineros"]:::pub --> N181("TRX-2017-09-23-Detenciones-OperacionHuracan-01<br/>$0"):::trx
  N181 --> N9["Corte Suprema de Chile"]:::priv
  N182(["Gonzalo Blu Rodriguez"]):::pers -. "autoriza" .-> N181
  N181 -. "suscribe" .-> N183(["Alex Smith Leay"]):::pers
  N180["Direccion de Inteligencia Policial de Carabineros"]:::pub --> N184("TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01<br/>$25.000.000"):::trx
  N184 --> N180["Direccion de Inteligencia Policial de Carabineros"]:::priv
  N185(["Patricio Marin Lazo"]):::pers -. "autoriza" .-> N184
  N184 -. "suscribe" .-> N183(["Alex Smith Leay"]):::pers
  N9["Corte Suprema de Chile"]:::pub --> N186("TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01<br/>$0"):::trx
  N186 --> N180["Direccion de Inteligencia Policial de Carabineros"]:::priv
  N187(["Leonardo Osses Sandoval"]):::pers -. "autoriza" .-> N186
  N186 -. "suscribe" .-> N183(["Alex Smith Leay"]):::pers
  N188["Itelecom Holding Chile SpA"]:::pub --> N190("TRX-2018-09-12-Sobornos-Itelecom-Licitacion-Iquique-01<br/>$125.000.000"):::trx
  N190 --> N189["Municipalidad de Iquique"]:::priv
  N191(["Leon Marcelo Lefort Hernandez"]):::pers -. "autoriza" .-> N190
  N190 -. "suscribe" .-> N192(["Guillermo Cejas Valenzuela"]):::pers
  N188["Itelecom Holding Chile SpA"]:::pub --> N194("TRX-2019-05-14-Licitacion-Luminarias-Chillan-01<br/>$37.000.000"):::trx
  N194 --> N193["Municipalidad de Chillan"]:::priv
  N191(["Leon Marcelo Lefort Hernandez"]):::pers -. "autoriza" .-> N194
  N194 -. "suscribe" .-> N195(["Marcelo Campos Henriquez"]):::pers
  N196["Factop SpA"]:::pub --> N197("TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01<br/>$190.000.000"):::trx
  N197 --> N119["Senado de la Republica de Chile"]:::priv
  N198(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N197
  N197 -. "suscribe" .-> N199(["Andres Chadwick Pinera"]):::pers
  N200["Cencosud SA"]:::pub --> N201("TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01<br/>$18.300.000.000"):::trx
  N201 --> N142["Fiscalia Nacional Economica"]:::priv
  N202(["Horst Paulmann Kemna"]):::pers -. "autoriza" .-> N201
  N201 -. "suscribe" .-> N203(["Enrique Ostale Brito"]):::pers
  N204["Compania Maritima de Chile SA"]:::pub --> N205("TRX-2020-08-14-Multas-Colusion-Navieras-CarCarriers-01<br/>$24.100.000.000"):::trx
  N205 --> N142["Fiscalia Nacional Economica"]:::priv
  N206(["Beltran Urenda Salamanca"]):::pers -. "autoriza" .-> N205
  N205 -. "suscribe" .-> N207(["Andronico Luksic Craig"]):::pers
  N73["Farmacias Salcobrand SA"]:::pub --> N208("TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01<br/>$2.180.000.000"):::trx
  N208 --> N171["Servicio Nacional del Consumidor"]:::priv
  N76(["Roberto Belloni Pechini"]):::pers -. "autoriza" .-> N208
  N208 -. "suscribe" .-> N209(["Jose Codner Chijner"]):::pers
  N89["Municipalidad de Maipu"]:::pub --> N210("TRX-2020-12-15-Deficit-Maipu-Certificados-01<br/>$30.972.000.000"):::trx
  N210 --> N89["Municipalidad de Maipu"]:::priv
  N211(["Cathy Barriga Guerra"]):::pers -. "autoriza" .-> N210
  N210 -. "suscribe" .-> N211(["Cathy Barriga Guerra"]):::pers
  N212["Municipalidad de Vitacura"]:::pub --> N214("TRX-2021-04-15-Subvencion-VitaDeportes-01<br/>$759.000.000"):::trx
  N214 --> N213["Vita Deportes"]:::priv
  N215(["Raul Torrealba del Pedregal"]):::pers -. "autoriza" .-> N214
  N214 -. "suscribe" .-> N216(["Domingo Prieto Urrejola"]):::pers
  N217["Numen Publicidad SpA"]:::pub --> N218("TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01<br/>$0"):::trx
  N218 --> N52["Renovacion Nacional"]:::priv
  N219(["Fernando Cerimedo"]):::pers -. "autoriza" .-> N218
  N218 -. "suscribe" .-> N52(["Renovacion Nacional"]):::pers
  N220["Seremi MINVU Antofagasta"]:::pub --> N222("TRX-2022-10-03-Convenio-DV-01<br/>$200.000.000"):::trx
  N222 --> N221["Fundacion Democracia Viva"]:::priv
  N223(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N222
  N222 -. "suscribe" .-> N224(["Daniel Andrade Schwarze"]):::pers
  N220["Seremi MINVU Antofagasta"]:::pub --> N225("TRX-2022-10-19-Convenio-DV-02<br/>$170.000.000"):::trx
  N225 --> N221["Fundacion Democracia Viva"]:::priv
  N223(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N225
  N225 -. "suscribe" .-> N224(["Daniel Andrade Schwarze"]):::pers
  N220["Seremi MINVU Antofagasta"]:::pub --> N227("TRX-2022-10-28-Convenio-ProCultura-Antofagasta<br/>$500.000.000"):::trx
  N227 --> N226["Fundacion ProCultura"]:::priv
  N223(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N227
  N227 -. "suscribe" .-> N228(["Alberto Larrain Salas"]):::pers
  N196["Factop SpA"]:::pub --> N229("TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01<br/>$0"):::trx
  N229 --> N9["Corte Suprema de Chile"]:::priv
  N198(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N229
  N229 -. "suscribe" .-> N230(["Gabriel Zaliasnik Schilkrut"]):::pers
  N231["GORE Biobio"]:::pub --> N232("TRX-2022-11-18-Convenio-ProCultura-Biobio<br/>$2.553.000.000"):::trx
  N232 --> N226["Fundacion ProCultura"]:::priv
  N233(["Rodrigo Diaz Worner"]):::pers -. "autoriza" .-> N232
  N232 -. "suscribe" .-> N228(["Alberto Larrain Salas"]):::pers
  N220["Seremi MINVU Antofagasta"]:::pub --> N234("TRX-2022-11-29-Convenio-DV-03<br/>$56.000.000"):::trx
  N234 --> N221["Fundacion Democracia Viva"]:::priv
  N223(["Carlos Contreras Gutierrez"]):::pers -. "autoriza" .-> N234
  N234 -. "suscribe" .-> N224(["Daniel Andrade Schwarze"]):::pers
  N231["GORE Biobio"]:::pub --> N236("TRX-2022-12-20-Convenio-EnTi-01<br/>$250.635.000"):::trx
  N236 --> N235["Fundacion En Ti"]:::priv
  N233(["Rodrigo Diaz Worner"]):::pers -. "autoriza" .-> N236
  N236 -. "suscribe" .-> N237(["Camila Polizzi Fonceca"]):::pers
  N238["Municipalidad de Santiago"]:::pub --> N240("TRX-2023-01-20-Compraventa-Clinica-SierraBella-01<br/>$0"):::trx
  N240 --> N239["Inmobiliaria San Valentino SpA"]:::priv
  N241(["Iraci Hassler Jacob"]):::pers -. "autoriza" .-> N240
  N240 -. "suscribe" .-> N242(["Felipe Sanchez Perez"]):::pers
  N196["Factop SpA"]:::pub --> N243("TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01<br/>$0"):::trx
  N243 --> N9["Corte Suprema de Chile"]:::priv
  N198(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N243
  N243 -. "suscribe" .-> N244(["Angela Vivanco Martinez"]):::pers
  N196["Factop SpA"]:::pub --> N245("TRX-2023-06-22-Reunion-Audios-01<br/>$100.000.000"):::trx
  N245 --> N19["Servicio Impuestos Internos"]:::priv
  N198(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N245
  N245 -. "suscribe" .-> N246(["Leonarda Villalobos Muth"]):::pers
  N123["Contraloria General de la Republica"]:::pub --> N247("TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01<br/>$0"):::trx
  N247 --> N220["Seremi MINVU Antofagasta"]:::priv
  N248(["Jorge Bermudez Soto"]):::pers -. "autoriza" .-> N247
  N247 -. "suscribe" .-> N223(["Carlos Contreras Gutierrez"]):::pers
  N196["Factop SpA"]:::pub --> N249("TRX-2023-08-25-Reporte-ROS-Factop-UAF-01<br/>$0"):::trx
  N249 --> N146["Unidad de Analisis Financiero"]:::priv
  N198(["Luis Hermosilla Osorio"]):::pers -. "autoriza" .-> N249
  N249 -. "suscribe" .-> N148(["Javier Cruz Tamburrino"]):::pers
  N63[""]:::pub --> N250("TRX-2023-12-14-Perjuicio-Fiscal-Operacion-Tributos-01<br/>$240.000.000.000"):::trx
  N250 --> N19["Servicio Impuestos Internos"]:::priv
  N63([""]):::pers -. "autoriza" .-> N250
  N250 -. "suscribe" .-> N63([""]):::pers
  N119["Senado de la Republica de Chile"]:::pub --> N252("TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01<br/>$35.000.000"):::trx
  N252 --> N251["Camila Flores Oporto"]:::priv
  N119(["Senado de la Republica de Chile"]):::pers -. "autoriza" .-> N252
  N252 -. "suscribe" .-> N251(["Camila Flores Oporto"]):::pers
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
| [[]] | 2 | $240.055.030.792 | **9995** | Alta Concentración (> 2.500) |
| [[Corporacion Nacional del Cobre de Chile]] | 1 | $98.580.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Empresas CMPC SA]] | 1 | $97.500.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Andes Iron SpA]] | 1 | $75.500.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Empresas La Polar SA]] | 1 | $68.634.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[AC Inversions SpA]] | 1 | $50.000.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Agrosuper SA]] | 1 | $38.400.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Municipalidad de Maipu]] | 1 | $30.972.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Direccion de Finanzas de Carabineros]] | 2 | $29.798.928.198 | **9074** | Alta Concentración (> 2.500) |
| [[Comando de Apoyo a la Fuerza del Ejercito]] | 4 | $28.350.000.000 | **3830** | Alta Concentración (> 2.500) |
| [[Compania Maritima de Chile SA]] | 1 | $24.100.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Cencosud SA]] | 1 | $18.300.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Bancard Inversiones Ltda]] | 2 | $13.550.000.000 | **5237** | Alta Concentración (> 2.500) |
| [[Fuerza Aerea de Chile]] | 1 | $6.000.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[GORE Biobio]] | 2 | $2.803.635.000 | **8372** | Alta Concentración (> 2.500) |
| [[Exportadora y de Gestion Caval Ltda]] | 1 | $2.500.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Riggs Bank y Sociedades Offshore Ashburton]] | 1 | $2.450.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Farmacias Salcobrand SA]] | 1 | $2.180.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[PricewaterhouseCoopers Consultores Auditores SpA]] | 1 | $2.100.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Empresas Penta SA]] | 2 | $1.458.000.000 | **9440** | Alta Concentración (> 2.500) |
| [[Ministerio de Obras Publicas]] | 1 | $1.253.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[SQM SA]] | 3 | $1.127.000.000 | **5131** | Alta Concentración (> 2.500) |
| [[Municipalidad de Cerro Navia]] | 1 | $1.120.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Seremi MINVU Antofagasta]] | 2 | $926.000.000 | **5032** | Alta Concentración (> 2.500) |
| [[Empresas Pullman Bus SA]] | 1 | $898.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Municipalidad de Vitacura]] | 1 | $759.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Instituto Nacional de Deportes Chiledeportes]] | 1 | $417.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Factop SpA]] | 2 | $290.000.000 | **5482** | Alta Concentración (> 2.500) |
| [[Municipalidad de San Ramon]] | 1 | $246.918.500 | **10000** | Alta Concentración (> 2.500) |
| [[Corpesca SA]] | 1 | $233.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[KDM Empresas SA]] | 1 | $186.500.000 | **10000** | Alta Concentración (> 2.500) |
| [[Itelecom Holding Chile SpA]] | 2 | $162.000.000 | **6475** | Alta Concentración (> 2.500) |
| [[Policia de Investigaciones de Chile]] | 1 | $146.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Universidad del Mar]] | 1 | $105.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Senado de la Republica de Chile]] | 1 | $35.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Direccion de Inteligencia Policial de Carabineros]] | 1 | $25.000.000 | **10000** | Alta Concentración (> 2.500) |
| [[Municipalidad de Antofagasta]] | 1 | $23.722.228 | **10000** | Alta Concentración (> 2.500) |
| [[Partido Democrata Cristiano]] | 1 | $20.000.000 | **10000** | Alta Concentración (> 2.500) |

---

## 4. Ranking de Nodos Puente (*Betweenness Centrality* & *PageRank*)

| Posición | Nodo / Entidad | Tipo de Nodo | Intermediación (Brandes) | PageRank | Rol Topológico |
| :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | [[Corte Suprema de Chile]] | `entidad_publica` | `0.2878` | `0.0160` | Conector Interregional / Puente Crítico |
| 2 | [[Bancard Inversiones Ltda]] | `entidad_privada` | `0.1192` | `0.0065` | Conector Interregional / Puente Crítico |
| 3 | [[Servicio Impuestos Internos]] | `entidad_publica` | `0.1157` | `0.0155` | Conector Interregional / Puente Crítico |
| 4 | [[Contraloria General de la Republica]] | `entidad_publica` | `0.0954` | `0.0041` | Conector Interregional / Puente Crítico |
| 5 | [[Augusto Pinochet Ugarte]] | `persona` | `0.0788` | `0.0071` | Conector Interregional / Puente Crítico |
| 6 | [[Unidad de Analisis Financiero]] | `entidad_publica` | `0.0732` | `0.0120` | Conector Interregional / Puente Crítico |
| 7 | [[Agrosuper SA]] | `entidad_privada` | `0.0543` | `0.0035` | Conector Interregional / Puente Crítico |
| 8 | [[Gonzalo Vial Vial]] | `persona` | `0.0543` | `0.0035` | Conector Interregional / Puente Crítico |
| 9 | [[Factop SpA]] | `entidad_privada` | `0.0512` | `0.0057` | Conector Interregional / Puente Crítico |
| 10 | [[Luis Hermosilla Osorio]] | `persona` | `0.0512` | `0.0057` | Conector Interregional / Puente Crítico |

---

## 5. Desglose de Aristas Reificadas en Pesos Chilenos (CLP) y UTM

| Nexo (`TRX`) | Fecha | Tipo | Origen | Destino | Monto (CLP) | Equivalencia (UTM) | Toma de Razón Individual |
| :--- | :---: | :---: | :--- | :--- | ---: | ---: | :---: |
| [[TRX-1971-09-09-Fondos-CIA-ElMercurio-01]] | 1971-09-09 | `desviacion_fondos` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Empresa El Mercurio SAP]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-1972-10-12-Fondos-CIA-Gremios-ParoCamioneros-01]] | 1972-10-12 | `gestion_influencia` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | 1975-08-15 | `desviacion_fondos` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | 1982-08-28 | `desviacion_fondos` | [[Bancard Inversiones Ltda]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | 1989-01-10 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Valmoval Ltda]] | $2.950.000.000 | 48477.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1991-01-31-Movimientos-Patrimoniales-ColoniaDignidad-01]] | 1991-01-31 | `desviacion_fondos` | [[Sociedad Benefactora y Educacional Dignidad]] | [[Servicio Impuestos Internos]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-1994-01-21-Operaciones-Futuros-Codelco-Davilazo-01]] | 1994-01-21 | `transferencia` | [[Corporacion Nacional del Cobre de Chile]] | [[Servicio Impuestos Internos]] | $98.580.000.000 | 1619969.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1994-12-15-Comisiones-Compra-Aviones-Mirage-FACh-01]] | 1994-12-15 | `soborno` | [[Fuerza Aerea de Chile]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | $6.000.000.000 | 98598.3 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]] | 1996-06-12 | `gestion_influencia` | [[Union Democrata Independiente]] | [[Sociedad Benefactora y Educacional Dignidad]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]] | 2000-05-15 | `acuerdo_colusorio` | [[Empresas CMPC SA]] | [[SCA Chile SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2001-08-20-Contratos-MOP-GATE-01]] | 2001-08-20 | `trato_directo` | [[Ministerio de Obras Publicas]] | [[Gestion Ambiental y Territorial SA]] | $1.253.000.000 | 20590.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2002-10-15-Sobornos-Plantas-Revision-Tecnica-Coimas-01]] | 2002-10-15 | `soborno` | [[Partido Democrata Cristiano]] | [[Ministerio de Obras Publicas]] | $20.000.000 | 328.7 UTM | Exento (< 5.000 UTM) |
| [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]] | 2003-10-15 | `desviacion_fondos` | [[Inversiones El Bosque Ltda]] | [[Servicio Impuestos Internos]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2003-11-05-Arista-Politica-Spiniak-01]] | 2003-11-05 | `gestion_influencia` | [[Renovacion Nacional]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2004-07-14-Gastos-Reservados-Riggs-01]] | 2004-07-14 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | $15.800.000.000 | 259642.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01]] | 2005-06-14 | `desviacion_fondos` | [[Sociedad Benefactora y Educacional Dignidad]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]] | 2005-08-10 | `desviacion_fondos` | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[Servicio Impuestos Internos]] | $2.450.000.000 | 40261.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2005-11-10-Desvio-Fondos-Chiledeportes-Publicam-01]] | 2005-11-10 | `adjudicacion` | [[Instituto Nacional de Deportes Chiledeportes]] | [[Publicam Limitada]] | $417.000.000 | 6852.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | 2006-07-24 | `gestion_influencia` | [[Bancard Inversiones Ltda]] | [[Comision para el Mercado Financiero]] | $5.300.000.000 | 87095.1 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]] | 2007-04-10 | `consulta_terceros` | [[Quiroz y Asociados Consultores SpA]] | [[Asociacion de Productores Avicolas de Chile AG]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]] | 2007-11-01 | `acuerdo_colusorio` | [[Farmacias Salcobrand SA]] | [[Farmacias Cruz Verde SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2008-01-15-Colusion-Cuotas-Produccion-Pollos-01]] | 2008-01-15 | `acuerdo_colusorio` | [[Agrosuper SA]] | [[Asociacion de Productores Avicolas de Chile AG]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]] | 2009-11-18 | `factura_falsa` | [[SQM SA]] | [[Bancard Inversiones Ltda]] | $340.000.000 | 5587.2 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]] | 2010-06-15 | `peritaje_forense` | [[Quiroz y Asociados Consultores SpA]] | [[Farmacias Salcobrand SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | 2010-08-19 | `cohecho` | [[SQM SA]] | [[Union Democrata Independiente]] | $730.000.000 | 19588.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01]] | 2010-11-15 | `cohecho_soborno` | [[KDM Empresas SA]] | [[Municipalidad de Maipu]] | $186.500.000 | 3064.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | 2010-12-10 | `trato_directo` | [[Andes Iron SpA]] | [[Bancard Inversiones Ltda]] | $75.500.000.000 | 1240694.8 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | 2011-03-10 | `transferencia` | [[Empresas Penta SA]] | [[Servicio Impuestos Internos]] | $42.000.000 | 690.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2011-04-15-Sobornos-Acreditacion-UniversidadDelMar-CNA-01]] | 2011-04-15 | `soborno` | [[Universidad del Mar]] | [[Comision Nacional de Acreditacion]] | $105.000.000 | 1725.5 UTM | Exento (< 5.000 UTM) |
| [[TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01]] | 2011-06-09 | `transferencia` | [[Empresas La Polar SA]] | [[Comision para el Mercado Financiero]] | $68.634.000.000 | 1127865.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]] | 2011-10-05 | `donacion` | [[SQM SA]] | [[Partido por la Democracia]] | $57.000.000 | 936.7 UTM | Exento (< 5.000 UTM) |
| [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | 2011-12-19 | `desviacion_fondos` | [[Sociedad de Inversiones Pampa Calichera SA]] | [[SQM SA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2012-03-22-Contratos-Residuos-CerroNavia-01]] | 2012-03-22 | `trato_directo` | [[Municipalidad de Cerro Navia]] | [[KDM Empresas SA]] | $1.120.000.000 | 18405.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01]] | 2012-07-11 | `cohecho` | [[Corpesca SA]] | [[Senado de la Republica de Chile]] | $233.000.000 | 3828.9 UTM | Exento (< 5.000 UTM) |
| [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | 2012-11-20 | `gestion_influencia` | [[Bancard Inversiones Ltda]] | [[Contraloria General de la Republica]] | $8.250.000.000 | 135572.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2013-07-15-Boletas-Penta-UDI-01]] | 2013-07-15 | `factura_falsa` | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | $1.260.000.000 | 20705.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2013-09-20-Boletas-Penta-Novoa-01]] | 2013-09-20 | `factura_falsa` | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | $156.000.000 | 2563.6 UTM | Exento (< 5.000 UTM) |
| [[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]] | 2014-02-18 | `cohecho_soborno` | [[]] | [[Municipalidad de Machali]] | $55.030.792 | 904.3 UTM | Exento (< 5.000 UTM) |
| [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]] | 2014-05-20 | `transferencia` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Frasim Ltda]] | $6.100.000.000 | 100241.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-01-29-Facturas-Caval-SII-01]] | 2015-01-29 | `factura_falsa` | [[Exportadora y de Gestion Caval Ltda]] | [[Servicio Impuestos Internos]] | $2.500.000.000 | 41082.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-04-20-Multas-Colusion-Buses-Interurbanos-01]] | 2015-04-20 | `transferencia` | [[Empresas Pullman Bus SA]] | [[Fiscalia Nacional Economica]] | $898.000.000 | 14756.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2014-07-24-Sanciones-SVS-CS-Auditorias-PwC-LaPolar-Cascadas-01]] | 2015-07-24 | `transferencia` | [[PricewaterhouseCoopers Consultores Auditores SpA]] | [[Empresas La Polar SA]] | $2.100.000.000 | 34509.4 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-08-14-GastosReservados-Ejercito-UAF-01]] | 2015-08-14 | `desviacion_fondos` | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Unidad de Analisis Financiero]] | $3.500.000.000 | 57515.7 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2015-10-01-Asesoria-Main-CMDS-Antofagasta-01]] | 2015-10-01 | `contrato` | [[Municipalidad de Antofagasta]] | [[Main Comunicacion Estrategica]] | $23.722.228 | 389.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01]] | 2015-10-29 | `compensacion_reparatoria` | [[Agrosuper SA]] | [[Corte Suprema de Chile]] | $38.400.000.000 | 631028.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2016-03-01-Estafa-Piramidal-Lavado-ACInversions-01]] | 2016-03-01 | `transferencia` | [[AC Inversions SpA]] | [[Unidad de Analisis Financiero]] | $50.000.000.000 | 821652.2 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | 2016-04-03 | `gestion_influencia` | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Servicio Impuestos Internos]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | 2016-04-05 | `desviacion_fondos` | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Unidad de Analisis Financiero]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | 2016-04-15 | `desviacion_fondos` | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | 2016-08-12 | `desviacion_fondos` | [[Fundacion CEMA Chile]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2016-11-10-Fondos-Direccion-Finanzas-Carabineros-01]] | 2016-11-10 | `transferencia` | [[Direccion de Finanzas de Carabineros]] | [[Direccion de Finanzas de Carabineros]] | $28.348.928.198 | 615064.3 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] | 2017-03-03 | `compensacion_reparatoria` | [[Empresas CMPC SA]] | [[Servicio Nacional del Consumidor]] | $97.500.000.000 | 1602221.7 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2017-03-06-Reportes-UAF-Carabineros-01]] | 2017-03-06 | `desviacion_fondos` | [[Direccion de Finanzas de Carabineros]] | [[Unidad de Analisis Financiero]] | $1.450.000.000 | 23827.9 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2017-05-15-Desvio-Gastos-Reservados-PDI-Espinosa-01]] | 2017-05-15 | `transferencia` | [[Policia de Investigaciones de Chile]] | [[Unidad de Analisis Financiero]] | $146.000.000 | 2399.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01]] | 2017-09-01 | `transferencia` | [[Municipalidad de San Ramon]] | [[Unidad de Analisis Financiero]] | $246.918.500 | 4057.6 UTM | Exento (< 5.000 UTM) |
| [[TRX-2017-09-23-Detenciones-OperacionHuracan-01]] | 2017-09-23 | `montaje_policial` | [[Direccion de Inteligencia Policial de Carabineros]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]] | 2017-10-15 | `desvio_fondos_reservados` | [[Direccion de Inteligencia Policial de Carabineros]] | [[Direccion de Inteligencia Policial de Carabineros]] | $25.000.000 | 410.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] | 2018-01-25 | `peritaje_forense` | [[Corte Suprema de Chile]] | [[Direccion de Inteligencia Policial de Carabineros]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2018-09-12-Sobornos-Itelecom-Licitacion-Iquique-01]] | 2018-09-12 | `soborno` | [[Itelecom Holding Chile SpA]] | [[Municipalidad de Iquique]] | $125.000.000 | 2054.1 UTM | Exento (< 5.000 UTM) |
| [[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]] | 2019-05-14 | `cohecho` | [[Itelecom Holding Chile SpA]] | [[Municipalidad de Chillan]] | $37.000.000 | 608.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | 2019-12-11 | `transferencia` | [[Factop SpA]] | [[Senado de la Republica de Chile]] | $190.000.000 | 3122.3 UTM | Exento (< 5.000 UTM) |
| [[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]] | 2020-04-08 | `transferencia` | [[Cencosud SA]] | [[Fiscalia Nacional Economica]] | $18.300.000.000 | 300724.7 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2020-08-14-Multas-Colusion-Navieras-CarCarriers-01]] | 2020-08-14 | `transferencia` | [[Compania Maritima de Chile SA]] | [[Fiscalia Nacional Economica]] | $24.100.000.000 | 396036.3 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]] | 2020-11-25 | `compensacion_reparatoria` | [[Farmacias Salcobrand SA]] | [[Servicio Nacional del Consumidor]] | $2.180.000.000 | 35824.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]] | 2020-12-15 | `transferencia` | [[Municipalidad de Maipu]] | [[Municipalidad de Maipu]] | $30.972.000.000 | 606949.0 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2021-04-15-Subvencion-VitaDeportes-01]] | 2021-04-15 | `transferencia` | [[Municipalidad de Vitacura]] | [[Vita Deportes]] | $759.000.000 | 14711.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]] | 2022-09-04 | `reunion_lobby` | [[Numen Publicidad SpA]] | [[Renovacion Nacional]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-10-03-Convenio-DV-01]] | 2022-10-03 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | $200.000.000 | 3316.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-10-19-Convenio-DV-02]] | 2022-10-19 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | $170.000.000 | 2818.8 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | 2022-10-28 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion ProCultura]] | $500.000.000 | 8290.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | 2022-11-15 | `coordinacion_mensajeria` | [[Factop SpA]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | 2022-11-18 | `convenio_directo` | [[GORE Biobio]] | [[Fundacion ProCultura]] | $2.553.000.000 | 41953.6 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2022-11-29-Convenio-DV-03]] | 2022-11-29 | `convenio_directo` | [[Seremi MINVU Antofagasta]] | [[Fundacion Democracia Viva]] | $56.000.000 | 920.3 UTM | Exento (< 5.000 UTM) |
| [[TRX-2022-12-20-Convenio-EnTi-01]] | 2022-12-20 | `convenio_directo` | [[GORE Biobio]] | [[Fundacion En Ti]] | $250.635.000 | 4098.2 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]] | 2023-01-20 | `trato_directo` | [[Municipalidad de Santiago]] | [[Inmobiliaria San Valentino SpA]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | 2023-02-09 | `llamada` | [[Factop SpA]] | [[Corte Suprema de Chile]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-06-22-Reunion-Audios-01]] | 2023-06-22 | `cohecho` | [[Factop SpA]] | [[Servicio Impuestos Internos]] | $100.000.000 | 1580.7 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | 2023-06-29 | `resolucion_administrativa` | [[Contraloria General de la Republica]] | [[Seremi MINVU Antofagasta]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | 2023-08-25 | `factura_falsa` | [[Factop SpA]] | [[Unidad de Analisis Financiero]] | $0 | 0.0 UTM | Exento (< 5.000 UTM) |
| [[TRX-2023-12-14-Perjuicio-Fiscal-Operacion-Tributos-01]] | 2023-12-14 | `factura_falsa` | [[]] | [[Servicio Impuestos Internos]] | $240.000.000.000 | 3943930.5 UTM | Afecto (>= 5.000 UTM) |
| [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]] | 2025-10-15 | `desviacion_fondos` | [[Senado de la Republica de Chile]] | [[Camila Flores Oporto]] | $35.000.000 | 575.2 UTM | Exento (< 5.000 UTM) |
