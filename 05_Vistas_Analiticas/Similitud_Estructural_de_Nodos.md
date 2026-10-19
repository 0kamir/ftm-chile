---
tipo_nodo: vista_analitica
titulo: "Predicción de Similitud estructural (Índices Adamic-Adar y Jaccard)"
actualizacion_automatica: true
tags:
  - dashboard
  - link-prediction
  - adamic-adar
---

# Similitud Estructural entre Nodos (*Link Prediction*)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.
>
> Los pares listados **no tienen un vínculo documentado**: el algoritmo solo indica que comparten vecinos en el grafo. Sirven para orientar una búsqueda de fuentes, nunca para afirmar una relación.


Aplicación de los algoritmos **Adamic-Adar ($AA$)** y **Coeficiente de Jaccard ($J$)** (Liben-Nowell & Kleinberg) sobre el grafo para identificar pares de actores (`Persona`, `Entidad Pública`, `Entidad Privada`) que no poseen un enlace directo en su ficha, pero comparten intermediarios, partidos políticos o transacciones puente:

$$AA(u, v) = \sum_{w \in \Gamma(u) \cap \Gamma(v)} \frac{1}{\ln |\Gamma(w)|}$$

---

## Top 15 Hipótesis de Asociación Estructural / Co-Operación Indirecta

