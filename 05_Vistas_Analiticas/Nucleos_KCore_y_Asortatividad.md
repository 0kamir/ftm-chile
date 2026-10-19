---
tipo_nodo: vista_analitica
titulo: "Descomposición k-Core, Capas de Cebolla, Asortatividad de Newman y Agujeros Estructurales de Burt"
actualizacion_automatica: true
tags:
  - k-core
  - asortatividad-newman
  - agujeros-estructurales-burt
  - analisis-forense
---

# 🧅 Núcleos $k$-Core, Asortatividad de Newman ($r$) y Agujeros Estructurales de Burt

> [!NOTE] Topología Núcleo-Periferia y Arbitraje de Agujeros Estructurales
> Esta vista implementa tres teoremas clásicos de la ciencia de redes criminales:
> 1. **Descomposición $k$-Core y *Onion Layers* (Batagelj & Zaversnik)**: Pela iterativamente la periferia del grafo hasta aislar el **Núcleo Profundo ($k_{\max}$)**.
> 2. **Coeficiente de Asortatividad de Grado de Newman ($r \in [-1, 1]$)**: Determina matemáticamente si la red es **disasortativa ($r < 0$)** —típico de células que compartimentan el riesgo mediante fundaciones u operadores satélite—.
> 3. **Restricción Estructural de Ronald Burt ($C_i$)**: Identifica los actores que explotan **Agujeros Estructurales** (menor restricción $C_i$ implica mayor poder de corretaje e intermediación exclusiva entre grupos desconectados).

## 1. Indicadores Estructurales Globales

- **Nodos Operativos Activos ($|V|$)**: `246` | **Aristas No Dirigidas ($|E|$)**: `417`
- **Coeficiente de Asortatividad de Grado de Newman ($r$)**: **`-0.0768`**
  - *Diagnóstico Topológico*: **Disasortativo (Arquitectura Hub-and-Spoke / Estrella: los grandes nodos articuladores operan a través de entidades instrumentales o testaferros periféricos)**
- **Degeneración / Coreness Máximo ($k_{\max}$)**: `3-Core`
- **Profundidad Máxima de Pelado (*Onion Layers*)**: `15 capas`

---

## 2. Brokers de Agujeros Estructurales (Menor Restricción de Burt $C_i$)

Actores institucionales, societarios y personales con grado $k_i \ge 2$ ordenados por **menor Restricción de Burt ($C_i$)** (mayor capacidad de arbitraje entre clústeres sin redundancia):

| Pos | Actor / Entidad | Tipo | Grado ($k_i$) | Restricción de Burt ($C_i$) | $k$-Core | Capa Cebolla |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | `13` | **`0.0769`** | `3` | `Capa #11` |
| **2** | [[Servicio Impuestos Internos]] | `entidad_publica` | `10` | **`0.1000`** | `3` | `Capa #11` |
| **3** | [[Union Democrata Independiente]] | `partido_politico` | `15` | **`0.1085`** | `3` | `Capa #11` |
| **4** | [[Renovacion Nacional]] | `partido_politico` | `10` | **`0.1169`** | `3` | `Capa #9` |
| **5** | [[Carlos Contreras Gutierrez]] | `persona` | `6` | **`0.1667`** | `3` | `Capa #13` |
| **6** | [[Augusto Pinochet Ugarte]] | `persona` | `8` | **`0.1725`** | `3` | `Capa #11` |
| **7** | [[Seremi MINVU Antofagasta]] | `entidad_publica` | `5` | **`0.2000`** | `3` | `Capa #13` |
| **8** | [[Comando de Apoyo a la Fuerza del Ejercito]] | `entidad_publica` | `5` | **`0.2000`** | `3` | `Capa #10` |
| **9** | [[Sergio Munoz Gajardo]] | `persona` | `5` | **`0.2000`** | `3` | `Capa #10` |
| **10** | [[Sebastian Pinera Echenique]] | `persona` | `7` | **`0.2180`** | `3` | `Capa #10` |
| **11** | [[Bancard Inversiones Ltda]] | `entidad_privada` | `6` | **`0.2629`** | `3` | `Capa #10` |
| **12** | [[Lucia Hiriart Rodriguez]] | `persona` | `6` | **`0.2631`** | `3` | `Capa #10` |
| **13** | [[Factop SpA]] | `entidad_privada` | `6` | **`0.3002`** | `3` | `Capa #13` |
| **14** | [[Luis Hermosilla Osorio]] | `persona` | `6` | **`0.3002`** | `3` | `Capa #13` |
| **15** | [[Carlos Alberto Delano Abbott]] | `persona` | `6` | **`0.3077`** | `3` | `Capa #11` |
| **16** | [[Daniel Andrade Schwarze]] | `persona` | `5` | **`0.3299`** | `3` | `Capa #15` |
| **17** | [[Unidad de Analisis Financiero]] | `entidad_publica` | `5` | **`0.3299`** | `3` | `Capa #10` |
| **18** | [[Alex Smith Leay]] | `persona` | `3` | **`0.3333`** | `3` | `Capa #9` |
| **19** | [[Andres Chadwick Pinera]] | `persona` | `3` | **`0.3333`** | `3` | `Capa #9` |
| **20** | [[Direccion de Inteligencia Policial de Carabineros]] | `entidad_publica` | `3` | **`0.3333`** | `3` | `Capa #9` |

