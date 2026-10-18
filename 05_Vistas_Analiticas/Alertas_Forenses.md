---
tipo_nodo: vista_analitica
titulo: "Sistema de Detección de Banderas Rojas (Red Flags Forenses)"
actualizacion_automatica: true
tags:
  - dashboard
  - alertas-forenses
  - osint
---

# Detector de Banderas Rojas (Red Flags Forenses)

Motor de reglas heurísticas en `DataviewJS` que cruza en tiempo real las propiedades de **Personas**, **Entidades Privadas**, **Entidades Públicas** y **Nexos Transaccionales (`03_Hechos_y_Nexos/`)** para detectar patrones atípicos de corrupción pública.

---

## 🚩 Alerta 1: Fraccionamiento Administrativo (Evasión de Toma de Razón CGR — Umbral 5.000 UTM)
Detecta pares `(entidad_origen → entidad_destino)` con **múltiples convenios individuales bajo 5.000 UTM (~$301.550.000 CLP)** cuya **suma acumulada supera las 5.000 UTM**, patrón típico de elusión del control preventivo de legalidad de la Contraloría General de la República.

```dataviewjs
const UTM_REF_2022 = 60310;
const UMBRAL_UTM = 5000;
const UMBRAL_CLP = UTM_REF_2022 * UMBRAL_UTM;

const nexos = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.tipo_nexo === "convenio_directo");

const pares = {};
for (let n of nexos) {
  const orig = String(n.entidad_origen || "");
  const dest = String(n.entidad_destino || "");
  const key = `${orig} ===> ${dest}`;
  if (!pares[key]) {
    pares[key] = { origen: n.entidad_origen, destino: n.entidad_destino, items: [], totalClp: 0 };
  }
  pares[key].items.push(n);
  pares[key].totalClp += Number(n.monto_clp || 0);
}

const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });
const filas = [];

for (let k of Object.keys(pares)) {
  const g = pares[k];
  const todosBajoUmbral = g.items.every(i => Number(i.monto_clp || 0) < UMBRAL_CLP);
  if (g.items.length >= 2 && todosBajoUmbral && g.totalClp >= UMBRAL_CLP) {
    const utmAcum = Math.round(g.totalClp / UTM_REF_2022);
    filas.push([
      g.origen,
      g.destino,
      g.items.length,
      fmt.format(g.totalClp),
      `${utmAcum.toLocaleString('es-CL')} UTM (> 5.000 UTM)`,
      g.items.map(i => i.file.link).join(", ")
    ]);
  }
}

if (filas.length === 0) {
  dv.paragraph("✅ *Sin alertas de fraccionamiento bajo umbral de Toma de Razón.*");
} else {
  dv.paragraph(`⚠️ **ALERTA CRÍTICA CGR: Se detectó fraccionamiento en ${filas.length} relación(es) contractual(es):**`);
  dv.table(
    ["Entidad Pública", "Entidad Receptora", "N° Cuotas", "Monto Acumulado", "Equivalencia UTM", "Convenios Fraccionados"],
    filas
  );
}
```

---

## 🚩 Alerta 2: Lobby Pre-Adjudicación (Audiencia Ley N° 20.730 seguida de Trato Directo en < 90 días)
Cruza todos los nexos de tipo `reunion_lobby` con los convenios o transferencias posteriores para detectar cuando un lobbista o entidad privada se adjudica recursos públicos a menos de 90 días de haberse reunido con la autoridad.

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const reuniones = nexos.where(p => p.tipo_nexo === "reunion_lobby");
const pagos = nexos.where(p => p.tipo_nexo === "convenio_directo" || p.tipo_nexo === "transferencia");
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });
const hallazgos = [];

for (let r of reuniones) {
  const rActores = new Set([
    String(r.entidad_origen), String(r.entidad_destino),
    String(r.firmante_origen), String(r.firmante_destino)
  ]);
  const fechaLobby = new Date(String(r.fecha));

  for (let p of pagos) {
    const fechaPago = new Date(String(p.fecha));
    const dias = Math.round((fechaPago - fechaLobby) / (1000 * 60 * 60 * 24));
    if (dias >= 0 && dias <= 90) {
      if (rActores.has(String(p.entidad_origen)) && rActores.has(String(p.entidad_destino))) {
        hallazgos.push([
          r.file.link,
          String(r.fecha),
          p.file.link,
          String(p.fecha),
          `${dias} días`,
          fmt.format(Number(p.monto_clp || 0)),
          p.entidad_destino
        ]);
      }
    }
  }
}

