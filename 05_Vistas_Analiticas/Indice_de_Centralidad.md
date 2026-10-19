---
tipo_nodo: vista_analitica
titulo: "Índice de Centralidad (0–100) y Proyección Bipartita Persona–Persona"
actualizacion_automatica: true
tags:
  - dashboard
  - centralidad
  - proyeccion-bipartita
  - osint
---

# Índice de Centralidad y Coaparición en Hechos

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.
>
> El puntaje mide cuán conectada está una persona en el grafo del vault (cantidad de hechos y causas en que aparece), no su responsabilidad: una persona absuelta o mencionada como testigo también puede tener un puntaje alto.


Vista analítica avanzada en `DataviewJS` que calcula un **puntaje de centralidad (`0–100 puntos`)** por cada persona registrada y proyecta el grafo bipartito `Persona ↔ Nexo TRX ↔ Persona` en una **matriz de vínculos directos entre operadores**.

---

## 1. Centralidad de cada Persona en el Grafo (`Score 0–100`)

El modelo pondera cuatro factores objetivos:
1. **Gravedad Procesal (hasta 30 pts)**: `formalizado`/`condenado` (+30 pts), `testigo` (+10 pts).
2. **Cuantía Operada Acumulada (hasta 30 pts)**: `>= $1.000M CLP` (+30 pts), `>= $400M CLP` (+25 pts), `>= $100M CLP` (+15 pts).
3. **Reiteración de Operaciones (hasta 20 pts)**: `>= 3 nexos` (+20 pts), `2 nexos` (+15 pts), `1 nexo` (+8 pts).
4. **Alcance Multirregional o Multi-Institucional (hasta 20 pts)**: Conecta `>= 2` reparticiones públicas o poderes del Estado (+20 pts).

```dataviewjs
const personas = dv.pages('"01_Entidades/Personas"');
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });

const ranking = [];

for (let p of personas) {
  const misNexos = nexos.where(n =>
    (n.firmante_origen && n.firmante_origen.path === p.file.path) ||
    (n.firmante_destino && n.firmante_destino.path === p.file.path)
  );

  let montoTotal = 0;
  const entidadesTocadas = new Set();

  for (let n of misNexos) {
    montoTotal += Number(n.monto_clp || 0);
    if (n.entidad_origen) entidadesTocadas.add(String(n.entidad_origen));
    if (n.entidad_destino) entidadesTocadas.add(String(n.entidad_destino));
  }

  let score = 0;
  // 1. Situación procesal
  const sit = String(p.situacion_procesal || "").toLowerCase();
  if (sit === "formalizado" || sit === "condenado") score += 30;
  else if (sit === "testigo") score += 10;

  // 2. Cuantía
  if (montoTotal >= 1000000000) score += 30;
  else if (montoTotal >= 400000000) score += 25;
  else if (montoTotal >= 100000000) score += 15;
  else if (montoTotal > 0) score += 5;

  // 3. Reiteración
  if (misNexos.length >= 3) score += 20;
  else if (misNexos.length === 2) score += 15;
  else if (misNexos.length === 1) score += 8;

  // 4. Alcance multi-institucional
  if (entidadesTocadas.size >= 3) score += 20;
  else if (entidadesTocadas.size === 2) score += 12;

  const nivel = score >= 80 ? "🔴 CRÍTICO" : (score >= 60 ? "🟠 ALTO" : "🟡 MEDIO");

  ranking.push({
    link: p.file.link,
    rol: p.rol_principal,
    partido: p.afiliacion_politica,
    situacion: p.situacion_procesal,
    numNexos: misNexos.length,
    monto: montoTotal,
    score: score,
    nivel: nivel
  });
}

ranking.sort((a, b) => b.score - a.score || b.monto - a.monto);

dv.table(
  ["Persona", "Score (0–100)", "Nivel de Centralidad", "Situación Procesal", "N° Nexos", "Flujo Vinculado (CLP)", "Partido"],
  ranking.map(r => [
    r.link,
    `**${r.score} / 100**`,
    r.nivel,
    r.situacion,
    r.numNexos,
    fmt.format(r.monto),
    r.partido
  ])
);
```

---

## 2. Proyección Bipartita Persona ↔ Persona (Pares de coaparición Directa)

Colapsa los nodos intermedios `03_Hechos_y_Nexos/` para revelar qué pares de personas naturales han actuado como contrapartes directas (`firmante_origen ↔ firmante_destino`), cuántas veces han operado juntas y el monto consolidado entre ambas.

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });
const pares = {};

for (let n of nexos) {
  const fo = String(n.firmante_origen || "");
  const fd = String(n.firmante_destino || "");
  if (!fo || !fd || fo === fd) continue;

  const key = `${fo} <===> ${fd}`;
  if (!pares[key]) {
    pares[key] = {
      origen: n.firmante_origen,
      destino: n.firmante_destino,
      count: 0,
      totalClp: 0,
      tipos: new Set(),
      causa: n.causa_vinculada
    };
  }
  pares[key].count += 1;
  pares[key].totalClp += Number(n.monto_clp || 0);
  pares[key].tipos.add(String(n.tipo_nexo));
}

const filasPares = Object.values(pares)
  .sort((a, b) => b.totalClp - a.totalClp || b.count - a.count)
  .map(p => [
    p.origen,
    p.destino,
    p.count,
    Array.from(p.tipos).join(", "),
    fmt.format(p.totalClp),
    p.causa
  ]);

dv.table(
  ["Operador / Firmante Origen", "Contraparte / Firmante Destino", "N° Operaciones Conjuntas", "Modalidades", "Monto Consolidado (CLP)", "Causa"],
  filasPares
);
```
