---
tipo_nodo: vista_analitica
titulo: "Detección de Agrupamientos de la red y Modularidad (Newman-Girvan Q)"
actualizacion_automatica: true
tags:
  - comunidades
  - modularidad-newman
  - analisis-de-redes
---

# Agrupamientos de la Red y Modularidad ($Q$)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.
>
> Un agrupamiento es un conjunto de nodos densamente conectados en el grafo, casi siempre porque aparecen en la misma causa o expediente. **No es una organización, una asociación ni una red delictiva.**


> [!NOTE] Análisis de modularidad (Clauset-Newman-Moore & Guimerà-Amaral)
> Esta vista aplica maximización aglomerativa de **Modularidad de Newman-Girvan ($Q$)** (algoritmo de Clauset-Newman-Moore sobre la red de actores, causas y transacciones, excluyendo artículos penales genéricos) para particionar el grafo en **Agrupamientos**, y calcula el **Coeficiente de Participación ($P_i$)** de Guimerà & Amaral (2005) para descubrir los *brokers* que conectan agrupamientos criminales o políticas distintas.

## 1. Indicadores Globales de Partición

- **Nodos Operativos Analizados**: `308`
- **Modularidad Global de Newman-Girvan ($Q$)**: `0.8288` *(Valores $Q > 0.70$ indican alta compartimentación celular con puentes específicos de articulación)*
- **Total de Agrupamientos Detectadas**: `20`
- **Enlaces Puente Inter-Comunidad Detectados**: `44`
- **Nodos Articuladores Inter-Agrupamiento ($P_i > 0$)**: `58`

---

## 2. Brokers Inter-Comunidad (Coeficiente de Participación $P_i > 0$)

