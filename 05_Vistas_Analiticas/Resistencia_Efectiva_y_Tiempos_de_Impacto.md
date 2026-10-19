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

- **Cobertura del Componente Gigante Conectado (LCC)**: **`226 / 239` nodos operativos (`94.6%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`58423.37 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`2.2979 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`705.44 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.7480`** | `0.1871` | `13` |
| **2** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.7387`** | `0.2039` | `10` |
| **3** | [[Union Democrata Independiente]] | `partido_politico` | **`0.7177`** | `0.2433` | `15` |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **`0.7003`** | `0.2778` | `7` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.6773`** | `0.3261` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.6767`** | `0.3273` | `5` |
| **7** | [[Sergio Munoz Gajardo]] | `persona` | **`0.6757`** | `0.3296` | `5` |
| **8** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.6717`** | `0.3383` | `8` |
| **9** | [[Renovacion Nacional]] | `partido_politico` | **`0.6708`** | `0.3404` | `10` |
| **10** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | **`0.6629`** | `0.3580` | `5` |
| **11** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`0.6618`** | `0.3604` | `5` |
| **12** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | **`0.6606`** | `0.3631` | `5` |
| **13** | [[Factop SpA]] | `entidad_privada` | **`0.6600`** | `0.3646` | `6` |
| **14** | [[Luis Hermosilla Osorio]] | `persona` | **`0.6600`** | `0.3646` | `6` |
| **15** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.6540`** | `0.3784` | `6` |
| **16** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.6523`** | `0.3825` | `5` |
| **17** | [[Caso Audios]] | `causa_judicial` | **`0.6477`** | `0.3931` | `5` |
| **18** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.6404`** | `0.4107` | `6` |
| **19** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.6391`** | `0.4140` | `5` |
| **20** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `nexo_transaccion` | **`0.6362`** | `0.4210` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3840 Ω`** | `2.6038 S` | `298.0 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4047 Ω`** | `2.4707 S` | `314.1 pasos` |
| **3** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4109 Ω`** | `2.4335 S` | `318.9 pasos` |
| **4** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4151 Ω`** | `2.4092 S` | `322.1 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4310 Ω`** | `2.3204 S` | `334.4 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4404 Ω`** | `2.2708 S` | `341.7 pasos` |
| **7** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4477 Ω`** | `2.2335 S` | `347.4 pasos` |
| **8** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4533 Ω`** | `2.2060 S` | `351.8 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4576 Ω`** | `2.1855 S` | `355.1 pasos` |
| **10** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4576 Ω`** | `2.1855 S` | `355.1 pasos` |
| **11** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4588 Ω`** | `2.1794 S` | `356.1 pasos` |
| **12** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4671 Ω`** | `2.1410 S` | `362.5 pasos` |
| **13** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4697 Ω`** | `2.1289 S` | `364.5 pasos` |
| **14** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4697 Ω`** | `2.1289 S` | `364.5 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4740 Ω`** | `2.1098 S` | `367.8 pasos` |
| **16** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4745 Ω`** | `2.1074 S` | `368.2 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4887 Ω`** | `2.0461 S` | `379.3 pasos` |
| **18** | [[Sebastian Pinera Echenique]] | [[Servicio Impuestos Internos]] | **`0.4938 Ω`** | `2.0249 S` | `383.2 pasos` |
| **19** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.4971 Ω`** | `2.0118 S` | `385.7 pasos` |
| **20** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5028 Ω`** | `1.9888 S` | `390.2 pasos` |
