---
tipo_nodo: vista_analitica
titulo: "Censo Triádico (Holland-Leinhardt), Lazos de Simmel y Cuadrángulos de Colusión (C4)"
actualizacion_automatica: true
tags:
  - censo-triadico
  - motivos-red
  - lazos-simmel
  - analisis-forense
---

# 🔺 Censo Triádico, Lazos de Simmel y Motivos Superiores ($\Delta, C_4$)

> [!IMPORTANT] Topología de Orden Superior (Higher-Order Network Science)
> Más allá de las aristas diádicas individuales, las redes de corrupción operan mediante **motivos estructurales cerrados**:
> 1. **Clausura Triádica ($\Delta_{uvw}$) y Lazos de Georg Simmel**: Dos nodos unidos además por terceros comunes poseen un *lazo simmeliano* de alta cohesión y confianza clandestina.
> 2. **Cuadrángulos Multi-Canal ($C_4: u - x - v - y - u$)**: Identifican pares de actores que interactúan de manera redundante a través de **múltiples transacciones o intermediarios paralelos** (p. ej. fraccionamiento de contratos o co-financiamiento ilegal).

## 1. Métricas Globales del Censo de Motivos

- **Nodos Operativos Activos ($|V|$)**: `229`
- **2-Caminos Abiertos (*Wedges* $\wedge$)**: `1276`
- **Triángulos Cerrados ($|\Delta|$)**: **`64`**
- **Índice de Transitividad Global ($T = 3|\Delta| / |\wedge|$)**: **`0.1505`**
- **Coeficiente de Clustering Local Promedio ($\bar{C}$)**: **`0.2522`**
- **Aristas Simmelianas (con incrustación $|N(u) \cap N(v)| \ge 1$)**: `164`
- **Pares de Actores en Cuadrángulos Multi-Canal ($C_4$)**: **`54`**

---

## 2. Cuadrángulos de Colusión y Redundancia Multi-Canal ($C_4$)

Pares de actores (`Persona`, `Entidad Pública/Privada`, `Partido`) que comparten **2 o más nodos intermedios**, formando ciclos cerrados de orden 4 ($C_4$):

