#!/usr/bin/env python3
"""
Motor de Detección de Anomalías, Cálculo de UTM, Índice de Concentración HHI,
Centralidad de Intermediación (Brandes), PageRank y Generador de Reporte Ejecutivo Markdown.

Ejecución:
  python3 00_Meta/Scripts/indicators_report.py
Genera:
  05_Vistas_Analiticas/Reporte_Automatico_de_Indicadores.md
"""

from collections import defaultdict, deque
import os
import re
import yaml
from descargo import descargo  # noqa: E402

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_REPORT = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Reporte_Automatico_de_Indicadores.md"
)

UTM_HISTORICA = {
    "2010-08": 37267,
    "2016-11": 46091,
    "2020-12": 51029,
    "2021-04": 51592,
    "2022-09": 59595,
    "2022-10": 60310,
    "2022-11": 60853,
    "2022-12": 61157,
    "2023-02": 61954,
    "2023-06": 63263,
}
DEFAULT_UTM = 60853
UMBRAL_TOMA_RAZON_UTM = 5000


def clean_link(val) -> str:
    if val is None:
        return ""
    m = re.search(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", str(val))
    return m.group(1).strip() if m else str(val).strip()


def fmt_clp(amount: int) -> str:
    return "$" + f"{int(amount):,}".replace(",", ".")


def compute_betweenness(adj: dict[str, set[str]]) -> dict[str, float]:
    """Algoritmo de Brandes sobre grafo no dirigido subyacente para detectar nodos puente."""
    vertices = list(adj.keys())
    cb = {v: 0.0 for v in vertices}
    for s in vertices:
        stack = []
        pred = {w: [] for w in vertices}
        sigma = {t: 0.0 for t in vertices}
        sigma[s] = 1.0
        dist = {t: -1 for t in vertices}
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = {v: 0.0 for v in vertices}
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                cb[w] += delta[w]

    n = len(vertices)
    scale = 1.0 / ((n - 1) * (n - 2)) if n > 2 else 1.0
    return {k: round(v * scale, 4) for k, v in cb.items()}


def compute_pagerank(adj: dict[str, set[str]], damping: float = 0.85, iterations: int = 40) -> dict[str, float]:
    """Algoritmo PageRank iterativo sobre la red."""
    nodes = list(adj.keys())
    n = len(nodes)
    if n == 0:
        return {}
    pr = {v: 1.0 / n for v in nodes}
    for _ in range(iterations):
        new_pr = {}
        for v in nodes:
            rank_sum = 0.0
            for u in adj[v]:
                deg = len(adj[u])
                if deg > 0:
                    rank_sum += pr[u] / deg
            new_pr[v] = (1.0 - damping) / n + damping * rank_sum
        pr = new_pr
    return {k: round(v, 4) for k, v in pr.items()}


def compute_hhi_by_origin(nexos: list[dict]) -> list[dict]:
    """
    Calcula el Índice de Herfindahl-Hirschman (HHI, escala 0 a 10.000) de concentración
    de asignaciones por cada órgano público emisor.
    """
    por_origen = defaultdict(lambda: defaultdict(int))
    for nx in nexos:
        if nx["monto_clp"] > 0:
            por_origen[nx["entidad_origen"]][nx["entidad_destino"]] += nx["monto_clp"]

    resultados = []
    for orig, destinos in por_origen.items():
        total = sum(destinos.values())
        if total <= 0:
            continue
        hhi = sum(((monto / total) * 100.0) ** 2 for monto in destinos.values())
        nivel = (
            "Alta Concentración (> 2.500)"
            if hhi >= 2500
            else "Concentración Moderada"
        )
        resultados.append(
            {
                "origen": orig,
                "num_receptores": len(destinos),
                "total_clp": total,
                "hhi": round(hhi),
                "nivel": nivel,
            }
        )
    return sorted(resultados, key=lambda r: r["total_clp"], reverse=True)


def main() -> int:
    notes = {}
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        # 06_Anexos queda fuera del grafo y de los análisis (menciones documentales sin imputación).
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "06_Anexos"]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fname), ROOT_DIR)
            if rel == "README.md" or rel.startswith("00_Meta/Plantillas/"):
                continue
            name = os.path.splitext(fname)[0]
            with open(os.path.join(dirpath, fname), "r", encoding="utf-8") as f:
                txt = f.read()
            m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
            if not m:
                continue
            meta = yaml.safe_load(m.group(1)) or {}
            notes[name] = meta

    nexos = []
    undirected_adj: dict[str, set[str]] = defaultdict(set)

    for name, meta in sorted(notes.items()):
        if meta.get("tipo_nodo") == "nexo_transaccion":
            fecha_str = str(meta.get("fecha", ""))
            ym = fecha_str[:7]
            utm_val = UTM_HISTORICA.get(ym, DEFAULT_UTM)
            monto = int(meta.get("monto_clp", 0))
            utm_equiv = round(monto / utm_val, 1)

            e_orig = clean_link(meta.get("entidad_origen"))
            e_dest = clean_link(meta.get("entidad_destino"))
            f_orig = clean_link(meta.get("firmante_origen"))
            f_dest = clean_link(meta.get("firmante_destino"))
            causa = clean_link(meta.get("causa_vinculada"))
            delito = clean_link(meta.get("delito_imputado"))

            for u, v in [
                (e_orig, name),
                (name, e_dest),
                (f_orig, name),
                (name, f_dest),
                (e_orig, f_orig),
                (e_dest, f_dest),
            ]:
                if u and v and u != v:
                    undirected_adj[u].add(v)
                    undirected_adj[v].add(u)

            nexos.append(
                {
                    "id": name,
                    "fecha": fecha_str,
                    "tipo_nexo": meta.get("tipo_nexo"),
                    "monto_clp": monto,
                    "utm": utm_equiv,
                    "entidad_origen": e_orig,
                    "entidad_destino": e_dest,
                    "firmante_origen": f_orig,
                    "firmante_destino": f_dest,
                    "causa": causa,
                    "delito": delito,
                }
            )

    # 1. Detectar Fraccionamiento bajo 5.000 UTM
    grupos_par = defaultdict(list)
    for nx in nexos:
        if nx["tipo_nexo"] == "convenio_directo":
            grupos_par[(nx["entidad_origen"], nx["entidad_destino"])].append(nx)

    alertas_fraccionamiento = []
    for (orig, dest), lista in grupos_par.items():
        total_utm = round(sum(x["utm"] for x in lista), 1)
        total_clp = sum(x["monto_clp"] for x in lista)
        indiv_bajo = all(x["utm"] < UMBRAL_TOMA_RAZON_UTM for x in lista)
        if len(lista) >= 2 and indiv_bajo and total_utm >= UMBRAL_TOMA_RAZON_UTM:
            alertas_fraccionamiento.append(
                {
                    "origen": orig,
                    "destino": dest,
                    "cuotas": len(lista),
                    "total_clp": total_clp,
                    "total_utm": total_utm,
                    "ids": [x["id"] for x in lista],
                }
            )

    # 2. Calcular Betweenness Centrality, PageRank y HHI
    betweenness = compute_betweenness(undirected_adj)
    pagerank = compute_pagerank(undirected_adj)
    top_puentes = sorted(
        [
            (
                node,
                score,
                pagerank.get(node, 0.0),
                notes.get(node, {}).get("tipo_nodo", "entidad"),
            )
            for node, score in betweenness.items()
            if not node.startswith("TRX-")
        ],
        key=lambda x: (x[1], x[2]),
        reverse=True,
    )[:10]

    hhi_table = compute_hhi_by_origin(nexos)

    total_global_clp = sum(x["monto_clp"] for x in nexos)
    total_global_utm = round(sum(x["utm"] for x in nexos), 1)

    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Reporte de Revisión Automatizada (UTM, HHI, PageRank, Brandes y Topología)"',
        "actualizacion_automatica: true",
        "tags:",
        "  - dashboard",
        "  - auditoria-cgr",
        "  - topologia",
        "---",
        "",
        "# Reporte Automático de Indicadores (montos, umbrales y centralidad)",
        "",
        *descargo("indicadores"),
        "",
        f"- **Monto Global Investigado**: **{fmt_clp(total_global_clp)} CLP** (Equivalente a **{total_global_utm:,.1f} UTM**)".replace(
            ",", "."
        ),
        f"- **Total de Aristas Reificadas (`TRX`)**: **{len(nexos)}**",
        f"- **Casos de Fraccionamiento bajo 5.000 UTM detectados**: **{len(alertas_fraccionamiento)}**",
        "",
        "---",
        "",
        "## 1. Diagrama Topológico de Flujos Financieros Reificados (Mermaid)",
        "",
        "```mermaid",
        "flowchart LR",
        '  classDef pub fill:#1b5e20,stroke:#81c784,color:#fff,stroke-width:2px;',
        '  classDef priv fill:#e65100,stroke:#ffb74d,color:#fff,stroke-width:2px;',
        '  classDef trx fill:#b71c1c,stroke:#ef9a9a,color:#fff,stroke-width:1.5px;',
        '  classDef pers fill:#0d47a1,stroke:#64b5f6,color:#fff,stroke-width:1.5px;',
    ]

    node_ids_map = {}

    def mid(label: str) -> str:
        if label not in node_ids_map:
            node_ids_map[label] = "N" + str(len(node_ids_map) + 1)
        return node_ids_map[label]

    for nx in nexos:
        o_id = mid(nx["entidad_origen"])
        d_id = mid(nx["entidad_destino"])
        t_id = mid(nx["id"])
        fo_id = mid(nx["firmante_origen"])
        fd_id = mid(nx["firmante_destino"])

        lines.append(
            f'  {o_id}["{nx["entidad_origen"]}"]:::pub --> {t_id}("{nx["id"]}<br/>{fmt_clp(nx["monto_clp"])}"):::trx'
        )
        lines.append(
            f'  {t_id} --> {d_id}["{nx["entidad_destino"]}"]:::priv'
        )
        lines.append(
            f'  {fo_id}(["{nx["firmante_origen"]}"]):::pers -. "autoriza" .-> {t_id}'
        )
        lines.append(
            f'  {t_id} -. "suscribe" .-> {fd_id}(["{nx["firmante_destino"]}"]):::pers'
        )

    lines.extend(
        [
            "```",
            "",
            "---",
            "",
            "## 2. Detección de Fraccionamiento Administrativo (Umbral Toma de Razón: 5.000 UTM)",
            "",
            "| Órgano Público | Entidad Receptora | N° Cuotas | Suma Acumulada (CLP) | Suma en UTM | Aristas Fraccionadas |",
            "| :--- | :--- | :---: | ---: | ---: | :--- |",
        ]
    )

    for af in alertas_fraccionamiento:
        enlaces = ", ".join(f"[[{i}]]" for i in af["ids"])
        lines.append(
            f"| [[{af['origen']}]] | [[{af['destino']}]] | {af['cuotas']} | **{fmt_clp(af['total_clp'])}** | **{af['total_utm']} UTM** | {enlaces} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 3. Índice de Concentración de Herfindahl-Hirschman (`HHI`) por Entidad Emisora",
            "",
            "| Entidad Emisora | N° Receptores | Monto Total Emitido (CLP) | Índice HHI (0–10.000) | Diagnóstico de Concentración |",
            "| :--- | :---: | ---: | ---: | :--- |",
        ]
    )

    for h in hhi_table:
        lines.append(
            f"| [[{h['origen']}]] | {h['num_receptores']} | {fmt_clp(h['total_clp'])} | **{h['hhi']}** | {h['nivel']} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 4. Ranking de Nodos Puente (*Betweenness Centrality* & *PageRank*)",
            "",
            "| Posición | Nodo / Entidad | Tipo de Nodo | Intermediación (Brandes) | PageRank | Rol Topológico |",
            "| :---: | :--- | :--- | ---: | ---: | :--- |",
        ]
    )

    for idx, (node, b_score, pr_score, t_nodo) in enumerate(top_puentes, 1):
        rol = (
            "Conector Interregional / Puente Crítico"
            if b_score >= 0.03
            else "Articulador de Subgrafo"
        )
        lines.append(
            f"| {idx} | [[{node}]] | `{t_nodo}` | `{b_score:.4f}` | `{pr_score:.4f}` | {rol} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 5. Desglose de Aristas Reificadas en Pesos Chilenos (CLP) y UTM",
            "",
            "| Nexo (`TRX`) | Fecha | Tipo | Origen | Destino | Monto (CLP) | Equivalencia (UTM) | Toma de Razón Individual |",
            "| :--- | :---: | :---: | :--- | :--- | ---: | ---: | :---: |",
        ]
    )

    for nx in sorted(nexos, key=lambda x: x["fecha"]):
        estado_tr = (
            "Exento (< 5.000 UTM)"
            if nx["utm"] < UMBRAL_TOMA_RAZON_UTM
            else "Afecto (>= 5.000 UTM)"
        )
        lines.append(
            f"| [[{nx['id']}]] | {nx['fecha']} | `{nx['tipo_nexo']}` | [[{nx['entidad_origen']}]] | [[{nx['entidad_destino']}]] | {fmt_clp(nx['monto_clp'])} | {nx['utm']} UTM | {estado_tr} |"
        )

    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[OK] Reporte generado: {os.path.relpath(OUT_REPORT, ROOT_DIR)}")
    print(f"     Fraccionamientos CGR detectados: {len(alertas_fraccionamiento)}")
    print(f"     Nodo con mayor intermediación  : {top_puentes[0][0]} (score={top_puentes[0][1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
