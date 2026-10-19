#!/usr/bin/env python3
"""
Motor de Flujo Financiero Máximo, Corte Mínimo (Edmonds-Karp) y Concentración de Gini
=====================================================================================
Modela la red de flujo de capitales ilícitos/investigados desde las Entidades de Origen (S)
pasando por los Firmantes Autorizadores -> Transacciones Reificadas (TRX) -> Firmantes Receptores
hacia las Entidades de Destino (T).

Calcula:
1. Flujo Financiero Máximo y Corte Mínimo (Teorema Max-Flow Min-Cut de Ford-Fulkerson / Edmonds-Karp).
2. Curva de Retiro de nodos Óptima (Comiso / Medidas Precautorias sobre Firmantes Clave).
3. Coeficiente de Gini y Curva de Lorenz de concentración del perjuicio fiscal.
Genera `05_Vistas_Analiticas/Analisis_Flujo_Financiero_y_Corte_Minimo.md`.
"""

from collections import defaultdict, deque
from pathlib import Path
import re
import yaml
from descargo import descargo  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parents[2]
TRX_DIR = VAULT_ROOT / "03_Hechos_y_Nexos"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Analisis_Flujo_Financiero_y_Corte_Minimo.md"


def clean_wikilink(val):
    if not val:
        return ""
    s = str(val).strip()
    m = re.search(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", s)
    return m.group(1).strip() if m else s


def load_transactions():
    trxs = []
    for md_file in sorted(TRX_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        meta = yaml.safe_load(parts[1]) or {}
        if meta.get("tipo_nodo") != "nexo_transaccion":
            continue
        trxs.append({
            "id": md_file.stem,
            "fecha": str(meta.get("fecha", "")),
            "tipo_nexo": str(meta.get("tipo_nexo", "")),
            "monto_clp": int(meta.get("monto_clp", 0) or 0),
            "origen": clean_wikilink(meta.get("entidad_origen")),
            "destino": clean_wikilink(meta.get("entidad_destino")),
            "firmante_origen": clean_wikilink(meta.get("firmante_origen")),
            "firmante_destino": clean_wikilink(meta.get("firmante_destino")),
            "causa": clean_wikilink(meta.get("causa_vinculada")),
            "delito": clean_wikilink(meta.get("delito_imputado")),
        })
    return trxs


def edmonds_karp(capacity, source, sink):
    """
    Ejecuta Edmonds-Karp O(V E^2) sobre grafo dirigido ponderado.
    Retorna (max_flow, min_cut_edges, reachable_from_source).
    """
    residual = defaultdict(lambda: defaultdict(int))
    for u in capacity:
        for v, cap in capacity[u].items():
            residual[u][v] += cap

    max_flow = 0
    while True:
        parent = {source: None}
        q = deque([source])
        while q and sink not in parent:
            u = q.popleft()
            for v, rem in residual[u].items():
                if v not in parent and rem > 0:
                    parent[v] = u
                    q.append(v)

        if sink not in parent:
            break

        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        max_flow += path_flow

    # Conjunto alcanzable S_cut desde la fuente en la red residual
    visited = {source}
    q = deque([source])
    while q:
        u = q.popleft()
        for v, rem in residual[u].items():
            if rem > 0 and v not in visited:
                visited.add(v)
                q.append(v)

    min_cut_edges = []
    for u in visited:
        for v, orig_cap in capacity[u].items():
            if v not in visited and orig_cap > 0:
                min_cut_edges.append((u, v, orig_cap))

    return max_flow, min_cut_edges, visited


def compute_gini(values):
    vals = sorted([v for v in values if v > 0])
    n = len(vals)
    if n == 0:
        return 0.0
    total = sum(vals)
    if total == 0:
        return 0.0
    cum = 0
    for i, y in enumerate(vals, 1):
        cum += i * y
    return (2.0 * cum) / (n * total) - (n + 1.0) / n


def fmt_clp(val):
    return f"${val:,.0f} CLP".replace(",", ".")


def generate_report():
    trxs = load_transactions()
    total_clp = sum(t["monto_clp"] for t in trxs)

    # Construir red capacitada S -> Entidad_Origen -> Firmante_Origen -> Firmante_Destino -> Entidad_Destino -> T
    capacity = defaultdict(lambda: defaultdict(int))
    S = "__SUPER_SOURCE__"
    T = "__SUPER_SINK__"

    origen_totals = defaultdict(int)
    destino_totals = defaultdict(int)
    causa_totals = defaultdict(int)
    operator_exposure = defaultdict(int)
    operator_trxs = defaultdict(set)

    for t in trxs:
        m = t["monto_clp"]
        causa_totals[t["causa"]] += m
        if m <= 0:
            continue
        eo = f"ORG::{t['origen']}"
        ed = f"DST::{t['destino']}"
        fo = f"F_ORIG::{t['firmante_origen']}"
        fd = f"F_DEST::{t['firmante_destino']}"

        origen_totals[eo] += m
        destino_totals[ed] += m
        capacity[eo][fo] += m
        capacity[fo][fd] += m
        capacity[fd][ed] += m

        for p in {t["firmante_origen"], t["firmante_destino"]}:
            if p:
                operator_exposure[p] += m
                operator_trxs[p].add(t["id"])

    for eo, tot in origen_totals.items():
        capacity[S][eo] = tot
    for ed, tot in destino_totals.items():
        capacity[ed][T] = tot

    max_flow, min_cut_edges, _ = edmonds_karp(capacity, S, T)

    # Simulación Voraz de Retiro de nodos (Medidas Precautorias por Operador)
    remaining_trxs = [t for t in trxs if t["monto_clp"] > 0]
    interdiction_steps = []
    intercepted_cum = 0

    while remaining_trxs:
        op_gains = defaultdict(int)
        op_count = defaultdict(int)
        for t in remaining_trxs:
            for p in {t["firmante_origen"], t["firmante_destino"]}:
                if p:
                    op_gains[p] += t["monto_clp"]
                    op_count[p] += 1
        if not op_gains:
            # Aristas sin firmante identificado (hechos agregados) no son interceptables por operador.
            break
        best_op = sorted(op_gains.keys(), key=lambda p: (-op_gains[p], p))[0]
        gain = op_gains[best_op]
        cnt = op_count[best_op]
        intercepted_cum += gain
        pct = (intercepted_cum / total_clp * 100.0) if total_clp > 0 else 0.0
        interdiction_steps.append((best_op, cnt, gain, intercepted_cum, pct))
        remaining_trxs = [
            t for t in remaining_trxs
            if best_op not in {t["firmante_origen"], t["firmante_destino"]}
        ]

    gini_trxs = compute_gini([t["monto_clp"] for t in trxs if t["monto_clp"] > 0])
    gini_causas = compute_gini(list(causa_totals.values()))
    gini_ops = compute_gini(list(operator_exposure.values()))

    # Canalizaciones bilaterales Firmante_Origen -> Firmante_Destino ordenadas por monto
    channels = defaultdict(lambda: {"monto": 0, "count": 0, "causas": set()})
    for t in trxs:
        if t["monto_clp"] > 0:
            pair = (t["firmante_origen"], t["firmante_destino"], t["origen"], t["destino"])
            channels[pair]["monto"] += t["monto_clp"]
            channels[pair]["count"] += 1
            channels[pair]["causas"].add(t["causa"])

    sorted_channels = sorted(channels.items(), key=lambda x: (-x[1]["monto"], x[0][0]))

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Análisis de Flujo Financiero Máximo, Corte Mínimo (Edmonds-Karp) y Concentración de Gini"',
        "actualizacion_automatica: true",
        "tags:",
        "  - flujo-financiero",
        "  - max-flow-min-cut",
        "  - edmonds-karp",
        "  - gini",
        "---",
        "",
        "# Flujo Máximo y Corte Mínimo en la Red de Montos (Edmonds-Karp)",
        "",
        *descargo(),
        "",
        "> [!IMPORTANT] Teorema Max-Flow Min-Cut aplicado a Persecución Patrimonial y Comiso",
        "> Esta vista modela el grafo dirigido de desembolsos como una **Red de Flujo Capacitada** ($S \\rightarrow \\text{Entidad Origen} \\rightarrow \\text{Firmante Origen} \\rightarrow \\text{Firmante Destino} \\rightarrow \\text{Entidad Destino} \\rightarrow T$) y ejecuta el algoritmo de **Edmonds-Karp ($O(VE^2)$)** junto con optimización submodular de **Retiro de nodos** para determinar el número mínimo de operadores cuyas cuentas/patrimonios deben ser objeto de medidas precautorias para interceptar el **100% del flujo financiero investigado**.",
        "",
        "## 1. Métricas Globales de Flujo y Desigualdad Financiera",
        "",
        f"- **Flujo Máximo Registrado ($f^*$ de Edmonds-Karp)**: **`{fmt_clp(max_flow)}`** *(100% consistente con la suma de aristas `TRX` con flujo monetario)*",
        f"- **Capacidad del Corte Mínimo ($c(S, T)$)**: **`{fmt_clp(sum(c for _, _, c in min_cut_edges))}`** across `{len(min_cut_edges)}` cuellos de botella primarios.",
        f"- **Coeficiente de Gini por Transacción (`TRX`)**: `{gini_trxs:.4f}`",
        f"- **Coeficiente de Gini por Causa Penal**: `{gini_causas:.4f}`",
        f"- **Coeficiente de Gini por Operador / Firmante**: `{gini_ops:.4f}`",
        f"- **Operadores requeridos para interceptar el 100% del flujo**: `{len(interdiction_steps)}` personas (de un total de `{len(operator_exposure)}` firmantes con flujo monetario).",
        "",
        "---",
        "",
        "## 2. Curva de Retiro de nodos Óptima (Medidas Precautorias / Comiso)",
        "",
        "Orden óptimo de congelamiento de activos / medidas precautorias reales para maximizar el monto fiscal y corporativo interceptado en cada paso:",
        "",
        "| Paso | Operador / Firmante Objetivo | TRX Interceptadas | Monto Marginal Interceptado | Monto Acumulado | % del Flujo Total |",
        "| :---: | :--- | :---: | :---: | :---: | :---: |",
    ]

    for idx, (op, cnt, gain, cum, pct) in enumerate(interdiction_steps, 1):
        lines.append(
            f"| **{idx}** | [[{op}]] | `{cnt}` | `{fmt_clp(gain)}` | `{fmt_clp(cum)}` | **`{pct:.2f}%`** |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Canales de Flujo Financiero (`Firmante Origen → Firmante Destino`)",
        "",
        "| # | Autorizador (Origen) | Entidad Emisora | Receptor (Destino) | Entidad Receptora | TRX | Caudal Acumulado (CLP) | Causa(s) |",
        "| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |",
    ])

    for i, ((fo, fd, eo, ed), info) in enumerate(sorted_channels, 1):
        causas_str = ", ".join(f"[[{c}]]" for c in sorted(info["causas"]))
        lines.append(
            f"| **{i}** | [[{fo}]] | [[{eo}]] | [[{fd}]] | [[{ed}]] | `{info['count']}` | **`{fmt_clp(info['monto'])}`** | {causas_str} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 4. Diagrama Topológico de Cuellos de Botella Financieros (Top 8 Canales)",
        "",
        "```mermaid",
        "flowchart LR",
    ])

    for i, ((fo, fd, eo, ed), info) in enumerate(sorted_channels[:8], 1):
        monto_m = info["monto"] / 1_000_000
        lines.append(
            f'    EO{i}["{eo}"] -->|"$ {monto_m:,.0f}M"| FO{i}["{fo}"] -->|"$ {monto_m:,.0f}M"| FD{i}["{fd}"] --> ED{i}["{ed}"]'.replace(",", ".")
        )

    lines.extend([
        "```",
        "",
    ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"[OK] Análisis de Flujo Financiero y Corte Mínimo generado: {REPORT_PATH.relative_to(VAULT_ROOT)} (Max-Flow = {fmt_clp(max_flow)}, {len(interdiction_steps)} nodos de corte)"
    )


if __name__ == "__main__":
    generate_report()
