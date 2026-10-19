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

- **Coeficiente de Ráfaga Temporal de Goh-Barabási ($B$)**: **`+0.2642`**
  - *Diagnóstico Cronológico*: **Dinámica de Ráfagas Sincronizadas (*Burst-Driven Process*, $B > 0$: los desembolsos se concentran en ventanas electorales y cierres presupuestarios)**
- **Intervalo Medio entre Transacciones ($\mu_\tau$)**: `294.9 días` | **Desviación Estándar ($\sigma_\tau$)**: `506.7 días`
- **Parámetro de Molloy-Reed Actual ($\kappa(2023) = \langle k^2 \rangle / \langle k \rangle$)**: **`4.3953`** *(Supercrítico: $\kappa > 2.0$)*
- **Coalescencia del Componente Gigante ($S(2023)$)**: **`91.4%`** (`213` de `233` nodos operativos unidos en un único macro-componente)

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
| **2003** | `11` | `50` | `69` | `43` | **`86.0%`** | `3.48` | `$53.393.000.000 CLP` |
| **2004** | `12` | `54` | `75` | `47` | **`87.0%`** | `3.52` | `$69.193.000.000 CLP` |
| **2005** | `14` | `57` | `87` | `50` | **`87.7%`** | `3.75` | `$71.643.000.000 CLP` |
| **2006** | `15` | `60` | `93` | `53` | **`88.3%`** | `3.76` | `$76.943.000.000 CLP` |
| **2007** | `17` | `72` | `105` | `53` | **`73.6%`** | `3.68` | `$76.943.000.000 CLP` |
| **2008** | `18` | `75` | `110` | `53` | **`70.7%`** | `3.69` | `$76.943.000.000 CLP` |
| **2009** | `19` | `80` | `117` | `58` | **`72.5%`** | `3.69` | `$77.283.000.000 CLP` |
| **2010** | `23` | `93` | `142` | `70` | **`75.3%`** | `3.81` | `$153.699.500.000 CLP` |
| **2011** | `25` | `102` | `157` | `79` | **`77.5%`** | `3.90` | `$153.741.500.000 CLP` |
| **2012** | `28` | `114` | `176` | `91` | **`79.8%`** | `3.97` | `$163.344.500.000 CLP` |
| **2013** | `31` | `120` | `190` | `97` | **`80.8%`** | `4.16` | `$164.760.500.000 CLP` |
| **2014** | `33` | `129` | `200` | `102` | **`79.1%`** | `4.10` | `$170.915.530.792 CLP` |
| **2015** | `38` | `141` | `221` | `134` | **`95.0%`** | `4.12` | `$215.315.530.792 CLP` |
| **2016** | `43` | `156` | `247` | `144` | **`92.3%`** | `4.21` | `$291.664.458.990 CLP` |
| **2017** | `47` | `166` | `266` | `159` | **`95.8%`** | `4.21` | `$390.639.458.990 CLP` |
| **2018** | `48` | `168` | `271` | `161` | **`95.8%`** | `4.24` | `$390.639.458.990 CLP` |
| **2019** | `50` | `179` | `285` | `166` | **`92.7%`** | `4.25` | `$390.866.458.990 CLP` |
| **2020** | `52` | `184` | `295` | `171` | **`92.9%`** | `4.27` | `$424.018.458.990 CLP` |
| **2021** | `53` | `190` | `302` | `177` | **`93.2%`** | `4.25` | `$424.777.458.990 CLP` |
| **2022** | `61` | `214` | `347` | `183` | **`85.5%`** | `4.29` | `$428.507.093.990 CLP` |
| **2023** | `67` | `230` | `378` | `210` | **`91.3%`** | `4.39` | `$669.087.093.990 CLP` |
| **2025** | `68` | `233` | `382` | `213` | **`91.4%`** | `4.40` | `$669.122.093.990 CLP` |

---

## 3. Curva de Crecimiento del Componente Gigante $S(t)$ y Caudal Auditado

```mermaid
xychart-beta
    title "Coalescencia del Componente Gigante S(t) (% de la Red Operativa)"
    x-axis [1971, 1972, 1975, 1982, 1989, 1991, 1996, 2000, 2001, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2025]
    y-axis "Fracción LCC (%)" 0 --> 100
    line [100.0, 100.0, 100.0, 100.0, 100.0, 77.8, 67.7, 56.8, 47.7, 86.0, 87.0, 87.7, 88.3, 73.6, 70.7, 72.5, 75.3, 77.5, 79.8, 80.8, 79.1, 95.0, 92.3, 95.8, 95.8, 92.7, 92.9, 93.2, 85.5, 91.3, 91.4]
```
