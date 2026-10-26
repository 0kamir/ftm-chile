---
tipo_nodo: vista_analitica
titulo: "Análisis de Flujo Financiero Máximo, Corte Mínimo (Edmonds-Karp) y Concentración de Gini"
actualizacion_automatica: true
tags:
  - flujo-financiero
  - max-flow-min-cut
  - edmonds-karp
  - gini
---

# Flujo Máximo y Corte Mínimo en la Red de Montos (Edmonds-Karp)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.


> [!IMPORTANT] Teorema Max-Flow Min-Cut aplicado a Persecución Patrimonial y Comiso
> Esta vista modela el grafo dirigido de desembolsos como una **Red de Flujo Capacitada** ($S \rightarrow \text{Entidad Origen} \rightarrow \text{Firmante Origen} \rightarrow \text{Firmante Destino} \rightarrow \text{Entidad Destino} \rightarrow T$) y ejecuta el algoritmo de **Edmonds-Karp ($O(VE^2)$)** y una selección voraz que determina cuántos firmantes concentran el **100% de los montos registrados** en el grafo. Es una medida de concentración de los datos, no una recomendación de medidas sobre personas.

## 1. Métricas Globales de Flujo y Desigualdad Financiera

- **Flujo Máximo Registrado ($f^*$ de Edmonds-Karp)**: **`$841.204.734.718 CLP`** *(100% consistente con la suma de aristas `TRX` con flujo monetario)*
- **Capacidad del Corte Mínimo ($c(S, T)$)**: **`$841.204.734.718 CLP`** across `38` cuellos de botella primarios.
- **Coeficiente de Gini por Transacción (`TRX`)**: `0.8362`
- **Coeficiente de Gini por Causa Penal**: `0.7724`
- **Coeficiente de Gini por Firmante**: `0.7827`
- **Firmantes que concentran el 100% de los montos**: `41` personas (de un total de `75` firmantes con flujo monetario).

---

## 2. Curva de Retiro de nodos Óptima (Medidas Precautorias / Comiso)

Orden óptimo de congelamiento de activos / medidas precautorias reales para maximizar el monto fiscal y corporativo interceptado en cada paso:

