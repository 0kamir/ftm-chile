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

- **Flujo Máximo Registrado ($f^*$ de Edmonds-Karp)**: **`$571.452.093.990 CLP`** *(100% consistente con la suma de aristas `TRX` con flujo monetario)*
- **Capacidad del Corte Mínimo ($c(S, T)$)**: **`$571.452.093.990 CLP`** across `24` cuellos de botella primarios.
- **Coeficiente de Gini por Transacción (`TRX`)**: `0.8574`
- **Coeficiente de Gini por Causa Penal**: `0.7892`
- **Coeficiente de Gini por Firmante**: `0.7931`
- **Firmantes que concentran el 100% de los montos**: `26` personas (de un total de `51` firmantes con flujo monetario).

---

## 2. Curva de Retiro de nodos Óptima (Medidas Precautorias / Comiso)

Orden óptimo de congelamiento de activos / medidas precautorias reales para maximizar el monto fiscal y corporativo interceptado en cada paso:

| Paso | Firmante | TRX Cubiertas | Monto Marginal Cubierto | Monto Acumulado | % del Flujo Total |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | [[Eliodoro Matte Larrain]] | `1` | `$97.500.000.000 CLP` | `$97.500.000.000 CLP` | **`17.06%`** |
| **2** | [[Sebastian Pinera Echenique]] | `3` | `$89.050.000.000 CLP` | `$186.550.000.000 CLP` | **`32.64%`** |
| **3** | [[Gonzalo Vial Vial]] | `1` | `$38.400.000.000 CLP` | `$224.950.000.000 CLP` | **`39.36%`** |
| **4** | [[Cathy Barriga Guerra]] | `1` | `$30.972.000.000 CLP` | `$255.922.000.000 CLP` | **`44.78%`** |
| **5** | [[Flavio Echeverria Cortez]] | `2` | `$29.798.928.198 CLP` | `$285.720.928.198 CLP` | **`50.00%`** |
| **6** | [[Augusto Pinochet Ugarte]] | `2` | `$18.750.000.000 CLP` | `$304.470.928.198 CLP` | **`53.28%`** |
| **7** | [[Juan Miguel Fuente-Alba Poblete]] | `2` | `$9.600.000.000 CLP` | `$314.070.928.198 CLP` | **`54.96%`** |
| **8** | [[Alberto Larrain Salas]] | `2` | `$3.053.000.000 CLP` | `$317.123.928.198 CLP` | **`55.49%`** |
| **9** | [[Natalia Compagnon Soto]] | `1` | `$2.500.000.000 CLP` | `$319.623.928.198 CLP` | **`55.93%`** |
| **10** | [[Lucia Hiriart Rodriguez]] | `1` | `$2.450.000.000 CLP` | `$322.073.928.198 CLP` | **`56.36%`** |
| **11** | [[Jose Codner Chijner]] | `1` | `$2.180.000.000 CLP` | `$324.253.928.198 CLP` | **`56.74%`** |
| **12** | [[Pablo Longueira Montes]] | `2` | `$1.990.000.000 CLP` | `$326.243.928.198 CLP` | **`57.09%`** |
| **13** | [[Marcelo Torres Ferrari]] | `2` | `$1.306.500.000 CLP` | `$327.550.428.198 CLP` | **`57.32%`** |
| **14** | [[Carlos Cruz Lorenzen]] | `1` | `$1.253.000.000 CLP` | `$328.803.428.198 CLP` | **`57.54%`** |
| **15** | [[Domingo Prieto Urrejola]] | `1` | `$759.000.000 CLP` | `$329.562.428.198 CLP` | **`57.67%`** |
| **16** | [[Carlos Contreras Gutierrez]] | `3` | `$426.000.000 CLP` | `$329.988.428.198 CLP` | **`57.75%`** |
| **17** | [[Patricio Contesse Gonzalez]] | `1` | `$340.000.000 CLP` | `$330.328.428.198 CLP` | **`57.81%`** |
| **18** | [[Luis Hermosilla Osorio]] | `2` | `$290.000.000 CLP` | `$330.618.428.198 CLP` | **`57.86%`** |
| **19** | [[Camila Polizzi Fonceca]] | `1` | `$250.635.000 CLP` | `$330.869.063.198 CLP` | **`57.90%`** |
| **20** | [[Francisco Mujica Ortuzar]] | `1` | `$233.000.000 CLP` | `$331.102.063.198 CLP` | **`57.94%`** |
| **21** | [[Carlos Alberto Delano Abbott]] | `1` | `$156.000.000 CLP` | `$331.258.063.198 CLP` | **`57.97%`** |
| **22** | [[Jorge Silva Menares]] | `1` | `$55.030.792 CLP` | `$331.313.093.990 CLP` | **`57.98%`** |
| **23** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `1` | `$42.000.000 CLP` | `$331.355.093.990 CLP` | **`57.98%`** |
| **24** | [[Leon Marcelo Lefort Hernandez]] | `1` | `$37.000.000 CLP` | `$331.392.093.990 CLP` | **`57.99%`** |
| **25** | [[Camila Flores Oporto]] | `1` | `$35.000.000 CLP` | `$331.427.093.990 CLP` | **`58.00%`** |
| **26** | [[Alex Smith Leay]] | `1` | `$25.000.000 CLP` | `$331.452.093.990 CLP` | **`58.00%`** |

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
| **7** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Oscar Aitken Lavanchy]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | `1` | **`$15.800.000.000 CLP`** | [[Caso Riggs]] |
| **8** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Santiago Valdes Gutierrez]] | [[Contraloria General de la Republica]] | `1` | **`$8.250.000.000 CLP`** | [[Caso Exalmar y Fideicomiso Ciego]] |
| **9** | [[Juan Miguel Fuente-Alba Poblete]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Jozo Santic Palomino]] | [[Frasim Ltda]] | `1` | **`$6.100.000.000 CLP`** | [[Caso Milicogate]] |
| **10** | [[Sebastian Pinera Echenique]] | [[Bancard Inversiones Ltda]] | [[Carlos Pavez Tolosa]] | [[Comision para el Mercado Financiero]] | `1` | **`$5.300.000.000 CLP`** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] |
| **11** | [[Juan Miguel Fuente-Alba Poblete]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$3.500.000.000 CLP`** | [[Caso Milicogate]] |
| **12** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | [[Augusto Pinochet Hiriart]] | [[Valmoval Ltda]] | `1` | **`$2.950.000.000 CLP`** | [[Caso Pinocheques]] |
| **13** | [[Rodrigo Diaz Worner]] | [[GORE Biobio]] | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | `1` | **`$2.553.000.000 CLP`** | [[Caso Convenios]] |
| **14** | [[Natalia Compagnon Soto]] | [[Exportadora y de Gestion Caval Ltda]] | [[Natalia Compagnon Soto]] | [[Servicio Impuestos Internos]] | `1` | **`$2.500.000.000 CLP`** | [[Caso Caval]] |
| **15** | [[Lucia Hiriart Rodriguez]] | [[Riggs Bank y Sociedades Offshore Ashburton]] | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | `1` | **`$2.450.000.000 CLP`** | [[Caso Riggs]] |
| **16** | [[Roberto Belloni Pechini]] | [[Farmacias Salcobrand SA]] | [[Jose Codner Chijner]] | [[Servicio Nacional del Consumidor]] | `1` | **`$2.180.000.000 CLP`** | [[Caso Colusion de las Farmacias]] |
| **17** | [[Flavio Echeverria Cortez]] | [[Direccion de Finanzas de Carabineros]] | [[Javier Cruz Tamburrino]] | [[Unidad de Analisis Financiero]] | `1` | **`$1.450.000.000 CLP`** | [[Caso Pacogate]] |
| **18** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | `1` | **`$1.260.000.000 CLP`** | [[Caso Penta]] |
| **19** | [[Carlos Cruz Lorenzen]] | [[Ministerio de Obras Publicas]] | [[Hector Pena Veliz]] | [[Gestion Ambiental y Territorial SA]] | `1` | **`$1.253.000.000 CLP`** | [[Caso MOP-Gate]] |
| **20** | [[Luis Plaza Sanchez]] | [[Municipalidad de Cerro Navia]] | [[Marcelo Torres Ferrari]] | [[KDM Empresas SA]] | `1` | **`$1.120.000.000 CLP`** | [[Caso Basura]] |
| **21** | [[Raul Torrealba del Pedregal]] | [[Municipalidad de Vitacura]] | [[Domingo Prieto Urrejola]] | [[Vita Deportes]] | `1` | **`$759.000.000 CLP`** | [[Caso Vitacura]] |
| **22** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[Pablo Longueira Montes]] | [[Union Democrata Independiente]] | `1` | **`$730.000.000 CLP`** | [[Caso SQM]] |
| **23** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | [[Alberto Larrain Salas]] | [[Fundacion ProCultura]] | `1` | **`$500.000.000 CLP`** | [[Caso Convenios]] |
| **24** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | [[Daniel Andrade Schwarze]] | [[Fundacion Democracia Viva]] | `3` | **`$426.000.000 CLP`** | [[Caso Convenios]] |
| **25** | [[Patricio Contesse Gonzalez]] | [[SQM SA]] | [[Santiago Valdes Gutierrez]] | [[Bancard Inversiones Ltda]] | `1` | **`$340.000.000 CLP`** | [[Caso SQM]] |
| **26** | [[Rodrigo Diaz Worner]] | [[GORE Biobio]] | [[Camila Polizzi Fonceca]] | [[Fundacion En Ti]] | `1` | **`$250.635.000 CLP`** | [[Caso Convenios]] |
| **27** | [[Francisco Mujica Ortuzar]] | [[Corpesca SA]] | [[Jaime Orpis Bouchon]] | [[Senado de la Republica de Chile]] | `1` | **`$233.000.000 CLP`** | [[Caso Corpesca]] |
| **28** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Andres Chadwick Pinera]] | [[Senado de la Republica de Chile]] | `1` | **`$190.000.000 CLP`** | [[Caso Audios]] |
| **29** | [[Fernando Leon Steffens]] | [[KDM Empresas SA]] | [[Marcelo Torres Ferrari]] | [[Municipalidad de Maipu]] | `1` | **`$186.500.000 CLP`** | [[Caso Basura]] |
| **30** | [[Carlos Alberto Delano Abbott]] | [[Empresas Penta SA]] | [[Jovino Novoa Vasquez]] | [[Union Democrata Independiente]] | `1` | **`$156.000.000 CLP`** | [[Caso Penta]] |
| **31** | [[Luis Hermosilla Osorio]] | [[Factop SpA]] | [[Leonarda Villalobos Muth]] | [[Servicio Impuestos Internos]] | `1` | **`$100.000.000 CLP`** | [[Caso Audios]] |
| **32** | [[]] | [[]] | [[Jorge Silva Menares]] | [[Municipalidad de Machali]] | `1` | **`$55.030.792 CLP`** | [[Caso Caval]] |
| **33** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | [[Empresas Penta SA]] | [[Pablo Wagner San Martin]] | [[Servicio Impuestos Internos]] | `1` | **`$42.000.000 CLP`** | [[Caso Penta]] |
| **34** | [[Leon Marcelo Lefort Hernandez]] | [[Itelecom Holding Chile SpA]] | [[Marcelo Campos Henriquez]] | [[Municipalidad de Chillan]] | `1` | **`$37.000.000 CLP`** | [[Caso Luminarias LED]] |
| **35** | [[Senado de la Republica de Chile]] | [[Senado de la Republica de Chile]] | [[Camila Flores Oporto]] | [[Camila Flores Oporto]] | `1` | **`$35.000.000 CLP`** | [[Caso Asignaciones Parlamentarias y Cuota Flores]] |
| **36** | [[Patricio Marin Lazo]] | [[Direccion de Inteligencia Policial de Carabineros]] | [[Alex Smith Leay]] | [[Direccion de Inteligencia Policial de Carabineros]] | `1` | **`$25.000.000 CLP`** | [[Caso Operacion Huracan]] |

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
    EO7["Comando de Apoyo a la Fuerza del Ejercito"] -->|"$ 15.800M"| FO7["Augusto Pinochet Ugarte"] -->|"$ 15.800M"| FD7["Oscar Aitken Lavanchy"] --> ED7["Riggs Bank y Sociedades Offshore Ashburton"]
    EO8["Bancard Inversiones Ltda"] -->|"$ 8.250M"| FO8["Sebastian Pinera Echenique"] -->|"$ 8.250M"| FD8["Santiago Valdes Gutierrez"] --> ED8["Contraloria General de la Republica"]
```