| # | Actor A ($u$) | Actor B ($v$) | Canales Comunes | Ciclos $C_4$ | Enlace Directo | Nodos Intermediarios Compartidos ($N(u) \cap N(v)$) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`5`** | `10` | `No` | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]], [[TRX-2022-11-29-Convenio-DV-03]], [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] |
| **2** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | **`5`** | `10` | `Sí` | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]], [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]], [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]], [[TRX-2023-06-22-Reunion-Audios-01]], [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] |
| **3** | [[Bancard Inversiones Ltda]] | [[Sebastian Pinera Echenique]] | **`4`** | `6` | `Sí` | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]], [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] |
| **4** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`4`** | `6` | `No` | [[Revolucion Democratica]], [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **5** | [[Alex Smith Leay]] | [[Direccion de Inteligencia Policial de Carabineros]] | **`3`** | `3` | `No` | [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] |
| **6** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`3`** | `3` | `No` | [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]], [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]] |
| **7** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`3`** | `3` | `No` | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **8** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`3`** | `3` | `No` | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]], [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] |
| **9** | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | **`3`** | `3` | `Sí` | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **10** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`3`** | `3` | `No` | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **11** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`3`** | `3` | `No` | [[Carlos Alberto Delano Abbott]], [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] |
| **12** | [[Farmacias Salcobrand SA]] | [[Roberto Belloni Pechini]] | **`3`** | `3` | `No` | [[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]], [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]], [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]] |
| **13** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`3`** | `3` | `No` | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **14** | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | **`3`** | `3` | `Sí` | [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]], [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]], [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] |
| **15** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Agustin Edwards Eastman]] | **`2`** | `1` | `No` | [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]], [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]] |
| **16** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Augusto Pinochet Ugarte]] | **`2`** | `1` | `No` | [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]], [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] |
| **17** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Manuel Contreras Sepulveda]] | **`2`** | `1` | `Sí` | [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]], [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] |
| **18** | [[Agrosuper SA]] | [[Gonzalo Vial Vial]] | **`2`** | `1` | `No` | [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]], [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]] |
| **19** | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | **`2`** | `1` | `Sí` | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]], [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] |
| **20** | [[Alex Smith Leay]] | [[Corte Suprema de Chile]] | **`2`** | `1` | `No` | [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] |
| **21** | [[Asociacion de Productores Avicolas de Chile AG]] | [[Juan Miguel Ovalle Garces]] | **`2`** | `1` | `Sí` | [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]], [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]] |
| **22** | [[Augusto Pinochet Hiriart]] | [[Augusto Pinochet Ugarte]] | **`2`** | `1` | `Sí` | [[Lucia Hiriart Rodriguez]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] |
| **23** | [[Augusto Pinochet Hiriart]] | [[Julio Ponce Lerou]] | **`2`** | `1` | `No` | [[Augusto Pinochet Ugarte]], [[Lucia Hiriart Rodriguez]] |
| **24** | [[Augusto Pinochet Ugarte]] | [[Lucia Hiriart Rodriguez]] | **`2`** | `1` | `Sí` | [[Augusto Pinochet Hiriart]], [[Julio Ponce Lerou]] |
| **25** | [[Augusto Pinochet Ugarte]] | [[Oscar Aitken Lavanchy]] | **`2`** | `1` | `No` | [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] |
| **26** | [[Augusto Pinochet Ugarte]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | **`2`** | `1` | `No` | [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] |
| **27** | [[Augusto Pinochet Ugarte]] | [[Valmoval Ltda]] | **`2`** | `1` | `No` | [[Augusto Pinochet Hiriart]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] |
| **28** | [[Bancard Inversiones Ltda]] | [[Santiago Valdes Gutierrez]] | **`2`** | `1` | `No` | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] |
| **29** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | **`2`** | `1` | `Sí` | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] |
| **30** | [[Carlos Alberto Delano Abbott]] | [[Jovino Novoa Vasquez]] | **`2`** | `1` | `No` | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]], [[Union Democrata Independiente]] |
| **31** | [[Carlos Alberto Delano Abbott]] | [[Pablo Longueira Montes]] | **`2`** | `1` | `No` | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[Union Democrata Independiente]] |
| **32** | [[Carlos Alberto Delano Abbott]] | [[Union Democrata Independiente]] | **`2`** | `1` | `Sí` | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] |
| **33** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | [[Pablo Wagner San Martin]] | **`2`** | `1` | `No` | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]], [[Union Democrata Independiente]] |
| **34** | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Juan Miguel Fuente-Alba Poblete]] | **`2`** | `1` | `No` | [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]], [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]] |
| **35** | [[Corte Suprema de Chile]] | [[Direccion de Inteligencia Policial de Carabineros]] | **`2`** | `1` | `No` | [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] |
| **36** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`2`** | `1` | `No` | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]], [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] |
| **37** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`2`** | `1` | `No` | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]], [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] |
| **38** | [[Direccion de Finanzas de Carabineros]] | [[Flavio Echeverria Cortez]] | **`2`** | `1` | `No` | [[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]], [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]] |
| **39** | [[Eliodoro Matte Larrain]] | [[Empresas CMPC SA]] | **`2`** | `1` | `No` | [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]], [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] |
| **40** | [[Eliodoro Matte Larrain]] | [[Gabriel Ruiz-Tagle Serrano]] | **`2`** | `1` | `No` | [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]], [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] |
| **41** | [[Empresas CMPC SA]] | [[Gabriel Ruiz-Tagle Serrano]] | **`2`** | `1` | `No` | [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]], [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] |
| **42** | [[GORE Biobio]] | [[Rodrigo Diaz Worner]] | **`2`** | `1` | `No` | [[TRX-2022-11-18-Convenio-ProCultura-Biobio]], [[TRX-2022-12-20-Convenio-EnTi-01]] |
| **43** | [[Jorge Quiroz Castro]] | [[Quiroz y Asociados Consultores SpA]] | **`2`** | `1` | `Sí` | [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]], [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]] |
| **44** | [[Jorge Zepeda Arancibia]] | [[Paul Schafer Schneider]] | **`2`** | `1` | `No` | [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]], [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] |
| **45** | [[Jorge Zepeda Arancibia]] | [[Sociedad Benefactora y Educacional Dignidad]] | **`2`** | `1` | `No` | [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]], [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] |
| **46** | [[KDM Empresas SA]] | [[Marcelo Torres Ferrari]] | **`2`** | `1` | `No` | [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]], [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]] |
| **47** | [[Lucia Hiriart Rodriguez]] | [[Sergio Munoz Gajardo]] | **`2`** | `1` | `No` | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]], [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] |
| **48** | [[Luis Plaza Sanchez]] | [[Marcelo Torres Ferrari]] | **`2`** | `1` | `No` | [[Renovacion Nacional]], [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]] |
| **49** | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | **`2`** | `1` | `Sí` | [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] |
| **50** | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | **`2`** | `1` | `Sí` | [[TRX-2010-08-19-Correo-Royalty-SQM-01]], [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] |
| **51** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | **`2`** | `1` | `Sí` | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]], [[TRX-2010-08-19-Correo-Royalty-SQM-01]] |
| **52** | [[Paul Schafer Schneider]] | [[Sociedad Benefactora y Educacional Dignidad]] | **`2`** | `1` | `Sí` | [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]], [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] |
| **53** | [[Santiago Valdes Gutierrez]] | [[Sebastian Pinera Echenique]] | **`2`** | `1` | `No` | [[Renovacion Nacional]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] |
| **54** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`2`** | `1` | `No` | [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]], [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] |

