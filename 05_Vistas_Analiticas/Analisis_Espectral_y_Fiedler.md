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

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `285` nodos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.019471`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `18.0996` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `929.56`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0097, 0.8136]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`5.0557`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.1978`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `218` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `67` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `15` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Patricio Contesse Gonzalez]] | `persona` | **`+0.00017`** | `0.0619` | `3` |
| **2** | [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]] | `nexo_transaccion` | **`+0.00018`** | `0.0070` | `3` |
| **3** | [[Caso Asignaciones Parlamentarias y Cuota Flores]] | `causa_judicial` | **`+0.00019`** | `0.0014` | `1` |
| **4** | [[Caso SQM]] | `causa_judicial` | **`+0.00054`** | `0.0535` | `3` |
| **5** | [[SQM SA]] | `entidad_privada` | **`+0.00058`** | `0.0694` | `5` |
| **6** | [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | `nexo_transaccion` | **`+0.00060`** | `0.0222` | `5` |
| **7** | [[Caso Spiniak]] | `causa_judicial` | **`-0.00063`** | `0.0132` | `2` |
| **8** | [[Sergio Munoz Gajardo]] | `persona` | **`-0.00076`** | `0.0390` | `5` |
| **9** | [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]] | `nexo_transaccion` | **`+0.00088`** | `0.0267` | `5` |
| **10** | [[Claudio Spiniak Vilensky]] | `persona` | **`+0.00090`** | `0.0066` | `2` |
| **11** | [[Inversiones El Bosque Ltda]] | `entidad_privada` | **`+0.00090`** | `0.0066` | `2` |
| **12** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `nexo_transaccion` | **`+0.00098`** | `0.0311` | `5` |
| **13** | [[Gonzalo Delaveau Swett]] | `persona` | **`+0.00098`** | `0.0064` | `2` |
| **14** | [[Caso CEMA Chile]] | `causa_judicial` | **`+0.00100`** | `0.0062` | `1` |
| **15** | [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] | `nexo_transaccion` | **`+0.00112`** | `0.0187` | `4` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Andes Iron SpA]] | `+0.00239` | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `-0.00269` |
| **2** | [[Andres Chadwick Pinera]] | `+0.00256` | [[Sebastian Pinera Echenique]] | `-0.00949` |
| **3** | [[Carlos Alberto Delano Abbott]] | `+0.00743` | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `-0.00269` |
| **4** | [[Caso SQM]] | `+0.00054` | [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]] | `-0.00513` |
| **5** | [[Corte Suprema de Chile]] | `+0.00188` | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `-0.00521` |
| **6** | [[Corte Suprema de Chile]] | `+0.00188` | [[TRX-2003-11-05-Arista-Politica-Spiniak-01]] | `-0.00213` |
| **7** | [[Municipalidad de Maipu]] | `+0.00199` | [[TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01]] | `-0.00230` |
| **8** | [[Patricio Contesse Gonzalez]] | `+0.00017` | [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]] | `-0.00513` |
| **9** | [[SQM SA]] | `+0.00058` | [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]] | `-0.00513` |
| **10** | [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]] | `+0.00088` | [[Caso Spiniak]] | `-0.00063` |
| **11** | [[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]] | `+0.00088` | [[Sergio Munoz Gajardo]] | `-0.00076` |
| **12** | [[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]] | `+0.00169` | [[Sergio Munoz Gajardo]] | `-0.00076` |
| **13** | [[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]] | `+0.00060` | [[Carlos Pavez Tolosa]] | `-0.00479` |
| **14** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `+0.00098` | [[Sergio Munoz Gajardo]] | `-0.00076` |
| **15** | [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]] | `+0.00018` | [[Camila Flores Oporto]] | `-0.00327` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Union Democrata Independiente]] | `partido_politico` | **`0.5398`** | `+0.01405` | `17` |
| **2** | [[Carlos Alberto Delano Abbott]] | `persona` | **`0.2851`** | `+0.00743` | `6` |
| **3** | [[TRX-2013-07-15-Boletas-Penta-UDI-01]] | `nexo_transaccion` | **`0.2635`** | `+0.01028` | `5` |
| **4** | [[TRX-2013-09-20-Boletas-Penta-Novoa-01]] | `nexo_transaccion` | **`0.2561`** | `+0.01082` | `5` |
| **5** | [[Pablo Longueira Montes]] | `persona` | **`0.1949`** | `+0.00986` | `3` |
| **6** | [[Empresas Penta SA]] | `entidad_privada` | **`0.1845`** | `+0.00958` | `4` |
| **7** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `nexo_transaccion` | **`0.1819`** | `+0.00506` | `5` |
| **8** | [[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]] | `nexo_transaccion` | **`0.1611`** | `+0.01051` | `5` |
| **9** | [[Jovino Novoa Vasquez]] | `persona` | **`0.1574`** | `+0.01256` | `2` |
| **10** | [[Andres Chadwick Pinera]] | `persona` | **`0.1438`** | `+0.00256` | `3` |
| **11** | [[Hernan Larrain Fernandez]] | `persona` | **`0.1386`** | `+0.01240` | `2` |
| **12** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `persona` | **`0.1320`** | `+0.01193` | `2` |
| **13** | [[Pablo Wagner San Martin]] | `persona` | **`0.1320`** | `+0.01193` | `2` |
| **14** | [[Caso Penta]] | `causa_judicial` | **`0.1281`** | `+0.01030` | `3` |
| **15** | [[TRX-2011-03-10-Pagos-Penta-Wagner-01]] | `nexo_transaccion` | **`0.1278`** | `+0.00958` | `5` |
| **16** | [[Gabriel Ruiz-Tagle Serrano]] | `persona` | **`0.1197`** | `+0.01642` | `3` |
| **17** | [[Beltran Urenda Salamanca]] | `persona` | **`0.1194`** | `+0.06519` | `3` |
| **18** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `nexo_transaccion` | **`0.1179`** | `-0.00269` | `5` |
| **19** | [[Sebastian Pinera Echenique]] | `persona` | **`0.1153`** | `-0.00949` | `7` |
| **20** | [[Jaime Orpis Bouchon]] | `persona` | **`0.1129`** | `+0.01092` | `2` |
