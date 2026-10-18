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

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `245` nodos operativos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.036180`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1168` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `445.46`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0181, 1.0418]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`5.0620`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.1975`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `180` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `65` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `24` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]] | `nexo_transaccion` | **`+0.00015`** | `0.0141` | `5` |
| **2** | [[Caso Corpesca]] | `causa_judicial` | **`+0.00016`** | `0.0028` | `1` |
| **3** | [[Corpesca SA]] | `entidad_privada` | **`+0.00016`** | `0.0035` | `2` |
| **4** | [[Francisco Mujica Ortuzar]] | `persona` | **`+0.00016`** | `0.0035` | `2` |
| **5** | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `nexo_transaccion` | **`-0.00059`** | `0.0473` | `5` |
| **6** | [[Caso Colonia Dignidad]] | `causa_judicial` | **`+0.00060`** | `0.0306` | `3` |
| **7** | [[Andes Iron SpA]] | `entidad_privada` | **`+0.00068`** | `0.0320` | `2` |
| **8** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `nexo_transaccion` | **`-0.00079`** | `0.0653` | `5` |
| **9** | [[Sociedad Benefactora y Educacional Dignidad]] | `entidad_privada` | **`+0.00100`** | `0.0356` | `4` |
| **10** | [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]] | `nexo_transaccion` | **`-0.00114`** | `0.0111` | `3` |
| **11** | [[Caso Municipalidad de Maipu]] | `causa_judicial` | **`-0.00119`** | `0.0022` | `1` |
| **12** | [[TRX-2011-03-10-Soborno-Penta-Wagner-01]] | `nexo_transaccion` | **`+0.00217`** | `0.0701` | `5` |
| **13** | [[Paul Schafer Schneider]] | `persona` | **`+0.00218`** | `0.0253` | `3` |
| **14** | [[Andres Chadwick Pinera]] | `persona` | **`+0.00229`** | `0.0695` | `3` |
| **15** | [[Caso Penta]] | `causa_judicial` | **`-0.00242`** | `0.0511` | `3` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Andes Iron SpA]] | `+0.00068` | [[Carlos Alberto Delano Abbott]] | `-0.00276` |
| **2** | [[Andres Chadwick Pinera]] | `+0.00229` | [[Union Democrata Independiente]] | `-0.00937` |
| **3** | [[Caso Colonia Dignidad]] | `+0.00060` | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `-0.00367` |
| **4** | [[Caso Colonia Dignidad]] | `+0.00060` | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `-0.00059` |
| **5** | [[Caso SQM]] | `+0.00290` | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `-0.00079` |
| **6** | [[Jorge Zepeda Arancibia]] | `+0.00278` | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `-0.00059` |
| **7** | [[Municipalidad de Maipu]] | `+0.00273` | [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]] | `-0.00114` |
| **8** | [[Patricio Contesse Gonzalez]] | `+0.00375` | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `-0.00079` |
| **9** | [[Paul Schafer Schneider]] | `+0.00218` | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `-0.00059` |
| **10** | [[SQM SA]] | `+0.00375` | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `-0.00079` |
| **11** | [[Sociedad Benefactora y Educacional Dignidad]] | `+0.00100` | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `-0.00367` |
| **12** | [[Sociedad Benefactora y Educacional Dignidad]] | `+0.00100` | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `-0.00059` |
| **13** | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | `+0.00397` | [[Corte Suprema de Chile]] | `-0.00947` |
| **14** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.00493` | [[Corte Suprema de Chile]] | `-0.00947` |
| **15** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `+0.00497` | [[Corte Suprema de Chile]] | `-0.00947` |
| **16** | [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] | `+0.00408` | [[Carlos Alberto Delano Abbott]] | `-0.00276` |
| **17** | [[TRX-2011-03-10-Soborno-Penta-Wagner-01]] | `+0.00217` | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `-0.00410` |
| **18** | [[TRX-2011-03-10-Soborno-Penta-Wagner-01]] | `+0.00217` | [[Caso Penta]] | `-0.00242` |
| **19** | [[TRX-2011-03-10-Soborno-Penta-Wagner-01]] | `+0.00217` | [[Empresas Penta SA]] | `-0.00250` |
| **20** | [[TRX-2011-03-10-Soborno-Penta-Wagner-01]] | `+0.00217` | [[Pablo Wagner San Martin]] | `-0.00367` |
| **21** | [[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]] | `+0.00015` | [[Jaime Orpis Bouchon]] | `-0.00470` |
| **22** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `+0.00314` | [[Corte Suprema de Chile]] | `-0.00947` |
| **23** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `+0.00508` | [[Corte Suprema de Chile]] | `-0.00947` |
| **24** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `+0.00508` | [[Corte Suprema de Chile]] | `-0.00947` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Caso Convenios]] | `causa_judicial` | **`0.3312`** | `+0.08013` | `9` |
| **2** | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | `nexo_transaccion` | **`0.2221`** | `+0.08000` | `5` |
| **3** | [[Carlos Contreras Gutierrez]] | `persona` | **`0.2211`** | `+0.08080` | `6` |
| **4** | [[TRX-2022-11-29-Convenio-DV-03]] | `nexo_transaccion` | **`0.2168`** | `+0.08209` | `5` |
| **5** | [[TRX-2022-10-19-Convenio-DV-02]] | `nexo_transaccion` | **`0.2168`** | `+0.08209` | `5` |
| **6** | [[TRX-2022-10-03-Convenio-DV-01]] | `nexo_transaccion` | **`0.2168`** | `+0.08209` | `5` |
| **7** | [[Seremi MINVU Antofagasta]] | `entidad_publica` | **`0.2056`** | `+0.08025` | `5` |
| **8** | [[Union Democrata Independiente]] | `partido_politico` | **`0.1867`** | `-0.00937` | `15` |
| **9** | [[Alberto Larrain Salas]] | `persona` | **`0.1832`** | `+0.07796` | `5` |
| **10** | [[Fundacion ProCultura]] | `entidad_privada` | **`0.1832`** | `+0.07796` | `5` |
| **11** | [[Daniel Andrade Schwarze]] | `persona` | **`0.1762`** | `+0.08318` | `5` |
| **12** | [[TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01]] | `nexo_transaccion` | **`0.1749`** | `+0.08431` | `5` |
| **13** | [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | `nexo_transaccion` | **`0.1749`** | `+0.08431` | `5` |
| **14** | [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | `nexo_transaccion` | **`0.1725`** | `+0.06040` | `5` |
| **15** | [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | `nexo_transaccion` | **`0.1682`** | `+0.07210` | `5` |
| **16** | [[Fundacion Democracia Viva]] | `entidad_privada` | **`0.1633`** | `+0.08311` | `4` |
| **17** | [[Factop SpA]] | `entidad_privada` | **`0.1351`** | `+0.00991` | `7` |
| **18** | [[Luis Hermosilla Osorio]] | `persona` | **`0.1351`** | `+0.00991` | `7` |
| **19** | [[Corte Suprema de Chile]] | `entidad_publica` | **`0.1294`** | `-0.00947` | `13` |
| **20** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.1203`** | `+0.02343` | `10` |