| Pos | Nodo Articulador | Tipo | Comunidad Base | Grado ($k_i$) | Coef. Participación ($P_i$) | Rol Topológico |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) | `10` | **`0.8000`** | Hub Conector Multi-Agrupamiento |
| **2** | [[Sergio Munoz Gajardo]] | `persona` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.7200`** | Hub Conector Multi-Agrupamiento |
| **3** | [[Servicio Impuestos Internos]] | `entidad_publica` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `9` | **`0.6420`** | Hub Conector Multi-Agrupamiento |
| **4** | [[Comando de Apoyo a la Fuerza del Ejercito]] | `entidad_publica` | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `5` | **`0.6400`** | Hub Conector Multi-Agrupamiento |
| **5** | [[Unidad de Analisis Financiero]] | `entidad_publica` | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `8` | **`0.5625`** | Hub Conector Multi-Agrupamiento |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.5600`** | Hub Conector Multi-Agrupamiento |
| **7** | [[TRX-2003-11-05-Arista-Politica-Spiniak-01]] | `nexo_transaccion` | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `5` | **`0.5600`** | Hub Conector Multi-Agrupamiento |
| **8** | [[TRX-2004-07-14-Gastos-Reservados-Riggs-01]] | `nexo_transaccion` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.5600`** | Hub Conector Multi-Agrupamiento |
| **9** | [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | `nexo_transaccion` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.5600`** | Hub Conector Multi-Agrupamiento |
| **10** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `nexo_transaccion` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.5600`** | Hub Conector Multi-Agrupamiento |
| **11** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `5` | **`0.5600`** | Hub Conector Multi-Agrupamiento |
| **12** | [[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]] | `nexo_transaccion` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `4` | **`0.5000`** | Hub Conector Multi-Agrupamiento |
| **13** | [[Caso Spiniak]] | `causa_judicial` | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `2` | **`0.5000`** | Hub Conector Multi-Agrupamiento |
| **14** | [[Jaime Orpis Bouchon]] | `persona` | Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `2` | **`0.5000`** | Hub Conector Multi-Agrupamiento |
| **15** | [[Karen Rojo Venegas]] | `persona` | Agrupamiento #17 (Caso Fraude en Municipalidad de Antofagasta) | `2` | **`0.5000`** | Hub Conector Multi-Agrupamiento |
| **16** | [[Servicio Nacional del Consumidor]] | `entidad_publica` | Agrupamiento #07 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) | `2` | **`0.5000`** | Hub Conector Multi-Agrupamiento |
| **17** | [[Union Democrata Independiente]] | `partido_politico` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `17` | **`0.4844`** | Hub Conector Multi-Agrupamiento |
| **18** | [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]] | `nexo_transaccion` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.4800`** | Hub Conector Multi-Agrupamiento |
| **19** | [[Beltran Urenda Salamanca]] | `persona` | Agrupamiento #09 (Caso Colusion de las Navieras / Caso Colusion de los Buses Interurbanos) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **20** | [[Camila Flores Oporto]] | `persona` | Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **21** | [[Carlos Pavez Tolosa]] | `persona` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **22** | [[Caso Colonia Dignidad]] | `causa_judicial` | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **23** | [[Cathy Barriga Guerra]] | `persona` | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **24** | [[Comision para el Mercado Financiero]] | `entidad_publica` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **25** | [[Contraloria General de la Republica]] | `entidad_publica` | Agrupamiento #08 (Caso Convenios) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **26** | [[Gabriel Ruiz-Tagle Serrano]] | `persona` | Agrupamiento #15 (Caso Colusion del Papel Tissue) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **27** | [[Partido por la Democracia]] | `partido_politico` | Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **28** | [[Patricio Rodrigo Salinas]] | `persona` | Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **29** | [[Santiago Valdes Gutierrez]] | `persona` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `3` | **`0.4444`** | Hub Conector Multi-Agrupamiento |
| **30** | [[Renovacion Nacional]] | `partido_politico` | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `11` | **`0.4298`** | Hub Conector Multi-Agrupamiento |
| **31** | [[Agustin Edwards Eastman]] | `persona` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `4` | **`0.3750`** | Hub Conector Multi-Agrupamiento |
| **32** | [[Andres Chadwick Pinera]] | `persona` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `4` | **`0.3750`** | Hub Conector Multi-Agrupamiento |
| **33** | [[Senado de la Republica de Chile]] | `entidad_publica` | Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `4` | **`0.3750`** | Hub Conector Multi-Agrupamiento |
| **34** | [[Sociedad Benefactora y Educacional Dignidad]] | `entidad_privada` | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) | `4` | **`0.3750`** | Hub Conector Multi-Agrupamiento |
| **35** | [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | `nexo_transaccion` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `4` | **`0.3750`** | Hub Conector Multi-Agrupamiento |
| **36** | [[SQM SA]] | `entidad_privada` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **37** | [[TRX-1972-10-12-Fondos-CIA-Gremios-ParoCamioneros-01]] | `nexo_transaccion` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **38** | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | `nexo_transaccion` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **39** | [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | `nexo_transaccion` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **40** | [[TRX-1991-01-31-Movimientos-Patrimoniales-ColoniaDignidad-01]] | `nexo_transaccion` | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **41** | [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]] | `nexo_transaccion` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **42** | [[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]] | `nexo_transaccion` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **43** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **44** | [[TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01]] | `nexo_transaccion` | Agrupamiento #14 (Caso La Polar) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **45** | [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | `nexo_transaccion` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **46** | [[TRX-2015-01-29-Facturas-Caval-SII-01]] | `nexo_transaccion` | Agrupamiento #13 (Caso Caval) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **47** | [[TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01]] | `nexo_transaccion` | Agrupamiento #07 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **48** | [[TRX-2016-03-01-Estafa-Piramidal-Lavado-ACInversions-01]] | `nexo_transaccion` | Agrupamiento #19 (Caso AC Inversions) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **49** | [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | `nexo_transaccion` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **50** | [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | `nexo_transaccion` | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **51** | [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] | `nexo_transaccion` | Agrupamiento #15 (Caso Colusion del Papel Tissue) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **52** | [[TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01]] | `nexo_transaccion` | Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **53** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `nexo_transaccion` | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **54** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `nexo_transaccion` | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **55** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `5` | **`0.3200`** | Hub Conector Multi-Agrupamiento |
| **56** | [[Augusto Pinochet Ugarte]] | `persona` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `11` | **`0.2975`** | Puente Inter-Clúster |
| **57** | [[Sebastian Pinera Echenique]] | `persona` | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `8` | **`0.2188`** | Puente Inter-Clúster |
| **58** | [[Lucia Hiriart Rodriguez]] | `persona` | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `9` | **`0.1975`** | Puente Inter-Clúster |

---

## 3. Puentes Estructurales entre Agrupamientos

| Nodo A | Agrupamiento A | Relación | Nodo B | Agrupamiento B |
| :--- | :--- | :---: | :--- | :--- |
| [[Camila Flores Oporto]] | Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `vinculo` | [[Renovacion Nacional]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) |
| [[Cathy Barriga Guerra]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `vinculo` | [[Union Democrata Independiente]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[Gabriel Ruiz-Tagle Serrano]] | Agrupamiento #15 (Caso Colusion del Papel Tissue) | `vinculo` | [[Union Democrata Independiente]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[Jaime Orpis Bouchon]] | Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `vinculo` | [[Union Democrata Independiente]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[Santiago Valdes Gutierrez]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Renovacion Nacional]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) |
| [[Sebastian Pinera Echenique]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Renovacion Nacional]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) |
| [[Karen Rojo Venegas]] | Agrupamiento #17 (Caso Fraude en Municipalidad de Antofagasta) | `vinculo` | [[Union Democrata Independiente]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[Beltran Urenda Salamanca]] | Agrupamiento #09 (Caso Colusion de las Navieras / Caso Colusion de los Buses Interurbanos) | `vinculo` | [[Union Democrata Independiente]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Comando de Apoyo a la Fuerza del Ejercito]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) |
| [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Servicio Impuestos Internos]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[SQM SA]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Contraloria General de la Republica]] | Agrupamiento #08 (Caso Convenios) |
| [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] | Agrupamiento #15 (Caso Colusion del Papel Tissue) | `vinculo` | [[Servicio Nacional del Consumidor]] | Agrupamiento #07 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) |
| [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `vinculo` | [[Senado de la Republica de Chile]] | Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) |
| [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `vinculo` | [[Andres Chadwick Pinera]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-2023-06-22-Reunion-Audios-01]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) | `vinculo` | [[Servicio Impuestos Internos]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-1972-10-12-Fondos-CIA-Gremios-ParoCamioneros-01]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Comando de Apoyo a la Fuerza del Ejercito]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) |
| [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Sergio Munoz Gajardo]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-1991-01-31-Movimientos-Patrimoniales-ColoniaDignidad-01]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) | `vinculo` | [[Servicio Impuestos Internos]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Sociedad Benefactora y Educacional Dignidad]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Caso Colonia Dignidad]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Caso Spiniak]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) |
| [[TRX-2003-11-05-Arista-Politica-Spiniak-01]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-2003-11-05-Arista-Politica-Spiniak-01]] | Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu) | `vinculo` | [[Sergio Munoz Gajardo]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2004-07-14-Gastos-Reservados-Riggs-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Comando de Apoyo a la Fuerza del Ejercito]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) |
| [[TRX-2004-07-14-Gastos-Reservados-Riggs-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Augusto Pinochet Ugarte]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Lucia Hiriart Rodriguez]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2015-01-29-Facturas-Caval-SII-01]] | Agrupamiento #13 (Caso Caval) | `vinculo` | [[Servicio Impuestos Internos]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01]] | Agrupamiento #07 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Carlos Pavez Tolosa]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Unidad de Analisis Financiero]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) |
| [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Agustin Edwards Eastman]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Augusto Pinochet Ugarte]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Corte Suprema de Chile]] | Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan) |
| [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Sergio Munoz Gajardo]] | Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01]] | Agrupamiento #14 (Caso La Polar) | `vinculo` | [[Comision para el Mercado Financiero]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01]] | Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas) | `vinculo` | [[Unidad de Analisis Financiero]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) |
| [[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Partido por la Democracia]] | Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas) |
| [[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]] | Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Patricio Rodrigo Salinas]] | Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas) |
| [[TRX-2016-03-01-Estafa-Piramidal-Lavado-ACInversions-01]] | Agrupamiento #19 (Caso AC Inversions) | `vinculo` | [[Unidad de Analisis Financiero]] | Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa) |