| Paso | Firmante | TRX Cubiertas | Monto Marginal Cubierto | Monto Acumulado | % del Flujo Total |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | [[Juan Pablo Davila Silva]] | `1` | `$98.580.000.000 CLP` | `$98.580.000.000 CLP` | **`11.72%`** |
| **2** | [[Eliodoro Matte Larrain]] | `1` | `$97.500.000.000 CLP` | `$196.080.000.000 CLP` | **`23.31%`** |
| **3** | [[Sebastian Pinera Echenique]] | `3` | `$89.050.000.000 CLP` | `$285.130.000.000 CLP` | **`33.90%`** |
| **4** | [[Julian Moreno de Pablo]] | `1` | `$68.634.000.000 CLP` | `$353.764.000.000 CLP` | **`42.05%`** |
| **5** | [[Patricio Santos Hernandez]] | `1` | `$50.000.000.000 CLP` | `$403.764.000.000 CLP` | **`48.00%`** |
| **6** | [[Gonzalo Vial Vial]] | `1` | `$38.400.000.000 CLP` | `$442.164.000.000 CLP` | **`52.56%`** |
| **7** | [[Cathy Barriga Guerra]] | `1` | `$30.972.000.000 CLP` | `$473.136.000.000 CLP` | **`56.25%`** |
| **8** | [[Flavio Echeverria Cortez]] | `2` | `$29.798.928.198 CLP` | `$502.934.928.198 CLP` | **`59.79%`** |
| **9** | [[Andronico Luksic Craig]] | `1` | `$24.100.000.000 CLP` | `$527.034.928.198 CLP` | **`62.65%`** |
| **10** | [[Augusto Pinochet Ugarte]] | `2` | `$18.750.000.000 CLP` | `$545.784.928.198 CLP` | **`64.88%`** |
| **11** | [[Enrique Ostale Brito]] | `1` | `$18.300.000.000 CLP` | `$564.084.928.198 CLP` | **`67.06%`** |
| **12** | [[Juan Miguel Fuente-Alba Poblete]] | `2` | `$9.600.000.000 CLP` | `$573.684.928.198 CLP` | **`68.20%`** |
| **13** | [[Jaime Estay Viveros]] | `1` | `$6.000.000.000 CLP` | `$579.684.928.198 CLP` | **`68.91%`** |
| **14** | [[Alberto Larrain Salas]] | `2` | `$3.053.000.000 CLP` | `$582.737.928.198 CLP` | **`69.27%`** |
| **15** | [[Natalia Compagnon Soto]] | `1` | `$2.500.000.000 CLP` | `$585.237.928.198 CLP` | **`69.57%`** |
| **16** | [[Lucia Hiriart Rodriguez]] | `1` | `$2.450.000.000 CLP` | `$587.687.928.198 CLP` | **`69.86%`** |
| **17** | [[Jose Codner Chijner]] | `1` | `$2.180.000.000 CLP` | `$589.867.928.198 CLP` | **`70.12%`** |
| **18** | [[Javier Gatica Menke]] | `1` | `$2.100.000.000 CLP` | `$591.967.928.198 CLP` | **`70.37%`** |
| **19** | [[Pablo Longueira Montes]] | `2` | `$1.990.000.000 CLP` | `$593.957.928.198 CLP` | **`70.61%`** |
| **20** | [[Marcelo Torres Ferrari]] | `2` | `$1.306.500.000 CLP` | `$595.264.428.198 CLP` | **`70.76%`** |
| **21** | [[Carlos Cruz Lorenzen]] | `1` | `$1.253.000.000 CLP` | `$596.517.428.198 CLP` | **`70.91%`** |
| **22** | [[Jesus Diez Gonzalez]] | `1` | `$898.000.000 CLP` | `$597.415.428.198 CLP` | **`71.02%`** |
| **23** | [[Domingo Prieto Urrejola]] | `1` | `$759.000.000 CLP` | `$598.174.428.198 CLP` | **`71.11%`** |
| **24** | [[Carlos Contreras Gutierrez]] | `3` | `$426.000.000 CLP` | `$598.600.428.198 CLP` | **`71.16%`** |
| **25** | [[Manuel Arancibia Morales]] | `1` | `$417.000.000 CLP` | `$599.017.428.198 CLP` | **`71.21%`** |
| **26** | [[Patricio Contesse Gonzalez]] | `1` | `$340.000.000 CLP` | `$599.357.428.198 CLP` | **`71.25%`** |
| **27** | [[Luis Hermosilla Osorio]] | `2` | `$290.000.000 CLP` | `$599.647.428.198 CLP` | **`71.28%`** |
| **28** | [[Camila Polizzi Fonceca]] | `1` | `$250.635.000 CLP` | `$599.898.063.198 CLP` | **`71.31%`** |
| **29** | [[Miguel Angel Aguilera Sanhueza]] | `1` | `$246.918.500 CLP` | `$600.144.981.698 CLP` | **`71.34%`** |
| **30** | [[Francisco Mujica Ortuzar]] | `1` | `$233.000.000 CLP` | `$600.377.981.698 CLP` | **`71.37%`** |
| **31** | [[Leon Marcelo Lefort Hernandez]] | `2` | `$162.000.000 CLP` | `$600.539.981.698 CLP` | **`71.39%`** |
| **32** | [[Carlos Alberto Delano Abbott]] | `1` | `$156.000.000 CLP` | `$600.695.981.698 CLP` | **`71.41%`** |
| **33** | [[Hector Espinosa Valenzuela]] | `1` | `$146.000.000 CLP` | `$600.841.981.698 CLP` | **`71.43%`** |
| **34** | [[Hector Zuniga Rogers]] | `1` | `$105.000.000 CLP` | `$600.946.981.698 CLP` | **`71.44%`** |
| **35** | [[Patricio Rodrigo Salinas]] | `1` | `$57.000.000 CLP` | `$601.003.981.698 CLP` | **`71.45%`** |
| **36** | [[Jorge Silva Menares]] | `1` | `$55.030.792 CLP` | `$601.059.012.490 CLP` | **`71.45%`** |
| **37** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `1` | `$42.000.000 CLP` | `$601.101.012.490 CLP` | **`71.46%`** |
| **38** | [[Camila Flores Oporto]] | `1` | `$35.000.000 CLP` | `$601.136.012.490 CLP` | **`71.46%`** |
| **39** | [[Alex Smith Leay]] | `1` | `$25.000.000 CLP` | `$601.161.012.490 CLP` | **`71.46%`** |
| **40** | [[Jose Miguel Izquierdo Sanchez]] | `1` | `$23.722.228 CLP` | `$601.184.734.718 CLP` | **`71.47%`** |
| **41** | [[Cristian Pareto Vergara]] | `1` | `$20.000.000 CLP` | `$601.204.734.718 CLP` | **`71.47%`** |