---

## 3. Lazos Fuertes de Simmel (Aristas con Mayor Incrustación Triádica)

| # | Nodo A ($u$) | Nodo B ($v$) | Fuerza Simmeliana ($|N(u) \cap N(v)|$) | Terceros Comunes en el Triángulo |
| :---: | :--- | :--- | :---: | :--- |
| **1** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | **`5`** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]], [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]], [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]], [[TRX-2023-06-22-Reunion-Audios-01]], [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] |
| **2** | [[Bancard Inversiones Ltda]] | [[Sebastian Pinera Echenique]] | **`4`** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]], [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] |
| **3** | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | **`3`** | [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **4** | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | **`3`** | [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]], [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]], [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] |
| **5** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Manuel Contreras Sepulveda]] | **`2`** | [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]], [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] |
| **6** | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | **`2`** | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]], [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] |
| **7** | [[Asociacion de Productores Avicolas de Chile AG]] | [[Juan Miguel Ovalle Garces]] | **`2`** | [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]], [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]] |
| **8** | [[Augusto Pinochet Hiriart]] | [[Augusto Pinochet Ugarte]] | **`2`** | [[Lucia Hiriart Rodriguez]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] |
| **9** | [[Augusto Pinochet Hiriart]] | [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | **`2`** | [[Augusto Pinochet Ugarte]], [[Valmoval Ltda]] |
| **10** | [[Augusto Pinochet Ugarte]] | [[Lucia Hiriart Rodriguez]] | **`2`** | [[Augusto Pinochet Hiriart]], [[Julio Ponce Lerou]] |
| **11** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | **`2`** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] |
| **12** | [[Carlos Alberto Delano Abbott]] | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | **`2`** | [[Empresas Penta SA]], [[Union Democrata Independiente]] |
| **13** | [[Carlos Alberto Delano Abbott]] | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | **`2`** | [[Empresas Penta SA]], [[Union Democrata Independiente]] |
| **14** | [[Carlos Alberto Delano Abbott]] | [[Union Democrata Independiente]] | **`2`** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] |
| **15** | [[Jorge Quiroz Castro]] | [[Quiroz y Asociados Consultores SpA]] | **`2`** | [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]], [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]] |
| **16** | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | **`2`** | [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] |
| **17** | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | **`2`** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]], [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] |
| **18** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | **`2`** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]], [[TRX-2010-08-19-Correo-Royalty-SQM-01]] |
| **19** | [[Paul Schafer Schneider]] | [[Sociedad Benefactora y Educacional Dignidad]] | **`2`** | [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]], [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] |
| **20** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | [[Union Democrata Independiente]] | **`2`** | [[Carlos Alberto Delano Abbott]], [[Pablo Longueira Montes]] |

---

## 4. Catálogo de Triángulos Cerrados Detectados ($\Delta_{uvw}$)

