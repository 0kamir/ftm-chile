---
tipo_nodo: vista_analitica
titulo: "Detección de Comunidades Operativas y Modularidad (Newman-Girvan Q)"
actualizacion_automatica: true
tags:
  - comunidades
  - modularidad-newman
  - analisis-forense
---

# 🧬 Detección de Comunidades Operativas y Modularidad ($Q$)

> [!NOTE] Ciencia de Redes aplicada a Estructuras de Corrupción (Clauset-Newman-Moore & Guimerà-Amaral)
> Esta vista aplica maximización aglomerativa de **Modularidad de Newman-Girvan ($Q$)** (algoritmo de Clauset-Newman-Moore sobre la red operativa de actores, causas y transacciones, excluyendo artículos penales genéricos) para particionar el grafo en **Células Operativas**, y calcula el **Coeficiente de Participación ($P_i$)** de Guimerà & Amaral (2005) para descubrir los *brokers* que conectan células criminales o políticas distintas.

## 1. Indicadores Globales de Partición

- **Nodos Operativos Analizados**: `236`
- **Modularidad Global de Newman-Girvan ($Q$)**: `0.8060` *(Valores $Q > 0.70$ indican alta compartimentación celular con puentes específicos de articulación)*
- **Total de Células Operativas Detectadas**: `15`
- **Enlaces Puente Inter-Comunidad Detectados**: `39`
- **Nodos Articuladores Inter-Célula ($P_i > 0$)**: `50`

---

## 2. Brokers Inter-Comunidad (Coeficiente de Participación $P_i > 0$)

| Pos | Nodo Articulador | Tipo | Comunidad Base | Grado ($k_i$) | Coef. Participación ($P_i$) | Rol Topológico |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | [[Servicio Impuestos Internos]] | `entidad_publica` | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) | `8` | **`0.7812`** | Hub Conector Multi-Célula |
| **2** | [[Sergio Munoz Gajardo]] | `persona` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.7200`** | Hub Conector Multi-Célula |
| **3** | [[Corte Suprema de Chile]] | `entidad_publica` | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) | `16` | **`0.7109`** | Hub Conector Multi-Célula |
| **4** | [[Comando de Apoyo a la Fuerza del Ejercito]] | `entidad_publica` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.6400`** | Hub Conector Multi-Célula |
| **5** | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | `nexo_transaccion` | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `5` | **`0.5600`** | Hub Conector Multi-Célula |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.5600`** | Hub Conector Multi-Célula |
| **7** | [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]] | `nexo_transaccion` | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) | `5` | **`0.5600`** | Hub Conector Multi-Célula |
| **8** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `5` | **`0.5600`** | Hub Conector Multi-Célula |
| **9** | [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | `nexo_transaccion` | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `5` | **`0.5600`** | Hub Conector Multi-Célula |
| **10** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.5600`** | Hub Conector Multi-Célula |
| **11** | [[Caso Spiniak]] | `causa_judicial` | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `2` | **`0.5000`** | Hub Conector Multi-Célula |
| **12** | [[Jaime Orpis Bouchon]] | `persona` | Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `2` | **`0.5000`** | Hub Conector Multi-Célula |
| **13** | [[Servicio Nacional del Consumidor]] | `entidad_publica` | Célula #04 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) | `2` | **`0.5000`** | Hub Conector Multi-Célula |
| **14** | [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]] | `nexo_transaccion` | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `5` | **`0.4800`** | Hub Conector Multi-Célula |
| **15** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `nexo_transaccion` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.4800`** | Hub Conector Multi-Célula |
| **16** | [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | `nexo_transaccion` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.4800`** | Hub Conector Multi-Célula |
| **17** | [[Camila Flores Oporto]] | `persona` | Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **18** | [[Carlos Pavez Tolosa]] | `persona` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **19** | [[Caso Colonia Dignidad]] | `causa_judicial` | Célula #14 (Caso Colonia Dignidad) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **20** | [[Caso Panama Papers Chile]] | `causa_judicial` | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **21** | [[Contraloria General de la Republica]] | `entidad_publica` | Célula #05 (Caso Convenios) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **22** | [[Gabriel Ruiz-Tagle Serrano]] | `persona` | Célula #12 (Caso Colusion del Papel Tissue) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **23** | [[Municipalidad de Maipu]] | `entidad_publica` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **24** | [[Santiago Valdes Gutierrez]] | `persona` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `3` | **`0.4444`** | Hub Conector Multi-Célula |
| **25** | [[Renovacion Nacional]] | `partido_politico` | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `11` | **`0.4298`** | Hub Conector Multi-Célula |
| **26** | [[Andres Chadwick Pinera]] | `persona` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `4` | **`0.3750`** | Hub Conector Multi-Célula |
| **27** | [[Mossack Fonseca y Sociedades Offshore Panama]] | `entidad_privada` | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `4` | **`0.3750`** | Hub Conector Multi-Célula |
| **28** | [[SQM SA]] | `entidad_privada` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `4` | **`0.3750`** | Hub Conector Multi-Célula |
| **29** | [[Senado de la Republica de Chile]] | `entidad_publica` | Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `4` | **`0.3750`** | Hub Conector Multi-Célula |
| **30** | [[Sociedad Benefactora y Educacional Dignidad]] | `entidad_privada` | Célula #14 (Caso Colonia Dignidad) | `4` | **`0.3750`** | Hub Conector Multi-Célula |
| **31** | [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | `nexo_transaccion` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `4` | **`0.3750`** | Hub Conector Multi-Célula |
| **32** | [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]] | `nexo_transaccion` | Célula #14 (Caso Colonia Dignidad) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **33** | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `nexo_transaccion` | Célula #14 (Caso Colonia Dignidad) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **34** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **35** | [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]] | `nexo_transaccion` | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **36** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **37** | [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | `nexo_transaccion` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **38** | [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]] | `nexo_transaccion` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **39** | [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]] | `nexo_transaccion` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **40** | [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]] | `nexo_transaccion` | Célula #04 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **41** | [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | `nexo_transaccion` | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **42** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `nexo_transaccion` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **43** | [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] | `nexo_transaccion` | Célula #12 (Caso Colusion del Papel Tissue) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **44** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `nexo_transaccion` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **45** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `nexo_transaccion` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **46** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **47** | [[Unidad de Analisis Financiero]] | `entidad_publica` | Célula #02 (Caso Audios / Caso Milicogate) | `5` | **`0.3200`** | Hub Conector Multi-Célula |
| **48** | [[Augusto Pinochet Ugarte]] | `persona` | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `11` | **`0.2975`** | Puente Inter-Clúster |
| **49** | [[Union Democrata Independiente]] | `partido_politico` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `15` | **`0.2400`** | Puente Inter-Clúster |
| **50** | [[Sebastian Pinera Echenique]] | `persona` | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `8` | **`0.2188`** | Puente Inter-Clúster |