---

## 3. Canales de Flujo Financiero (`Firmante Origen → Firmante Destino`)

| # | Autorizador (Origen) | Entidad Emisora | Receptor (Destino) | Entidad Receptora | TRX | Caudal Acumulado (CLP) | Causa(s) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | [[]] | [[]] | [[]] | [[Servicio Impuestos Internos]] | `1` | **`$240.000.000.000 CLP`** | [[Caso Megafraude Tributario Operacion Tributos]] |
| **2** | [[Juan Pablo Davila Silva]] | [[Corporacion Nacional del Cobre de Chile]] | [[Juan Pablo Davila Silva]] | [[Servicio Impuestos Internos]] | `1` | **`$98.580.000.000 CLP`** | [[Caso Codelco Davilazo]] |
| **3** | [[Eliodoro Matte Larrain]] | [[Empresas CMPC SA]] | [[Gabriel Ruiz-Tagle Serrano]] | [[Servicio Nacional del Consumidor]] | `1` | **`$97.500.000.000 CLP`** | [[Caso Colusion del Papel Tissue]] |
| **4** | [[Carlos Alberto Delano Abbott]] | [[Andes Iron SpA]] | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | `1` | **`$75.500.000.000 CLP`** | [[Caso Minera Dominga Pandora Papers]] |
| **5** | [[Pablo Alcalde Saavedra]] | [[Empresas La Polar SA]] | [[Julian Moreno de Pablo]] | [[Comision para el Mercado Financiero]] | `1` | **`$68.634.000.000 CLP`** | [[Caso La Polar]] |
| **6** | [[Patricio Santos Hernandez]] | [[AC Inversions SpA]] | [[Patricio Santos Hernandez]] | [[Unidad de Analisis Financiero]] | `1` | **`$50.000.000.000 CLP`** | [[Caso AC Inversions]] |
| **7** | [[Gonzalo Vial Vial]] | [[Agrosuper SA]] | [[Manuel Ariztia Ruiz]] | [[Corte Suprema de Chile]] | `1` | **`$38.400.000.000 CLP`** | [[Caso Colusion de los Pollos]] |
| **8** | [[Cathy Barriga Guerra]] | [[Municipalidad de Maipu]] | [[Cathy Barriga Guerra]] | [[Municipalidad de Maipu]] | `1` | **`$30.972.000.000 CLP`** | [[Caso Municipalidad de Maipu]] |
| **9** | [[Flavio Echeverria Cortez]] | [[Direccion de Finanzas de Carabineros]] | [[Jaime Paz Meneses]] | [[Direccion de Finanzas de Carabineros]] | `1` | **`$28.348.928.198 CLP`** | [[Caso Pacogate]] |
| **10** | [[Beltran Urenda Salamanca]] | [[Compania Maritima de Chile SA]] | [[Andronico Luksic Craig]] | [[Fiscalia Nacional Economica]] | `1` | **`$24.100.000.000 CLP`** | [[Caso Colusion de las Navieras]] |
| **11** | [[Horst Paulmann Kemna]] | [[Cencosud SA]] | [[Enrique Ostale Brito]] | [[Fiscalia Nacional Economica]] | `1` | **`$18.300.000.000 CLP`** | [[Caso Colusion de los Supermercados]] |
| **12** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | `1` | **`$15.800.000.000 CLP`** | [[Caso Riggs]] |
| **13** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Santiago Valdes Gutierrez]] | [[Contraloria General de la Republica]] | `1` | **`$8.250.000.000 CLP`** | [[Caso Exalmar y Fideicomiso Ciego]] |
| **14** | [[Juan Miguel Fuente-Alba Poblete]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Jozo Santic Palomino]] | [[Frasim Ltda]] | `1` | **`$6.100.000.000 CLP`** | [[Caso Milicogate]] |
| **15** | [[Ramon Vega Hidalgo]] | [[Fuerza Aerea de Chile]] | [[Jaime Estay Viveros]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | `1` | **`$6.000.000.000 CLP`** | [[Caso Mirage]] |
| **16** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Carlos Pavez Tolosa]] | [[Comision para el Mercado Financiero]] | `1` | **`$5.300.000.000 CLP`** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] |
| **17** | [[Juan Miguel Fuente-Alba Poblete]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$3.500.000.000 CLP`** | [[Caso Milicogate]] |
| **18** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Augusto Pinochet Hiriart]] | [[Valmoval Ltda]] | `1` | **`$2.950.000.000 CLP`** | [[Caso Pinocheques]] |
| **19** | [[Rodrigo Diaz Worner]] | [[GORE Biobio]] | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | `1` | **`$2.553.000.000 CLP`** | [[Caso Convenios]] |
| **20** | [[Natalia Compagnon Soto]] | [[Exportadora y de Gestion Caval Ltda]] | [[Natalia Compagnon Soto]] | [[Servicio Impuestos Internos]] | `1` | **`$2.500.000.000 CLP`** | [[Caso Caval]] |
| **21** | [[Lucia Hiriart Rodriguez]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | `1` | **`$2.450.000.000 CLP`** | [[Caso Riggs]] |
| **22** | [[Roberto Belloni Pechini]] | [[Farmacias Salcobrand SA]] | [[Jose Codner Chijner]] | [[Servicio Nacional del Consumidor]] | `1` | **`$2.180.000.000 CLP`** | [[Caso Colusion de las Farmacias]] |
| **23** | [[Javier Gatica Menke]] | [[PricewaterhouseCoopers Consultores Auditores SpA]] | [[]] | [[Empresas La Polar SA]] | `1` | **`$2.100.000.000 CLP`** | [[Caso La Polar]] |
| **24** | [[Flavio Echeverria Cortez]] | [[Direccion de Finanzas de Carabineros]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$1.450.000.000 CLP`** | [[Caso Pacogate]] |
| **25** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | `1` | **`$1.260.000.000 CLP`** | [[Caso Penta]] |
| **26** | [[Carlos Cruz Lorenzen]] | [[Ministerio de Obras Publicas]] | [[Hector Pena Veliz]] | [[Gestion Ambiental y Territorial SA]] | `1` | **`$1.253.000.000 CLP`** | [[Caso MOP-Gate]] |
| **27** | [[Luis Plaza Sanchez]] | [[Municipalidad de Cerro Navia]] | [[Marcelo Torres Ferrari]] | [[KDM Empresas SA]] | `1` | **`$1.120.000.000 CLP`** | [[Caso Basura]] |
| **28** | [[Pedro Farias Soto]] | [[Empresas Pullman Bus SA]] | [[Jesus Diez Gonzalez]] | [[Fiscalia Nacional Economica]] | `1` | **`$898.000.000 CLP`** | [[Caso Colusion de los Buses Interurbanos]] |
| **29** | [[Raul Torrealba del Pedregal]] | [[Municipalidad de Vitacura]] | [[Domingo Prieto Urrejola]] | [[Vita Deportes]] | `1` | **`$759.000.000 CLP`** | [[Caso Vitacura]] |
| **30** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | `1` | **`$730.000.000 CLP`** | [[Caso SQM]] |
| **31** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | `1` | **`$500.000.000 CLP`** | [[Caso Convenios]] |
| **32** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | `3` | **`$426.000.000 CLP`** | [[Caso Convenios]] |
| **33** | [[]] | [[Instituto Nacional de Deportes Chiledeportes]] | [[Manuel Arancibia Morales]] | [[Publicam Limitada]] | `1` | **`$417.000.000 CLP`** | [[Caso Chiledeportes y Facturas Publicam]] |
| **34** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[Santiago Valdes Gutierrez]] | [[Bancard Inversiones Ltda]] | `1` | **`$340.000.000 CLP`** | [[Caso SQM]] |
| **35** | [[Rodrigo Diaz Worner]] | [[GORE Biobio]] | [[Camila Polizzi Fonceca]] | [[Fundacion En Ti]] | `1` | **`$250.635.000 CLP`** | [[Caso Convenios]] |
| **36** | [[Miguel Angel Aguilera Sanhueza]] | [[Municipalidad de San Ramon]] | [[Miguel Angel Aguilera Sanhueza]] | [[Unidad de Analisis Financiero]] | `1` | **`$246.918.500 CLP`** | [[Caso Municipalidad de San Ramon]] |
| **37** | [[Francisco Mujica Ortuzar]] | [[Corpesca SA]] | [[Jaime Orpis Bouchon]] | [[Senado de la Republica de Chile]] | `1` | **`$233.000.000 CLP`** | [[Caso Corpesca]] |
| **38** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Andres Chadwick Pinera]] | [[Senado de la Republica de Chile]] | `1` | **`$190.000.000 CLP`** | [[Caso Audios]] |
| **39** | [[Fernando Leon Steffens]] | [[KDM Empresas SA]] | [[Marcelo Torres Ferrari]] | [[Municipalidad de Maipu]] | `1` | **`$186.500.000 CLP`** | [[Caso Basura]] |
| **40** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[Jovino Novoa Vasquez]] | [[Union Democrata Independiente]] | `1` | **`$156.000.000 CLP`** | [[Caso Penta]] |
| **41** | [[Hector Espinosa Valenzuela]] | [[Policia de Investigaciones de Chile]] | [[Hector Espinosa Valenzuela]] | [[Unidad de Analisis Financiero]] | `1` | **`$146.000.000 CLP`** | [[Caso Gastos Reservados PDI Hector Espinosa]] |
| **42** | [[Leon Marcelo Lefort Hernandez]] | [[Itelecom Holding Chile SpA]] | [[Guillermo Cejas Valenzuela]] | [[Municipalidad de Iquique]] | `1` | **`$125.000.000 CLP`** | [[Caso Luminarias LED]] |
| **43** | [[Hector Zuniga Rogers]] | [[Universidad del Mar]] | [[Luis Eugenio Diaz Corvalan]] | [[Comision Nacional de Acreditacion]] | `1` | **`$105.000.000 CLP`** | [[Caso CNA Acreditaciones Universitarias]] |
| **44** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Leonarda Villalobos Muth]] | [[Servicio Impuestos Internos]] | `1` | **`$100.000.000 CLP`** | [[Caso Audios]] |
| **45** | [[]] | [[SQM SA]] | [[Patricio Rodrigo Salinas]] | [[Partido por la Democracia]] | `1` | **`$57.000.000 CLP`** | [[Caso SQM]] |
| **46** | [[]] | [[]] | [[Jorge Silva Menares]] | [[Municipalidad de Machali]] | `1` | **`$55.030.792 CLP`** | [[Caso Caval]] |
| **47** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | [[Empresas Penta SA]] | [[Pablo Wagner San Martin]] | [[Servicio Impuestos Internos]] | `1` | **`$42.000.000 CLP`** | [[Caso Penta]] |
| **48** | [[Leon Marcelo Lefort Hernandez]] | [[Itelecom Holding Chile SpA]] | [[Marcelo Campos Henriquez]] | [[Municipalidad de Chillan]] | `1` | **`$37.000.000 CLP`** | [[Caso Luminarias LED]] |
| **49** | [[Senado de la Republica de Chile]] | [[Senado de la Republica de Chile]] | [[Camila Flores Oporto]] | [[Camila Flores Oporto]] | `1` | **`$35.000.000 CLP`** | [[Caso Asignaciones Parlamentarias y Cuota Flores]] |
| **50** | [[Patricio Marin Lazo]] | [[Direccion de Inteligencia Policial de Carabineros]] | [[Alex Smith Leay]] | [[Direccion de Inteligencia Policial de Carabineros]] | `1` | **`$25.000.000 CLP`** | [[Caso Operacion Huracan]] |
| **51** | [[Karen Rojo Venegas]] | [[Municipalidad de Antofagasta]] | [[Jose Miguel Izquierdo Sanchez]] | [[Main Comunicacion Estrategica]] | `1` | **`$23.722.228 CLP`** | [[Caso Fraude en Municipalidad de Antofagasta]] |
| **52** | [[Cristian Pareto Vergara]] | [[Partido Democrata Cristiano]] | [[Victor Manuel Rebolledo Gonzalez]] | [[Ministerio de Obras Publicas]] | `1` | **`$20.000.000 CLP`** | [[Caso Coimas]] |

