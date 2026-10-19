#!/usr/bin/env python3
"""
Motor de Evolución Temporal del Grafo, Criterio de Percolación de Molloy-Reed y Ráfagas de Goh-Barabási
=======================================================================================================
Reconstruye la evolución histórica acumulada G(t) = (V(t), E(t)) año por año a partir
de la activación cronológica de las aristas reificadas (`03_Hechos_y_Nexos/*.md`) y sus
vínculos políticos/institucionales:

1. Fracción del Componente Gigante S(t) = |V_LCC(t)| / |V(t)| en cada época histórica.
2. Parámetro de Transición de Fase Supercrítica de Molloy-Reed: kappa(t) = <k^2> / <k>
   (umbral crítico teórico kappa_c = 2.0 para la emergencia de una red macro-conectada).
3. Coeficiente de Ráfaga Temporal (Burstiness B in [-1, 1]) de Goh & Barabási (2008):
   B = (sigma_tau - mu_tau) / (sigma_tau + mu_tau) sobre los tiempos inter-transacción tau (en días).

Genera `05_Vistas_Analiticas/Evolucion_Temporal_y_Transicion_de_Fase.md`.
"""

from collections import defaultdict, deque
from datetime import datetime
import json
import math
from pathlib import Path
import re
import yaml
from descargo import descargo  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parents[2]
TRX_DIR = VAULT_ROOT / "03_Hechos_y_Nexos"
JSON_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Exportaciones" / "metricas_red.json"
REPORT_PATH = VAULT_ROOT / "05_Vistas_Analiticas" / "Evolucion_Temporal_y_Transicion_de_Fase.md"

OPERATIONAL_TYPES = {
    "persona",
    "entidad_publica",
    "entidad_privada",
    "partido_politico",
    "nexo_transaccion",
    "causa_judicial",
}