---

## 3. Puentes Estructurales entre Células Operativas

| Nodo A | Célula A | Relación | Nodo B | Célula B |
| :--- | :--- | :---: | :--- | :--- |
| [[Camila Flores Oporto]] | Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `vinculo` | [[Renovacion Nacional]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) |
| [[Gabriel Ruiz-Tagle Serrano]] | Célula #12 (Caso Colusion del Papel Tissue) | `vinculo` | [[Union Democrata Independiente]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[Jaime Orpis Bouchon]] | Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) | `vinculo` | [[Union Democrata Independiente]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[Santiago Valdes Gutierrez]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Renovacion Nacional]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) |
| [[Sebastian Pinera Echenique]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Renovacion Nacional]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) |
| [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Sergio Munoz Gajardo]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) | `vinculo` | [[Caso Spiniak]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) |
| [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `vinculo` | [[Sergio Munoz Gajardo]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]] | Célula #14 (Caso Colonia Dignidad) | `vinculo` | [[Servicio Impuestos Internos]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Sociedad Benefactora y Educacional Dignidad]] | Célula #14 (Caso Colonia Dignidad) |
| [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Caso Colonia Dignidad]] | Célula #14 (Caso Colonia Dignidad) |
| [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Servicio Impuestos Internos]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Contraloria General de la Republica]] | Célula #05 (Caso Convenios) |
| [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Comando de Apoyo a la Fuerza del Ejercito]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Augusto Pinochet Ugarte]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Augusto Pinochet Ugarte]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]] | Célula #12 (Caso Colusion del Papel Tissue) | `vinculo` | [[Servicio Nacional del Consumidor]] | Célula #04 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) |
| [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]] | Célula #04 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Sergio Munoz Gajardo]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | Célula #14 (Caso Colonia Dignidad) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]] | Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral) | `vinculo` | [[Municipalidad de Maipu]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) | `vinculo` | [[Servicio Impuestos Internos]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[SQM SA]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Comando de Apoyo a la Fuerza del Ejercito]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Comando de Apoyo a la Fuerza del Ejercito]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) |
| [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Servicio Impuestos Internos]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) |
| [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Carlos Pavez Tolosa]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) | `vinculo` | [[Unidad de Analisis Financiero]] | Célula #02 (Caso Audios / Caso Milicogate) |
| [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Mossack Fonseca y Sociedades Offshore Panama]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) |
| [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Caso Panama Papers Chile]] | Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile) |
| [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | Célula #06 (Caso CEMA Chile / Caso Cascadas) | `vinculo` | [[Corte Suprema de Chile]] | Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan) |
| [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Senado de la Republica de Chile]] | Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca) |
| [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Andres Chadwick Pinera]] | Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca) |
| [[TRX-2023-06-22-Reunion-Audios-01]] | Célula #02 (Caso Audios / Caso Milicogate) | `vinculo` | [[Servicio Impuestos Internos]] | Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos) |