| # | Vértice 1 | Vértice 2 | Vértice 3 | Arquetipo Estructural del Motivo |
| :---: | :--- | :--- | :--- | :--- |
| **1** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Manuel Contreras Sepulveda]] | [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **2** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Manuel Contreras Sepulveda]] | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **3** | [[Agustin Edwards Eastman]] | [[Empresa El Mercurio SAP]] | [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **4** | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **5** | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **6** | [[Andes Iron SpA]] | [[Carlos Alberto Delano Abbott]] | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **7** | [[Asociacion de Productores Avicolas de Chile AG]] | [[Juan Miguel Ovalle Garces]] | [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **8** | [[Asociacion de Productores Avicolas de Chile AG]] | [[Juan Miguel Ovalle Garces]] | [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **9** | [[Augusto Pinochet Hiriart]] | [[Augusto Pinochet Ugarte]] | [[Lucia Hiriart Rodriguez]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **10** | [[Augusto Pinochet Hiriart]] | [[Augusto Pinochet Ugarte]] | [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **11** | [[Augusto Pinochet Hiriart]] | [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | [[Valmoval Ltda]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **12** | [[Augusto Pinochet Ugarte]] | [[Julio Ponce Lerou]] | [[Lucia Hiriart Rodriguez]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **13** | [[Bancard Inversiones Ltda]] | [[Sebastian Pinera Echenique]] | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **14** | [[Bancard Inversiones Ltda]] | [[Sebastian Pinera Echenique]] | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **15** | [[Bancard Inversiones Ltda]] | [[Sebastian Pinera Echenique]] | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **16** | [[Bancard Inversiones Ltda]] | [[Sebastian Pinera Echenique]] | [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **17** | [[Camila Polizzi Fonceca]] | [[Fundacion En Ti]] | [[TRX-2022-12-20-Convenio-EnTi-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **18** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **19** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **20** | [[Carlos Alberto Delano Abbott]] | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **21** | [[Carlos Alberto Delano Abbott]] | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **22** | [[Carlos Cruz Lorenzen]] | [[Ministerio de Obras Publicas]] | [[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **23** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | [[Cathy Barriga Guerra]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **24** | [[Carlos Pavez Tolosa]] | [[Comision para el Mercado Financiero]] | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **25** | [[Claudio Spiniak Vilensky]] | [[Inversiones El Bosque Ltda]] | [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **26** | [[Contraloria General de la Republica]] | [[Jorge Bermudez Soto]] | [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **27** | [[Corpesca SA]] | [[Francisco Mujica Ortuzar]] | [[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **28** | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | [[TRX-2022-10-03-Convenio-DV-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **29** | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | [[TRX-2022-10-19-Convenio-DV-02]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **30** | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | [[TRX-2022-11-29-Convenio-DV-03]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **31** | [[Domingo Prieto Urrejola]] | [[TRX-2021-04-15-Subvencion-VitaDeportes-01]] | [[Vita Deportes]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **32** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **33** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **34** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **35** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | [[TRX-2023-06-22-Reunion-Audios-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **36** | [[Factop SpA]] | [[Luis Hermosilla Osorio]] | [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **37** | [[Felipe Sanchez Perez]] | [[Inmobiliaria San Valentino SpA]] | [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **38** | [[Fernando Cerimedo]] | [[Numen Publicidad SpA]] | [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **39** | [[Fernando Leon Steffens]] | [[KDM Empresas SA]] | [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **40** | [[Frasim Ltda]] | [[Jozo Santic Palomino]] | [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **41** | [[Fundacion CEMA Chile]] | [[Lucia Hiriart Rodriguez]] | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **42** | [[Gestion Ambiental y Territorial SA]] | [[Hector Pena Veliz]] | [[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **43** | [[Gonzalo Delaveau Swett]] | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **44** | [[Hernan Larrain Fernandez]] | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **45** | [[Iraci Hassler Jacob]] | [[Municipalidad de Santiago]] | [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **46** | [[Itelecom Holding Chile SpA]] | [[Leon Marcelo Lefort Hernandez]] | [[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **47** | [[Javier Cruz Tamburrino]] | [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]] | [[Unidad de Analisis Financiero]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **48** | [[Javier Cruz Tamburrino]] | [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]] | [[Unidad de Analisis Financiero]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **49** | [[Javier Cruz Tamburrino]] | [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | [[Unidad de Analisis Financiero]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **50** | [[Jorge Quiroz Castro]] | [[Quiroz y Asociados Consultores SpA]] | [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **51** | [[Jorge Quiroz Castro]] | [[Quiroz y Asociados Consultores SpA]] | [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **52** | [[Jorge Silva Menares]] | [[Municipalidad de Machali]] | [[TRX-2014-02-18-Soborno-Caval-Machali-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **53** | [[Jovino Novoa Vasquez]] | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **54** | [[Julio Ponce Lerou]] | [[Sociedad de Inversiones Pampa Calichera SA]] | [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **55** | [[Luis Plaza Sanchez]] | [[Municipalidad de Cerro Navia]] | [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **56** | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **57** | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **58** | [[Pablo Longueira Montes]] | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **59** | [[Pablo Longueira Montes]] | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | [[Union Democrata Independiente]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
| **60** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **61** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **62** | [[Paul Schafer Schneider]] | [[Sociedad Benefactora y Educacional Dignidad]] | [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **63** | [[Paul Schafer Schneider]] | [[Sociedad Benefactora y Educacional Dignidad]] | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | Triángulo Operativo Directo (`Entidad ↔ Persona ↔ TRX`) |
| **64** | [[Pia Guzman Mena]] | [[Renovacion Nacional]] | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | Triángulo de Endogamia Partidaria (`Partido ↔ Actor ↔ TRX/Entidad`) |
