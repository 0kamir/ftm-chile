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

- **Dimensión del Subespacio Conectado ($N_{\text{LCC}}$)**: `226` nodos operativos
- **Conectividad Algebraica de Fiedler ($\lambda_2$)**: **`0.037892`** *(Un valor positivo bajo confirma un cuello de botella espectral entre dos macro-ecosistemas conectados por pocos puentes)*
- **Mayor Autovalor Laplaciano ($\lambda_{\max}$)**: `16.1168` | **Razón Espectral ($\lambda_{\max} / \lambda_2$)**: `425.34`
- **Cotas Isoperimétricas de Cheeger ($h(G)$)**: `[0.0189, 1.0662]`
- **Radio Espectral de Adyacencia ($\rho(A) = \mu_{\max}$)**: **`5.0502`**
- **Umbral Crítico de Difusión / Contagio Institucional ($\tau_c = 1/\rho(A)$)**: **`0.1980`**
- **Partición de Hemisferios de Fiedler**:
  - **Hemisferio Positivo ($v_2(i) \ge 0$)**: `178` nodos
  - **Hemisferio Negativo ($v_2(i) < 0$)**: `48` nodos
  - **Aristas en el Corte Espectral de Fiedler**: `20` enlaces inter-hemisféricos

---

## 2. Línea de Falla Espectral (Nodos Bisagra con $|v_2(i)| \approx 0$)

Los nodos cuyas coordenadas en el autovector de Fiedler son más cercanas a cero constituyen la **frontera espectral** exacta que articula ambos hemisferios de la red:

| Pos | Nodo en la Frontera Espectral | Tipo | Coordenada de Fiedler ($v_2(i)$) | Centralidad Autovector ($x_i$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Jovino Novoa Vasquez]] | `persona` | **`-0.00002`** | `0.0439` | `2` |
| **2** | [[Hernan Larrain Fernandez]] | `persona` | **`+0.00056`** | `0.0388` | `2` |
| **3** | [[Corte Suprema de Chile]] | `entidad_publica` | **`-0.00178`** | `0.0791` | `13` |
| **4** | [[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]] | `nexo_transaccion` | **`-0.00196`** | `0.0186` | `3` |
| **5** | [[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]] | `nexo_transaccion` | **`-0.00196`** | `0.0186` | `3` |
| **6** | [[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]] | `nexo_transaccion` | **`-0.00196`** | `0.0186` | `3` |
| **7** | [[Caso Archivos Epstein Menciones Chile]] | `causa_judicial` | **`-0.00199`** | `0.0110` | `3` |
| **8** | [[Andres Velasco Branes]] | `persona` | **`-0.00204`** | `0.0037` | `1` |
| **9** | [[Eduardo Guendelman Israel]] | `persona` | **`-0.00204`** | `0.0037` | `1` |
| **10** | [[Andronico Luksic Craig]] | `persona` | **`-0.00204`** | `0.0037` | `1` |
| **11** | [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] | `nexo_transaccion` | **`-0.00217`** | `0.0226` | `5` |
| **12** | [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]] | `nexo_transaccion` | **`-0.00217`** | `0.0226` | `5` |
| **13** | [[Caso Operacion Huracan]] | `causa_judicial` | **`-0.00224`** | `0.0102` | `3` |
| **14** | [[Direccion de Inteligencia Policial de Carabineros]] | `entidad_publica` | **`-0.00224`** | `0.0102` | `3` |
| **15** | [[Alex Smith Leay]] | `persona` | **`-0.00224`** | `0.0102` | `3` |

---

## 3. Aristas del Corte Espectral de Fiedler ($v_2(u) \ge 0 \leftrightarrow v_2(v) < 0$)

