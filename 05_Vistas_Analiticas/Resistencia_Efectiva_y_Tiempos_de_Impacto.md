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

- **Cobertura del Componente Gigante Conectado (LCC)**: **`233 / 246` nodos operativos (`94.7%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`62232.90 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`2.3025 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`745.14 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.7456`** | `0.1891` | `13` |
| **2** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.7423`** | `0.1950` | `10` |
| **3** | [[Union Democrata Independiente]] | `partido_politico` | **`0.7159`** | `0.2445` | `15` |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **`0.6989`** | `0.2784` | `7` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.6758`** | `0.3270` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.6753`** | `0.3282` | `5` |
| **7** | [[Sergio Munoz Gajardo]] | `persona` | **`0.6750`** | `0.3288` | `5` |
| **8** | [[Renovacion Nacional]] | `partido_politico` | **`0.6728`** | `0.3335` | `10` |
| **9** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.6701`** | `0.3396` | `8` |
| **10** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | **`0.6624`** | `0.3568` | `5` |
| **11** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`0.6616`** | `0.3586` | `5` |
| **12** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | **`0.6607`** | `0.3608` | `5` |
| **13** | [[Factop SpA]] | `entidad_privada` | **`0.6593`** | `0.3640` | `6` |
| **14** | [[Luis Hermosilla Osorio]] | `persona` | **`0.6593`** | `0.3640` | `6` |
| **15** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.6527`** | `0.3792` | `6` |
| **16** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.6526`** | `0.3793` | `5` |
| **17** | [[Caso Audios]] | `causa_judicial` | **`0.6470`** | `0.3926` | `5` |
| **18** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.6390`** | `0.4118` | `6` |
| **19** | [[TRX-2011-03-10-Soborno-Penta-Wagner-01]] | `nexo_transaccion` | **`0.6388`** | `0.4125` | `5` |
| **20** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `nexo_transaccion` | **`0.6351`** | `0.4215` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3840 Ω`** | `2.6038 S` | `309.5 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4047 Ω`** | `2.4707 S` | `326.2 pasos` |
| **3** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4109 Ω`** | `2.4336 S` | `331.2 pasos` |
| **4** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4150 Ω`** | `2.4094 S` | `334.5 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4308 Ω`** | `2.3214 S` | `347.2 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4394 Ω`** | `2.2760 S` | `354.1 pasos` |
| **7** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4477 Ω`** | `2.2339 S` | `360.8 pasos` |
| **8** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4533 Ω`** | `2.2061 S` | `365.4 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4566 Ω`** | `2.1901 S` | `368.0 pasos` |
| **10** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4566 Ω`** | `2.1901 S` | `368.0 pasos` |
| **11** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4585 Ω`** | `2.1812 S` | `369.5 pasos` |
| **12** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4668 Ω`** | `2.1422 S` | `376.2 pasos` |
| **13** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4697 Ω`** | `2.1289 S` | `378.6 pasos` |
| **14** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4697 Ω`** | `2.1289 S` | `378.6 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4740 Ω`** | `2.1098 S` | `382.0 pasos` |
| **16** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4744 Ω`** | `2.1080 S` | `382.3 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4880 Ω`** | `2.0492 S` | `393.3 pasos` |
| **18** | [[Sebastian Pinera Echenique]] | [[Servicio Impuestos Internos]] | **`0.4933 Ω`** | `2.0270 S` | `397.6 pasos` |
| **19** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.4971 Ω`** | `2.0118 S` | `400.6 pasos` |
| **20** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5028 Ω`** | `1.9888 S` | `405.3 pasos` |
