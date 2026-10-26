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
> 1. **Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$)**: Identifica los nodos con menor impedancia global hacia el resto del grafo.
> 2. **Tiempo de Conmutación e Impacto de Tetali ($H_{uv} + H_{vu}$)** y **Constante de Kemeny ($K(G)$)**: Miden el número esperado de pasos de una auditoría o contagio estocástico para transitar entre dos actores cualesquiera.

## 1. Invariantes Eléctricos y Estocásticos del Grafo

- **Cobertura del Componente Gigante Conectado (LCC)**: **`285 / 308` nodos (`92.5%`)**
- **Índice Total de Kirchhoff ($Kf(G) = N \operatorname{Tr}(L^+)$)**: **`141347.48 Ω`**
- **Resistencia Efectiva Promedio entre Pares ($\bar{\Omega}$)**: **`3.4926 Ω`**
- **Constante de Kemeny de la Cadena de Markov ($K(G)$)**: **`1233.97 pasos`**

---

## 2. Ranking de Centralidad por Flujo de Corriente ($C_{\text{CF}}(u)$ — Menor Impedancia Global)

| Pos | Nodo Operativo | Categoría | Cercanía de Corriente ($C_{\text{CF}}$) | Auto-Potencial $L^+_{uu}$ | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Union Democrata Independiente]] | `partido_politico` | **`0.5050`** | `0.2330` | `17` |
| **2** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.5032`** | `0.2402` | `10` |
| **3** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.4915`** | `0.2872` | `9` |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **`0.4907`** | `0.2904` | `7` |
| **5** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.4805`** | `0.3336` | `6` |
| **6** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `nexo_transaccion` | **`0.4768`** | `0.3497` | `5` |
| **7** | [[Sergio Munoz Gajardo]] | `persona` | **`0.4726`** | `0.3685` | `5` |
| **8** | [[Renovacion Nacional]] | `partido_politico` | **`0.4718`** | `0.3721` | `10` |
| **9** | [[Augusto Pinochet Ugarte]] | `persona` | **`0.4712`** | `0.3746` | `8` |
| **10** | [[TRX-2003-11-05-Arista-Politica-Spiniak-01]] | `nexo_transaccion` | **`0.4660`** | `0.3980` | `5` |
| **11** | [[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]] | `nexo_transaccion` | **`0.4651`** | `0.4025` | `5` |
| **12** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.4633`** | `0.4107` | `6` |
| **13** | [[Luis Hermosilla Osorio]] | `persona` | **`0.4624`** | `0.4149` | `6` |
| **14** | [[Factop SpA]] | `entidad_privada` | **`0.4624`** | `0.4149` | `6` |
| **15** | [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] | `nexo_transaccion` | **`0.4615`** | `0.4192` | `5` |
| **16** | [[Lucia Hiriart Rodriguez]] | `persona` | **`0.4613`** | `0.4199` | `6` |
| **17** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `nexo_transaccion` | **`0.4573`** | `0.4391` | `5` |
| **18** | [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]] | `nexo_transaccion` | **`0.4569`** | `0.4409` | `5` |
| **19** | [[Caso Audios]] | `causa_judicial` | **`0.4563`** | `0.4435` | `5` |
| **20** | [[TRX-2023-08-25-Reporte-ROS-Factop-UAF-01]] | `nexo_transaccion` | **`0.4563`** | `0.4438` | `5` |

---

## 3. Pares de Actores No Adyacentes con Menor Resistencia Efectiva (Conductos Multi-Ruta)

Pares de actores sin arista directa cuya **Resistencia Efectiva ($\Omega_{uv}$)** es mínima debido a la existencia de múltiples caminos paralelos cortos:

| # | Actor A ($u$) | Actor B ($v$) | Resistencia Efectiva ($\Omega_{uv}$) | Conductancia ($\Omega_{uv}^{-1}$) | Tiempo Conmutación ($H_{uv}+H_{vu}$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Carlos Contreras Gutierrez]] | [[Seremi MINVU Antofagasta]] | **`0.3841 Ω`** | `2.6038 S` | `340.3 pasos` |
| **2** | [[Carlos Contreras Gutierrez]] | [[Daniel Andrade Schwarze]] | **`0.4058 Ω`** | `2.4645 S` | `359.5 pasos` |
| **3** | [[Empresas Penta SA]] | [[Union Democrata Independiente]] | **`0.4173 Ω`** | `2.3965 S` | `369.7 pasos` |
| **4** | [[Corte Suprema de Chile]] | [[Servicio Impuestos Internos]] | **`0.4315 Ω`** | `2.3173 S` | `382.3 pasos` |
| **5** | [[Corte Suprema de Chile]] | [[Sergio Munoz Gajardo]] | **`0.4321 Ω`** | `2.3143 S` | `382.8 pasos` |
| **6** | [[Sebastian Pinera Echenique]] | [[Union Democrata Independiente]] | **`0.4474 Ω`** | `2.2350 S` | `396.4 pasos` |
| **7** | [[Augusto Pinochet Ugarte]] | [[Comando de Apoyo a la Fuerza del Ejercito]] | **`0.4526 Ω`** | `2.2094 S` | `401.0 pasos` |
| **8** | [[Corte Suprema de Chile]] | [[Luis Hermosilla Osorio]] | **`0.4644 Ω`** | `2.1532 S` | `411.5 pasos` |
| **9** | [[Corte Suprema de Chile]] | [[Factop SpA]] | **`0.4644 Ω`** | `2.1532 S` | `411.5 pasos` |
| **10** | [[Servicio Impuestos Internos]] | [[Union Democrata Independiente]] | **`0.4690 Ω`** | `2.1320 S` | `415.6 pasos` |
| **11** | [[Carlos Contreras Gutierrez]] | [[Fundacion Democracia Viva]] | **`0.4710 Ω`** | `2.1233 S` | `417.3 pasos` |
| **12** | [[Daniel Andrade Schwarze]] | [[Seremi MINVU Antofagasta]] | **`0.4710 Ω`** | `2.1233 S` | `417.3 pasos` |
| **13** | [[Corte Suprema de Chile]] | [[Sebastian Pinera Echenique]] | **`0.4714 Ω`** | `2.1215 S` | `417.6 pasos` |
| **14** | [[Corte Suprema de Chile]] | [[Union Democrata Independiente]] | **`0.4771 Ω`** | `2.0962 S` | `422.7 pasos` |
| **15** | [[Augusto Pinochet Ugarte]] | [[Corte Suprema de Chile]] | **`0.4802 Ω`** | `2.0826 S` | `425.4 pasos` |
| **16** | [[Sergio Munoz Gajardo]] | [[Servicio Impuestos Internos]] | **`0.4827 Ω`** | `2.0716 S` | `427.7 pasos` |
| **17** | [[Bancard Inversiones Ltda]] | [[Union Democrata Independiente]] | **`0.4978 Ω`** | `2.0089 S` | `441.0 pasos` |
| **18** | [[Corte Suprema de Chile]] | [[Lucia Hiriart Rodriguez]] | **`0.5042 Ω`** | `1.9832 S` | `446.7 pasos` |
| **19** | [[Fundacion Democracia Viva]] | [[Seremi MINVU Antofagasta]] | **`0.5043 Ω`** | `1.9830 S` | `446.8 pasos` |
| **20** | [[Bancard Inversiones Ltda]] | [[Corte Suprema de Chile]] | **`0.5232 Ω`** | `1.9113 S` | `463.6 pasos` |
