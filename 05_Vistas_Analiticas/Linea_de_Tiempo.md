---
tipo_nodo: vista_analitica
titulo: "Línea de Tiempo de Hechos, Transferencias y Evidencias"
actualizacion_automatica: true
tags:
  - dashboard
  - cronologia
  - osint
---

# Línea de Tiempo (Reconstrucción Cronológica de Hechos)

Vista secuencial de todos los actos societarios, resoluciones administrativas, convenios de transferencia y reuniones periciadas en el vault.

---

## 1. Secuencia Cronológica Unificada (Constituciones + Transacciones `TRX`)

```dataviewjs
const eventos = [];
const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 });

// 1. Constituciones de Entidades Privadas
for (let priv of dv.pages('"01_Entidades/Privadas"')) {
  if (priv.fecha_constitucion) {
    eventos.push({
      fecha: String(priv.fecha_constitucion),
      categoria: "🏢 Constitución Societaria",
      nodo: priv.file.link,
      detalle: `Constitución de ${priv.razon_social} (Rep. Legal: ${priv.representante_legal})`,
      monto: "—"
    });
  }
}

// 2. Aristas Reificadas (Transacciones y Hechos)
for (let trx of dv.pages('"03_Hechos_y_Nexos"')) {
  if (trx.fecha) {
    eventos.push({
      fecha: String(trx.fecha),
      categoria: `💸 Nexo (${trx.tipo_nexo})`,
      nodo: trx.file.link,
      detalle: `${trx.entidad_origen} → ${trx.entidad_destino} (${trx.firmante_origen} / ${trx.firmante_destino})`,
      monto: fmt.format(Number(trx.monto_clp || 0))
    });
  }
}

eventos.sort((a, b) => a.fecha.localeCompare(b.fecha));

dv.table(
  ["Fecha", "Tipo de Hito", "Nodo / Registro", "Descripción Relacional", "Monto Involucrado"],
  eventos.map(e => [e.fecha, e.categoria, e.nodo, e.detalle, e.monto])
);
```

---

## 2. Índice Maestro de Vistas Analíticas (MOC)
- [[Dashboard_General]] — Cuantificación global en CLP, matriz general de nexos y control de medidas cautelares.
- [[Senales_para_Revision]] — Detector heurístico de fraccionamiento bajo 5.000 UTM, endogamia partidaria, constitución reciente y nodos puente.
- [[Reporte_Automatico_de_Indicadores]] — Informe técnico generado por `indicators_report.py` con conversión a UTM históricas, ranking de centralidad de intermediación (*Brandes*) y diagrama Mermaid.
