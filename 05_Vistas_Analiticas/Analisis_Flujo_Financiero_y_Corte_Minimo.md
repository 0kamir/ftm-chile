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

# 💰 Análisis de Flujo Financiero Máximo y Corte Mínimo (Edmonds-Karp)

> [!IMPORTANT] Teorema Max-Flow Min-Cut aplicado a Persecución Patrimonial y Comiso
> Esta vista modela el grafo dirigido de desembolsos como una **Red de Flujo Capacitada** ($S \rightarrow \text{Entidad Origen} \rightarrow \text{Firmante Origen} \rightarrow \text{Firmante Destino} \rightarrow \text{Entidad Destino} \rightarrow T$) y ejecuta el algoritmo de **Edmonds-Karp ($O(VE^2)$)** junto con optimización submodular de **Interdicción Patrimonial** para determinar el número mínimo de operadores cuyas cuentas/patrimonios deben ser objeto de medidas precautorias para interceptar el **100% del flujo financiero investigado**.

## 1. Métricas Globales de Flujo y Desigualdad Financiera

- **Flujo Máximo Auditado ($f^*$ de Edmonds-Karp)**: **`$669.122.093.990 CLP`** *(100% consistente con la suma de aristas `TRX` con flujo monetario)*
- **Capacidad del Corte Mínimo ($c(S, T)$)**: **`$669.122.093.990 CLP`** across `31` cuellos de botella primarios.
- **Coeficiente de Gini por Transacción (`TRX`)**: `0.8283`
- **Coeficiente de Gini por Causa Penal**: `0.7517`
- **Coeficiente de Gini por Operador / Firmante**: `0.7618`
- **Operadores requeridos para interceptar el 100% del flujo**: `30` personas (de un total de `61` firmantes con flujo monetario).

---

## 2. Curva de Interdicción Patrimonial Óptima (Medidas Precautorias / Comiso)

Orden óptimo de congelamiento de activos / medidas precautorias reales para maximizar el monto fiscal y corporativo interceptado en cada paso:

| Paso | Operador / Firmante Objetivo | TRX Interceptadas | Monto Marginal Interceptado | Monto Acumulado | % del Flujo Total |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | [[Sebastian Pinera Echenique]] | `4` | `$107.550.000.000 CLP` | `$107.550.000.000 CLP` | **`16.07%`** |
| **2** | [[Eliodoro Matte Larrain]] | `1` | `$97.500.000.000 CLP` | `$205.050.000.000 CLP` | **`30.64%`** |
| **3** | [[Agustin Edwards Eastman]] | `3` | `$43.800.000.000 CLP` | `$248.850.000.000 CLP` | **`37.19%`** |
| **4** | [[Gonzalo Vial Vial]] | `1` | `$38.400.000.000 CLP` | `$287.250.000.000 CLP` | **`42.93%`** |
| **5** | [[Cathy Barriga Guerra]] | `1` | `$30.972.000.000 CLP` | `$318.222.000.000 CLP` | **`47.56%`** |
| **6** | [[Flavio Echeverria Cortez]] | `2` | `$29.798.928.198 CLP` | `$348.020.928.198 CLP` | **`52.01%`** |
| **7** | [[Augusto Pinochet Ugarte]] | `4` | `$24.650.000.000 CLP` | `$372.670.928.198 CLP` | **`55.70%`** |
| **8** | [[Carlos Pavez Tolosa]] | `1` | `$14.200.000.000 CLP` | `$386.870.928.198 CLP` | **`57.82%`** |
| **9** | [[Sergio Munoz Gajardo]] | `4` | `$13.550.000.000 CLP` | `$400.420.928.198 CLP` | **`59.84%`** |
| **10** | [[Juan Miguel Fuente-Alba Poblete]] | `2` | `$9.600.000.000 CLP` | `$410.020.928.198 CLP` | **`61.28%`** |
| **11** | [[Jorge Zepeda Arancibia]] | `1` | `$3.450.000.000 CLP` | `$413.470.928.198 CLP` | **`61.79%`** |
| **12** | [[Alberto Larrain Salas]] | `2` | `$3.053.000.000 CLP` | `$416.523.928.198 CLP` | **`62.25%`** |
| **13** | [[Natalia Compagnon Soto]] | `1` | `$2.500.000.000 CLP` | `$419.023.928.198 CLP` | **`62.62%`** |
| **14** | [[Jose Codner Chijner]] | `1` | `$2.180.000.000 CLP` | `$421.203.928.198 CLP` | **`62.95%`** |
| **15** | [[Pablo Longueira Montes]] | `2` | `$1.990.000.000 CLP` | `$423.193.928.198 CLP` | **`63.25%`** |
| **16** | [[Marcelo Torres Ferrari]] | `2` | `$1.306.500.000 CLP` | `$424.500.428.198 CLP` | **`63.44%`** |
| **17** | [[Carlos Cruz Lorenzen]] | `1` | `$1.253.000.000 CLP` | `$425.753.428.198 CLP` | **`63.63%`** |
| **18** | [[Luis Hermosilla Osorio]] | `3` | `$770.000.000 CLP` | `$426.523.428.198 CLP` | **`63.74%`** |
| **19** | [[Domingo Prieto Urrejola]] | `1` | `$759.000.000 CLP` | `$427.282.428.198 CLP` | **`63.86%`** |
| **20** | [[Carlos Contreras Gutierrez]] | `3` | `$426.000.000 CLP` | `$427.708.428.198 CLP` | **`63.92%`** |
| **21** | [[Patricio Contesse Gonzalez]] | `1` | `$340.000.000 CLP` | `$428.048.428.198 CLP` | **`63.97%`** |
| **22** | [[Camila Polizzi Fonceca]] | `1` | `$250.635.000 CLP` | `$428.299.063.198 CLP` | **`64.01%`** |
| **23** | [[Hartmut Hopp Miottel]] | `1` | `$240.000.000 CLP` | `$428.539.063.198 CLP` | **`64.04%`** |
| **24** | [[Francisco Mujica Ortuzar]] | `1` | `$233.000.000 CLP` | `$428.772.063.198 CLP` | **`64.08%`** |
| **25** | [[Carlos Alberto Delano Abbott]] | `1` | `$156.000.000 CLP` | `$428.928.063.198 CLP` | **`64.10%`** |
| **26** | [[Jorge Silva Menares]] | `1` | `$55.030.792 CLP` | `$428.983.093.990 CLP` | **`64.11%`** |
| **27** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `1` | `$42.000.000 CLP` | `$429.025.093.990 CLP` | **`64.12%`** |
| **28** | [[Leon Marcelo Lefort Hernandez]] | `1` | `$37.000.000 CLP` | `$429.062.093.990 CLP` | **`64.12%`** |
| **29** | [[Camila Flores Oporto]] | `1` | `$35.000.000 CLP` | `$429.097.093.990 CLP` | **`64.13%`** |
| **30** | [[Alex Smith Leay]] | `1` | `$25.000.000 CLP` | `$429.122.093.990 CLP` | **`64.13%`** |

---

## 3. Canales de Flujo Financiero (`Firmante Origen → Firmante Destino`)

