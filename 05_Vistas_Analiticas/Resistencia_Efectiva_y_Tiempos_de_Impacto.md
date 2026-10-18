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

- **Cobertura del Componente Gigante Conectado (LCC)**: **`245 / 252` nodos operativos (`97.2%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`71536.32 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`2.3933 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`800.76 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.7201`** | `0.1912` | `13` |
| **2** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.7183`** | `0.1948` | `10` |
| **3** | [[Union Democrata Independiente]] | `partido_politico` | **`0.6909`** | `0.2497` | `15` |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **`0.6762`** | `0.2811` | `7` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.6545`** | `0.3299` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.6540`** | `0.3311` | `5` |
| **7** | [[Sergio Munoz Gajardo]] | `persona` | **`0.6536`** | `0.3321` | `5` |
| **8** | [[Renovacion Nacional]] | `partido_politico` | **`0.6506`** | `0.3390` | `10` |
| **9** | [[Factop SpA]] | `entidad_privada` | **`0.6496`** | `0.3413` | `7` |
| **10** | [[Luis Hermosilla Osorio]] | `persona` | **`0.6496`** | `0.3413` | `7` |
| **11** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.6486`** | `0.3437` | `8` |
| **12** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | **`0.6455`** | `0.3511` | `5` |
| **13** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | **`0.6415`** | `0.3608` | `5` |
| **14** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`0.6412`** | `0.3615` | `5` |
| **15** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.6367`** | `0.3723` | `5` |
| **16** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.6324`** | `0.3831` | `6` |
| **17** | [[Caso Audios]] | `causa_judicial` | **`0.6318`** | `0.3845` | `5` |
| **18** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `nexo_transaccion` | **`0.6205`** | `0.4133` | `5` |
| **19** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `nexo_transaccion` | **`0.6205`** | `0.4133` | `5` |
| **20** | [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | `nexo_transaccion` | **`0.6197`** | `0.4153` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3840 Ω`** | `2.6038 S` | `322.6 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4047 Ω`** | `2.4707 S` | `340.0 pasos` |
| **3** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4109 Ω`** | `2.4336 S` | `345.2 pasos` |
| **4** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4150 Ω`** | `2.4094 S` | `348.6 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4308 Ω`** | `2.3214 S` | `361.8 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4394 Ω`** | `2.2760 S` | `369.1 pasos` |
| **7** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4477 Ω`** | `2.2339 S` | `376.0 pasos` |
| **8** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4477 Ω`** | `2.2338 S` | `376.0 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4477 Ω`** | `2.2338 S` | `376.0 pasos` |
| **10** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4533 Ω`** | `2.2061 S` | `380.8 pasos` |
| **11** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4585 Ω`** | `2.1812 S` | `385.1 pasos` |
| **12** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4668 Ω`** | `2.1422 S` | `392.1 pasos` |
| **13** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4697 Ω`** | `2.1289 S` | `394.6 pasos` |
| **14** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4697 Ω`** | `2.1289 S` | `394.6 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4740 Ω`** | `2.1098 S` | `398.1 pasos` |
| **16** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4744 Ω`** | `2.1080 S` | `398.5 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4880 Ω`** | `2.0492 S` | `409.9 pasos` |
| **18** | [[Sebastian Pinera Echenique]] | [[Servicio Impuestos Internos]] | **`0.4933 Ω`** | `2.0270 S` | `414.4 pasos` |
| **19** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.4971 Ω`** | `2.0118 S` | `417.5 pasos` |
| **20** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5028 Ω`** | `1.9888 S` | `422.4 pasos` |
