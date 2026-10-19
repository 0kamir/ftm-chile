---
tipo_nodo: vista_analitica
titulo: "Análisis Espectral Laplaciano, Valor de Fiedler y Centralidad de Perron-Frobenius"
actualizacion_automatica: true
tags:
  - teoria-espectral
  - fiedler-laplaciano
  - perron-frobenius
  - analisis-forense
---

# 🌈 Teoría Espectral de Grafos: Conectividad de Fiedler ($\lambda_2$) y Bisección Laplaciana

> [!IMPORTANT] Álgebra Lineal Espectral sobre el Componente Gigante Conectado (LCC)
> Esta vista diagonaliza de forma exacta (rotaciones simétricas de Jacobi) la **Matriz Laplaciana Combinatoria ($L = D - A$)** y la **Matriz de Adyacencia ($A$)** sobre el Componente Gigante Conectado de la red operativa:
> 1. **Conectividad Algebraica de Fiedler ($\lambda_2$)**: Mide la robustez estructural frente a la escisión de la red (Desigualdad de Cheeger: $\frac{\lambda_2}{2} \le h(G) \le \sqrt{2 d_{\max} \lambda_2}$).
> 2. **Bisección Espectral por Vector de Fiedler ($v_2$)**: Divide el LCC en dos hemisferios polares ($v_2(i) \ge 0$ vs. $v_2(i) < 0$) y localiza la **Línea de Falla Espectral ($v_2(i) \approx 0$)** donde convergen los aparatos partidarios/tributarios y los aparatos regionales/municipales.
> 3. **Autovector Principal de Perron-Frobenius ($\rho(A)$)**: Cuantifica la influencia recursiva y el umbral de contagio institucional ($\tau_c = 1/\rho(A)$).

## 1. Invariantes Espectrales del Componente Gigante (LCC)

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `216` nodos operativos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.020759`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1167` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `776.37`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0104, 0.7892]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`4.9816`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.2007`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `191` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `25` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `8` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`-0.00097`** | `0.1142` | `6` |
| **2** | [[Sebastian Pinera Echenique]] | `persona` | **`+0.00127`** | `0.1407` | `7` |
| **3** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `nexo_transaccion` | **`+0.00385`** | `0.0644` | `5` |
| **4** | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | `nexo_transaccion` | **`+0.00561`** | `0.0663` | `5` |
| **5** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`+0.00594`** | `0.1257` | `5` |
| **6** | [[Caso Minera Dominga Pandora Papers]] | `causa_judicial` | **`+0.00607`** | `0.0252` | `1` |
| **7** | [[Santiago Valdes Gutierrez]] | `persona` | **`-0.00681`** | `0.0421` | `3` |
| **8** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] | `causa_judicial` | **`+0.00773`** | `0.0346` | `2` |
| **9** | [[Caso SQM]] | `causa_judicial` | **`+0.00794`** | `0.0456` | `2` |
| **10** | [[Renovacion Nacional]] | `partido_politico` | **`+0.00798`** | `0.0797` | `10` |
| **11** | [[Percy Marin Vera]] | `persona` | **`+0.00815`** | `0.0160` | `1` |
| **12** | [[Comision para el Mercado Financiero]] | `entidad_publica` | **`+0.00856`** | `0.0179` | `2` |
| **13** | [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]] | `nexo_transaccion` | **`+0.00872`** | `0.0186` | `4` |
| **14** | [[Patricio Contesse Gonzalez]] | `persona` | **`+0.00873`** | `0.0579` | `3` |
| **15** | [[Fernando Cerimedo]] | `persona` | **`+0.00890`** | `0.0047` | `2` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Renovacion Nacional]] | `+0.00798` | [[Santiago Valdes Gutierrez]] | `-0.00681` |
| **2** | [[Sebastian Pinera Echenique]] | `+0.00127` | [[Bancard Inversiones Ltda]] | `-0.00097` |
| **3** | [[Sebastian Pinera Echenique]] | `+0.00127` | [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | `-0.03213` |
| **4** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.00968` | [[Bancard Inversiones Ltda]] | `-0.00097` |
| **5** | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | `+0.00561` | [[Bancard Inversiones Ltda]] | `-0.00097` |
| **6** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `+0.00385` | [[Bancard Inversiones Ltda]] | `-0.00097` |
| **7** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `+0.00385` | [[Santiago Valdes Gutierrez]] | `-0.00681` |
| **8** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `+0.00594` | [[Bancard Inversiones Ltda]] | `-0.00097` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Union Democrata Independiente]] | `partido_politico` | **`0.4701`** | `+0.01711` | `15` |
| **2** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.2671`** | `+0.01343` | `6` |
| **3** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `nexo_transaccion` | **`0.2433`** | `+0.01565` | `5` |
| **4** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `nexo_transaccion` | **`0.2364`** | `+0.01600` | `5` |
| **5** | [[Empresas Penta SA]] | `entidad_privada` | **`0.1762`** | `+0.01581` | `4` |
| **6** | [[Pablo Longueira Montes]] | `persona` | **`0.1759`** | `+0.01497` | `3` |
| **7** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.1727`** | `+0.02273` | `13` |
| **8** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `nexo_transaccion` | **`0.1627`** | `+0.01186` | `5` |
| **9** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `nexo_transaccion` | **`0.1488`** | `+0.01985` | `5` |
| **10** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `persona` | **`0.1467`** | `+0.01738` | `3` |
| **11** | [[Andres Chadwick Pinera]] | `persona` | **`0.1436`** | `+0.01272` | `3` |
| **12** | [[Jovino Novoa Vasquez]] | `persona` | **`0.1418`** | `+0.01673` | `2` |
| **13** | [[Sebastian Pinera Echenique]] | `persona` | **`0.1407`** | `+0.00127` | `7` |
| **14** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.1309`** | `+0.01783` | `5` |
| **15** | [[Cathy Barriga Guerra]] | `persona` | **`0.1295`** | `+0.01684` | `3` |
| **16** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`0.1257`** | `+0.00594` | `5` |
| **17** | [[Factop SpA]] | `entidad_privada` | **`0.1247`** | `+0.02219` | `6` |
| **18** | [[Luis Hermosilla Osorio]] | `persona` | **`0.1247`** | `+0.02219` | `6` |
| **19** | [[Hernan Larrain Fernandez]] | `persona` | **`0.1242`** | `+0.01867` | `2` |
| **20** | [[Caso Penta]] | `causa_judicial` | **`0.1226`** | `+0.01661` | `3` |
