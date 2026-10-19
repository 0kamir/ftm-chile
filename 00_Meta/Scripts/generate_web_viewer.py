#!/usr/bin/env python3
"""
Generador del Visor Web Interactivo Autónomo (HTML5 + Canvas Force-Directed Graph).
Lee `05_Vistas_Analiticas/Exportaciones/metricas_red.json` y compila un dashboard web
autocontenido (`05_Vistas_Analiticas/Exportaciones/visor_red.html`) con soporte para:
- Inspección de Grafo Local a Profundidad 1 y 2 (`Depth = 1`, `Depth = 2`)
- Filtro por tipo de nodo y buscador en tiempo real
- Ficha lateral con RUT, flujos emitidos/recibidos en CLP y conexiones directas
"""

import json
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
JSON_PATH = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json"
)
HTML_OUT = os.path.join(
    ROOT_DIR, "05_Vistas_Analiticas", "Exportaciones", "visor_red.html"
)


def main() -> int:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    embedded_json = json.dumps(graph_data, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Visor de la Red FTM-Chile</title>
  <style>
    :root {{
      --bg: #0f172a;
      --panel: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --muted: #94a3b8;
      --accent: #38bdf8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, -apple-system, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }}
    #sidebar {{
      width: 380px; background: var(--panel); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; padding: 18px; gap: 14px; overflow-y: auto;
    }}
    h1 {{ font-size: 1.05rem; font-weight: 700; color: var(--accent); line-height: 1.35; }}
    .kpi-box {{
      background: #0f172a; border: 1px solid var(--border); border-radius: 8px; padding: 12px;
      display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
    }}
    .kpi-full {{ grid-column: 1 / -1; border-top: 1px solid var(--border); padding-top: 8px; }}
    .kpi-label {{ font-size: 0.72rem; color: var(--muted); text-transform: uppercase; }}
    .kpi-val {{ font-size: 1.05rem; font-weight: 700; color: #facc15; margin-top: 2px; }}
    label {{ font-size: 0.78rem; color: var(--muted); display: block; margin-bottom: 4px; }}
    input, select, button {{
      width: 100%; padding: 8px 10px; border-radius: 6px; border: 1px solid var(--border);
      background: #0f172a; color: var(--text); font-size: 0.85rem;
    }}
    button {{
      background: #0284c7; border-color: #0369a1; cursor: pointer; font-weight: 600;
      transition: background 0.15s;
    }}
    button:hover {{ background: #0369a1; }}
    .legend {{ display: flex; flex-wrap: wrap; gap: 6px; font-size: 0.75rem; }}
    .badge {{ padding: 3px 8px; border-radius: 999px; font-weight: 600; color: #fff; }}
    #details {{
      background: #0f172a; border: 1px solid var(--border); border-radius: 8px;
      padding: 12px; font-size: 0.83rem; line-height: 1.5; flex: 1; overflow-y: auto;
    }}
    #canvas-wrap {{ flex: 1; position: relative; }}
    canvas {{ display: block; width: 100%; height: 100%; cursor: grab; }}
    canvas:active {{ cursor: grabbing; }}
  </style>
</head>
<body>
  <div id="sidebar">
    <h1>Visor de Redes Reificadas (Aleph / ICIJ)</h1>
    <div class="kpi-box">
      <div>
        <div class="kpi-label">Nodos Registrados</div>
        <div class="kpi-val" id="kpi-nodes">0</div>
      </div>
      <div>
        <div class="kpi-label">Aristas Dirigidas</div>
        <div class="kpi-val" id="kpi-edges">0</div>
      </div>
      <div class="kpi-full">
        <div class="kpi-label">Monto Global Investigado</div>
        <div class="kpi-val" id="kpi-clp">$0 CLP</div>
      </div>
    </div>

    <div>
      <label for="search">Buscar Entidad / Persona / Transacción</label>
      <input id="search" type="text" placeholder="Ej: ProCultura, Hermosilla, Democracia Viva..." />
    </div>

    <div>
      <label for="depth">Modo de Navegación (Local Graph Depth)</label>
      <select id="depth">
        <option value="all">Grafo Global Completo</option>
        <option value="1">Grafo Local — Profundidad 1 (Directos)</option>
        <option value="2" selected>Grafo Local — Profundidad 2 (Estándar)</option>
      </select>
    </div>

    <button id="btn-reset">Restablecer Vista Global</button>

    <div class="legend">
      <span class="badge" style="background:#2563eb">Persona</span>
      <span class="badge" style="background:#16a34a">Ent. Pública</span>
      <span class="badge" style="background:#ea580c">Ent. Privada</span>
      <span class="badge" style="background:#9333ea">Partido</span>
      <span class="badge" style="background:#dc2626">Nexo TRX</span>
      <span class="badge" style="background:#ca8a04">Causa</span>
      <span class="badge" style="background:#64748b">Evidencia / Delito</span>
    </div>

    <div id="details">
      <strong>Haz clic en cualquier nodo del grafo</strong> para inspeccionar su vecindad a Profundidad 2, su RUT y sus flujos financieros asociados.
    </div>
  </div>

  <div id="canvas-wrap">
    <canvas id="graph"></canvas>
  </div>

  <script>
    const DATA = {embedded_json};
    const COLORS = {{
      persona: "#2563eb",
      entidad_publica: "#16a34a",
      entidad_privada: "#ea580c",
      partido_politico: "#9333ea",
      nexo_transaccion: "#dc2626",
      causa_judicial: "#ca8a04",
      evidencia_documental: "#64748b",
      tipo_penal: "#be123c",
      vista_analitica: "#0d9488",
      meta_taxonomia: "#475569"
    }};

    const fmtClp = new Intl.NumberFormat("es-CL", {{ style: "currency", currency: "CLP", maximumFractionDigits: 0 }});
    document.getElementById("kpi-nodes").textContent = DATA.resumen.total_nodos;
    document.getElementById("kpi-edges").textContent = DATA.resumen.total_aristas;
    document.getElementById("kpi-clp").textContent = fmtClp.format(DATA.resumen.monto_total_clp) + " CLP";

    const canvas = document.getElementById("graph");
    const ctx = canvas.getContext("2d");
    let width = canvas.width = canvas.parentElement.clientWidth;
    let height = canvas.height = canvas.parentElement.clientHeight;

    window.addEventListener("resize", () => {{
      width = canvas.width = canvas.parentElement.clientWidth;
      height = canvas.height = canvas.parentElement.clientHeight;
    }});

    const nodeMap = new Map();
    const nodes = DATA.nodos
      .filter(n => n.tipo_nodo !== "vista_analitica" && n.tipo_nodo !== "meta_taxonomia")
      .map((n, idx, arr) => {{
        const angle = (2 * Math.PI * idx) / arr.length;
        const r = Math.min(width, height) * 0.34;
        const obj = {{
          ...n,
          x: width / 2 + r * Math.cos(angle),
          y: height / 2 + r * Math.sin(angle),
          vx: 0,
          vy: 0,
          radius: n.tipo_nodo === "nexo_transaccion" ? 11 : (n.tipo_nodo === "causa_judicial" ? 14 : 10)
        }};
        nodeMap.set(n.id, obj);
        return obj;
      }});

    const edges = DATA.aristas
      .filter(e => nodeMap.has(e.source) && nodeMap.has(e.target))
      .map(e => ({{
        ...e,
        sourceNode: nodeMap.get(e.source),
        targetNode: nodeMap.get(e.target)
      }}));

    let selectedNode = nodeMap.get("Fundacion ProCultura") || nodes[0];
    let depthMode = document.getElementById("depth").value;
    let searchQuery = "";

    function getVisibleSet() {{
      if (depthMode === "all" || !selectedNode) {{
        return new Set(nodes.map(n => n.id));
      }}
      const maxHops = Number(depthMode);
      const visited = new Set([selectedNode.id]);
      let frontier = [selectedNode.id];
      for (let hop = 0; hop < maxHops; hop++) {{
        const next = [];
        for (const u of frontier) {{
          for (const e of edges) {{
            if (e.source === u && !visited.has(e.target)) {{
              visited.add(e.target);
              next.push(e.target);
            }} else if (e.target === u && !visited.has(e.source)) {{
              visited.add(e.source);
              next.push(e.source);
            }}
          }}
        }}
        frontier = next;
      }}
      return visited;
    }}

    function esc(t) {{
      return String(t ?? "").replace(/[&<>"']/g, c => ({{"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}})[c]);
    }}

    function fuentesHtml(node) {{
      const fuentes = (node.fuentes || []).filter(f => String(f.url).startsWith("http://") || String(f.url).startsWith("https://"));
      if (!fuentes.length) return `<div style="color:#94a3b8">Sin fuentes registradas en esta nota.</div>`;
      return `<ul style="padding-left:16px;margin-top:4px">` + fuentes.map(f =>
        `<li><a href="${{esc(f.url)}}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8">${{esc(f.titulo || f.url)}}</a>` +
        `<div style="color:#94a3b8;font-size:0.8rem">${{esc(f.medio)}}${{f.tipo ? " · " + esc(f.tipo) : ""}}${{f.fecha ? " · " + esc(f.fecha) : ""}}</div></li>`
      ).join("") + `</ul>`;
    }}

    function updateDetails(node) {{
      if (!node) return;
      const connected = edges.filter(e => e.source === node.id || e.target === node.id);
      const listHtml = connected.map(e => {{
        const other = e.source === node.id ? e.target : e.source;
        const dir = e.source === node.id ? "→" : "←";
        return `<li><code>${{e.relation}}</code> ${{dir}} <strong>${{other}}</strong></li>`;
      }}).join("");

      document.getElementById("details").innerHTML = `
        <div style="font-size:0.98rem;font-weight:700;color:#38bdf8;margin-bottom:6px">${{node.id}}</div>
        <div><strong>Tipo:</strong> <code>${{node.tipo_nodo}}</code></div>
        ${{node.rut ? `<div><strong>RUT / RUC:</strong> ${{node.rut}}</div>` : ""}}
        ${{node.monto_clp > 0 ? `<div><strong>Monto Transacción:</strong> ${{fmtClp.format(node.monto_clp)}}</div>` : ""}}
        ${{node.flujo_emitido_clp > 0 ? `<div><strong>Flujo Autorizado/Emitido:</strong> ${{fmtClp.format(node.flujo_emitido_clp)}}</div>` : ""}}
        ${{node.flujo_recibido_clp > 0 ? `<div><strong>Flujo Recibido/Suscrito:</strong> ${{fmtClp.format(node.flujo_recibido_clp)}}</div>` : ""}}
        ${{node.situacion_procesal ? `<div><strong>Situación procesal:</strong> ${{esc(node.situacion_procesal)}}</div>` : ""}}
        ${{node.monto_origen ? `<div><strong>Origen del monto:</strong> <code>${{esc(node.monto_origen)}}</code></div>` : ""}}
        ${{node.estado_verificacion ? `<div><strong>Verificación:</strong> <code>${{esc(node.estado_verificacion)}}</code></div>` : ""}}
        <hr style="border-color:#334155;margin:8px 0"/>
        <div><strong>Fuentes (${{(node.fuentes || []).length}}):</strong></div>
        ${{fuentesHtml(node)}}
        <hr style="border-color:#334155;margin:8px 0"/>
        <div><strong>Conexiones directas (${{connected.length}}):</strong></div>
        <ul style="padding-left:16px;margin-top:4px">${{listHtml}}</ul>
      `;
    }}

    updateDetails(selectedNode);

    function stepPhysics() {{
      const visible = getVisibleSet();
      const visNodes = nodes.filter(n => visible.has(n.id));
      for (let i = 0; i < visNodes.length; i++) {{
        for (let j = i + 1; j < visNodes.length; j++) {{
          const a = visNodes[i], b = visNodes[j];
          let dx = b.x - a.x, dy = b.y - a.y;
          let dist = Math.sqrt(dx * dx + dy * dy) || 1;
          let rep = 2200 / (dist * dist);
          let fx = (dx / dist) * rep, fy = (dy / dist) * rep;
          a.vx -= fx; a.vy -= fy;
          b.vx += fx; b.vy += fy;
        }}
      }}
      for (const e of edges) {{
        if (!visible.has(e.source) || !visible.has(e.target)) continue;
        const a = e.sourceNode, b = e.targetNode;
        let dx = b.x - a.x, dy = b.y - a.y;
        let dist = Math.sqrt(dx * dx + dy * dy) || 1;
        let force = (dist - 135) * 0.018;
        let fx = (dx / dist) * force, fy = (dy / dist) * force;
        a.vx += fx; a.vy += fy;
        b.vx -= fx; b.vy -= fy;
      }}
      for (const n of visNodes) {{
        n.vx += (width / 2 - n.x) * 0.004;
        n.vy += (height / 2 - n.y) * 0.004;
        n.vx *= 0.82; n.vy *= 0.82;
        n.x = Math.max(40, Math.min(width - 40, n.x + n.vx));
        n.y = Math.max(40, Math.min(height - 40, n.y + n.vy));
      }}
    }}

    function draw() {{
      stepPhysics();
      ctx.clearRect(0, 0, width, height);
      const visible = getVisibleSet();

      for (const e of edges) {{
        if (!visible.has(e.source) || !visible.has(e.target)) continue;
        const a = e.sourceNode, b = e.targetNode;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 1.4;
        ctx.stroke();
      }}

      for (const n of nodes) {{
        if (!visible.has(n.id)) continue;
        const matchesSearch = searchQuery && n.id.toLowerCase().includes(searchQuery);
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.radius + (selectedNode === n ? 4 : 0), 0, Math.PI * 2);
        ctx.fillStyle = COLORS[n.tipo_nodo] || "#38bdf8";
        ctx.fill();
        ctx.lineWidth = (selectedNode === n || matchesSearch) ? 3 : 1.5;
        ctx.strokeStyle = matchesSearch ? "#facc15" : (selectedNode === n ? "#fff" : "#0f172a");
        ctx.stroke();

        ctx.fillStyle = "#e2e8f0";
        ctx.font = selectedNode === n ? "bold 11px sans-serif" : "10px sans-serif";
        ctx.fillText(n.id, n.x + n.radius + 5, n.y + 3);
      }}
      requestAnimationFrame(draw);
    }}

    canvas.addEventListener("click", (ev) => {{
      const rect = canvas.getBoundingClientRect();
      const mx = ev.clientX - rect.left, my = ev.clientY - rect.top;
      const visible = getVisibleSet();
      for (const n of nodes) {{
        if (!visible.has(n.id)) continue;
        const dx = mx - n.x, dy = my - n.y;
        if (Math.sqrt(dx * dx + dy * dy) <= n.radius + 6) {{
          selectedNode = n;
          updateDetails(n);
          break;
        }}
      }}
    }});

    document.getElementById("depth").addEventListener("change", (ev) => {{
      depthMode = ev.target.value;
    }});

    document.getElementById("search").addEventListener("input", (ev) => {{
      searchQuery = ev.target.value.trim().toLowerCase();
      if (searchQuery) {{
        const found = nodes.find(n => n.id.toLowerCase().includes(searchQuery));
        if (found) {{
          selectedNode = found;
          updateDetails(found);
        }}
      }}
    }});

    document.getElementById("btn-reset").addEventListener("click", () => {{
      document.getElementById("depth").value = "all";
      depthMode = "all";
    }});

    draw();
  </script>
</body>
</html>
"""
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(
        f"[OK] Visor Web generado: {os.path.relpath(HTML_OUT, ROOT_DIR)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
