---
tipo_nodo: vista_analitica
titulo: "Simulación de Percolación y Desarticulación de Nodos Clave (Key Player Problem)"
actualizacion_automatica: true
tags:
  - dashboard
  - percolacion
  - desarticulacion-red
---

# Simulación Forense de Desarticulación de Red (*Key Player Problem*)

Modelamiento topológico basado en el protocolo de **percolación dirigida adaptativa** (Borgatti, 2006): evalúa cómo se fragmenta la Componente Gigante (`LCC`) de la red de corrupción al neutralizar secuencialmente los actores con mayor centralidad de intermediación recalculada en cada paso.

---

## 1. Curva de Degradación de la Componente Gigante (`LCC %`)

```mermaid
xychart-beta
  title "Caída del Tamaño de la Componente Gigante (LCC %) tras Remoción Dirigida"
  x-axis ["Paso 0", "Paso 1", "Paso 2", "Paso 3", "Paso 4", "Paso 5", "Paso 6"]
  y-axis "Porcentaje de la Red Conectada (%)" 0 --> 100
  line [90.6, 80.7, 74.0, 58.3, 54.3, 53.8, 53.4]
  bar [90.6, 80.7, 74.0, 58.3, 54.3, 53.8, 53.4]
```

---

## 2. Secuencia Óptima de Neutralización de Nodos Puente

| Paso ($k$) | Nodo Neutralizado / Removido | Tipo de Actor | Islas Resultantes (Componentes) | Nodos en Mayor Componente (`LCC`) | Cohesión Residual (`LCC %`) |
| :---: | :--- | :--- | :---: | :---: | ---: |
| **0** | Estado Inicial (Sin remoción) | `—` | **13** | 202 de 223 | **90.6%** |
| **1** | [[Servicio Impuestos Internos]] | `entidad_publica` | **16** | 180 de 223 | **80.7%** |
| **2** | [[Corte Suprema de Chile]] | `entidad_publica` | **20** | 165 de 223 | **74.0%** |
| **3** | [[Union Democrata Independiente]] | `partido_politico` | **23** | 130 de 223 | **58.3%** |
| **4** | [[Renovacion Nacional]] | `partido_politico` | **25** | 121 de 223 | **54.3%** |
| **5** | [[Sebastian Pinera Echenique]] | `persona` | **25** | 120 de 223 | **53.8%** |
| **6** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **25** | 119 de 223 | **53.4%** |
