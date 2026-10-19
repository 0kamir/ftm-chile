---
tipo_nodo: vista_analitica
titulo: "Análisis Espectral Laplaciano, Valor de Fiedler y Centralidad de Perron-Frobenius"
actualizacion_automatica: true
tags:
  - teoria-espectral
  - fiedler-laplaciano
  - perron-frobenius
  - analisis-de-redes
---

# Teoría Espectral de Grafos: Conectividad de Fiedler ($\lambda_2$) y Bisección Laplaciana

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.


> [!IMPORTANT] Álgebra Lineal Espectral sobre el Componente Gigante Conectado (LCC)
> Esta vista diagonaliza de forma exacta (rotaciones simétricas de Jacobi) la **Matriz Laplaciana Combinatoria ($L = D - A$)** y la **Matriz de Adyacencia ($A$)** sobre el Componente Gigante Conectado de la red:
> 1. **Conectividad Algebraica de Fiedler ($\lambda_2$)**: Mide la robustez estructural frente a la escisión de la red (Desigualdad de Cheeger: $\frac{\lambda_2}{2} \le h(G) \le \sqrt{2 d_{\max} \lambda_2}$).
> 2. **Bisección Espectral por Vector de Fiedler ($v_2$)**: Divide el LCC en dos hemisferios polares ($v_2(i) \ge 0$ vs. $v_2(i) < 0$) y localiza la **Línea de Falla Espectral ($v_2(i) \approx 0$)** donde convergen los aparatos partidarios/tributarios y los aparatos regionales/municipales.
> 3. **Autovector Principal de Perron-Frobenius ($\rho(A)$)**: Cuantifica la influencia recursiva y el umbral de contagio institucional ($\tau_c = 1/\rho(A)$).

## 1. Invariantes Espectrales del Componente Gigante (LCC)

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `209` nodos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.020839`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1167` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `773.40`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0104, 0.7907]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`4.9347`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.2026`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `184` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `25` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `8` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`-0.00020`** | `0.1166` | `6` |
| **2** | [[Sebastian Pinera Echenique]] | `persona` | **`+0.00203`** | `0.1431` | `7` |
| **3** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `nexo_transaccion` | **`+0.00470`** | `0.0680` | `5` |
| **4** | [[Santiago Valdes Gutierrez]] | `persona` | **`-0.00601`** | `0.0432` | `3` |
| **5** | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | `nexo_transaccion` | **`+0.00637`** | `0.0679` | `5` |
| **6** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`+0.00680`** | `0.1325` | `5` |
| **7** | [[Caso Minera Dominga Pandora Papers]] | `causa_judicial` | **`+0.00694`** | `0.0269` | `1` |
| **8** | [[Caso LAN Informacion Privilegiada y Banco de Talca]] | `causa_judicial` | **`+0.00842`** | `0.0332` | `2` |
| **9** | [[Renovacion Nacional]] | `partido_politico` | **`+0.00879`** | `0.0779` | `10` |
| **10** | [[Caso SQM]] | `causa_judicial` | **`+0.00883`** | `0.0485` | `2` |
| **11** | [[Percy Marin Vera]] | `persona` | **`+0.00898`** | `0.0158` | `1` |
| **12** | [[Comision para el Mercado Financiero]] | `entidad_publica` | **`+0.00935`** | `0.0185` | `2` |
| **13** | [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]] | `nexo_transaccion` | **`+0.00961`** | `0.0184` | `4` |
| **14** | [[Patricio Contesse Gonzalez]] | `persona` | **`+0.00961`** | `0.0618` | `3` |
| **15** | [[Fernando Cerimedo]] | `persona` | **`+0.00981`** | `0.0047` | `2` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Renovacion Nacional]] | `+0.00879` | [[Santiago Valdes Gutierrez]] | `-0.00601` |
| **2** | [[Sebastian Pinera Echenique]] | `+0.00203` | [[Bancard Inversiones Ltda]] | `-0.00020` |
| **3** | [[Sebastian Pinera Echenique]] | `+0.00203` | [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]] | `-0.03140` |
| **4** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.01028` | [[Bancard Inversiones Ltda]] | `-0.00020` |
| **5** | [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]] | `+0.00637` | [[Bancard Inversiones Ltda]] | `-0.00020` |
| **6** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `+0.00470` | [[Bancard Inversiones Ltda]] | `-0.00020` |
| **7** | [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]] | `+0.00470` | [[Santiago Valdes Gutierrez]] | `-0.00601` |
| **8** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `+0.00680` | [[Bancard Inversiones Ltda]] | `-0.00020` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Union Democrata Independiente]] | `partido_politico` | **`0.4859`** | `+0.01806` | `15` |
| **2** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.2832`** | `+0.01437` | `6` |
| **3** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `nexo_transaccion` | **`0.2576`** | `+0.01662` | `5` |
| **4** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `nexo_transaccion` | **`0.2503`** | `+0.01697` | `5` |
| **5** | [[Empresas Penta SA]] | `entidad_privada` | **`0.1871`** | `+0.01679` | `4` |
| **6** | [[Pablo Longueira Montes]] | `persona` | **`0.1854`** | `+0.01593` | `3` |
| **7** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `nexo_transaccion` | **`0.1716`** | `+0.01277` | `5` |
| **8** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `nexo_transaccion` | **`0.1544`** | `+0.02067` | `5` |
| **9** | [[Jovino Novoa Vasquez]] | `persona` | **`0.1492`** | `+0.01770` | `2` |
| **10** | [[Andres Chadwick Pinera]] | `persona` | **`0.1478`** | `+0.01354` | `3` |
| **11** | [[Sebastian Pinera Echenique]] | `persona` | **`0.1431`** | `+0.00203` | `7` |
| **12** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`0.1325`** | `+0.00680` | `5` |
| **13** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.1321`** | `+0.01884` | `5` |
| **14** | [[Hernan Larrain Fernandez]] | `persona` | **`0.1298`** | `+0.01957` | `2` |
| **15** | [[Caso Penta]] | `causa_judicial` | **`0.1297`** | `+0.01760` | `3` |
| **16** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `persona` | **`0.1252`** | `+0.01865` | `2` |
| **17** | [[Pablo Wagner San Martin]] | `persona` | **`0.1252`** | `+0.01865` | `2` |
| **18** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.1224`** | `+0.02286` | `10` |
| **19** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **`0.1166`** | `-0.00020` | `6` |
| **20** | [[Factop SpA]] | `entidad_privada` | **`0.1142`** | `+0.02281` | `6` |