---

## 4. Radiografía de Agrupamientos Detectadas

### Agrupamiento #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca)
- **Tamaño del Clúster**: `35` nodos | **Flujo Registrado en la Agrupamiento**: `$91.635.000.000 CLP`
- **Personas Involucradas (13)**: [[Andres Chadwick Pinera]], [[Carlos Alberto Delano Abbott]], [[Carlos Eugenio Lavin Garcia-Huidobro]], [[Carlos Pavez Tolosa]], [[Hartmut Hopp Miottel]], [[Hernan Larrain Fernandez]], [[Jovino Novoa Vasquez]], [[Loreto Letelier]], [[Pablo Longueira Montes]], [[Pablo Wagner San Martin]], [[Patricio Contesse Gonzalez]], [[Santiago Valdes Gutierrez]], [[Sebastian Pinera Echenique]]
- **Entidades Públicas/Privadas (6)**: [[Andes Iron SpA]], [[Bancard Inversiones Ltda]], [[Comision para el Mercado Financiero]], [[Empresas Penta SA]], [[SQM SA]], [[Union Democrata Independiente]]
- **Transacciones Reificadas (11)**: [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]], [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]], [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]], [[TRX-2010-08-19-Correo-Royalty-SQM-01]], [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]], [[TRX-2011-03-10-Pagos-Penta-Wagner-01]], [[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]], [[TRX-2013-07-15-Boletas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Penta-Novoa-01]]

