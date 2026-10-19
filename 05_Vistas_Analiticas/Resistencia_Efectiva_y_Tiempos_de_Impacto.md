---
tipo_nodo: vista_analitica
titulo: "Resistencia Efectiva de Kirchhoff, Pseudoinversa L+ y Tiempos de Impacto de Markov"
actualizacion_automatica: true
tags:
  - resistencia-efectiva
  - indice-kirchhoff
  - moore-penrose
  - constante-kemeny
---

# ⚡ Resistencia Efectiva de Kirchhoff ($\Omega_{uv}$), Pseudoinversa $L^+$ y Tiempos de Impacto ($H_{uv}$)

> [!IMPORTANT] Redes Eléctricas de Kirchhoff y Cadenas de Markov sobre Grafos Forenses
> A diferencia de la distancia geodésica más corta (que ignora caminos alternativos), la **Distancia de Resistencia Efectiva de Klein & Randić ($\Omega_{uv} = L^+_{uu} + L^+_{vv} - 2L^+_{uv}$)** modela cada vínculo como un resistor de $1\,\Omega$ y pondera simultáneamente **todos los caminos paralelos** entre dos sujetos:
> 1. **Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$)**: Identifica los nodos con menor impedancia global hacia el resto del aparato criminal/institucional.
> 2. **Tiempo de Conmutación e Impacto de Tetali ($H_{uv} + H_{vu}$)** y **Constante de Kemeny ($K(G)$)**: Miden el número esperado de pasos de una auditoría o contagio estocástico para transitar entre dos actores cualesquiera.

## 1. Invariantes Eléctricos y Estocásticos del Grafo

- **Cobertura del Componente Gigante Conectado (LCC)**: **`216 / 236` nodos operativos (`91.5%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`60770.46 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`2.6172 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`783.77 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.6614`** | `0.2025` | `13` |
| **2** | [[Union Democrata Independiente]] | `partido_politico` | **`0.6388`** | `0.2557` | `15` |
| **3** | [[Sebastian Pinera Echenique]] | `persona` | **`0.6299`** | `0.2778` | `7` |
| **4** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.6295`** | `0.2786` | `8` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.6109`** | `0.3269` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.6092`** | `0.3314` | `5` |
| **7** | [[Renovacion Nacional]] | `partido_politico` | **`0.6059`** | `0.3402` | `10` |
| **8** | [[Sergio Munoz Gajardo]] | `persona` | **`0.6033`** | `0.3474` | `5` |
| **9** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.5966`** | `0.3660` | `8` |
| **10** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | **`0.5959`** | `0.3679` | `5` |
| **11** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`0.5871`** | `0.3930` | `5` |
| **12** | [[Factop SpA]] | `entidad_privada` | **`0.5831`** | `0.4046` | `6` |
| **13** | [[Luis Hermosilla Osorio]] | `persona` | **`0.5831`** | `0.4046` | `6` |
| **14** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.5823`** | `0.4067` | `6` |
| **15** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.5818`** | `0.4082` | `5` |
| **16** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.5778`** | `0.4202` | `6` |
| **17** | [[Caso Audios]] | `causa_judicial` | **`0.5735`** | `0.4332` | `5` |
| **18** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.5717`** | `0.4386` | `5` |
| **19** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `nexo_transaccion` | **`0.5688`** | `0.4473` | `5` |
| **20** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `nexo_transaccion` | **`0.5669`** | `0.4532` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3841 Ω`** | `2.6038 S` | `278.8 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4058 Ω`** | `2.4645 S` | `294.6 pasos` |
| **3** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4152 Ω`** | `2.4085 S` | `301.4 pasos` |
| **4** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4308 Ω`** | `2.3213 S` | `312.7 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4322 Ω`** | `2.3137 S` | `313.8 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4475 Ω`** | `2.2346 S` | `324.9 pasos` |
| **7** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4544 Ω`** | `2.2009 S` | `329.9 pasos` |
| **8** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4655 Ω`** | `2.1482 S` | `338.0 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4655 Ω`** | `2.1482 S` | `338.0 pasos` |
| **10** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4710 Ω`** | `2.1233 S` | `341.9 pasos` |
| **11** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4710 Ω`** | `2.1233 S` | `341.9 pasos` |
| **12** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4711 Ω`** | `2.1226 S` | `342.0 pasos` |
| **13** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4731 Ω`** | `2.1137 S` | `343.5 pasos` |
| **14** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4803 Ω`** | `2.0822 S` | `348.7 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4808 Ω`** | `2.0799 S` | `349.1 pasos` |
| **16** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4820 Ω`** | `2.0746 S` | `349.9 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4977 Ω`** | `2.0091 S` | `361.4 pasos` |
| **18** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5043 Ω`** | `1.9830 S` | `366.1 pasos` |
| **19** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.5046 Ω`** | `1.9816 S` | `366.4 pasos` |
| **20** | [[Bancard Inversiones Ltda]] | [[Corte Suprema de Chile]] | **`0.5265 Ω`** | `1.8994 S` | `382.2 pasos` |
