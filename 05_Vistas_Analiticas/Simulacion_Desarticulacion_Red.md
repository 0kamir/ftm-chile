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
  line [84.7, 77.8, 65.3, 58.8, 58.3, 53.7, 53.2]
  bar [84.7, 77.8, 65.3, 58.8, 58.3, 53.7, 53.2]
```

---

## 2. Secuencia Óptima de Neutralización de Nodos Puente

| Paso ($k$) | Nodo Neutralizado / Removido | Tipo de Actor | Islas Resultantes (Componentes) | Nodos en Mayor Componente (`LCC`) | Cohesión Residual (`LCC %`) |
| :---: | :--- | :--- | :---: | :---: | ---: |
| **0** | Estado Inicial (Sin remoción) | `—` | **18** | 183 de 216 | **84.7%** |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **22** | 168 de 216 | **77.8%** |
| **2** | [[Union Democrata Independiente]] | `partido_politico` | **24** | 141 de 216 | **65.3%** |
| **3** | [[Servicio Impuestos Internos]] | `entidad_publica` | **27** | 127 de 216 | **58.8%** |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **27** | 126 de 216 | **58.3%** |
| **5** | [[Renovacion Nacional]] | `partido_politico` | **30** | 116 de 216 | **53.7%** |
| **6** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **30** | 115 de 216 | **53.2%** |
