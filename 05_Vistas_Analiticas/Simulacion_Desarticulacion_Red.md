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
  line [83.9, 79.6, 66.8, 60.2, 59.7, 55.0, 54.5]
  bar [83.9, 79.6, 66.8, 60.2, 59.7, 55.0, 54.5]
```

---

## 2. Secuencia Óptima de Neutralización de Nodos Puente

| Paso ($k$) | Nodo Neutralizado / Removido | Tipo de Actor | Islas Resultantes (Componentes) | Nodos en Mayor Componente (`LCC`) | Cohesión Residual (`LCC %`) |
| :---: | :--- | :--- | :---: | :---: | ---: |
| **0** | Estado Inicial (Sin remoción) | `—` | **19** | 177 de 211 | **83.9%** |
| **1** | [[Corte Suprema de Chile]] | `entidad_publica` | **20** | 168 de 211 | **79.6%** |
| **2** | [[Union Democrata Independiente]] | `partido_politico` | **22** | 141 de 211 | **66.8%** |
| **3** | [[Servicio Impuestos Internos]] | `entidad_publica` | **25** | 127 de 211 | **60.2%** |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **25** | 126 de 211 | **59.7%** |
| **5** | [[Renovacion Nacional]] | `partido_politico` | **28** | 116 de 211 | **55.0%** |
| **6** | [[Bancard Inversiones Ltda]] | `entidad_privada` | **28** | 115 de 211 | **54.5%** |