---

## 3. Radiografía del Núcleo Profundo ($k$-Core = `3` y Capas Internas)

| # | Nodo del Núcleo | Categoría | $k$-Core | Capa Cebolla (*Onion Layer*) | Grado ($k_i$) | Restricción $C_i$ |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **1** | [[Daniel Andrade Schwarze]] | `persona` | **`3`** | **`Capa #15`** | `5` | `0.3299` |
| **2** | [[Fundacion Democracia Viva]] | `entidad_privada` | **`3`** | **`Capa #15`** | `4` | `0.4300` |
| **3** | [[TRX-2022-10-03-Convenio-DV-01]] | `nexo_transaccion` | **`3`** | **`Capa #14`** | `5` | `0.2401` |
| **4** | [[TRX-2022-10-19-Convenio-DV-02]] | `nexo_transaccion` | **`3`** | **`Capa #14`** | `5` | `0.2401` |
| **5** | [[TRX-2022-11-29-Convenio-DV-03]] | `nexo_transaccion` | **`3`** | **`Capa #14`** | `5` | `0.2401` |
| **6** | [[Caso Convenios]] | `causa_judicial` | **`3`** | **`Capa #13`** | `9` | `0.1111` |
| **7** | [[Carlos Contreras Gutierrez]] | `persona` | **`3`** | **`Capa #13`** | `6` | `0.1667` |
| **8** | [[Factop SpA]] | `entidad_privada` | **`3`** | **`Capa #13`** | `6` | `0.3002` |
| **9** | [[Luis Hermosilla Osorio]] | `persona` | **`3`** | **`Capa #13`** | `6` | `0.3002` |
| **10** | [[Seremi MINVU Antofagasta]] | `entidad_publica` | **`3`** | **`Capa #13`** | `5` | `0.2000` |
| **11** | [[Caso Audios]] | `causa_judicial` | **`3`** | **`Capa #12`** | `5` | `0.2000` |
| **12** | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | `nexo_transaccion` | **`3`** | **`Capa #12`** | `5` | `0.2352` |
| **13** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `nexo_transaccion` | **`3`** | **`Capa #12`** | `5` | `0.2289` |
| **14** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `nexo_transaccion` | **`3`** | **`Capa #12`** | `5` | `0.2289` |
| **15** | [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | `nexo_transaccion` | **`3`** | **`Capa #12`** | `5` | `0.2352` |
| **16** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | **`3`** | **`Capa #12`** | `5` | `0.2289` |
| **17** | [[Union Democrata Independiente]] | `partido_politico` | **`3`** | **`Capa #11`** | `15` | `0.1085` |
| **18** | [[Corte Suprema de Chile]] | `entidad_publica` | **`3`** | **`Capa #11`** | `13` | `0.0769` |
| **19** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`3`** | **`Capa #11`** | `10` | `0.1000` |
| **20** | [[Augusto Pinochet Ugarte]] | `persona` | **`3`** | **`Capa #11`** | `8` | `0.1725` |
| **21** | [[Carlos Alberto Delano Abbott]] | `persona` | **`3`** | **`Capa #11`** | `6` | `0.3077` |
| **22** | [[Alberto Larrain Salas]] | `persona` | **`3`** | **`Capa #11`** | `5` | `0.3600` |
| **23** | [[Fundacion ProCultura]] | `entidad_privada` | **`3`** | **`Capa #11`** | `5` | `0.3600` |
| **24** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`3`** | **`Capa #11`** | `5` | `0.2267` |
| **25** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`3`** | **`Capa #11`** | `5` | `0.2000` |