### Agrupamiento #02 (Caso Audios / Caso Gastos Reservados PDI Hector Espinosa)
- **Tamaño del Clúster**: `30` nodos | **Flujo Registrado en la Agrupamiento**: `$39.834.928.198 CLP`
- **Personas Involucradas (10)**: [[Angela Vivanco Martinez]], [[Flavio Echeverria Cortez]], [[Gabriel Zaliasnik Schilkrut]], [[Hector Espinosa Valenzuela]], [[Jaime Paz Meneses]], [[Javier Cruz Tamburrino]], [[Jozo Santic Palomino]], [[Juan Miguel Fuente-Alba Poblete]], [[Leonarda Villalobos Muth]], [[Luis Hermosilla Osorio]]
- **Entidades Públicas/Privadas (6)**: [[Comando de Apoyo a la Fuerza del Ejercito]], [[Direccion de Finanzas de Carabineros]], [[Factop SpA]], [[Frasim Ltda]], [[Policia de Investigaciones de Chile]], [[Unidad de Analisis Financiero]]
- **Transacciones Reificadas (10)**: [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]], [[TRX-2015-08-14-GastosReservados-Ejercito-UAF-01]], [[TRX-2016-11-10-Fondos-Direccion-Finanzas-Carabineros-01]], [[TRX-2017-03-06-Reportes-UAF-Carabineros-01]], [[TRX-2017-05-15-Desvio-Gastos-Reservados-PDI-Espinosa-01]], [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]], [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]], [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]], [[TRX-2023-06-22-Reunion-Audios-01]], [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]]

### Agrupamiento #03 (Caso Codelco Davilazo / Caso Megafraude Tributario Operacion Tributos)
- **Tamaño del Clúster**: `28` nodos | **Flujo Registrado en la Agrupamiento**: `$362.830.000.000 CLP`
- **Personas Involucradas (8)**: [[Alfredo Ovalle Rodriguez]], [[Claudio Spiniak Vilensky]], [[Gonzalo Delaveau Swett]], [[Jaime Estay Viveros]], [[Juan Pablo Davila Silva]], [[Oscar Aitken Lavanchy]], [[Ramon Vega Hidalgo]], [[Sergio Munoz Gajardo]]
- **Entidades Públicas/Privadas (6)**: [[Corporacion Nacional del Cobre de Chile]], [[Fuerza Aerea de Chile]], [[Inversiones El Bosque Ltda]], [[Mossack Fonseca y Sociedades Offshore Panama]], [[Riggs Bank y Sociedades Offshore Ashburton]], [[Servicio Impuestos Internos]]
- **Transacciones Reificadas (9)**: [[TRX-1994-01-21-Operaciones-Futuros-Codelco-Davilazo-01]], [[TRX-1994-12-15-Comisiones-Compra-Aviones-Mirage-FACh-01]], [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]], [[TRX-2004-07-14-Gastos-Reservados-Riggs-01]], [[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]], [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]], [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]], [[TRX-2023-12-14-Perjuicio-Fiscal-Operacion-Tributos-01]]

### Agrupamiento #04 (Caso Basura / Caso Municipalidad de Maipu)
- **Tamaño del Clúster**: `27` nodos | **Flujo Registrado en la Agrupamiento**: `$33.037.500.000 CLP`
- **Personas Involucradas (9)**: [[Cathy Barriga Guerra]], [[Domingo Prieto Urrejola]], [[Fernando Cerimedo]], [[Fernando Leon Steffens]], [[Luis Plaza Sanchez]], [[Marcelo Torres Ferrari]], [[Percy Marin Vera]], [[Pia Guzman Mena]], [[Raul Torrealba del Pedregal]]
- **Entidades Públicas/Privadas (7)**: [[KDM Empresas SA]], [[Municipalidad de Cerro Navia]], [[Municipalidad de Maipu]], [[Municipalidad de Vitacura]], [[Numen Publicidad SpA]], [[Renovacion Nacional]], [[Vita Deportes]]
- **Transacciones Reificadas (6)**: [[TRX-2003-11-05-Arista-Politica-Spiniak-01]], [[TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01]], [[TRX-2012-03-22-Contratos-Residuos-CerroNavia-01]], [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]], [[TRX-2021-04-15-Subvencion-VitaDeportes-01]], [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]

