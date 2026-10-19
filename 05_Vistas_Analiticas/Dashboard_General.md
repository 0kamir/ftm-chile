---
tipo_nodo: vista_analitica
titulo: "Dashboard General de Auditoría Forense y Redes de Corrupción"
actualizacion_automatica: true
tags:
  - dashboard
  - analisis-forense
  - osint
---

# Dashboard General Forense — Auditoría de Casos de Corrupción en Chile

Panel central de inteligencia de fuentes abiertas (OSINT) y contabilidad forense basado en **aristas reificadas** (modelo inspirado en *FollowTheMoney* de OCCRP Aleph e ICIJ Offshore Leaks).

> **Suite de Vistas Analíticas (`05_Vistas_Analiticas/`)**:
> - [[Alertas_Forenses]] — 5 detectores de Banderas Rojas (Fraccionamiento CGR `< 5.000 UTM`, Lobby Pre-Adjudicación `< 90 días`, Endogamia Partidaria, Constitución Reciente `< 365 días` y Nodos Puente).
> - [[Reporte_Auditoria_Automatizada]] — Conversión a UTM históricas, Índice de Concentración `HHI`, PageRank Forense, Centralidad de Brandes y Diagrama Mermaid.
> - [[Indice_Riesgo_Forense]] — Scoring de exposición `0–100 pts` por sujeto y Proyección Bipartita `Persona ↔ Persona`.
> - [[Prediccion_Vinculos_Ocultos]] — Estimadores topológicos **Adamic-Adar ($AA$)** y **Jaccard ($J$)** para inferir asociaciones estructurales indirectas.
> - [[Deteccion_Comunidades_Operativas]] — Partición de células operativas vía **Modularidad de Newman-Girvan ($Q$)** y **Coeficiente de Participación ($P_i$)** de Guimerà-Amaral.
> - [[Analisis_Flujo_Financiero_y_Corte_Minimo]] — Red de flujo capacitado (**Edmonds-Karp Max-Flow / Min-Cut**), curva de interdicción patrimonial y **Coeficiente de Gini**.
> - [[Nucleos_KCore_y_Asortatividad]] — Descomposición **$k$-Core / Onion Layers**, **Asortatividad de Grado de Newman ($r$)** y **Agujeros Estructurales de Burt ($C_i$)**.
> - [[Analisis_Espectral_y_Fiedler]] — Diagonalización de **Laplaciana ($L = D - A$)**, **Valor y Bisección de Fiedler ($\lambda_2, v_2$)** y **Autovector de Perron-Frobenius ($\rho(A)$)**.
> - [[Evolucion_Temporal_y_Transicion_de_Fase]] — Dinámica acumulada **$G(t)$**, **Criterio de Percolación de Molloy-Reed ($\kappa(t)$)** y **Ráfagas de Goh-Barabási ($B$)**.
> - [[Censo_Triadico_y_Motivos_Superiores]] — Clausura triádica ($\Delta$), **Lazos Fuertes de Simmel** y **Cuadrángulos Multi-Canal ($C_4$)**.
> - [[Resistencia_Efectiva_y_Tiempos_de_Impacto]] — Pseudoinversa de Moore-Penrose ($L^+$), **Índice de Kirchhoff ($\Omega_{uv}$)** y **Constante de Kemeny ($K(G)$)**.
> - [[Redes_Parentesco_y_Clanes_Familiares]] — Capa multiplex de parentesco (`vinculos_familiares`), **Clanes Dinásticos** (Piñera–Chadwick, Pinochet–Hiriart–Ponce Lerou, Lavín–Barriga) y atajos geodésicos ($\Delta d$).
> - [[Menciones de Chilenos en Archivos Epstein]] — Anexo documental fuera del grafo: menciones reportadas por la prensa, sin imputación.
> - [[Auditoria_Benford_y_Montos]] — Test estadístico de Ley de Benford y detección de montos redondos discrecionales (`$10M CLP`).
> - [[Simulacion_Desarticulacion_Red]] — Simulación de percolación dirigida (*Key Player Problem*) y fragmentación de la red.
> - [[Matriz_Partidos_y_Regiones]] — Distribución del perjuicio fiscal por Partido Político y por Región.
> - [[Linea_de_Tiempo]] — Reconstrucción cronológica secuencial de constituciones societarias y desembolsos.

---

## 1. Cuantificación Global del Perjuicio Fiscal Investigado (DataviewJS)

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');

let montoGlobalClp = 0;
let conteoNexos = 0;
const porCausa = {};

for (let nexo of nexos) {
  const monto = Number(nexo.monto_clp || 0);
  montoGlobalClp += monto;
  conteoNexos += 1;

  const causaKey = nexo.causa_vinculada ? String(nexo.causa_vinculada) : "Sin causa asignada";
  porCausa[causaKey] = (porCausa[causaKey] || 0) + monto;
}

const clpFormatter = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
});

dv.header(3, `Monto Global Acumulado en el Vault: ${clpFormatter.format(montoGlobalClp)} CLP`);
dv.paragraph(`Total consolidado a partir de **${conteoNexos}** hecho(s)/nexo(s) transaccional(es) en \`03_Hechos_y_Nexos/\`.`);

const filasCausas = Object.entries(porCausa)
  .sort((a, b) => b[1] - a[1])
  .map(([causa, subtotal]) => [
    causa,
    clpFormatter.format(subtotal)
  ]);

if (filasCausas.length > 0) {
  dv.table(["Causa Judicial", "Subtotal Investigado (CLP)"], filasCausas);
}
```

---

## 2. Matriz General de Hechos y Nexos Reificados (Dataview TABLE)

```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / ID",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo Nexo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
SORT fecha DESC
```

---

## 3. Personas con Situación Procesal Activa y Medidas Cautelares

### 3.1 Tabla Procesal Detallada
```dataview
TABLE WITHOUT ID
  file.link AS "Persona Imputada",
  rut AS "RUT",
  rol_principal AS "Rol / Cargo",
  afiliacion_politica AS "Afiliación Política",
  situacion_procesal AS "Situación Procesal",
  medida_cautelar AS "Medida Cautelar / Condena Activa"
FROM "01_Entidades/Personas"
WHERE (situacion_procesal != "ninguna" AND situacion_procesal != "") OR (medida_cautelar != "" AND medida_cautelar != null)
SORT file.name ASC
```

### 3.2 Listado Rápido de Control Cautelar y Condenas
```dataview
LIST
  "**Situación:** " + situacion_procesal + " | **Cautelar/Condena:** " + medida_cautelar + " (" + afiliacion_politica + ")"
FROM "01_Entidades/Personas"
WHERE (situacion_procesal = "formalizado" OR situacion_procesal = "condenado") OR (medida_cautelar != "" AND medida_cautelar != null)
SORT file.name ASC
```

---

## 4. Directorio de Causas Penales Monitoreadas

```dataview
TABLE WITHOUT ID
  file.link AS "Causa",
  ruc AS "RUC",
  año_inicio AS "Año Inicio",
  tribunal_o_fiscalia AS "Fiscalía / Tribunal",
  fiscal_a_cargo AS "Fiscal / Ministro a Cargo",
  estado_judicial AS "Estado Judicial",
  delito_principal AS "Delito Principal"
FROM "02_Causas"
SORT año_inicio DESC
```
