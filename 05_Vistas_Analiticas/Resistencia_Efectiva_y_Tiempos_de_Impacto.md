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

# Resistencia Efectiva de Kirchhoff ($\Omega_{uv}$), Pseudoinversa $L^+$ y Tiempos de Impacto ($H_{uv}$)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.


> [!IMPORTANT] Redes Eléctricas de Kirchhoff y Cadenas de Markov sobre Grafos
> A diferencia de la distancia geodésica más corta (que ignora caminos alternativos), la **Distancia de Resistencia Efectiva de Klein & Randić ($\Omega_{uv} = L^+_{uu} + L^+_{vv} - 2L^+_{uv}$)** modela cada vínculo como un resistor de $1\,\Omega$ y pondera simultáneamente **todos los caminos paralelos** entre dos sujetos:
> 1. **Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$)**: Identifica los nodos con menor impedancia global hacia el resto del aparato criminal/institucional.
> 2. **Tiempo de Conmutación e Impacto de Tetali ($H_{uv} + H_{vu}$)** y **Constante de Kemeny ($K(G)$)**: Miden el número esperado de pasos de una auditoría o contagio estocástico para transitar entre dos actores cualesquiera.

## 1. Invariantes Eléctricos y Estocásticos del Grafo

- **Cobertura del Componente Gigante Conectado (LCC)**: **`209 / 229` nodos (`91.3%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`57130.29 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`2.6284 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`768.15 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.6531`** | `0.2159` | `10` |
| **2** | [[Union Democrata Independiente]] | `partido_politico` | **`0.6368`** | `0.2548` | `15` |
| **3** | [[Sebastian Pinera Echenique]] | `persona` | **`0.6276`** | `0.2778` | `7` |
| **4** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.6261`** | `0.2816` | `8` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.6088`** | `0.3268` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.6057`** | `0.3351` | `5` |
| **7** | [[Renovacion Nacional]] | `partido_politico` | **`0.6036`** | `0.3409` | `10` |
| **8** | [[Sergio Munoz Gajardo]] | `persona` | **`0.5998`** | `0.3513` | `5` |
| **9** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.5935`** | `0.3690` | `8` |
| **10** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `nexo_transaccion` | **`0.5924`** | `0.3721` | `5` |
| **11** | [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]] | `nexo_transaccion` | **`0.5841`** | `0.3959` | `5` |
| **12** | [[Factop SpA]] | `entidad_privada` | **`0.5795`** | `0.4094` | `6` |
| **13** | [[Luis Hermosilla Osorio]] | `persona` | **`0.5795`** | `0.4094` | `6` |
| **14** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.5792`** | `0.4103` | `6` |
| **15** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.5789`** | `0.4112` | `5` |
| **16** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.5760`** | `0.4200` | `6` |
| **17** | [[Caso Audios]] | `causa_judicial` | **`0.5700`** | `0.4379` | `5` |
| **18** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.5651`** | `0.4533` | `5` |
| **19** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `nexo_transaccion` | **`0.5650`** | `0.4535` | `5` |
| **20** | [[TRX-2023-06-22-Reunion-Audios-01]] | `nexo_transaccion` | **`0.5637`** | `0.4577` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3841 Ω`** | `2.6038 S` | `271.1 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4058 Ω`** | `2.4645 S` | `286.5 pasos` |
| **3** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4173 Ω`** | `2.3964 S` | `294.6 pasos` |
| **4** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4315 Ω`** | `2.3172 S` | `304.7 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4322 Ω`** | `2.3137 S` | `305.1 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4476 Ω`** | `2.2340 S` | `316.0 pasos` |
| **7** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4544 Ω`** | `2.2009 S` | `320.8 pasos` |
| **8** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4655 Ω`** | `2.1481 S` | `328.7 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4655 Ω`** | `2.1481 S` | `328.7 pasos` |
| **10** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4710 Ω`** | `2.1233 S` | `332.5 pasos` |
| **11** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4710 Ω`** | `2.1233 S` | `332.5 pasos` |
| **12** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4719 Ω`** | `2.1192 S` | `333.1 pasos` |
| **13** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4732 Ω`** | `2.1132 S` | `334.1 pasos` |
| **14** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4803 Ω`** | `2.0822 S` | `339.1 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4808 Ω`** | `2.0797 S` | `339.5 pasos` |
| **16** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4828 Ω`** | `2.0713 S` | `340.8 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4978 Ω`** | `2.0089 S` | `351.4 pasos` |
| **18** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5043 Ω`** | `1.9830 S` | `356.0 pasos` |
| **19** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.5047 Ω`** | `1.9815 S` | `356.3 pasos` |
| **20** | [[Bancard Inversiones Ltda]] | [[Corte Suprema de Chile]] | **`0.5265 Ω`** | `1.8992 S` | `371.7 pasos` |
