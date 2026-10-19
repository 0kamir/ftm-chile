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

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `209` nodos operativos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.020839`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1167` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `773.38`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0104, 0.7907]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`4.9684`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.2013`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `184` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `25` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `8` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`-0.00021`** | `0.1078` | `6` |
| **2** | [[Sebastian Pinera Echenique]] | `persona` | **`+0.00204`** | `0.1332` | `7` |
| **3** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `nexo_transaccion` | **`+0.00470`** | `0.0645` | `5` |
| **4** | [[Santiago Valdes Gutierrez]] | `persona` | **`-0.00599`** | `0.0395` | `3` |
| **5** | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | `nexo_transaccion` | **`+0.00637`** | `0.0622` | `5` |
| **6** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`+0.00679`** | `0.1279` | `5` |
| **7** | [[Caso Minera Dominga Pandora Papers]] | `causa_judicial` | **`+0.00693`** | `0.0257` | `1` |
| **8** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] | `causa_judicial` | **`+0.00841`** | `0.0298` | `2` |
| **9** | [[Caso SQM]] | `causa_judicial` | **`+0.00882`** | `0.0480` | `2` |
| **10** | [[Renovacion Nacional]] | `partido_politico` | **`+0.00884`** | `0.0699` | `10` |
| **11** | [[Percy Marin Vera]] | `persona` | **`+0.00903`** | `0.0141` | `1` |
| **12** | [[Comision para el Mercado Financiero]] | `entidad_publica` | **`+0.00934`** | `0.0168` | `2` |
| **13** | [[Patricio Contesse Gonzalez]] | `persona` | **`+0.00961`** | `0.0609` | `3` |
| **14** | [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]] | `nexo_transaccion` | **`+0.00966`** | `0.0164` | `4` |
| **15** | [[Fernando Cerimedo]] | `persona` | **`+0.00986`** | `0.0041` | `2` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Renovacion Nacional]] | `+0.00884` | [[Santiago Valdes Gutierrez]] | `-0.00599` |
| **2** | [[Sebastian Pinera Echenique]] | `+0.00204` | [[Bancard Inversiones Ltda]] | `-0.00021` |
| **3** | [[Sebastian Pinera Echenique]] | `+0.00204` | [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | `-0.03139` |
| **4** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.01028` | [[Bancard Inversiones Ltda]] | `-0.00021` |
| **5** | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | `+0.00637` | [[Bancard Inversiones Ltda]] | `-0.00021` |
| **6** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `+0.00470` | [[Bancard Inversiones Ltda]] | `-0.00021` |
| **7** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `+0.00470` | [[Santiago Valdes Gutierrez]] | `-0.00599` |
| **8** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `+0.00679` | [[Bancard Inversiones Ltda]] | `-0.00021` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Union Democrata Independiente]] | `partido_politico` | **`0.5030`** | `+0.01805` | `15` |
| **2** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.2854`** | `+0.01435` | `6` |
| **3** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `nexo_transaccion` | **`0.2612`** | `+0.01659` | `5` |
| **4** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `nexo_transaccion` | **`0.2538`** | `+0.01695` | `5` |
| **5** | [[Empresas Penta SA]] | `entidad_privada` | **`0.1889`** | `+0.01674` | `4` |
| **6** | [[Pablo Longueira Montes]] | `persona` | **`0.1889`** | `+0.01591` | `3` |
| **7** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `nexo_transaccion` | **`0.1741`** | `+0.01276` | `5` |
| **8** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `persona` | **`0.1570`** | `+0.01833` | `3` |
| **9** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `nexo_transaccion` | **`0.1567`** | `+0.02066` | `5` |
| **10** | [[Jovino Novoa Vasquez]] | `persona` | **`0.1523`** | `+0.01768` | `2` |
| **11** | [[Andres Chadwick Pinera]] | `persona` | **`0.1461`** | `+0.01353` | `3` |
| **12** | [[Cathy Barriga Guerra]] | `persona` | **`0.1390`** | `+0.01782` | `3` |
| **13** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.1381`** | `+0.01874` | `5` |
| **14** | [[Sebastian Pinera Echenique]] | `persona` | **`0.1332`** | `+0.00204` | `7` |
| **15** | [[Hernan Larrain Fernandez]] | `persona` | **`0.1328`** | `+0.01956` | `2` |
| **16** | [[Caso Penta]] | `causa_judicial` | **`0.1314`** | `+0.01755` | `3` |
| **17** | [[Pablo Wagner San Martin]] | `persona` | **`0.1290`** | `+0.01859` | `2` |
| **18** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`0.1279`** | `+0.00679` | `5` |
| **19** | [[Gabriel Ruiz-Tagle Serrano]] | `persona` | **`0.1142`** | `+0.03007` | `3` |
| **20** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.1078`** | `-0.00021` | `6` |
