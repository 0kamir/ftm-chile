---
tipo_nodo: vista_analitica
titulo: "Simulación de Percolación y Fragmentación de Nodos Clave (Key Player Problem)"
actualizacion_automatica: true
tags:
  - dashboard
  - percolacion
  - robustez-red
---

# Robustez de la Red ante la Eliminación de Nodos (*Key Player Problem*)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.
>
> La simulación elimina nodos del grafo para medir su conectividad. Es un ejercicio matemático y no describe ni sugiere acciones sobre personas reales.


Modelamiento topológico basado en el protocolo de **percolación dirigida adaptativa** (Borgatti, 2006): evalúa cómo se fragmenta la Componente Gigante (`LCC`) de la red al eliminar secuencialmente los actores con mayor centralidad de intermediación recalculada en cada paso.

---

## 1. Curva de Degradación de la Componente Gigante (`LCC %`)

```mermaid
xychart-beta
  title "Caída del Tamaño de la Componente Gigante (LCC %) tras Remoción Dirigida"
  x-axis ["Paso 0", "Paso 1", "Paso 2", "Paso 3", "Paso 4", "Paso 5", "Paso 6"]
  y-axis "Porcentaje de la Red Conectada (%)" 0 --> 100
  line [86.6, 78.3, 66.1, 59.9, 59.6, 52.3, 49.8]
  bar [86.6, 78.3, 66.1, 59.9, 59.6, 52.3, 49.8]
```

---

## 2. Secuencia de Eliminación de Nodos Puente

| Paso ($k$) | Nodo Eliminado | Tipo de Actor | Islas Resultantes (Componentes) | Nodos en Mayor Componente (`LCC`) | Cohesión Residual (`LCC %`) |
| :---: | :--- | :--- | :---: | :---: | ---: |
| **0** | Estado Inicial (Sin remoción) | `—` | **20** | 240 de 277 | **86.6%** |
| **1** | [[Union Democrata Independiente]] | `partido_politico` | **23** | 217 de 277 | **78.3%** |
| **2** | [[Corte Suprema de Chile]] | `entidad_publica` | **25** | 183 de 277 | **66.1%** |
| **3** | [[Servicio Impuestos Internos]] | `entidad_publica` | **29** | 166 de 277 | **59.9%** |
| **4** | [[Sebastian Pinera Echenique]] | `persona` | **29** | 165 de 277 | **59.6%** |
| **5** | [[Renovacion Nacional]] | `partido_politico` | **33** | 145 de 277 | **52.3%** |
| **6** | [[Unidad de Analisis Financiero]] | `entidad_publica` | **35** | 138 de 277 | **49.8%** |