---

## 4. Radiografía de Células Operativas Detectadas

### Célula #01 (Caso Exalmar y Fideicomiso Ciego / Caso LAN Informacion Privilegiada y Banco de Talca)
- **Tamaño del Clúster**: `38` nodos | **Flujo Auditado en la Célula**: `$141.290.000.000 CLP`
- **Personas Involucradas (14)**: [[Andres Chadwick Pinera]], [[Carlos Alberto Delano Abbott]], [[Carlos Eugenio Lavin Garcia-Huidobro]], [[Carlos Pavez Tolosa]], [[Cathy Barriga Guerra]], [[Hartmut Hopp Miottel]], [[Hernan Larrain Fernandez]], [[Jovino Novoa Vasquez]], [[Loreto Letelier]], [[Pablo Longueira Montes]], [[Pablo Wagner San Martin]], [[Patricio Contesse Gonzalez]], [[Santiago Valdes Gutierrez]], [[Sebastian Pinera Echenique]]
- **Entidades Públicas/Privadas (7)**: [[Andes Iron SpA]], [[Bancard Inversiones Ltda]], [[Comision para el Mercado Financiero]], [[Empresas Penta SA]], [[Municipalidad de Maipu]], [[SQM SA]], [[Union Democrata Independiente]]
- **Transacciones Reificadas (11)**: [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]], [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]], [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]], [[TRX-2010-08-19-Correo-Royalty-SQM-01]], [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]], [[TRX-2011-03-10-Pagos-Penta-Wagner-01]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]], [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]], [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]], [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]

### Célula #02 (Caso Audios / Caso Milicogate)
- **Tamaño del Clúster**: `25` nodos | **Flujo Auditado en la Célula**: `$40.168.928.198 CLP`
- **Personas Involucradas (9)**: [[Angela Vivanco Martinez]], [[Flavio Echeverria Cortez]], [[Gabriel Zaliasnik Schilkrut]], [[Jaime Paz Meneses]], [[Javier Cruz Tamburrino]], [[Jozo Santic Palomino]], [[Juan Miguel Fuente-Alba Poblete]], [[Leonarda Villalobos Muth]], [[Luis Hermosilla Osorio]]
- **Entidades Públicas/Privadas (4)**: [[Direccion de Finanzas de Carabineros]], [[Factop SpA]], [[Frasim Ltda]], [[Unidad de Analisis Financiero]]
- **Transacciones Reificadas (9)**: [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]], [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]], [[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]], [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]], [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]], [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]], [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]], [[TRX-2023-06-22-Reunion-Audios-01]], [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]]

### Célula #03 (Caso Basura / Caso Operaciones Digitales e Injerencia Electoral)
- **Tamaño del Clúster**: `23` nodos | **Flujo Auditado en la Célula**: `$2.185.500.000 CLP`
- **Personas Involucradas (8)**: [[Domingo Prieto Urrejola]], [[Fernando Cerimedo]], [[Fernando Leon Steffens]], [[Luis Plaza Sanchez]], [[Marcelo Torres Ferrari]], [[Percy Marin Vera]], [[Pia Guzman Mena]], [[Raul Torrealba del Pedregal]]
- **Entidades Públicas/Privadas (6)**: [[KDM Empresas SA]], [[Municipalidad de Cerro Navia]], [[Municipalidad de Vitacura]], [[Numen Publicidad SpA]], [[Renovacion Nacional]], [[Vita Deportes]]
- **Transacciones Reificadas (5)**: [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]], [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]], [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]], [[TRX-2021-04-15-Subvencion-VitaDeportes-01]], [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]

