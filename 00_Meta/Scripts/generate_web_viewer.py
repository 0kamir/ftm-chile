#!/usr/bin/env python3
"""
Generador del Visor Web Interactivo Autónomo (HTML5 + Canvas Force-Directed Graph).
Lee `05_Vistas_Analiticas/Exportaciones/metricas_red.json` y compila un dashboard web
autocontenido (`05_Vistas_Analiticas/Exportaciones/visor_red.html`) con soporte para:
- Inspección de Grafo Local a Profundidad 1 y 2 (`Depth = 1`, `Depth = 2`)
- Filtros multicriterio en tiempo real (Tipo de Nodo, Macro-Causa Judicial, Situación Procesal / Origen)
- Trazador interactivo de Camino Más Corto (BFS Shortest Path) iluminado sobre el grafo
- Zoom, Pan y arrastre de nodos en el lienzo HTML5 Canvas
- Ficha lateral con flujos en CLP y UF histórica, conexiones navegables y fuentes URL + Wayback Machine
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Visor de la Red FTM-Chile | OSINT & Grafos Reificados</title>
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
      width: 410px; background: var(--panel); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; padding: 14px 16px; gap: 10px; overflow-y: auto;
    }}
    h1 {{ font-size: 1rem; font-weight: 700; color: var(--accent); line-height: 1.3; }}
    .kpi-box {{
      background: #0f172a; border: 1px solid var(--border); border-radius: 8px; padding: 10px;
      display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px;
    }}
    .kpi-full {{ grid-column: 1 / -1; border-top: 1px solid var(--border); padding-top: 6px; display: flex; justify-content: space-between; align-items: baseline; }}
    .kpi-label {{ font-size: 0.68rem; color: var(--muted); text-transform: uppercase; }}
    .kpi-val {{ font-size: 0.95rem; font-weight: 700; color: #facc15; margin-top: 2px; }}
    .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
    label {{ font-size: 0.72rem; color: var(--muted); display: block; margin-bottom: 3px; }}
    input, select, button {{
      width: 100%; padding: 6px 8px; border-radius: 6px; border: 1px solid var(--border);
      background: #0f172a; color: var(--text); font-size: 0.8rem;
    }}
    button {{
      background: #0284c7; border-color: #0369a1; cursor: pointer; font-weight: 600;
      transition: background 0.15s;
    }}
    button:hover {{ background: #0369a1; }}
    button.secondary {{ background: #334155; border-color: #475569; }}
    button.secondary:hover {{ background: #475569; }}
    .path-box {{
      background: #0f172a; border: 1px solid var(--border); border-radius: 8px; padding: 8px 10px;
      display: flex; flex-direction: column; gap: 6px;
    }}
    .legend {{ display: flex; flex-wrap: wrap; gap: 5px; font-size: 0.7rem; }}
    .badge {{ padding: 2px 7px; border-radius: 999px; font-weight: 600; color: #fff; cursor: pointer; }}
    #details {{
      background: #0f172a; border: 1px solid var(--border); border-radius: 8px;
      padding: 12px; font-size: 0.81rem; line-height: 1.48; flex: 1; overflow-y: auto;
    }}
    #canvas-wrap {{ flex: 1; position: relative; }}
    canvas {{ display: block; width: 100%; height: 100%; cursor: grab; }}
    canvas:active {{ cursor: grabbing; }}
    .canvas-hud {{
      position: absolute; bottom: 14px; right: 14px; background: rgba(15, 23, 42, 0.86);
      border: 1px solid var(--border); border-radius: 8px; padding: 6px 10px;
      font-size: 0.74rem; color: var(--muted); pointer-events: none;
    }}
  </style>
</head>
<body>
  <div id="sidebar">
    <h1>Visor Forense FTM-Chile (Aleph / ICIJ)</h1>
    <div class="kpi-box">
      <div>
        <div class="kpi-label">Nodos</div>
        <div class="kpi-val" id="kpi-nodes">0</div>
      </div>
      <div>
        <div class="kpi-label">Aristas</div>
        <div class="kpi-val" id="kpi-edges">0</div>
      </div>
      <div>
        <div class="kpi-label">Fuentes URL</div>
        <div class="kpi-val" id="kpi-sources" style="color:#38bdf8">0</div>
      </div>
      <div class="kpi-full">
        <div>
          <div class="kpi-label">Flujo Nominal / UF Histórica</div>
          <div class="kpi-val" id="kpi-clp">$0 CLP</div>
        </div>
        <div id="kpi-uf" style="font-size:0.78rem;color:#38bdf8;font-weight:700">0 UF</div>
      </div>
    </div>

    <div>
      <label for="search">Buscar Persona / Entidad / Causa / Transacción</label>
      <input id="search" type="text" list="node-list" placeholder="Ej: ProCultura, Hermosilla, SQM, Caso Convenios..." />
      <datalist id="node-list"></datalist>
    </div>

    <div class="grid-2">
      <div>
        <label for="depth">Modo de Navegación</label>
        <select id="depth">
          <option value="all">Grafo Global Completo</option>
          <option value="1">Local — Profundidad 1</option>
          <option value="2" selected>Local — Profundidad 2</option>
        </select>
      </div>
      <div>
        <label for="type-filter">Filtrar por Tipo de Nodo</label>
        <select id="type-filter">
          <option value="all">Todos los tipos</option>
          <option value="persona">Personas</option>
          <option value="entidad_publica">Entidades Públicas</option>
          <option value="entidad_privada">Entidades Privadas</option>
          <option value="partido_politico">Partidos Políticos</option>
          <option value="nexo_transaccion">Aristas TRX</option>
          <option value="causa_judicial">Causas Judiciales</option>
          <option value="evidencia_documental">Evidencias Primarias</option>
          <option value="tipo_penal">Delitos / Tipos Penales</option>
        </select>
      </div>
    </div>

    <div class="grid-2">
      <div>
        <label for="case-filter">Filtrar por Macro-Causa</label>
        <select id="case-filter">
          <option value="all">Todas las causas (32)</option>
        </select>
      </div>
      <div>
        <label for="status-filter">Situación / Calidad Monto</label>
        <select id="status-filter">
          <option value="all">Todos los estados</option>
          <option value="condenado">Condenado / Sentencia Firme</option>
          <option value="formalizado">Formalizado / Acusado</option>
          <option value="sobreseido">Sobreseído / Absuelto</option>
          <option value="resolucion_administrativa">Resolución Admin. (TDLC/CGR)</option>
        </select>
      </div>
    </div>

    <div class="path-box">
      <div style="font-size:0.74rem;font-weight:700;color:#facc15">Trazador de Camino Más Corto (BFS Shortest Path)</div>
      <div class="grid-2">
        <input id="path-src" type="text" list="node-list" placeholder="Nodo Origen (A)" />
        <input id="path-dst" type="text" list="node-list" placeholder="Nodo Destino (B)" />
      </div>
      <div class="grid-2">
        <button id="btn-path">Trazar Ruta Mínima</button>
        <button id="btn-reset" class="secondary">Restablecer Vista</button>
      </div>
      <div id="path-result" style="font-size:0.75rem;color:#cbd5e1;display:none"></div>
    </div>

    <div class="legend">
      <span class="badge" style="background:#2563eb" onclick="setTypeFilter('persona')">Persona</span>
      <span class="badge" style="background:#16a34a" onclick="setTypeFilter('entidad_publica')">Ent. Pública</span>
      <span class="badge" style="background:#ea580c" onclick="setTypeFilter('entidad_privada')">Ent. Privada</span>
      <span class="badge" style="background:#9333ea" onclick="setTypeFilter('partido_politico')">Partido</span>
      <span class="badge" style="background:#dc2626" onclick="setTypeFilter('nexo_transaccion')">Nexo TRX</span>
      <span class="badge" style="background:#ca8a04" onclick="setTypeFilter('causa_judicial')">Causa</span>
      <span class="badge" style="background:#64748b" onclick="setTypeFilter('evidencia_documental')">Evidencia</span>
      <span class="badge" style="background:#be123c" onclick="setTypeFilter('tipo_penal')">Delito</span>
    </div>

    <div id="details">
      <strong>Haz clic en cualquier nodo del grafo</strong> para inspeccionar su vecindad, sus flujos en CLP/UF y abrir directamente sus fuentes URL verificadas.
    </div>
  </div>

  <div id="canvas-wrap">
    <canvas id="graph"></canvas>
    <div class="canvas-hud">Rueda: Zoom · Arrastrar fondo: Mover · Clic/Arrastrar nodo: Inspeccionar</div>
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
    const fmtUf = new Intl.NumberFormat("es-CL", {{ maximumFractionDigits: 1 }});
    document.getElementById("kpi-nodes").textContent = DATA.resumen.total_nodos;
    document.getElementById("kpi-edges").textContent = DATA.resumen.total_aristas;
    document.getElementById("kpi-sources").textContent = DATA.resumen.total_fuentes_url || 0;
    document.getElementById("kpi-clp").textContent = fmtClp.format(DATA.resumen.monto_total_clp) + " CLP";
    document.getElementById("kpi-uf").textContent = fmtUf.format(DATA.resumen.monto_total_uf || 0) + " UF";

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
      .filter(n => n.tipo_nodo !== "vista_analitica" && n.tipo_nodo !== "meta_taxonomia" && n.tipo_nodo !== "meta_flujo")
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

    const datalist = document.getElementById("node-list");
    nodes.slice().sort((a, b) => a.id.localeCompare(b.id)).forEach(n => {{
      const opt = document.createElement("option");
      opt.value = n.id;
      datalist.appendChild(opt);
    }});

    const caseSelect = document.getElementById("case-filter");
    nodes.filter(n => n.tipo_nodo === "causa_judicial").sort((a, b) => a.id.localeCompare(b.id)).forEach(c => {{
      const opt = document.createElement("option");
      opt.value = c.id;
      opt.textContent = c.id;
      caseSelect.appendChild(opt);
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
    let typeFilter = "all";
    let caseFilter = "all";
    let statusFilter = "all";
    let searchQuery = "";
    let highlightedPath = new Set();

    // Estado de cámara (Zoom / Pan / Drag)
    let camScale = 1;
    let camX = 0;
    let camY = 0;
    let draggingNode = null;
    let isPanning = false;
    let panStartX = 0, panStartY = 0;

    function findShortestPath(srcId, dstId) {{
      if (!nodeMap.has(srcId) || !nodeMap.has(dstId)) return null;
      if (srcId === dstId) return [srcId];
      const queue = [[srcId]];
      const visited = new Set([srcId]);
      while (queue.length > 0) {{
        const path = queue.shift();
        const curr = path[path.length - 1];
        for (const e of edges) {{
          const next = e.source === curr ? e.target : (e.target === curr ? e.source : null);
          if (next && !visited.has(next)) {{
            const newPath = [...path, next];
            if (next === dstId) return newPath;
            visited.add(next);
            queue.push(newPath);
          }}
        }}
      }}
      return null;
    }}

    function matchesFilters(n) {{
      if (typeFilter !== "all" && n.tipo_nodo !== typeFilter) return false;
      if (caseFilter !== "all") {{
        const inCase = n.id === caseFilter || (n.causas || []).includes(caseFilter);
        if (!inCase) return false;
      }}
      if (statusFilter !== "all") {{
        const sp = (n.situacion_procesal || "").toLowerCase();
        const mo = (n.monto_origen || "").toLowerCase();
        if (statusFilter === "condenado" && sp !== "condenado" && mo !== "sentencia") return false;
        if (statusFilter === "formalizado" && sp !== "formalizado" && sp !== "acusado" && mo !== "acusacion") return false;
        if (statusFilter === "sobreseido" && sp !== "sobreseido" && sp !== "absuelto") return false;
        if (statusFilter === "resolucion_administrativa" && mo !== "resolucion_administrativa") return false;
      }}
      return true;
    }}

    function getVisibleSet() {{
      if (highlightedPath.size > 0) {{
        return new Set(highlightedPath);
      }}
      let baseSet;
      if (depthMode === "all" || !selectedNode) {{
        baseSet = new Set(nodes.map(n => n.id));
      }} else {{
        const maxHops = Number(depthMode);
        baseSet = new Set([selectedNode.id]);
        let frontier = [selectedNode.id];
        for (let hop = 0; hop < maxHops; hop++) {{
          const next = [];
          for (const u of frontier) {{
            for (const e of edges) {{
              if (e.source === u && !baseSet.has(e.target)) {{
                baseSet.add(e.target);
                next.push(e.target);
              }} else if (e.target === u && !baseSet.has(e.source)) {{
                baseSet.add(e.source);
                next.push(e.source);
              }}
            }}
          }}
          frontier = next;
        }}
      }}
      const filtered = new Set();
      for (const id of baseSet) {{
        const n = nodeMap.get(id);
        if (n && matchesFilters(n)) filtered.add(id);
      }}
      return filtered;
    }}

    function esc(t) {{
      return String(t ?? "").replace(/[&<>"']/g, c => ({{"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}})[c]);
    }}

    function selectNodeById(id) {{
      const found = nodeMap.get(id);
      if (found) {{
        selectedNode = found;
        updateDetails(found);
      }}
    }}

    function setTypeFilter(t) {{
      const sel = document.getElementById("type-filter");
      sel.value = sel.value === t ? "all" : t;
      typeFilter = sel.value;
      if (typeFilter !== "all") {{
        document.getElementById("depth").value = "all";
        depthMode = "all";
      }}
    }}

    function fuentesHtml(node) {{
      const fuentes = (node.fuentes || []).filter(f => String(f.url).startsWith("http://") || String(f.url).startsWith("https://"));
      if (!fuentes.length) return `<div style="color:#94a3b8">Sin fuentes registradas en esta nota.</div>`;
      return `<div style="display:flex;flex-direction:column;gap:6px;margin-top:6px">` + fuentes.map(f => {{
        const badgeBg = f.tipo === "primaria" ? "#059669" : "#2563eb";
        const archUrl = f.archivo && (String(f.archivo).startsWith("http://") || String(f.archivo).startsWith("https://"))
          ? f.archivo
          : `https://web.archive.org/web/*/${{f.url}}`;
        const archLabel = f.archivo ? "copia archivada ↗" : "Wayback ↺";
        return `<div style="background:#1e293b;border:1px solid #334155;border-radius:6px;padding:7px 9px">` +
          `<a href="${{esc(f.url)}}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8;font-weight:600;text-decoration:none;display:block;line-height:1.35">${{esc(f.titulo || f.url)}} ↗</a>` +
          `<div style="color:#94a3b8;font-size:0.75rem;margin-top:4px;display:flex;flex-wrap:wrap;align-items:center;gap:6px">` +
          `<span style="background:${{badgeBg}};color:#fff;padding:1px 6px;border-radius:4px;font-size:0.67rem;text-transform:uppercase;font-weight:700">${{esc(f.tipo || "fuente")}}</span>` +
          `<span>${{esc(f.medio)}}${{f.fecha ? " · " + esc(f.fecha) : ""}}</span>` +
          `· <a href="${{esc(archUrl)}}" target="_blank" rel="noopener noreferrer" style="color:#a78bfa;text-decoration:underline">${{archLabel}}</a>` +
          `</div></div>`;
      }}).join("") + `</div>`;
    }}

    function updateDetails(node) {{
      if (!node) return;
      const connected = edges.filter(e => e.source === node.id || e.target === node.id);
      const listHtml = connected.map(e => {{
        const other = e.source === node.id ? e.target : e.source;
        const dir = e.source === node.id ? "→" : "←";
        return `<li><code>${{esc(e.relation)}}</code> ${{dir}} <a href="#" onclick="selectNodeById('${{esc(other).replace(/'/g, "\\\\'")}}');return false;" style="color:#f8fafc;font-weight:700;text-decoration:underline">${{esc(other)}}</a></li>`;
      }}).join("");

      const causasHtml = (node.causas && node.causas.length)
        ? `<div><strong>Causas vinculadas:</strong> ` + node.causas.map(c => `<a href="#" onclick="selectNodeById('${{esc(c).replace(/'/g, "\\\\'")}}');return false;" style="color:#facc15">${{esc(c)}}</a>`).join(" · ") + `</div>`
        : "";

      document.getElementById("details").innerHTML = `
        <div style="font-size:0.98rem;font-weight:700;color:#38bdf8;margin-bottom:6px">${{esc(node.id)}}</div>
        <div><strong>Tipo:</strong> <code>${{esc(node.tipo_nodo)}}</code>${{node.fecha ? ` · <strong>Fecha/Año:</strong> ${{esc(node.fecha)}}` : ""}}</div>
        ${{node.rut ? `<div><strong>RUT / RUC:</strong> ${{esc(node.rut)}}</div>` : ""}}
        ${{node.monto_clp > 0 ? `<div><strong>Monto Transacción:</strong> ${{fmtClp.format(node.monto_clp)}} (${{fmtUf.format(node.monto_uf || 0)}} UF)</div>` : ""}}
        ${{node.flujo_emitido_clp > 0 ? `<div><strong>Flujo Autorizado/Emitido:</strong> ${{fmtClp.format(node.flujo_emitido_clp)}} (${{fmtUf.format(node.flujo_emitido_uf || 0)}} UF)</div>` : ""}}
        ${{node.flujo_recibido_clp > 0 ? `<div><strong>Flujo Recibido/Suscrito:</strong> ${{fmtClp.format(node.flujo_recibido_clp)}} (${{fmtUf.format(node.flujo_recibido_uf || 0)}} UF)</div>` : ""}}
        ${{node.situacion_procesal ? `<div><strong>Situación procesal:</strong> <code>${{esc(node.situacion_procesal)}}</code></div>` : ""}}
        ${{node.monto_origen ? `<div><strong>Origen del monto:</strong> <code>${{esc(node.monto_origen)}}</code></div>` : ""}}
        ${{node.estado_verificacion ? `<div><strong>Verificación:</strong> <code>${{esc(node.estado_verificacion)}}</code></div>` : ""}}
        ${{causasHtml}}
        <hr style="border-color:#334155;margin:8px 0"/>
        <div><strong>Fuentes con Link URL (${{(node.fuentes || []).length}}):</strong></div>
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
          if (draggingNode !== a) {{ a.vx -= fx; a.vy -= fy; }}
          if (draggingNode !== b) {{ b.vx += fx; b.vy += fy; }}
        }}
      }}
      for (const e of edges) {{
        if (!visible.has(e.source) || !visible.has(e.target)) continue;
        const a = e.sourceNode, b = e.targetNode;
        let dx = b.x - a.x, dy = b.y - a.y;
        let dist = Math.sqrt(dx * dx + dy * dy) || 1;
        let force = (dist - 135) * 0.018;
        let fx = (dx / dist) * force, fy = (dy / dist) * force;
        if (draggingNode !== a) {{ a.vx += fx; a.vy += fy; }}
        if (draggingNode !== b) {{ b.vx -= fx; b.vy -= fy; }}
      }}
      for (const n of visNodes) {{
        if (draggingNode === n) continue;
        n.vx += (width / 2 - n.x) * 0.004;
        n.vy += (height / 2 - n.y) * 0.004;
        n.vx *= 0.82; n.vy *= 0.82;
        n.x = Math.max(40, Math.min(width - 40, n.x + n.vx));
        n.y = Math.max(40, Math.min(height - 40, n.y + n.vy));
      }}
    }}

    function screenToWorld(sx, sy) {{
      return {{
        x: (sx - camX) / camScale,
        y: (sy - camY) / camScale
      }};
    }}

    function draw() {{
      stepPhysics();
      ctx.clearRect(0, 0, width, height);
      ctx.save();
      ctx.translate(camX, camY);
      ctx.scale(camScale, camScale);

      const visible = getVisibleSet();

      for (const e of edges) {{
        if (!visible.has(e.source) || !visible.has(e.target)) continue;
        const a = e.sourceNode, b = e.targetNode;
        const inPath = highlightedPath.has(e.source) && highlightedPath.has(e.target);
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = inPath ? "#facc15" : "#475569";
        ctx.lineWidth = inPath ? 2.8 : 1.4;
        ctx.stroke();
      }}

      for (const n of nodes) {{
        if (!visible.has(n.id)) continue;
        const matchesSearch = searchQuery && n.id.toLowerCase().includes(searchQuery);
        const inPath = highlightedPath.has(n.id);
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.radius + (selectedNode === n ? 4 : 0), 0, Math.PI * 2);
        ctx.fillStyle = COLORS[n.tipo_nodo] || "#38bdf8";
        ctx.fill();
        ctx.lineWidth = (selectedNode === n || matchesSearch || inPath) ? 3 : 1.5;
        ctx.strokeStyle = (matchesSearch || inPath) ? "#facc15" : (selectedNode === n ? "#fff" : "#0f172a");
        ctx.stroke();

        ctx.fillStyle = "#e2e8f0";
        ctx.font = (selectedNode === n || inPath) ? "bold 11px sans-serif" : "10px sans-serif";
        ctx.fillText(n.id, n.x + n.radius + 5, n.y + 3);
      }}
      ctx.restore();
      requestAnimationFrame(draw);
    }}

    canvas.addEventListener("wheel", (ev) => {{
      ev.preventDefault();
      const rect = canvas.getBoundingClientRect();
      const mx = ev.clientX - rect.left, my = ev.clientY - rect.top;
      const zoom = ev.deltaY < 0 ? 1.12 : 0.89;
      const nextScale = Math.max(0.35, Math.min(3.5, camScale * zoom));
      camX = mx - ((mx - camX) * nextScale) / camScale;
      camY = my - ((my - camY) * nextScale) / camScale;
      camScale = nextScale;
    }}, {{ passive: false }});

    canvas.addEventListener("mousedown", (ev) => {{
      const rect = canvas.getBoundingClientRect();
      const w = screenToWorld(ev.clientX - rect.left, ev.clientY - rect.top);
      const visible = getVisibleSet();
      for (const n of nodes) {{
        if (!visible.has(n.id)) continue;
        const dx = w.x - n.x, dy = w.y - n.y;
        if (Math.sqrt(dx * dx + dy * dy) <= n.radius + 6) {{
          draggingNode = n;
          selectedNode = n;
          updateDetails(n);
          return;
        }}
      }}
      isPanning = true;
      panStartX = ev.clientX - camX;
      panStartY = ev.clientY - camY;
    }});

    window.addEventListener("mousemove", (ev) => {{
      if (draggingNode) {{
        const rect = canvas.getBoundingClientRect();
        const w = screenToWorld(ev.clientX - rect.left, ev.clientY - rect.top);
        draggingNode.x = w.x;
        draggingNode.y = w.y;
        draggingNode.vx = 0;
        draggingNode.vy = 0;
      }} else if (isPanning) {{
        camX = ev.clientX - panStartX;
        camY = ev.clientY - panStartY;
      }}
    }});

    window.addEventListener("mouseup", () => {{
      draggingNode = null;
      isPanning = false;
    }});

    document.getElementById("depth").addEventListener("change", (ev) => {{
      depthMode = ev.target.value;
      highlightedPath.clear();
      document.getElementById("path-result").style.display = "none";
    }});

    document.getElementById("type-filter").addEventListener("change", (ev) => {{
      typeFilter = ev.target.value;
      if (typeFilter !== "all") {{
        document.getElementById("depth").value = "all";
        depthMode = "all";
      }}
    }});

    document.getElementById("case-filter").addEventListener("change", (ev) => {{
      caseFilter = ev.target.value;
      if (caseFilter !== "all") {{
        document.getElementById("depth").value = "all";
        depthMode = "all";
        selectNodeById(caseFilter);
      }}
    }});

    document.getElementById("status-filter").addEventListener("change", (ev) => {{
      statusFilter = ev.target.value;
      if (statusFilter !== "all") {{
        document.getElementById("depth").value = "all";
        depthMode = "all";
      }}
    }});

    document.getElementById("search").addEventListener("input", (ev) => {{
      searchQuery = ev.target.value.trim().toLowerCase();
      if (searchQuery) {{
        const exact = nodeMap.get(ev.target.value.trim());
        const found = exact || nodes.find(n => n.id.toLowerCase().includes(searchQuery));
        if (found) {{
          selectedNode = found;
          updateDetails(found);
        }}
      }}
    }});

    document.getElementById("btn-path").addEventListener("click", () => {{
      const srcVal = document.getElementById("path-src").value.trim();
      const dstVal = document.getElementById("path-dst").value.trim();
      const resBox = document.getElementById("path-result");
      const srcNode = nodeMap.get(srcVal) || nodes.find(n => n.id.toLowerCase().includes(srcVal.toLowerCase()));
      const dstNode = nodeMap.get(dstVal) || nodes.find(n => n.id.toLowerCase().includes(dstVal.toLowerCase()));
      resBox.style.display = "block";
      if (!srcNode || !dstNode) {{
        resBox.innerHTML = `<span style="color:#f87171">Seleccione dos nodos válidos del grafo.</span>`;
        return;
      }}
      const path = findShortestPath(srcNode.id, dstNode.id);
      if (!path) {{
        highlightedPath.clear();
        resBox.innerHTML = `<span style="color:#f87171">No existe ruta conectada entre ambos nodos.</span>`;
        return;
      }}
      highlightedPath = new Set(path);
      selectedNode = srcNode;
      updateDetails(srcNode);
      resBox.innerHTML = `<strong>Ruta (${{path.length - 1}} saltos):</strong> ` +
        path.map(p => `<a href="#" onclick="selectNodeById('${{esc(p).replace(/'/g, "\\\\'")}}');return false;" style="color:#38bdf8">${{esc(p)}}</a>`).join(" → ");
    }});

    document.getElementById("btn-reset").addEventListener("click", () => {{
      document.getElementById("depth").value = "all";
      document.getElementById("type-filter").value = "all";
      document.getElementById("case-filter").value = "all";
      document.getElementById("status-filter").value = "all";
      document.getElementById("search").value = "";
      document.getElementById("path-result").style.display = "none";
      depthMode = "all";
      typeFilter = "all";
      caseFilter = "all";
      statusFilter = "all";
      searchQuery = "";
      highlightedPath.clear();
      camScale = 1; camX = 0; camY = 0;
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
