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
  line [86.2, 79.4, 67.0, 59.2, 54.6, 54.1, 53.7]
  bar [86.2, 79.4, 67.0, 59.2, 54.6, 54.1, 53.7]
```

---

## 2. Secuencia Óptima de Neutralización de Nodos Puente

| Paso ($k$) | Nodo Neutralizado / Removido | Tipo de Actor | Islas Resultantes (Componentes) | Nodos en Mayor Componente (`LCC`) | Cohesión Residual (`LCC %`) |
| :---: | :--- | :--- | :---: | :---: | ---: |
| **0** | Estado Inicial (Sin remoción) | `—` | **17** | 188 de 218 | **86.2%** |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **21** | 173 de 218 | **79.4%** |
| **2** | [[Union Democrata Independiente]] | `partido_politico` | **23** | 146 de 218 | **67.0%** |
| **3** | [[Servicio Impuestos Internos]] | `entidad_publica` | **26** | 129 de 218 | **59.2%** |
| **4** | [[Renovacion Nacional]] | `partido_politico` | **29** | 119 de 218 | **54.6%** |
| **5** | [[Sebastian Pinera Echenique]] | `persona` | **29** | 118 de 218 | **54.1%** |
| **6** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **29** | 117 de 218 | **53.7%** |