### Célula #04 (Caso Colusion de las Farmacias / Caso Colusion de los Pollos)
- **Tamaño del Clúster**: `21` nodos | **Flujo Auditado en la Célula**: `$40.580.000.000 CLP`
- **Personas Involucradas (7)**: [[Gonzalo Vial Vial]], [[Guillermo Harding Alvarado]], [[Jorge Quiroz Castro]], [[Jose Codner Chijner]], [[Juan Miguel Ovalle Garces]], [[Manuel Ariztia Ruiz]], [[Roberto Belloni Pechini]]
- **Entidades Públicas/Privadas (6)**: [[Agrosuper SA]], [[Asociacion de Productores Avicolas de Chile AG]], [[Farmacias Cruz Verde SA]], [[Farmacias Salcobrand SA]], [[Quiroz y Asociados Consultores SpA]], [[Servicio Nacional del Consumidor]]
- **Transacciones Reificadas (6)**: [[TRX-2007-04-10-Modelo-Proyeccion-Demanda-APA-Pollos-01]], [[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]], [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]], [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]], [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]], [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]

### Célula #05 (Caso Convenios)
- **Tamaño del Clúster**: `21` nodos | **Flujo Auditado en la Célula**: `$3.729.635.000 CLP`
- **Personas Involucradas (6)**: [[Alberto Larrain Salas]], [[Camila Polizzi Fonceca]], [[Carlos Contreras Gutierrez]], [[Daniel Andrade Schwarze]], [[Jorge Bermudez Soto]], [[Rodrigo Diaz Worner]]
- **Entidades Públicas/Privadas (7)**: [[Contraloria General de la Republica]], [[Fundacion Democracia Viva]], [[Fundacion En Ti]], [[Fundacion ProCultura]], [[GORE Biobio]], [[Revolucion Democratica]], [[Seremi MINVU Antofagasta]]
- **Transacciones Reificadas (7)**: [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]], [[TRX-2022-11-18-Convenio-ProCultura-Biobio]], [[TRX-2022-11-29-Convenio-DV-03]], [[TRX-2022-12-20-Convenio-EnTi-01]], [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]]

### Célula #06 (Caso CEMA Chile / Caso Cascadas)
- **Tamaño del Clúster**: `21` nodos | **Flujo Auditado en la Célula**: `$35.500.000.000 CLP`
- **Personas Involucradas (6)**: [[Augusto Pinochet Hiriart]], [[Augusto Pinochet Ugarte]], [[Julio Ponce Lerou]], [[Lucia Hiriart Rodriguez]], [[Oscar Aitken Lavanchy]], [[Sergio Munoz Gajardo]]
- **Entidades Públicas/Privadas (5)**: [[Comando de Apoyo a la Fuerza del Ejercito]], [[Fundacion CEMA Chile]], [[Riggs Bank y Sociedades Offshore Ashburton]], [[Sociedad de Inversiones Pampa Calichera SA]], [[Valmoval Ltda]]
- **Transacciones Reificadas (6)**: [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]], [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]], [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]], [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]

### Célula #07 (Caso Archivos Epstein Menciones Chile / Caso Operacion Huracan)
- **Tamaño del Clúster**: `17` nodos | **Flujo Auditado en la Célula**: `$25.000.000 CLP`
- **Personas Involucradas (7)**: [[Alex Smith Leay]], [[Andres Velasco Branes]], [[Andronico Luksic Craig]], [[Eduardo Guendelman Israel]], [[Gonzalo Blu Rodriguez]], [[Leonardo Osses Sandoval]], [[Patricio Marin Lazo]]
- **Entidades Públicas/Privadas (2)**: [[Corte Suprema de Chile]], [[Direccion de Inteligencia Policial de Carabineros]]
- **Transacciones Reificadas (6)**: [[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]], [[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]], [[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]], [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]]