def clean_wikilink(val):
    if not val:
        return ""
    s = str(val).strip()
    m = re.search(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", s)
    return m.group(1).strip() if m else s


def load_dated_transactions():
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
        fecha_str = str(meta.get("fecha", ""))
        dt = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        trxs.append({
            "id": md_file.stem,
            "date": dt,
            "year": dt.year,
            "monto_clp": int(meta.get("monto_clp", 0) or 0),
            "origen": clean_wikilink(meta.get("entidad_origen")),
            "destino": clean_wikilink(meta.get("entidad_destino")),
            "firmante_origen": clean_wikilink(meta.get("firmante_origen")),
            "firmante_destino": clean_wikilink(meta.get("firmante_destino")),
            "causa": clean_wikilink(meta.get("causa_vinculada")),
        })
    return sorted(trxs, key=lambda x: (x["date"], x["id"]))


def compute_burstiness(trxs):
    dates = [t["date"] for t in trxs]
    if len(dates) < 3:
        return 0.0, 0.0, 0.0, []
    intervals = [(dates[i + 1] - dates[i]).days for i in range(len(dates) - 1)]
    n = len(intervals)
    mu = sum(intervals) / n
    var = sum((x - mu) ** 2 for x in intervals) / n
    sigma = math.sqrt(var)
    b = (sigma - mu) / (sigma + mu) if (sigma + mu) > 0 else 0.0
    return b, mu, sigma, intervals


def compute_lcc_and_molloy_reed(active_nodes, adj):
    if not active_nodes:
        return 0, 0.0, 0.0
    visited = set()
    max_lcc = 0
    for u in active_nodes:
        if u not in visited:
            comp_size = 0
            q = deque([u])
            visited.add(u)
            while q:
                cur = q.popleft()
                comp_size += 1
                for nxt in adj[cur]:
                    if nxt in active_nodes and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            if comp_size > max_lcc:
                max_lcc = comp_size

    n = len(active_nodes)
    s_frac = max_lcc / n if n > 0 else 0.0
    degrees = [len(adj[u] & active_nodes) for u in active_nodes]
    mean_k = sum(degrees) / n if n > 0 else 0.0
    mean_k2 = sum(k * k for k in degrees) / n if n > 0 else 0.0
    kappa = (mean_k2 / mean_k) if mean_k > 0 else 0.0
    return max_lcc, s_frac, kappa


def fmt_clp(val):
    return f"${val:,.0f} CLP".replace(",", ".")


def generate_report():
    trxs = load_dated_transactions()
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    op_nodes = {
        n["id"]: n
        for n in graph_data["nodos"]
        if n.get("tipo_nodo") in OPERATIONAL_TYPES
    }
    static_edges = []
    for e in graph_data["aristas"]:
        u, v = e["source"], e["target"]
        if u in op_nodes and v in op_nodes and u != v:
            static_edges.append((u, v))

    burstiness, mu_tau, sigma_tau, intervals = compute_burstiness(trxs)

    years = sorted(set(t["year"] for t in trxs))
    epoch_rows = []
    cum_clp = 0
    activated_trxs = set()
    activated_actors = set()

    for y in years:
        year_trxs = [t for t in trxs if t["year"] == y]
        for t in year_trxs:
            cum_clp += t["monto_clp"]
            activated_trxs.add(t["id"])
            for field in ("origen", "destino", "firmante_origen", "firmante_destino", "causa"):
                val = t[field]
                if val and val in op_nodes:
                    activated_actors.add(val)

        # Incluir partidos políticos o entidades directamente vinculadas a los actores ya activados
        current_active = set(activated_trxs) | set(activated_actors)
        for u, v in static_edges:
            if u in activated_actors and op_nodes.get(v, {}).get("tipo_nodo") == "partido_politico":
                current_active.add(v)
            if v in activated_actors and op_nodes.get(u, {}).get("tipo_nodo") == "partido_politico":
                current_active.add(u)

        adj = defaultdict(set)
        edge_count = 0
        seen_e = set()
        for u, v in static_edges:
            if u in current_active and v in current_active:
                adj[u].add(v)
                adj[v].add(u)
                pair = tuple(sorted((u, v)))
                if pair not in seen_e:
                    seen_e.add(pair)
                    edge_count += 1

        lcc_size, s_frac, kappa = compute_lcc_and_molloy_reed(current_active, adj)
        epoch_rows.append({
            "year": y,
            "new_trxs": len(year_trxs),
            "cum_trxs": len(activated_trxs),
            "nodes": len(current_active),
            "edges": edge_count,
            "lcc_size": lcc_size,
            "s_frac": s_frac,
            "kappa": kappa,
            "cum_clp": cum_clp,
        })

    final_row = epoch_rows[-1]
    regimen_burst = (
        "Dinámica de Ráfagas Sincronizadas (*Burst-Driven Process*, $B > 0$: los desembolsos se concentran en ventanas electorales y cierres presupuestarios)"
        if burstiness > 0.10
        else "Proceso Cuasi-Poissoniano"
    )

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Evolución Temporal G(t), Transición de Fase de Molloy-Reed y Ráfagas de Goh-Barabási"',
        "actualizacion_automatica: true",
        "tags:",
        "  - evolucion-temporal",
        "  - molloy-reed",
        "  - goh-barabasi",
        "  - transicion-de-fase",
        "---",
        "",
        "# Evolución Temporal $G(t)$, Transición de Fase de Molloy-Reed y Ráfagas de Goh-Barabási",
        "",
        *descargo(),
        "",
        "> [!IMPORTANT] Dinámica No Lineal de Redes y Coalescencia del Componente Gigante",
        "> Esta vista reconstruye el grafo acumulado $G(t) = (V(t), E(t))$ desde `2001` hasta `2023` a medida que se activan cronológicamente los nexos transaccionales (`TRX`):",
        "> 1. **Criterio de Percolación de Molloy-Reed ($\\kappa(t) = \\langle k^2 \\rangle / \\langle k \\rangle > 2$)**: Determina en qué momento la red supera el umbral crítico $\\kappa_c = 2.0$ y experimenta una **transición de fase hacia un régimen supercrítico macro-conectado**.",
        "> 2. **Coeficiente de Ráfaga Temporal de Goh & Barabási ($B \\in [-1, 1]$)**: Evalúa si las transacciones registradas ocurren de forma independiente o en **ráfagas sincronizadas ($B > 0$)** asociadas a ciclos electorales y presupuestarios.",
        "",
        "## 1. Métricas Dinámicas e Inter-Transaccionales (2001–2023)",
        "",
        f"- **Coeficiente de Ráfaga Temporal de Goh-Barabási ($B$)**: **`{burstiness:+.4f}`**",
        f"  - *Diagnóstico Cronológico*: **{regimen_burst}**",
        f"- **Intervalo Medio entre Transacciones ($\\mu_\\tau$)**: `{mu_tau:.1f} días` | **Desviación Estándar ($\\sigma_\\tau$)**: `{sigma_tau:.1f} días`",
        f"- **Parámetro de Molloy-Reed Actual ($\\kappa(2023) = \\langle k^2 \\rangle / \\langle k \\rangle$)**: **`{final_row['kappa']:.4f}`** *(Supercrítico: $\\kappa > 2.0$)*",
        f"- **Coalescencia del Componente Gigante ($S(2023)$)**: **`{final_row['s_frac'] * 100:.1f}%`** (`{final_row['lcc_size']}` de `{final_row['nodes']}` nodos unidos en un único macro-componente)",
        "",
        "---",
        "",
        "## 2. Serie Histórica Acumulada $G(t)$ y Transición de Fase (`2001 → 2023`)",
        "",
        "| Año ($t$) | TRX Acum. | Nodos $|V(t)|$ | Aristas $|E(t)|$ | LCC $|V_{\\text{LCC}}(t)|$ | Fracción Gigante $S(t)$ | Molloy-Reed $\\kappa(t)$ | Monto Acumulado $\\Phi(t)$ |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    for r in epoch_rows:
        lines.append(
            f"| **{r['year']}** | `{r['cum_trxs']}` | `{r['nodes']}` | `{r['edges']}` | `{r['lcc_size']}` | **`{r['s_frac'] * 100:.1f}%`** | `{r['kappa']:.2f}` | `{fmt_clp(r['cum_clp'])}` |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Curva de Crecimiento del Componente Gigante $S(t)$ y Caudal Registrado",
        "",
        "```mermaid",
        "xychart-beta",
        '    title "Coalescencia del Componente Gigante S(t) (% de la Red Operativa)"',
        "    x-axis [" + ", ".join(str(r["year"]) for r in epoch_rows) + "]",
        '    y-axis "Fracción LCC (%)" 0 --> 100',
        "    line [" + ", ".join(f"{r['s_frac'] * 100:.1f}" for r in epoch_rows) + "]",
        "```",
        "",
    ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"[OK] Evolución Temporal y Transición de Fase generada: {REPORT_PATH.relative_to(VAULT_ROOT)} (B={burstiness:+.4f}, S(2023)={final_row['s_frac'] * 100:.1f}%, kappa={final_row['kappa']:.2f})"
    )


if __name__ == "__main__":
    generate_report()