| Ranking | Actor A | Actor B | Índice Adamic-ar ($AA$) | Similitud Jaccard ($J$) | Nodos Puente / Vecinos Comunes ($\Gamma(u) \cap \Gamma(v)$) |
| :---: | :--- | :--- | ---: | ---: | :--- |
| **1** | [[Carlos Contreras Gutierrez]] (`persona`) | [[Seremi MINVU Antofagasta]] (`entidad_publica`) | **`6.9088`** | `0.7857` | [[Alberto Larrain Salas]], [[Contraloria General de la Republica]], [[Daniel Andrade Schwarze]], [[Fundacion Democracia Viva]], [[Fundacion ProCultura]], [[Jorge Bermudez Soto]], [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]], [[TRX-2022-11-29-Convenio-DV-03]], [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] |
| **2** | [[Farmacias Salcobrand SA]] (`entidad_privada`) | [[Roberto Belloni Pechini]] (`persona`) | **`5.8368`** | `0.8182` | [[Farmacias Cruz Verde SA]], [[Guillermo Harding Alvarado]], [[Jorge Quiroz Castro]], [[Jose Codner Chijner]], [[Quiroz y Asociados Consultores SpA]], [[Servicio Nacional del Consumidor]], [[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]], [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]], [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]] |
| **3** | [[Augusto Pinochet Ugarte]] (`persona`) | [[Comando de Apoyo a la Fuerza del Ejercito]] (`entidad_publica`) | **`5.3713`** | `0.3600` | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]], [[Agustin Edwards Eastman]], [[Augusto Pinochet Hiriart]], [[Oscar Aitken Lavanchy]], [[Riggs Bank y Sociedades Offshore Ashburton]], [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]], [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[Valmoval Ltda]] |
| **4** | [[Corte Suprema de Chile]] (`entidad_publica`) | [[Sergio Munoz Gajardo]] (`persona`) | **`5.1499`** | `0.2195` | [[Bancard Inversiones Ltda]], [[Fundacion CEMA Chile]], [[Lucia Hiriart Rodriguez]], [[Pia Guzman Mena]], [[Renovacion Nacional]], [[Sebastian Pinera Echenique]], [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]], [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] |
| **5** | [[Alex Smith Leay]] (`persona`) | [[Direccion de Inteligencia Policial de Carabineros]] (`entidad_publica`) | **`4.9894`** | `0.7778` | [[Corte Suprema de Chile]], [[Gonzalo Blu Rodriguez]], [[Leonardo Osses Sandoval]], [[Patricio Marin Lazo]], [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] |
| **6** | [[Carlos Contreras Gutierrez]] (`persona`) | [[Daniel Andrade Schwarze]] (`persona`) | **`4.5673`** | `0.4286` | [[Fundacion Democracia Viva]], [[Revolucion Democratica]], [[Seremi MINVU Antofagasta]], [[TRX-2022-10-03-Convenio-DV-01]], [[TRX-2022-10-19-Convenio-DV-02]], [[TRX-2022-11-29-Convenio-DV-03]] |
| **7** | [[KDM Empresas SA]] (`entidad_privada`) | [[Marcelo Torres Ferrari]] (`persona`) | **`4.0648`** | `0.6667` | [[Fernando Leon Steffens]], [[Luis Plaza Sanchez]], [[Municipalidad de Cerro Navia]], [[Municipalidad de Maipu]], [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]], [[TRX-2012-03-22-Fraude-Residuos-CerroNavia-01]] |
| **8** | [[GORE Biobio]] (`entidad_publica`) | [[Rodrigo Diaz Worner]] (`persona`) | **`3.9132`** | `0.7500` | [[Alberto Larrain Salas]], [[Camila Polizzi Fonceca]], [[Fundacion En Ti]], [[Fundacion ProCultura]], [[TRX-2022-11-18-Convenio-ProCultura-Biobio]], [[TRX-2022-12-20-Convenio-EnTi-01]] |
| **9** | [[Sergio Munoz Gajardo]] (`persona`) | [[Servicio Impuestos Internos]] (`entidad_publica`) | **`3.7540`** | `0.1622` | [[Claudio Spiniak Vilensky]], [[Inversiones El Bosque Ltda]], [[Lucia Hiriart Rodriguez]], [[Riggs Bank y Sociedades Offshore Ashburton]], [[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]], [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] |
| **10** | [[Comando de Apoyo a la Fuerza del Ejercito]] (`entidad_publica`) | [[Juan Miguel Fuente-Alba Poblete]] (`persona`) | **`3.6986`** | `0.3333` | [[Frasim Ltda]], [[Javier Cruz Tamburrino]], [[Jozo Santic Palomino]], [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]], [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]], [[Unidad de Analisis Financiero]] |
| **11** | [[Agrosuper SA]] (`entidad_privada`) | [[Gonzalo Vial Vial]] (`persona`) | **`3.4754`** | `0.7500` | [[Asociacion de Productores Avicolas de Chile AG]], [[Corte Suprema de Chile]], [[Juan Miguel Ovalle Garces]], [[Manuel Ariztia Ruiz]], [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]], [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]] |
| **12** | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] (`entidad_privada`) | [[Agustin Edwards Eastman]] (`persona`) | **`3.3839`** | `0.4286` | [[Augusto Pinochet Ugarte]], [[Comando de Apoyo a la Fuerza del Ejercito]], [[Empresa El Mercurio SAP]], [[Manuel Contreras Sepulveda]], [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]], [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]] |
| **13** | [[Alex Smith Leay]] (`persona`) | [[Corte Suprema de Chile]] (`entidad_publica`) | **`3.3663`** | `0.1351` | [[Direccion de Inteligencia Policial de Carabineros]], [[Gonzalo Blu Rodriguez]], [[Leonardo Osses Sandoval]], [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] |
| **14** | [[Corte Suprema de Chile]] (`entidad_publica`) | [[Direccion de Inteligencia Policial de Carabineros]] (`entidad_publica`) | **`3.3663`** | `0.1351` | [[Alex Smith Leay]], [[Gonzalo Blu Rodriguez]], [[Leonardo Osses Sandoval]], [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]], [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] |
| **15** | [[Direccion de Finanzas de Carabineros]] (`entidad_publica`) | [[Flavio Echeverria Cortez]] (`persona`) | **`3.3550`** | `0.7143` | [[Jaime Paz Meneses]], [[Javier Cruz Tamburrino]], [[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]], [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]], [[Unidad de Analisis Financiero]] |