### Célula #08 (Caso Operacion FUBELT Intervencion CIA y DINA / Caso Panama Papers Chile)
- **Tamaño del Clúster**: `14` nodos | **Flujo Auditado en la Célula**: `$60.100.000.000 CLP`
- **Personas Involucradas (4)**: [[Agustin Edwards Eastman]], [[Alfredo Ovalle Rodriguez]], [[Gonzalo Delaveau Swett]], [[Manuel Contreras Sepulveda]]
- **Entidades Públicas/Privadas (3)**: [[Agencia Central de Inteligencia CIA y Escuela de las Americas]], [[Empresa El Mercurio SAP]], [[Mossack Fonseca y Sociedades Offshore Panama]]
- **Transacciones Reificadas (5)**: [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]], [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]], [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]], [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]], [[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]]

### Célula #09 (Caso Caval / Caso Megafraude Tributario Operacion Tributos)
- **Tamaño del Clúster**: `14` nodos | **Flujo Auditado en la Célula**: `$243.035.030.792 CLP`
- **Personas Involucradas (4)**: [[Claudio Spiniak Vilensky]], [[Jorge Silva Menares]], [[Mauricio Valero Illanes]], [[Natalia Compagnon Soto]]
- **Entidades Públicas/Privadas (4)**: [[Exportadora y de Gestion Caval Ltda]], [[Inversiones El Bosque Ltda]], [[Municipalidad de Machali]], [[Servicio Impuestos Internos]]
- **Transacciones Reificadas (4)**: [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]], [[TRX-2014-02-18-Soborno-Caval-Machali-01]], [[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]], [[TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01]]

### Célula #10 (Caso Asignaciones Parlamentarias y Cuota Flores / Caso Corpesca)
- **Tamaño del Clúster**: `9` nodos | **Flujo Auditado en la Célula**: `$268.000.000 CLP`
- **Personas Involucradas (3)**: [[Camila Flores Oporto]], [[Francisco Mujica Ortuzar]], [[Jaime Orpis Bouchon]]
- **Entidades Públicas/Privadas (2)**: [[Corpesca SA]], [[Senado de la Republica de Chile]]
- **Transacciones Reificadas (2)**: [[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]], [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]

### Célula #11 (Caso MOP-Gate)
- **Tamaño del Clúster**: `7` nodos | **Flujo Auditado en la Célula**: `$1.253.000.000 CLP`
- **Personas Involucradas (2)**: [[Carlos Cruz Lorenzen]], [[Hector Pena Veliz]]
- **Entidades Públicas/Privadas (3)**: [[Gestion Ambiental y Territorial SA]], [[Ministerio de Obras Publicas]], [[Partido Socialista de Chile]]
- **Transacciones Reificadas (1)**: [[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]

### Célula #12 (Caso Colusion del Papel Tissue)
- **Tamaño del Clúster**: `7` nodos | **Flujo Auditado en la Célula**: `$97.500.000.000 CLP`
- **Personas Involucradas (2)**: [[Eliodoro Matte Larrain]], [[Gabriel Ruiz-Tagle Serrano]]
- **Entidades Públicas/Privadas (2)**: [[Empresas CMPC SA]], [[SCA Chile SA]]
- **Transacciones Reificadas (2)**: [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]], [[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]]

### Célula #13 (Caso Sierra Bella)
- **Tamaño del Clúster**: `7` nodos | **Flujo Auditado en la Célula**: `$0 CLP`
- **Personas Involucradas (2)**: [[Felipe Sanchez Perez]], [[Iraci Hassler Jacob]]
- **Entidades Públicas/Privadas (3)**: [[Inmobiliaria San Valentino SpA]], [[Municipalidad de Santiago]], [[Partido Comunista de Chile]]
- **Transacciones Reificadas (1)**: [[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]

### Célula #14 (Caso Colonia Dignidad)
- **Tamaño del Clúster**: `6` nodos | **Flujo Auditado en la Célula**: `$3.450.000.000 CLP`
- **Personas Involucradas (2)**: [[Jorge Zepeda Arancibia]], [[Paul Schafer Schneider]]
- **Entidades Públicas/Privadas (1)**: [[Sociedad Benefactora y Educacional Dignidad]]
- **Transacciones Reificadas (2)**: [[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]], [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]]

### Célula #15 (Caso Luminarias LED)
- **Tamaño del Clúster**: `6` nodos | **Flujo Auditado en la Célula**: `$37.000.000 CLP`
- **Personas Involucradas (2)**: [[Leon Marcelo Lefort Hernandez]], [[Marcelo Campos Henriquez]]
- **Entidades Públicas/Privadas (2)**: [[Itelecom Holding Chile SpA]], [[Municipalidad de Chillan]]
- **Transacciones Reificadas (1)**: [[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]