| # | Autorizador (Origen) | Entidad Emisora | Receptor (Destino) | Entidad Receptora | TRX | Caudal Acumulado (CLP) | Causa(s) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | [[]] | [[]] | [[]] | [[Servicio Impuestos Internos]] | `1` | **`$240.000.000.000 CLP`** | [[Caso Megafraude Tributario Operacion Tributos]] |
| **2** | [[Eliodoro Matte Larrain]] | [[Empresas CMPC SA]] | [[Gabriel Ruiz-Tagle Serrano]] | [[Servicio Nacional del Consumidor]] | `1` | **`$97.500.000.000 CLP`** | [[Caso Colusion del Papel Tissue]] |
| **3** | [[Carlos Alberto Delano Abbott]] | [[Andes Iron SpA]] | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | `1` | **`$75.500.000.000 CLP`** | [[Caso Minera Dominga Pandora Papers]] |
| **4** | [[Gonzalo Vial Vial]] | [[Agrosuper SA]] | [[Manuel Ariztia Ruiz]] | [[Corte Suprema de Chile]] | `1` | **`$38.400.000.000 CLP`** | [[Caso Colusion de los Pollos]] |
| **5** | [[Cathy Barriga Guerra]] | [[Municipalidad de Maipu]] | [[Cathy Barriga Guerra]] | [[Municipalidad de Maipu]] | `1` | **`$30.972.000.000 CLP`** | [[Caso Municipalidad de Maipu]] |
| **6** | [[Flavio Echeverria Cortez]] | [[Direccion de Finanzas de Carabineros]] | [[Jaime Paz Meneses]] | [[Direccion de Finanzas de Carabineros]] | `1` | **`$28.348.928.198 CLP`** | [[Caso Pacogate]] |
| **7** | [[Agustin Edwards Eastman]] | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Alfredo Ovalle Rodriguez]] | [[Unidad de Analisis Financiero]] | `1` | **`$19.500.000.000 CLP`** | [[Caso Panama Papers Chile]] |
| **8** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Sergio Munoz Gajardo]] | [[Corte Suprema de Chile]] | `1` | **`$18.500.000.000 CLP`** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] |
| **9** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | `1` | **`$15.800.000.000 CLP`** | [[Caso Riggs]] |
| **10** | [[Agustin Edwards Eastman]] | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | `1` | **`$14.800.000.000 CLP`** | [[Caso Operacion FUBELT Intervencion CIA y DINA]] |
| **11** | [[Gonzalo Delaveau Swett]] | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Carlos Pavez Tolosa]] | [[Servicio Impuestos Internos]] | `1` | **`$14.200.000.000 CLP`** | [[Caso Panama Papers Chile]] |
| **12** | [[Lucia Hiriart Rodriguez]] | [[Fundacion CEMA Chile]] | [[Sergio Munoz Gajardo]] | [[Corte Suprema de Chile]] | `1` | **`$10.500.000.000 CLP`** | [[Caso CEMA Chile]] |
| **13** | [[Manuel Contreras Sepulveda]] | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Agustin Edwards Eastman]] | [[Empresa El Mercurio SAP]] | `1` | **`$9.500.000.000 CLP`** | [[Caso Operacion FUBELT Intervencion CIA y DINA]] |
| **14** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Santiago Valdes Gutierrez]] | [[Contraloria General de la Republica]] | `1` | **`$8.250.000.000 CLP`** | [[Caso Exalmar y Fideicomiso Ciego]] |
| **15** | [[Juan Miguel Fuente-Alba Poblete]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Jozo Santic Palomino]] | [[Frasim Ltda]] | `1` | **`$6.100.000.000 CLP`** | [[Caso Milicogate]] |
| **16** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Carlos Pavez Tolosa]] | [[Comision para el Mercado Financiero]] | `1` | **`$5.300.000.000 CLP`** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] |
| **17** | [[Oscar Aitken Lavanchy]] | [[Mossack Fonseca y Sociedades Offshore Panama]] | [[Augusto Pinochet Ugarte]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | `1` | **`$3.800.000.000 CLP`** | [[Caso Panama Papers Chile]] |
| **18** | [[Juan Miguel Fuente-Alba Poblete]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$3.500.000.000 CLP`** | [[Caso Milicogate]] |
| **19** | [[Paul Schafer Schneider]] | [[Sociedad Benefactora y Educacional Dignidad]] | [[Jorge Zepeda Arancibia]] | [[Servicio Impuestos Internos]] | `1` | **`$3.450.000.000 CLP`** | [[Caso Colonia Dignidad]] |
| **20** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Augusto Pinochet Hiriart]] | [[Valmoval Ltda]] | `1` | **`$2.950.000.000 CLP`** | [[Caso Pinocheques]] |
| **21** | [[Rodrigo Diaz Worner]] | [[GORE Biobio]] | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | `1` | **`$2.553.000.000 CLP`** | [[Caso Convenios]] |
| **22** | [[Natalia Compagnon Soto]] | [[Exportadora y de Gestion Caval Ltda]] | [[Natalia Compagnon Soto]] | [[Servicio Impuestos Internos]] | `1` | **`$2.500.000.000 CLP`** | [[Caso Caval]] |
| **23** | [[Lucia Hiriart Rodriguez]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | `1` | **`$2.450.000.000 CLP`** | [[Caso Riggs]] |
| **24** | [[Roberto Belloni Pechini]] | [[Farmacias Salcobrand SA]] | [[Jose Codner Chijner]] | [[Servicio Nacional del Consumidor]] | `1` | **`$2.180.000.000 CLP`** | [[Caso Colusion de las Farmacias]] |
| **25** | [[Manuel Contreras Sepulveda]] | [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | `1` | **`$2.100.000.000 CLP`** | [[Caso Operacion FUBELT Intervencion CIA y DINA]] |
| **26** | [[Flavio Echeverria Cortez]] | [[Direccion de Finanzas de Carabineros]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$1.450.000.000 CLP`** | [[Caso Pacogate]] |
| **27** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | `1` | **`$1.260.000.000 CLP`** | [[Caso Penta]] |
| **28** | [[Carlos Cruz Lorenzen]] | [[Ministerio de Obras Publicas]] | [[Hector Pena Veliz]] | [[Gestion Ambiental y Territorial SA]] | `1` | **`$1.253.000.000 CLP`** | [[Caso MOP-Gate]] |
| **29** | [[Luis Plaza Sanchez]] | [[Municipalidad de Cerro Navia]] | [[Marcelo Torres Ferrari]] | [[KDM Empresas SA]] | `1` | **`$1.120.000.000 CLP`** | [[Caso Basura]] |
| **30** | [[Raul Torrealba del Pedregal]] | [[Municipalidad de Vitacura]] | [[Domingo Prieto Urrejola]] | [[Vita Deportes]] | `1` | **`$759.000.000 CLP`** | [[Caso Vitacura]] |
| **31** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | `1` | **`$730.000.000 CLP`** | [[Caso SQM]] |
| **32** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | `1` | **`$500.000.000 CLP`** | [[Caso Convenios]] |
| **33** | [[Claudio Spiniak Vilensky]] | [[Inversiones El Bosque Ltda]] | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | `1` | **`$480.000.000 CLP`** | [[Caso Spiniak]] |
| **34** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$480.000.000 CLP`** | [[Caso Audios]] |
| **35** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | `3` | **`$426.000.000 CLP`** | [[Caso Convenios]] |
| **36** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[Santiago Valdes Gutierrez]] | [[Bancard Inversiones Ltda]] | `1` | **`$340.000.000 CLP`** | [[Caso SQM]] |
| **37** | [[Rodrigo Diaz Worner]] | [[GORE Biobio]] | [[Camila Polizzi Fonceca]] | [[Fundacion En Ti]] | `1` | **`$250.635.000 CLP`** | [[Caso Convenios]] |
| **38** | [[Hernan Larrain Fernandez]] | [[Union Democrata Independiente]] | [[Hartmut Hopp Miottel]] | [[Sociedad Benefactora y Educacional Dignidad]] | `1` | **`$240.000.000 CLP`** | [[Caso Colonia Dignidad]] |
| **39** | [[Francisco Mujica Ortuzar]] | [[Corpesca SA]] | [[Jaime Orpis Bouchon]] | [[Senado de la Republica de Chile]] | `1` | **`$233.000.000 CLP`** | [[Caso Corpesca]] |
| **40** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Andres Chadwick Pinera]] | [[Senado de la Republica de Chile]] | `1` | **`$190.000.000 CLP`** | [[Caso Audios]] |
| **41** | [[Fernando Leon Steffens]] | [[KDM Empresas SA]] | [[Marcelo Torres Ferrari]] | [[Municipalidad de Maipu]] | `1` | **`$186.500.000 CLP`** | [[Caso Basura]] |
| **42** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[Jovino Novoa Vasquez]] | [[Union Democrata Independiente]] | `1` | **`$156.000.000 CLP`** | [[Caso Penta]] |
| **43** | [[Pia Guzman Mena]] | [[Renovacion Nacional]] | [[Sergio Munoz Gajardo]] | [[Corte Suprema de Chile]] | `1` | **`$120.000.000 CLP`** | [[Caso Spiniak]] |
| **44** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Leonarda Villalobos Muth]] | [[Servicio Impuestos Internos]] | `1` | **`$100.000.000 CLP`** | [[Caso Audios]] |
| **45** | [[]] | [[]] | [[Jorge Silva Menares]] | [[Municipalidad de Machali]] | `1` | **`$55.030.792 CLP`** | [[Caso Caval]] |
| **46** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | [[Empresas Penta SA]] | [[Pablo Wagner San Martin]] | [[Servicio Impuestos Internos]] | `1` | **`$42.000.000 CLP`** | [[Caso Penta]] |
| **47** | [[Leon Marcelo Lefort Hernandez]] | [[Itelecom Holding Chile SpA]] | [[Marcelo Campos Henriquez]] | [[Municipalidad de Chillan]] | `1` | **`$37.000.000 CLP`** | [[Caso Luminarias LED]] |
| **48** | [[Senado de la Republica de Chile]] | [[Senado de la Republica de Chile]] | [[Camila Flores Oporto]] | [[Camila Flores Oporto]] | `1` | **`$35.000.000 CLP`** | [[Caso Asignaciones Parlamentarias y Cuota Flores]] |
| **49** | [[Patricio Marin Lazo]] | [[Direccion de Inteligencia Policial de Carabineros]] | [[Alex Smith Leay]] | [[Direccion de Inteligencia Policial de Carabineros]] | `1` | **`$25.000.000 CLP`** | [[Caso Operacion Huracan]] |

---

## 4. Diagrama Topológico de Cuellos de Botella Financieros (Top 8 Canales)

```mermaid
flowchart LR
    EO1[""] -->|"$ 240.000M"| FO1[""] -->|"$ 240.000M"| FD1[""] --> ED1["Servicio Impuestos Internos"]
    EO2["Empresas CMPC SA"] -->|"$ 97.500M"| FO2["Eliodoro Matte Larrain"] -->|"$ 97.500M"| FD2["Gabriel Ruiz-Tagle Serrano"] --> ED2["Servicio Nacional del Consumidor"]
    EO3["Andes Iron SpA"] -->|"$ 75.500M"| FO3["Carlos Alberto Delano Abbott"] -->|"$ 75.500M"| FD3["Sebastian Pinera Echenique"] --> ED3["Bancard Inversiones Ltda"]
    EO4["Agrosuper SA"] -->|"$ 38.400M"| FO4["Gonzalo Vial Vial"] -->|"$ 38.400M"| FD4["Manuel Ariztia Ruiz"] --> ED4["Corte Suprema de Chile"]
    EO5["Municipalidad de Maipu"] -->|"$ 30.972M"| FO5["Cathy Barriga Guerra"] -->|"$ 30.972M"| FD5["Cathy Barriga Guerra"] --> ED5["Municipalidad de Maipu"]
    EO6["Direccion de Finanzas de Carabineros"] -->|"$ 28.349M"| FO6["Flavio Echeverria Cortez"] -->|"$ 28.349M"| FD6["Jaime Paz Meneses"] --> ED6["Direccion de Finanzas de Carabineros"]
    EO7["Mossack Fonseca y Sociedades Offshore Panama"] -->|"$ 19.500M"| FO7["Agustin Edwards Eastman"] -->|"$ 19.500M"| FD7["Alfredo Ovalle Rodriguez"] --> ED7["Unidad de Analisis Financiero"]
    EO8["Bancard Inversiones Ltda"] -->|"$ 18.500M"| FO8["Sebastian Pinera Echenique"] -->|"$ 18.500M"| FD8["Sergio Munoz Gajardo"] --> ED8["Corte Suprema de Chile"]
```
