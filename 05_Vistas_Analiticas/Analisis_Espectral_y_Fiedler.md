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

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `218` nodos operativos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.038235`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1168` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `421.52`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0191, 1.0710]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`5.0478`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.1981`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `171` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `47` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `20` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **`-0.00011`** | `0.0743` | `13` |
| **2** | [[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]] | `nexo_transaccion` | **`-0.00012`** | `0.0175` | `3` |
| **3** | [[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]] | `nexo_transaccion` | **`-0.00012`** | `0.0175` | `3` |
| **4** | [[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]] | `nexo_transaccion` | **`-0.00012`** | `0.0175` | `3` |
| **5** | [[Caso Archivos Epstein Menciones Chile]] | `causa_judicial` | **`-0.00012`** | `0.0104` | `3` |
| **6** | [[Andres Velasco Branes]] | `persona` | **`-0.00012`** | `0.0035` | `1` |
| **7** | [[Andronico Luksic Craig]] | `persona` | **`-0.00012`** | `0.0035` | `1` |
| **8** | [[Eduardo Guendelman Israel]] | `persona` | **`-0.00012`** | `0.0035` | `1` |
| **9** | [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] | `nexo_transaccion` | **`-0.00013`** | `0.0213` | `5` |
| **10** | [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]] | `nexo_transaccion` | **`-0.00013`** | `0.0213` | `5` |
| **11** | [[Direccion de Inteligencia Policial de Carabineros]] | `entidad_publica` | **`-0.00013`** | `0.0096` | `3` |
| **12** | [[Alex Smith Leay]] | `persona` | **`-0.00013`** | `0.0096` | `3` |
| **13** | [[Caso Operacion Huracan]] | `causa_judicial` | **`-0.00013`** | `0.0096` | `3` |
| **14** | [[Gonzalo Blu Rodriguez]] | `persona` | **`-0.00013`** | `0.0042` | `1` |
| **15** | [[Leonardo Osses Sandoval]] | `persona` | **`-0.00013`** | `0.0042` | `1` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Andres Chadwick Pinera]] | `+0.01155` | [[Union Democrata Independiente]] | `-0.00085` |
| **2** | [[Carlos Alberto Delano Abbott]] | `+0.00625` | [[Union Democrata Independiente]] | `-0.00085` |
| **3** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `+0.00480` | [[Union Democrata Independiente]] | `-0.00085` |
| **4** | [[Cathy Barriga Guerra]] | `+0.00558` | [[Union Democrata Independiente]] | `-0.00085` |
| **5** | [[Hernan Larrain Fernandez]] | `+0.00192` | [[Union Democrata Independiente]] | `-0.00085` |
| **6** | [[Jaime Orpis Bouchon]] | `+0.00569` | [[Union Democrata Independiente]] | `-0.00085` |
| **7** | [[Jovino Novoa Vasquez]] | `+0.00151` | [[Union Democrata Independiente]] | `-0.00085` |
| **8** | [[Pablo Longueira Montes]] | `+0.00436` | [[Union Democrata Independiente]] | `-0.00085` |
| **9** | [[Pablo Wagner San Martin]] | `+0.00440` | [[Union Democrata Independiente]] | `-0.00085` |
| **10** | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | `+0.01635` | [[Corte Suprema de Chile]] | `-0.00011` |
| **11** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.01471` | [[Corte Suprema de Chile]] | `-0.00011` |
| **12** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `+0.00462` | [[Union Democrata Independiente]] | `-0.00085` |
| **13** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `+0.01657` | [[Corte Suprema de Chile]] | `-0.00011` |
| **14** | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `+0.00744` | [[Corte Suprema de Chile]] | `-0.00011` |
| **15** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `+0.00937` | [[Union Democrata Independiente]] | `-0.00085` |
| **16** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `+0.00439` | [[Union Democrata Independiente]] | `-0.00085` |
| **17** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `+0.00381` | [[Union Democrata Independiente]] | `-0.00085` |
| **18** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `+0.01392` | [[Corte Suprema de Chile]] | `-0.00011` |
| **19** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `+0.01361` | [[Corte Suprema de Chile]] | `-0.00011` |
| **20** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `+0.01361` | [[Corte Suprema de Chile]] | `-0.00011` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Caso Convenios]] | `causa_judicial` | **`0.3738`** | `+0.06052` | `9` |
| **2** | [[Carlos Contreras Gutierrez]] | `persona` | **`0.2529`** | `+0.06219` | `6` |
| **3** | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | `nexo_transaccion` | **`0.2514`** | `+0.06075` | `5` |
| **4** | [[TRX-2022-11-29-Convenio-DV-03]] | `nexo_transaccion` | **`0.2479`** | `+0.06289` | `5` |
| **5** | [[TRX-2022-10-03-Convenio-DV-01]] | `nexo_transaccion` | **`0.2479`** | `+0.06289` | `5` |
| **6** | [[TRX-2022-10-19-Convenio-DV-02]] | `nexo_transaccion` | **`0.2479`** | `+0.06289` | `5` |
| **7** | [[Seremi MINVU Antofagasta]] | `entidad_publica` | **`0.2350`** | `+0.06178` | `5` |
| **8** | [[Alberto Larrain Salas]] | `persona` | **`0.2037`** | `+0.05847` | `5` |
| **9** | [[Fundacion ProCultura]] | `entidad_privada` | **`0.2037`** | `+0.05847` | `5` |
| **10** | [[Daniel Andrade Schwarze]] | `persona` | **`0.2023`** | `+0.06381` | `5` |
| **11** | [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | `nexo_transaccion` | **`0.1954`** | `+0.06128` | `5` |
| **12** | [[TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01]] | `nexo_transaccion` | **`0.1954`** | `+0.06128` | `5` |
| **13** | [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | `nexo_transaccion` | **`0.1911`** | `+0.05712` | `5` |
| **14** | [[Fundacion Democracia Viva]] | `entidad_privada` | **`0.1874`** | `+0.06373` | `4` |
| **15** | [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | `nexo_transaccion` | **`0.1824`** | `+0.04834` | `5` |
| **16** | [[Union Democrata Independiente]] | `partido_politico` | **`0.1393`** | `-0.00085` | `15` |
| **17** | [[TRX-2022-12-20-Convenio-EnTi-01]] | `nexo_transaccion` | **`0.1272`** | `+0.06492` | `5` |
| **18** | [[Rodrigo Diaz Worner]] | `persona` | **`0.1026`** | `+0.06330` | `3` |
| **19** | [[GORE Biobio]] | `entidad_publica` | **`0.1026`** | `+0.06330` | `3` |
| **20** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.0912`** | `+0.02583` | `9` |