---

## 4. Diagrama Topológico de Cuellos de Botella Financieros (Top 8 Canales)

```mermaid
flowchart LR
    EO1[""] -->|"$ 240.000M"| FO1[""] -->|"$ 240.000M"| FD1[""] --> ED1["Servicio Impuestos Internos"]
    EO2["Corporacion Nacional del Cobre de Chile"] -->|"$ 98.580M"| FO2["Juan Pablo Davila Silva"] -->|"$ 98.580M"| FD2["Juan Pablo Davila Silva"] --> ED2["Servicio Impuestos Internos"]
    EO3["Empresas CMPC SA"] -->|"$ 97.500M"| FO3["Eliodoro Matte Larrain"] -->|"$ 97.500M"| FD3["Gabriel Ruiz-Tagle Serrano"] --> ED3["Servicio Nacional del Consumidor"]
    EO4["Andes Iron SpA"] -->|"$ 75.500M"| FO4["Carlos Alberto Delano Abbott"] -->|"$ 75.500M"| FD4["Sebastian Pinera Echenique"] --> ED4["Bancard Inversiones Ltda"]
    EO5["Empresas La Polar SA"] -->|"$ 68.634M"| FO5["Pablo Alcalde Saavedra"] -->|"$ 68.634M"| FD5["Julian Moreno de Pablo"] --> ED5["Comision para el Mercado Financiero"]
    EO6["AC Inversions SpA"] -->|"$ 50.000M"| FO6["Patricio Santos Hernandez"] -->|"$ 50.000M"| FD6["Patricio Santos Hernandez"] --> ED6["Unidad de Analisis Financiero"]
    EO7["Agrosuper SA"] -->|"$ 38.400M"| FO7["Gonzalo Vial Vial"] -->|"$ 38.400M"| FD7["Manuel Ariztia Ruiz"] --> ED7["Corte Suprema de Chile"]
    EO8["Municipalidad de Maipu"] -->|"$ 30.972M"| FO8["Cathy Barriga Guerra"] -->|"$ 30.972M"| FD8["Cathy Barriga Guerra"] --> ED8["Municipalidad de Maipu"]
```