| # | Nodo Hemisferio Positivo ($v_2 \ge 0$) | Coordenada $v_2(u)$ | Nodo Hemisferio Negativo ($v_2 < 0$) | Coordenada $v_2(v)$ |
| :---: | :--- | :---: | :--- | :---: |
| **1** | [[Andres Chadwick Pinera]] | `+0.00975` | [[Union Democrata Independiente]] | `-0.00238` |
| **2** | [[Carlos Alberto Delano Abbott]] | `+0.00465` | [[Union Democrata Independiente]] | `-0.00238` |
| **3** | [[Carlos Eugenio Lavin Garcia-Huidobro]] | `+0.00339` | [[Union Democrata Independiente]] | `-0.00238` |
| **4** | [[Cathy Barriga Guerra]] | `+0.00373` | [[Union Democrata Independiente]] | `-0.00238` |
| **5** | [[Hernan Larrain Fernandez]] | `+0.00056` | [[Union Democrata Independiente]] | `-0.00238` |
| **6** | [[Jaime Orpis Bouchon]] | `+0.00374` | [[Union Democrata Independiente]] | `-0.00238` |
| **7** | [[Pablo Longueira Montes]] | `+0.00270` | [[Union Democrata Independiente]] | `-0.00238` |
| **8** | [[Pablo Wagner San Martin]] | `+0.00321` | [[Union Democrata Independiente]] | `-0.00238` |
| **9** | [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]] | `+0.01452` | [[Corte Suprema de Chile]] | `-0.00178` |
| **10** | [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] | `+0.01290` | [[Corte Suprema de Chile]] | `-0.00178` |
| **11** | [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]] | `+0.00347` | [[Union Democrata Independiente]] | `-0.00238` |
| **12** | [[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]] | `+0.01460` | [[Corte Suprema de Chile]] | `-0.00178` |
| **13** | [[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]] | `+0.00650` | [[Corte Suprema de Chile]] | `-0.00178` |
| **14** | [[TRX-2010-08-19-Correo-Royalty-SQM-01]] | `+0.00749` | [[Union Democrata Independiente]] | `-0.00238` |
| **15** | [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] | `+0.00289` | [[Union Democrata Independiente]] | `-0.00238` |
| **16** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `+0.00235` | [[Jovino Novoa Vasquez]] | `-0.00002` |
| **17** | [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]] | `+0.00235` | [[Union Democrata Independiente]] | `-0.00238` |
| **18** | [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] | `+0.01234` | [[Corte Suprema de Chile]] | `-0.00178` |
| **19** | [[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]] | `+0.01204` | [[Corte Suprema de Chile]] | `-0.00178` |
| **20** | [[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]] | `+0.01204` | [[Corte Suprema de Chile]] | `-0.00178` |

---

## 4. Ranking de Centralidad de Autovector de Perron-Frobenius ($A x = \rho(A) x$)

| Pos | Nodo Operativo | Tipo | Autovector Perron-Frobenius ($x_i$) | Coordenada Fiedler ($v_2(i)$) | Grado ($k_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | [[Caso Convenios]] | `causa_judicial` | **`0.3697`** | `+0.05881` | `9` |
| **2** | [[Carlos Contreras Gutierrez]] | `persona` | **`0.2495`** | `+0.06030` | `6` |
| **3** | [[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]] | `nexo_transaccion` | **`0.2486`** | `+0.05904` | `5` |
| **4** | [[TRX-2022-10-03-Convenio-DV-01]] | `nexo_transaccion` | **`0.2447`** | `+0.06100` | `5` |
| **5** | [[TRX-2022-11-29-Convenio-DV-03]] | `nexo_transaccion` | **`0.2447`** | `+0.06100` | `5` |
| **6** | [[TRX-2022-10-19-Convenio-DV-02]] | `nexo_transaccion` | **`0.2447`** | `+0.06100` | `5` |
| **7** | [[Seremi MINVU Antofagasta]] | `entidad_publica` | **`0.2319`** | `+0.05990` | `5` |
| **8** | [[Alberto Larrain Salas]] | `persona` | **`0.2021`** | `+0.05699` | `5` |
| **9** | [[Fundacion ProCultura]] | `entidad_privada` | **`0.2021`** | `+0.05699` | `5` |
| **10** | [[Daniel Andrade Schwarze]] | `persona` | **`0.1995`** | `+0.06189` | `5` |
| **11** | [[TRX-2022-09-12-Reunion-Lobby-ProCultura-Biobio-01]] | `nexo_transaccion` | **`0.1934`** | `+0.05964` | `5` |
| **12** | [[TRX-2022-11-18-Convenio-ProCultura-Biobio]] | `nexo_transaccion` | **`0.1934`** | `+0.05964` | `5` |
| **13** | [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]] | `nexo_transaccion` | **`0.1887`** | `+0.05517` | `5` |
| **14** | [[Fundacion Democracia Viva]] | `entidad_privada` | **`0.1848`** | `+0.06181` | `4` |
| **15** | [[TRX-2023-05-10-Liquidacion-Tributaria-ProCultura-SII-01]] | `nexo_transaccion` | **`0.1831`** | `+0.04748` | `5` |
| **16** | [[Union Democrata Independiente]] | `partido_politico` | **`0.1474`** | `-0.00238` | `15` |
| **17** | [[TRX-2022-12-20-Convenio-EnTi-01]] | `nexo_transaccion` | **`0.1257`** | `+0.06311` | `5` |
| **18** | [[GORE Biobio]] | `entidad_publica` | **`0.1015`** | `+0.06157` | `3` |
| **19** | [[Rodrigo Diaz Worner]] | `persona` | **`0.1015`** | `+0.06157` | `3` |
| **20** | [[Servicio Impuestos Internos]] | `entidad_publica` | **`0.1014`** | `+0.02711` | `10` |
