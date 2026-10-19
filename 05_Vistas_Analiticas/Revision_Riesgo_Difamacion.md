---
tipo_nodo: vista_analitica
tags:
  - vista/revision-legal
---

# Revisión Preliminar de Riesgo de Difamación

> Este archivo lo genera `make screen` (triaje con un modelo local de Ollama). Cada hallazgo es una señal para revisar contra las fuentes, no un dictamen.

## Revisión editorial del 2026-10-19
Se ejecutaron dos pasadas del triaje sobre todo el vault (226 notas):

- **Primera pasada:** 193 hallazgos. Se corrigieron 43 frases que afirmaban como probados hechos sin sentencia, contradecían la situación procesal o usaban calificativos sin base judicial; el resto se descartó como falso positivo.
- **Segunda pasada:** 189 hallazgos, de los cuales 110 ya estaban revisados. Se corrigieron 13 frases más.

Las correcciones quedaron registradas en el campo `historial_correcciones` de cada nota. Para obtener un listado actualizado, ejecuta `make screen`.
