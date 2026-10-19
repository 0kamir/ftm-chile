---
tipo_nodo: vista_analitica
titulo: "Matriz de Auditoría por Partido Político y Distribución Regional"
actualizacion_automatica: true
tags:
  - dashboard
  - partidos-politicos
  - regiones
  - osint
---

# Matriz por Partido Político y Distribución Territorial

Análisis multidimensional en `DataviewJS` que cruza las aristas reificadas (`03_Hechos_y_Nexos/`) con la **militancia partidaria** de los firmantes (`01_Entidades/Partidos/`) y la **jurisdicción regional** de los órganos públicos (`01_Entidades/Publicas/`).

---

## 1. Exposición Financiera por Afiliación Política del Autorizador (`firmante_origen`)

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const porPartido = {};
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });

for (let n of nexos) {
  const monto = Number(n.monto_clp || 0);
  const fOrig = n.firmante_origen ? dv.page(n.firmante_origen.path) : null;
  const partido = fOrig && fOrig.afiliacion_politica ? String(fOrig.afiliacion_politica) : "No especificado";

  if (!porPartido[partido]) {
    porPartido[partido] = { partido, nexosCount: 0, totalClp: 0, personas: new Set() };
  }
  porPartido[partido].nexosCount += 1;
  porPartido[partido].totalClp += monto;
  if (fOrig) porPartido[partido].personas.add(String(n.firmante_origen));
}

const filas = Object.values(porPartido)
  .sort((a, b) => b.totalClp - a.totalClp)
  .map(r => [
    r.partido,
    Array.from(r.personas).join(", "),
    r.nexosCount,
    fmt.format(r.totalClp)
  ]);

dv.table(
  ["Afiliación Política (Autorizador)", "Autoridades / Operadores", "N° Nexos", "Monto Total Autorizado (CLP)"],
  filas
);
```

---

## 2. Distribución Territorial del Perjuicio Investigado por Región

```dataviewjs
const nexos = dv.pages('"03_Hechos_y_Nexos"');
const porRegion = {};
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });

for (let n of nexos) {
  const monto = Number(n.monto_clp || 0);
  let pub = n.entidad_origen ? dv.page(n.entidad_origen.path) : null;
  if (!pub || pub.tipo_nodo !== "entidad_publica") {
    pub = n.entidad_destino ? dv.page(n.entidad_destino.path) : null;
  }

  const region = (pub && pub.region) ? String(pub.region) : "Sin región asignada";
  const categoria = (pub && pub.categoria) ? String(pub.categoria) : "Otro";

  if (!porRegion[region]) {
    porRegion[region] = { region, categorias: new Set(), organos: new Set(), count: 0, total: 0 };
  }
  porRegion[region].categorias.add(categoria);
  if (pub) porRegion[region].organos.add(String(pub.file.link));
  porRegion[region].count += 1;
  porRegion[region].total += monto;
}

const filasReg = Object.values(porRegion)
  .sort((a, b) => b.total - a.total)
  .map(r => [
    r.region,
    Array.from(r.categorias).join(" / "),
    Array.from(r.organos).join(", "),
    r.count,
    fmt.format(r.total)
  ]);

dv.table(
  ["Región", "Categoría Estatal", "Órganos Públicos Involucrados", "N° Nexos", "Monto Investigado (CLP)"],
  filasReg
);
```

---

## 3. Directorio de Partidos Políticos Registrados

```dataview
TABLE WITHOUT ID
  file.link AS "Partido Político",
  sigla AS "Sigla",
  rut AS "RUT",
  coalicion AS "Coalición / Pacto",
  estado_registro AS "Estado Legal"
FROM "01_Entidades/Partidos"
SORT sigla ASC
```