if (hallazgos.length === 0) {
  dv.paragraph("✅ *Sin alertas de lobby pre-adjudicación en ventana de 90 días.*");
} else {
  dv.paragraph(`⚠️ **Se detectaron ${hallazgos.length} adjudicación(es) precedidas por audiencia de lobby en menos de 90 días:**`);
  dv.table(
    ["Audiencia Lobby", "Fecha Lobby", "Convenio Adjudicado", "Fecha Convenio", "Ventana", "Monto Adjudicado", "Beneficiario"],
    hallazgos
  );
}
```

---

## 🚩 Alerta 3: Endogamia Partidaria / Conflicto de Interés Político
Detecta transacciones donde el **Firmante Público (`firmante_origen`)** y el **Firmante Receptor (`firmante_destino`)** comparten la misma **afiliación política** (excluyendo independientes).

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const alertas = [];

const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });

for (let nexo of nexos) {
  const fOrigen = nexo.firmante_origen ? dv.page(nexo.firmante_origen.path) : null;
  const fDestino = nexo.firmante_destino ? dv.page(nexo.firmante_destino.path) : null;

  if (fOrigen && fDestino && fOrigen.file.path !== fDestino.file.path) {
    const partOrigen = String(fOrigen.afiliacion_politica || "").trim();
    const partDestino = String(fDestino.afiliacion_politica || "").trim();

    if (
      partOrigen !== "" &&
      partOrigen === partDestino &&
      !partOrigen.toLowerCase().includes("independiente")
    ) {
      alertas.push([
        nexo.file.link,
        nexo.fecha,
        fOrigen.file.link,
        fDestino.file.link,
        partOrigen,
        fmt.format(Number(nexo.monto_clp || 0)),
        nexo.causa_vinculada
      ]);
    }
  }
}

if (alertas.length === 0) {
  dv.paragraph("✅ *Sin alertas de coincidencia partidaria detectadas.*");
} else {
  dv.paragraph(`⚠️ **Se detectaron ${alertas.length} operación(es) con coincidencia de militancia política entre autorizador y receptor:**`);
  dv.table(
    ["Nexo", "Fecha", "Firmante Origen", "Firmante Destino", "Partido Común", "Monto (CLP)", "Causa"],
    alertas
  );
}
```

---

## 🚩 Alerta 4: Entidades Receptoras de Constitución Reciente (< 365 días)
Detecta convenios o transferencias adjudicadas a **Entidades Privadas (`01_Entidades/Privadas/`)** cuya `fecha_constitucion` sea inferior a 1 año (365 días) respecto de la `fecha` de la transacción.

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const alertas = [];
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });

for (let nexo of nexos) {
  const entDestino = nexo.entidad_destino ? dv.page(nexo.entidad_destino.path) : null;
  if (entDestino && entDestino.fecha_constitucion && nexo.fecha) {
    const fechaTrx = new Date(String(nexo.fecha));
    const fechaConst = new Date(String(entDestino.fecha_constitucion));
    const diffDias = Math.round((fechaTrx - fechaConst) / (1000 * 60 * 60 * 24));

    if (!isNaN(diffDias) && diffDias >= 0 && diffDias < 365) {
      alertas.push([
        nexo.file.link,
        entDestino.file.link,
        String(entDestino.fecha_constitucion),
        String(nexo.fecha),
        `${diffDias} días`,
        fmt.format(Number(nexo.monto_clp || 0)),
        nexo.causa_vinculada
      ]);
    }
  }
}

if (alertas.length === 0) {
  dv.paragraph("✅ *Sin alertas de constitución societaria reciente.*");
} else {
  dv.paragraph(`⚠️ **Se detectaron ${alertas.length} transferencia(s) a entidades con menos de 1 año de antigüedad:**`);
  dv.table(
    ["Nexo", "Entidad Receptora", "Constitución", "Fecha Traspaso", "Antigüedad al Traspaso", "Monto (CLP)", "Causa"],
    alertas
  );
}
```

---

## 🚩 Alerta 5: Nodos Puente Multirregionales (Entidades con Múltiples Órganos Financiadores)
Identifica fundaciones o empresas privadas que reciben recursos desde **2 o más órganos públicos distintos**, actuando como conectores interregionales.

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => Number(p.monto_clp || 0) > 0);
const porReceptor = {};

for (let n of nexos) {
  const dest = String(n.entidad_destino || "");
  const orig = String(n.entidad_origen || "");
  if (!dest || dest === orig) continue;
  if (!porReceptor[dest]) {
    porReceptor[dest] = { link: n.entidad_destino, origenes: new Set(), nexos: [], total: 0 };
  }
  porReceptor[dest].origenes.add(orig);
  porReceptor[dest].nexos.push(n.file.link);
  porReceptor[dest].total += Number(n.monto_clp || 0);
}

const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });
const puentes = Object.values(porReceptor).filter(r => r.origenes.size >= 2);

if (puentes.length === 0) {
  dv.paragraph("✅ *Sin nodos puente multirregionales detectados.*");
} else {
  dv.table(
    ["Entidad Puente", "N° Órganos Públicos", "Reparticiones Conectadas", "Monto Consolidado", "Nexos"],
    puentes.map(p => [
      p.link,
      p.origenes.size,
      Array.from(p.origenes).join(" / "),
      fmt.format(p.total),
      p.nexos.join(", ")
    ])
  );
}
```