### Agrupamiento #05 (Caso CNA Acreditaciones Universitarias / Caso Coimas)
- **Tamaño del Clúster**: `25` nodos | **Flujo Registrado en la Agrupamiento**: `$1.624.918.500 CLP`
- **Personas Involucradas (8)**: [[Carlos Cruz Lorenzen]], [[Cristian Pareto Vergara]], [[Hector Pena Veliz]], [[Hector Zuniga Rogers]], [[Luis Eugenio Diaz Corvalan]], [[Miguel Angel Aguilera Sanhueza]], [[Patricio Rodrigo Salinas]], [[Victor Manuel Rebolledo Gonzalez]]
- **Entidades Públicas/Privadas (9)**: [[Comision Nacional de Acreditacion]], [[Corporacion Chile Ambiente]], [[Gestion Ambiental y Territorial SA]], [[Ministerio de Obras Publicas]], [[Municipalidad de San Ramon]], [[Partido Democrata Cristiano]], [[Partido Socialista de Chile]], [[Partido por la Democracia]], [[Universidad del Mar]]
- **Transacciones Reificadas (4)**: [[TRX-2001-08-20-Contratos-MOP-GATE-01]], [[TRX-2002-10-15-Sobornos-Plantas-Revision-Tecnica-Coimas-01]], [[TRX-2011-04-15-Sobornos-Acreditacion-UniversidadDelMar-CNA-01]], [[TRX-2017-09-01-Enriquecimiento-Ilicito-y-Lavado-SanRamon-01]]

### Agrupamiento #06 (Caso CEMA Chile / Caso Cascadas)
- **Tamaño del Clúster**: `21` nodos | **Flujo Registrado en la Agrupamiento**: `$2.950.000.000 CLP`
- **Personas Involucradas (6)**: [[Agustin Edwards Eastman]], [[Augusto Pinochet Hiriart]], [[Augusto Pinochet Ugarte]], [[Julio Ponce Lerou]], [[Lucia Hiriart Rodriguez]], [[Manuel Contreras Sepulveda]]
- **Entidades Públicas/Privadas (5)**: [[Agencia Central de Inteligencia CIA y Escuela de las Americas]], [[Empresa El Mercurio SAP]], [[Fundacion CEMA Chile]], [[Sociedad de Inversiones Pampa Calichera SA]], [[Valmoval Ltda]]
- **Transacciones Reificadas (6)**: [[TRX-1971-09-09-Fondos-CIA-ElMercurio-01]], [[TRX-1972-10-12-Fondos-CIA-Gremios-ParoCamioneros-01]], [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]], [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]], [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]

### Agrupamiento #07 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos)
- **Tamaño del Clúster**: `21` nodos | **Flujo Registrado en la Agrupamiento**: `$40.580.000.000 CLP`
- **Personas Involucradas (7)**: [[Gonzalo Vial Vial]], [[Guillermo Harding Alvarado]], [[Jorge Quiroz Castro]], [[Jose Codner Chijner]], [[Juan Miguel Ovalle Garces]], [[Manuel Ariztia Ruiz]], [[Roberto Belloni Pechini]]
- **Entidades Públicas/Privadas (6)**: [[Agrosuper SA]], [[Asociacion de Productores Avicolas de Chile AG]], [[Farmacias Cruz Verde SA]], [[Farmacias Salcobrand SA]], [[Quiroz y Asociados Consultores SpA]], [[Servicio Nacional del Consumidor]]
- **Transacciones Reificadas (6)**: [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]], [[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]], [[TRX-2008-01-15-Colusion-Cuotas-Produccion-Pollos-01]], [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]], [[TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01]], [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]

