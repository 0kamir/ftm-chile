---
tipo_nodo: vista_analitica
titulo: "Evolución Temporal G(t), Transición de Fase de Molloy-Reed y Ráfagas de Goh-Barabási"
actualizacion_automatica: true
tags:
  - evolucion-temporal
  - molloy-reed
  - goh-barabasi
  - transicion-de-fase
---

# ⏳ Evolución Temporal $G(t)$, Transición de Fase de Molloy-Reed y Ráfagas de Goh-Barabási

> [!IMPORTANT] Dinámica No Lineal de Redes Criminales y Coalescencia del Componente Gigante
> Esta vista reconstruye el grafo acumulado $G(t) = (V(t), E(t))$ desde `2001` hasta `2023` a medida que se activan cronológicamente los nexos transaccionales (`TRX`):
> 1. **Criterio de Percolación de Molloy-Reed ($\kappa(t) = \langle k^2 \rangle / \langle k \rangle > 2$)**: Determina en qué momento la red supera el umbral crítico $\kappa_c = 2.0$ y experimenta una **transición de fase hacia un régimen supercrítico macro-conectado**.
> 2. **Coeficiente de Ráfaga Temporal de Goh & Barabási ($B \in [-1, 1]$)**: Evalúa si las transacciones ilícitas ocurren de forma independiente o en **ráfagas sincronizadas ($B > 0$)** asociadas a ciclos electorales y presupuestarios.

## 1. Métricas Dinámicas e Inter-Transaccionales (2001–2023)

- **Coeficiente de Ráfaga Temporal de Goh-Barabási ($B$)**: **`+0.2759`**
  - *Diagnóstico Cronológico*: **Dinámica de Ráfagas Sincronizadas (*Burst-Driven Process*, $B > 0$: los desembolsos se concentran en ventanas electorales y cierres presupuestarios)**
- **Intervalo Medio entre Transacciones ($\mu_\tau$)**: `277.9 días` | **Desviación Estándar ($\sigma_\tau$)**: `489.7 días`
- **Parámetro de Molloy-Reed Actual ($\kappa(2023) = \langle k^2 \rangle / \langle k \rangle$)**: **`4.5000`** *(Supercrítico: $\kappa > 2.0$)*
- **Coalescencia del Componente Gigante ($S(2023)$)**: **`94.7%`** (`232` de `245` nodos operativos unidos en un único macro-componente)

---

## 2. Serie Histórica Acumulada $G(t)$ y Transición de Fase (`2001 → 2023`)

