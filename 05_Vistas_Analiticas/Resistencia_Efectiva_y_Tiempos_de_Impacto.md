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

- **Cobertura del Componente Gigante Conectado (LCC)**: **`209 / 229` nodos operativos (`91.3%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`56912.27 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`2.6183 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`767.08 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.6553`** | `0.2158` | `10` |
| **2** | [[Union Democrata Independiente]] | `partido_politico` | **`0.6389`** | `0.2547` | `15` |
| **3** | [[Sebastian Pinera Echenique]] | `persona` | **`0.6296`** | `0.2778` | `7` |
| **4** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.6287`** | `0.2801` | `8` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.6107`** | `0.3268` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.6076`** | `0.3351` | `5` |
| **7** | [[Renovacion Nacional]] | `partido_politico` | **`0.6059`** | `0.3397` | `10` |
| **8** | [[Sergio Munoz Gajardo]] | `persona` | **`0.6017`** | `0.3511` | `5` |
| **9** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.5954`** | `0.3687` | `8` |
| **10** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | **`0.5942`** | `0.3721` | `5` |
| **11** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`0.5860`** | `0.3954` | `5` |
| **12** | [[Factop SpA]] | `entidad_privada` | **`0.5813`** | `0.4091` | `6` |
| **13** | [[Luis Hermosilla Osorio]] | `persona` | **`0.5813`** | `0.4091` | `6` |
| **14** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.5810`** | `0.4100` | `6` |
| **15** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.5807`** | `0.4110` | `5` |
| **16** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.5779`** | `0.4191` | `6` |
| **17** | [[Caso Audios]] | `causa_judicial` | **`0.5718`** | `0.4377` | `5` |
| **18** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.5717`** | `0.4380` | `5` |
| **19** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `nexo_transaccion` | **`0.5667`** | `0.4533` | `5` |
| **20** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | **`0.5654`** | `0.4572` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3841 Ω`** | `2.6038 S` | `271.9 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4058 Ω`** | `2.4645 S` | `287.3 pasos` |
| **3** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4152 Ω`** | `2.4085 S` | `294.0 pasos` |
| **4** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4308 Ω`** | `2.3213 S` | `305.0 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4322 Ω`** | `2.3137 S` | `306.0 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4475 Ω`** | `2.2346 S` | `316.8 pasos` |
| **7** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4544 Ω`** | `2.2009 S` | `321.7 pasos` |
| **8** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4655 Ω`** | `2.1482 S` | `329.6 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4655 Ω`** | `2.1482 S` | `329.6 pasos` |
| **10** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4710 Ω`** | `2.1233 S` | `333.4 pasos` |
| **11** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4710 Ω`** | `2.1233 S` | `333.4 pasos` |
| **12** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4711 Ω`** | `2.1226 S` | `333.6 pasos` |
| **13** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4731 Ω`** | `2.1137 S` | `335.0 pasos` |
| **14** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4803 Ω`** | `2.0822 S` | `340.0 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4808 Ω`** | `2.0799 S` | `340.4 pasos` |
| **16** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4820 Ω`** | `2.0746 S` | `341.3 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4977 Ω`** | `2.0091 S` | `352.4 pasos` |
| **18** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5043 Ω`** | `1.9830 S` | `357.0 pasos` |
| **19** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.5046 Ω`** | `1.9816 S` | `357.3 pasos` |
| **20** | [[Bancard Inversiones Ltda]] | [[Corte Suprema de Chile]] | **`0.5265 Ω`** | `1.8994 S` | `372.8 pasos` |