### Agrupamiento #08 (Caso Convenios)
- **Tamaño del Clúster**: `21` nodos | **Flujo Registrado en la Agrupamiento**: `$3.729.635.000 CLP`
- **Personas Involucradas (6)**: [[Alberto Larrain Salas]], [[Camila Polizzi Fonceca]], [[Carlos Contreras Gutierrez]], [[Daniel Andrade Schwarze]], [[Jorge Bermudez Soto]], [[Rodrigo Diaz Worner]]
- **Entidades Públicas/Privadas (7)**: [[Contraloria General de la Republica]], [[Fundacion Democracia Viva]], [[Fundacion En Ti]], [[Fundacion ProCultura]], [[GORE Biobio]], [[Revolucion Democratica]], [[Seremi MINVU Antofagasta]]
- **Transacciones Reificadas (7)**: [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]], [[TRX-2022-11-18-Convenio-ProCultura-Biobio]], [[TRX-2022-11-29-Convenio-DV-03]], [[TRX-2022-12-20-Convenio-EnTi-01]], [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]]

### Agrupamiento #09 (Caso Colusion de las Navieras / Caso Colusion de los Buses Interurbanos)
- **Tamaño del Clúster**: `19` nodos | **Flujo Registrado en la Agrupamiento**: `$43.298.000.000 CLP`
- **Personas Involucradas (6)**: [[Andronico Luksic Craig]], [[Beltran Urenda Salamanca]], [[Enrique Ostale Brito]], [[Horst Paulmann Kemna]], [[Jesus Diez Gonzalez]], [[Pedro Farias Soto]]
- **Entidades Públicas/Privadas (7)**: [[Cencosud SA]], [[Compania Maritima de Chile SA]], [[Compania Sud Americana de Vapores SA]], [[Empresas Pullman Bus SA]], [[Empresas Tur Bus SA]], [[Fiscalia Nacional Economica]], [[Walmart Chile SA]]
- **Transacciones Reificadas (3)**: [[TRX-2015-04-20-Multas-Colusion-Buses-Interurbanos-01]], [[TRX-2020-04-08-Multas-Colusion-Supermercados-Pollo-01]], [[TRX-2020-08-14-Multas-Colusion-Navieras-CarCarriers-01]]

### Agrupamiento #10 (Caso Colonia Dignidad / Caso Operacion Huracan)
- **Tamaño del Clúster**: `16` nodos | **Flujo Registrado en la Agrupamiento**: `$25.000.000 CLP`
- **Personas Involucradas (6)**: [[Alex Smith Leay]], [[Gonzalo Blu Rodriguez]], [[Jorge Zepeda Arancibia]], [[Leonardo Osses Sandoval]], [[Patricio Marin Lazo]], [[Paul Schafer Schneider]]
- **Entidades Públicas/Privadas (3)**: [[Corte Suprema de Chile]], [[Direccion de Inteligencia Policial de Carabineros]], [[Sociedad Benefactora y Educacional Dignidad]]
- **Transacciones Reificadas (5)**: [[TRX-1991-01-31-Movimientos-Patrimoniales-ColoniaDignidad-01]], [[TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01]], [[TRX-2017-09-23-Detenciones-OperacionHuracan-01]], [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]]

### Agrupamiento #11 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca)
- **Tamaño del Clúster**: `9` nodos | **Flujo Registrado en la Agrupamiento**: `$268.000.000 CLP`
- **Personas Involucradas (3)**: [[Camila Flores Oporto]], [[Francisco Mujica Ortuzar]], [[Jaime Orpis Bouchon]]
- **Entidades Públicas/Privadas (2)**: [[Corpesca SA]], [[Senado de la Republica de Chile]]
- **Transacciones Reificadas (2)**: [[TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01]], [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]

### Agrupamiento #12 (Caso Luminarias LED)
- **Tamaño del Clúster**: `9` nodos | **Flujo Registrado en la Agrupamiento**: `$162.000.000 CLP`
- **Personas Involucradas (3)**: [[Guillermo Cejas Valenzuela]], [[Leon Marcelo Lefort Hernandez]], [[Marcelo Campos Henriquez]]
- **Entidades Públicas/Privadas (3)**: [[Itelecom Holding Chile SpA]], [[Municipalidad de Chillan]], [[Municipalidad de Iquique]]
- **Transacciones Reificadas (2)**: [[TRX-2018-09-12-Sobornos-Itelecom-Licitacion-Iquique-01]], [[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]]