| Año ($t$) | TRX Acum. | Nodos $|V(t)|$ | Aristas $|E(t)|$ | LCC $|V_{\text{LCC}}(t)|$ | Fracción Gigante $S(t)$ | Molloy-Reed $\kappa(t)$ | Monto Acumulado $\Phi(t)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1971** | `1` | `6` | `7` | `6` | **`100.0%`** | `3.00` | `$9.500.000.000 CLP` |
| **1972** | `2` | `9` | `12` | `9` | **`100.0%`** | `3.42` | `$24.300.000.000 CLP` |
| **1975** | `3` | `11` | `17` | `11` | **`100.0%`** | `3.76` | `$26.400.000.000 CLP` |
| **1982** | `4` | `17` | `24` | `17` | **`100.0%`** | `3.58` | `$44.900.000.000 CLP` |
| **1989** | `5` | `21` | `31` | `21` | **`100.0%`** | `3.65` | `$47.850.000.000 CLP` |
| **1991** | `6` | `27` | `37` | `21` | **`77.8%`** | `3.54` | `$51.300.000.000 CLP` |
| **1996** | `7` | `31` | `43` | `21` | **`67.7%`** | `3.53` | `$51.540.000.000 CLP` |
| **2000** | `8` | `37` | `49` | `21` | **`56.8%`** | `3.49` | `$51.540.000.000 CLP` |
| **2001** | `9` | `44` | `57` | `21` | **`47.7%`** | `3.42` | `$52.793.000.000 CLP` |
| **2002** | `10` | `45` | `62` | `24` | **`53.3%`** | `3.53` | `$53.243.000.000 CLP` |
| **2003** | `12` | `51` | `74` | `51` | **`100.0%`** | `3.58` | `$53.843.000.000 CLP` |
| **2004** | `13` | `55` | `80` | `55` | **`100.0%`** | `3.61` | `$69.643.000.000 CLP` |
| **2005** | `15` | `58` | `92` | `58` | **`100.0%`** | `3.83` | `$73.943.000.000 CLP` |
| **2006** | `16` | `61` | `98` | `61` | **`100.0%`** | `3.84` | `$79.243.000.000 CLP` |
| **2007** | `18` | `73` | `110` | `61` | **`83.6%`** | `3.75` | `$79.243.000.000 CLP` |
| **2008** | `19` | `76` | `115` | `61` | **`80.3%`** | `3.76` | `$79.243.000.000 CLP` |
| **2009** | `20` | `81` | `122` | `66` | **`81.5%`** | `3.75` | `$79.583.000.000 CLP` |
| **2010** | `24` | `94` | `147` | `78` | **`83.0%`** | `3.86` | `$174.313.000.000 CLP` |
| **2011** | `26` | `103` | `163` | `87` | **`84.5%`** | `3.98` | `$198.855.000.000 CLP` |
| **2012** | `29` | `115` | `182` | `99` | **`86.1%`** | `4.03` | `$208.458.000.000 CLP` |
| **2013** | `32` | `121` | `196` | `105` | **`86.8%`** | `4.21` | `$209.874.000.000 CLP` |
| **2014** | `34` | `132` | `209` | `110` | **`83.3%`** | `4.15` | `$216.114.000.000 CLP` |
| **2015** | `39` | `143` | `231` | `143` | **`100.0%`** | `4.19` | `$260.514.000.000 CLP` |
| **2016** | `44` | `158` | `257` | `153` | **`96.8%`** | `4.27` | `$336.862.928.198 CLP` |
| **2017** | `48` | `168` | `276` | `168` | **`100.0%`** | `4.26` | `$435.837.928.198 CLP` |
| **2018** | `49` | `170` | `281` | `170` | **`100.0%`** | `4.30` | `$435.837.928.198 CLP` |
| **2019** | `51` | `181` | `295` | `175` | **`96.7%`** | `4.30` | `$439.227.928.198 CLP` |
| **2020** | `53` | `186` | `305` | `180` | **`96.8%`** | `4.32` | `$472.379.928.198 CLP` |
| **2021** | `54` | `192` | `312` | `186` | **`96.9%`** | `4.30` | `$473.138.928.198 CLP` |
| **2022** | `63` | `217` | `362` | `192` | **`88.5%`** | `4.36` | `$476.868.563.198 CLP` |
| **2023** | `71` | `240` | `408` | `227` | **`94.6%`** | `4.50` | `$750.963.563.198 CLP` |
| **2025** | `72` | `243` | `412` | `230` | **`94.7%`** | `4.50` | `$750.998.563.198 CLP` |
| **2026** | `73` | `245` | `416` | `232` | **`94.7%`** | `4.50` | `$750.998.563.198 CLP` |

---

## 3. Curva de Crecimiento del Componente Gigante $S(t)$ y Caudal Auditado

```mermaid
xychart-beta
    title "Coalescencia del Componente Gigante S(t) (% de la Red Operativa)"
    x-axis [1971, 1972, 1975, 1982, 1989, 1991, 1996, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2025, 2026]
    y-axis "Fracción LCC (%)" 0 --> 100
    line [100.0, 100.0, 100.0, 100.0, 100.0, 77.8, 67.7, 56.8, 47.7, 53.3, 100.0, 100.0, 100.0, 100.0, 83.6, 80.3, 81.5, 83.0, 84.5, 86.1, 86.8, 83.3, 100.0, 96.8, 100.0, 100.0, 96.7, 96.8, 96.9, 88.5, 94.6, 94.7, 94.7]
```
