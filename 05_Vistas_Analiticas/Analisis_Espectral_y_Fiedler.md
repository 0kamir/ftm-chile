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

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `233` nodos operativos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.037603`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1168` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `428.61`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0188, 1.0621]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`5.0509`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.1980`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `184` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `49` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `20` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Hernan Larrain Fernandez]] | `persona` | **`-0.00059`** | `0.0396` | `2` |
| **2** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `nexo_transaccion` | **`+0.00112`** | `0.0754` | `5` |
| **3** | [[Jovino Novoa Vasquez]] | `persona` | **`-0.00128`** | `0.0447` | `2` |
| **4** | [[Pablo Longueira Montes]] | `persona` | **`+0.00133`** | `0.0555` | `3` |
| **5** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `nexo_transaccion` | **`+0.00165`** | `0.0776` | `5` |
| **6** | [[Pablo Wagner San Martin]] | `persona` | **`+0.00221`** | `0.0413` | `2` |
| **7** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `persona` | **`+0.00221`** | `0.0495` | `3` |
| **8** | [[Cathy Barriga Guerra]] | `persona` | **`+0.00222`** | `0.0413` | `3` |
| **9** | [[Jaime Orpis Bouchon]] | `persona` | **`+0.00235`** | `0.0317` | `2` |
| **10** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `nexo_transaccion` | **`+0.00247`** | `0.0496` | `5` |
| **11** | [[Hartmut Hopp Miottel]] | `persona` | **`+0.00257`** | `0.0098` | `1` |
| **12** | [[Corte Suprema de Chile]] | `entidad_publica` | **`-0.00323`** | `0.0807` | `13` |
| **13** | [[Carlos Alberto Delano Abbott]] | `persona` | **`+0.00331`** | `0.0855` | `6` |
| **14** | [[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]] | `nexo_transaccion` | **`-0.00354`** | `0.0190` | `3` |
| **15** | [[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]] | `nexo_transaccion` | **`-0.00354`** | `0.0190` | `3` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Andres Chadwick Pinera]] | `+0.00829` | [[Union Democrata Independiente]] | `-0.00363` |
| **2** | [[Carlos Alberto Delano Abbott]] | `+0.00331` | [[Union Democrata Independiente]] | `-0.00363` |
| **3** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `+0.00221` | [[Union Democrata Independiente]] | `-0.00363` |
| **4** | [[Cathy Barriga Guerra]] | `+0.00222` | [[Union Democrata Independiente]] | `-0.00363` |
| **5** | [[Jaime Orpis Bouchon]] | `+0.00235` | [[Union Democrata Independiente]] | `-0.00363` |
| **6** | [[Pablo Longueira Montes]] | `+0.00133` | [[Union Democrata Independiente]] | `-0.00363` |
| **7** | [[Pablo Wagner San Martin]] | `+0.00221` | [[Union Democrata Independiente]] | `-0.00363` |
| **8** | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | `+0.01290` | [[Corte Suprema de Chile]] | `-0.00323` |
| **9** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.01136` | [[Corte Suprema de Chile]] | `-0.00323` |
| **10** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `+0.00247` | [[Hernan Larrain Fernandez]] | `-0.00059` |
| **11** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `+0.00247` | [[Union Democrata Independiente]] | `-0.00363` |
| **12** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `+0.01297` | [[Corte Suprema de Chile]] | `-0.00323` |
| **13** | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `+0.00564` | [[Corte Suprema de Chile]] | `-0.00323` |
| **14** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `+0.00593` | [[Union Democrata Independiente]] | `-0.00363` |
| **15** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `+0.00165` | [[Union Democrata Independiente]] | `-0.00363` |
| **16** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `+0.00112` | [[Jovino Novoa Vasquez]] | `-0.00128` |
| **17** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `+0.00112` | [[Union Democrata Independiente]] | `-0.00363` |
| **18** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `+0.01094` | [[Corte Suprema de Chile]] | `-0.00323` |
| **19** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `+0.01071` | [[Corte Suprema de Chile]] | `-0.00323` |
| **20** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `+0.01071` | [[Corte Suprema de Chile]] | `-0.00323` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Caso Convenios]] | `causa_judicial` | **`0.3682`** | `+0.05709` | `9` |
| **2** | [[Carlos Contreras Gutierrez]] | `persona` | **`0.2483`** | `+0.05842` | `6` |
| **3** | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | `nexo_transaccion` | **`0.2475`** | `+0.05732` | `5` |
| **4** | [[TRX-2022-10-03-Convenio-DV-01]] | `nexo_transaccion` | **`0.2435`** | `+0.05913` | `5` |
| **5** | [[TRX-2022-10-19-Convenio-DV-02]] | `nexo_transaccion` | **`0.2435`** | `+0.05913` | `5` |
| **6** | [[TRX-2022-11-29-Convenio-DV-03]] | `nexo_transaccion` | **`0.2435`** | `+0.05913` | `5` |
| **7** | [[Seremi MINVU Antofagasta]] | `entidad_publica` | **`0.2308`** | `+0.05803` | `5` |
| **8** | [[Alberto Larrain Salas]] | `persona` | **`0.2014`** | `+0.05545` | `5` |
| **9** | [[Fundacion ProCultura]] | `entidad_privada` | **`0.2014`** | `+0.05545` | `5` |
| **10** | [[Daniel Andrade Schwarze]] | `persona` | **`0.1985`** | `+0.05997` | `5` |
| **11** | [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | `nexo_transaccion` | **`0.1927`** | `+0.05796` | `5` |
| **12** | [[TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01]] | `nexo_transaccion` | **`0.1927`** | `+0.05796` | `5` |
| **13** | [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | `nexo_transaccion` | **`0.1879`** | `+0.05328` | `5` |
| **14** | [[Fundacion Democracia Viva]] | `entidad_privada` | **`0.1839`** | `+0.05990` | `4` |
| **15** | [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | `nexo_transaccion` | **`0.1832`** | `+0.04649` | `5` |
| **16** | [[Union Democrata Independiente]] | `partido_politico` | **`0.1501`** | `-0.00363` | `15` |
| **17** | [[TRX-2022-12-20-Convenio-EnTi-01]] | `nexo_transaccion` | **`0.1251`** | `+0.06127` | `5` |
| **18** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.1044`** | `+0.02792` | `10` |
| **19** | [[GORE Biobio]] | `entidad_publica` | **`0.1011`** | `+0.05981` | `3` |
| **20** | [[Rodrigo Diaz Worner]] | `persona` | **`0.1011`** | `+0.05981` | `3` |