### Agrupamiento #13 (Caso Caval)
- **Tamaño del Clúster**: `8` nodos | **Flujo Registrado en la Agrupamiento**: `$2.555.030.792 CLP`
- **Personas Involucradas (3)**: [[Jorge Silva Menares]], [[Mauricio Valero Illanes]], [[Natalia Compagnon Soto]]
- **Entidades Públicas/Privadas (2)**: [[Exportadora y de Gestion Caval Ltda]], [[Municipalidad de Machali]]
- **Transacciones Reificadas (2)**: [[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]], [[TRX-2015-01-29-Facturas-Caval-SII-01]]

### Agrupamiento #14 (Caso La Polar)
- **Tamaño del Clúster**: `8` nodos | **Flujo Registrado en la Agrupamiento**: `$70.734.000.000 CLP`
- **Personas Involucradas (3)**: [[Javier Gatica Menke]], [[Julian Moreno de Pablo]], [[Pablo Alcalde Saavedra]]
- **Entidades Públicas/Privadas (2)**: [[Empresas La Polar SA]], [[PricewaterhouseCoopers Consultores Auditores SpA]]
- **Transacciones Reificadas (2)**: [[TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01]], [[TRX-2014-07-24-Sanciones-SVS-CS-Auditorias-PwC-LaPolar-Cascadas-01]]

### Agrupamiento #15 (Caso Colusion del Papel Tissue)
- **Tamaño del Clúster**: `7` nodos | **Flujo Registrado en la Agrupamiento**: `$97.500.000.000 CLP`
- **Personas Involucradas (2)**: [[Eliodoro Matte Larrain]], [[Gabriel Ruiz-Tagle Serrano]]
- **Entidades Públicas/Privadas (2)**: [[Empresas CMPC SA]], [[SCA Chile SA]]
- **Transacciones Reificadas (2)**: [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]], [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]]

### Agrupamiento #16 (Caso Sierra Bella)
- **Tamaño del Clúster**: `7` nodos | **Flujo Registrado en la Agrupamiento**: `$0 CLP`
- **Personas Involucradas (2)**: [[Felipe Sanchez Perez]], [[Iraci Hassler Jacob]]
- **Entidades Públicas/Privadas (3)**: [[Inmobiliaria San Valentino SpA]], [[Municipalidad de Santiago]], [[Partido Comunista de Chile]]
- **Transacciones Reificadas (1)**: [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]

### Agrupamiento #17 (Caso Fraude en Municipalidad de Antofagasta)
- **Tamaño del Clúster**: `6` nodos | **Flujo Registrado en la Agrupamiento**: `$23.722.228 CLP`
- **Personas Involucradas (2)**: [[Jose Miguel Izquierdo Sanchez]], [[Karen Rojo Venegas]]
- **Entidades Públicas/Privadas (2)**: [[Main Comunicacion Estrategica]], [[Municipalidad de Antofagasta]]
- **Transacciones Reificadas (1)**: [[TRX-2015-10-01-Asesoria-Main-CMDS-Antofagasta-01]]

### Agrupamiento #18 (Caso Chiledeportes y Facturas Publicam)
- **Tamaño del Clúster**: `5` nodos | **Flujo Registrado en la Agrupamiento**: `$417.000.000 CLP`
- **Personas Involucradas (1)**: [[Manuel Arancibia Morales]]
- **Entidades Públicas/Privadas (2)**: [[Instituto Nacional de Deportes Chiledeportes]], [[Publicam Limitada]]
- **Transacciones Reificadas (1)**: [[TRX-2005-11-10-Desvio-Fondos-Chiledeportes-Publicam-01]]

### Agrupamiento #19 (Caso AC Inversions)
- **Tamaño del Clúster**: `4` nodos | **Flujo Registrado en la Agrupamiento**: `$50.000.000.000 CLP`
- **Personas Involucradas (1)**: [[Patricio Santos Hernandez]]
- **Entidades Públicas/Privadas (1)**: [[AC Inversions SpA]]
- **Transacciones Reificadas (1)**: [[TRX-2016-03-01-Estafa-Piramidal-Lavado-ACInversions-01]]

### Agrupamiento #20 (SMU SA)
- **Tamaño del Clúster**: `2` nodos | **Flujo Registrado en la Agrupamiento**: `$0 CLP`
- **Personas Involucradas (1)**: [[Alvaro Saieh Bendeck]]
- **Entidades Públicas/Privadas (1)**: [[SMU SA]]
- **Transacciones Reificadas (0)**: _Ninguna_
