#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kinship_and_clans.py
====================
Motor Analítico de Redes de Parentesco, Clanes Familiares y Puentes Dinásticos
(Capa Multiplex `vinculos_familiares` sobre el Grafo de Aristas Reificadas).

Modela formalmente cómo los vínculos de consanguinidad y afinidad (`vinculos_familiares`)
operan como atajos geodésicos (Small-World Shortcuts) que acoplan macro-causas judiciales,
estudios jurídicos de lobby (ej. Caso Audios: Chadwick–Hermosilla–Piñera), privatizaciones
(Clan Pinochet–Hiriart–Ponce Lerou) y gobiernos comunales/corporativos (Clan Lavín–Barriga).

Genera: 05_Vistas_Analiticas/Redes_Parentesco_y_Clanes_Familiares.md
"""

import os
import json
from collections import defaultdict, deque

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
METRICAS_JSON = os.path.join(VAULT_ROOT, "05_Vistas_Analiticas", "Exportaciones", "metricas_red.json")
OUTPUT_MD = os.path.join(VAULT_ROOT, "05_Vistas_Analiticas", "Redes_Parentesco_y_Clanes_Familiares.md")

CLAN_METADATA = {
    frozenset(["Sebastian Pinera Echenique", "Andres Chadwick Pinera"]): {
        "nombre_clan": "Clan Piñera–Chadwick (Eje Ejecutivo–UDI–Alonso de Córdova / Caso Audios)",
        "tipo_parentesco": "Consanguinidad colateral en 4° grado (Primos hermanos: hijos de hermanos Piñera Carvallo)",
        "descripcion": (
            "Articula el poder presidencial y financiero del Grupo Bancard ([[Sebastian Pinera Echenique]]) "
            "con la conducción política de la [[Union Democrata Independiente]] y del Ministerio del Interior "
            "([[Andres Chadwick Pinera]]). A través de la comunidad de oficina en Alonso de Córdova y la defensa "
            "en la Acusación Constitucional de 2019, conecta directamente al clan con el operador legal y penal "
            "[[Luis Hermosilla Osorio]], el factoring [[Factop SpA]] y la red de nombramientos en la [[Corte Suprema de Chile]] ([[Angela Vivanco Martinez]])."
        ),
    },
    frozenset(["Augusto Pinochet Ugarte", "Lucia Hiriart Rodriguez", "Augusto Pinochet Hiriart", "Julio Ponce Lerou"]): {
        "nombre_clan": "Clan Pinochet–Hiriart–Ponce Lerou (Eje Cívico-Militar, CEMA, Riggs y Sociedades Cascada/SQM)",
        "tipo_parentesco": "Matrimonio (Pinochet–Hiriart), filiación directa (Pinochet Hiriart) y afinidad en 1° grado (ex yerno Julio Ponce Lerou)",
        "descripcion": (
            "Conecta la captura patrimonial directa de fondos reservados y bienes fiscales durante la dictadura "
            "([[Caso Pinocheques]], [[Caso Riggs]] y [[Caso CEMA Chile]]) con el control post-privatización de [[SQM SA]] "
            "y las [[Sociedad de Inversiones Pampa Calichera SA|Sociedades Cascada]] ([[Caso Cascadas]]), desde donde a su vez "
            "se financió transversalmente a la élite partidaria entre 2009 y 2015 ([[Caso SQM]])."
        ),
    },
    frozenset(["Carlos Eugenio Lavin Garcia-Huidobro", "Cathy Barriga Guerra"]): {
        "nombre_clan": "Clan Lavín–Barriga (Eje Holding Penta – Municipalidad de Maipú)",
        "tipo_parentesco": "Afinidad colateral extendida (vía Joaquín Lavín Infante, primo hermano de Carlos Eugenio Lavín y suegro de Cathy Barriga)",
        "descripcion": (
            "Vincula a la cúpula financiera fundadora de [[Empresas Penta SA]] ([[Carlos Eugenio Lavin Garcia-Huidobro]], "
            "condenado en [[Caso Penta]]) con la administración alcaldicia de la [[Municipalidad de Maipu]] "
            "([[Cathy Barriga Guerra]], formalizada por [[Fraude al Fisco]] en [[Caso Municipalidad de Maipu]])."
        ),
    },
}


def fmt_clp(val: int) -> str:
    return "$" + f"{int(val):,}".replace(",", ".")


def bfs_shortest_path(adj: dict, start: str, goal: str):
    if start == goal:
        return [start]
    visited = {start}
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        curr = path[-1]
        for nxt in sorted(adj.get(curr, [])):
            if nxt == goal:
                return path + [nxt]
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])
    return None


def main():
    with open(METRICAS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = {n["id"]: n for n in data["nodos"]}
    edges = data["aristas"]

    # Build undirected graphs: full graph G and graph without kinship edges G_no_fam
    adj_full = defaultdict(set)
    adj_no_fam = defaultdict(set)
    adj_fam = defaultdict(set)
    fam_edges = []

    for e in edges:
        u, v, rel = e["source"], e["target"], e["relation"]
        if u not in nodes or v not in nodes:
            continue
        adj_full[u].add(v)
        adj_full[v].add(u)
        if rel == "vinculos_familiares":
            adj_fam[u].add(v)
            adj_fam[v].add(u)
            if u < v:
                fam_edges.append((u, v))
        else:
            adj_no_fam[u].add(v)
            adj_no_fam[v].add(u)

    # Map each person to their transactions (TRX) and causes
    person_trxs = defaultdict(set)
    person_causes = defaultdict(set)
    trx_amounts = {}
    trx_causes = {}

    for nid, n in nodes.items():
        if n.get("tipo_nodo") == "nexo_transaccion":
            amt = int(n.get("monto_clp", 0) or 0)
            trx_amounts[nid] = amt

    # Inspect edges from nexo_transaccion
    for e in edges:
        u, v, rel = e["source"], e["target"], e["relation"]
        if nodes.get(u, {}).get("tipo_nodo") == "nexo_transaccion":
            if rel == "causa_vinculada" and nodes.get(v, {}).get("tipo_nodo") == "causa_judicial":
                trx_causes[u] = v
            elif rel in ("firmante_origen", "firmante_destino") and nodes.get(v, {}).get("tipo_nodo") == "persona":
                person_trxs[v].add(u)

    for p, trxs in person_trxs.items():
        for t in trxs:
            if t in trx_causes:
                person_causes[p].add(trx_causes[t])

    # Connected components in adj_fam
    visited_fam = set()
    clans = []
    for p in sorted(adj_fam.keys()):
        if p not in visited_fam:
            comp = set()
            q = deque([p])
            visited_fam.add(p)
            while q:
                curr = q.popleft()
                comp.add(curr)
                for nxt in sorted(adj_fam[curr]):
                    if nxt not in visited_fam:
                        visited_fam.add(nxt)
                        q.append(nxt)
            clans.append(sorted(comp))

    # Enrich each clan with metrics
    clan_records = []
    total_clan_clp = 0
    all_clan_trxs = set()
    for members in clans:
        fset = frozenset(members)
        meta = CLAN_METADATA.get(fset, {
            "nombre_clan": "Clan " + " / ".join(members),
            "tipo_parentesco": "Parentesco / Afinidad Documentada",
            "descripcion": "Subgrafo familiar detectado automáticamente.",
        })
        trxs = set()
        causes = set()
        for m in members:
            trxs |= person_trxs.get(m, set())
            causes |= person_causes.get(m, set())
        monto_clan = sum(trx_amounts.get(t, 0) for t in trxs)
        all_clan_trxs |= trxs
        clan_records.append({
            "members": members,
            "nombre_clan": meta["nombre_clan"],
            "tipo_parentesco": meta["tipo_parentesco"],
            "descripcion": meta["descripcion"],
            "trxs": sorted(trxs),
            "causes": sorted(causes),
            "monto_clan": monto_clan,
        })

    clan_records.sort(key=lambda c: c["monto_clan"], reverse=True)
    total_clan_clp = sum(trx_amounts.get(t, 0) for t in all_clan_trxs)

    # Calculate Geodesic Shortcuts created by Kinship links
    shortcut_pairs = [
        ("Sebastian Pinera Echenique", "Luis Hermosilla Osorio", "Conexión entre Ex Presidente Piñera y su operador legal/penal vía su primo Andrés Chadwick"),
        ("Bancard Inversiones Ltda", "Factop SpA", "Acoplamiento entre el family office presidencial y el factoring del Caso Audios vía el Clan Piñera–Chadwick"),
        ("Caso Minera Dominga Pandora Papers", "Caso Audios", "Puente inter-causas entre los negocios offshore presidenciales y la red de Alonso de Córdova"),
        ("Augusto Pinochet Ugarte", "SQM SA", "Puente dinástico entre la cúpula militar y el control de la minera no metálica vía Julio Ponce Lerou"),
        ("Caso Riggs", "Caso Cascadas", "Acoplamiento entre cuentas secretas de la familia Pinochet y las operaciones bursátiles de las Sociedades Cascada"),
        ("Caso Pinocheques", "Caso CEMA Chile", "Integración patrimonial entre los cheques de FAMAE a Pinochet Hiriart y los inmuebles fiscales de Lucía Hiriart"),
        ("Caso Penta", "Caso Municipalidad de Maipu", "Atajo familiar entre el holding Penta (Carlos Eugenio Lavín) y el municipio de Maipú (Cathy Barriga)"),
    ]

    shortcut_results = []
    for u, v, label in shortcut_pairs:
        path_with = bfs_shortest_path(adj_full, u, v)
        path_without = bfs_shortest_path(adj_no_fam, u, v)
        d_with = len(path_with) - 1 if path_with else None
        d_without = len(path_without) - 1 if path_without else None
        delta = (d_without - d_with) if (d_with is not None and d_without is not None) else None
        shortcut_results.append({
            "u": u,
            "v": v,
            "label": label,
            "d_with": d_with,
            "d_without": d_without,
            "delta": delta,
            "path_with": path_with,
        })

    # Write Markdown Analytical View
    lines = [
        "---",
        "tipo_nodo: vista_analitica",
        'titulo: "Redes de Parentesco, Clanes Familiares y Puentes Dinásticos"',
        "actualizacion_automatica: true",
        "tags:",
        "  - vista-analitica",
        "  - parentesco",
        "  - clanes-familiares",
        "  - caso-audios",
        "  - grafos-multiplex",
        "---",
        "",
        "# Redes de Parentesco, Clanes Familiares y Puentes Dinásticos ($G_{\\text{fam}}$)",
        "",
        "> **Modelamiento Matemático de Parentesco en Grafos Multiplex**: En el estudio de captura del Estado y corrupción sistémica, los lazos de consanguinidad (padres, hijos, primos hermanos) y afinidad (cónyuges, suegros, yernos, cuñados) conforman una capa estructural independiente ($E_{\\text{fam}}$) que se superpone a la red de transacciones financieras ($E_{\\text{trx}}$) y militancias políticas ($E_{\\text{pol}}$). Mediante el atributo YAML `vinculos_familiares` en el esquema `persona`, el motor de grafos cuantifica cómo los clanes familiares reducen la distancia geodésica ($\\Delta d$) entre macro-causas judiciales y concentran flujos patrimoniales.",
        "",
        "## 1. Resumen Ejecutivo de la Capa de Parentesco (`vinculos_familiares`)",
        f"- **Clanes Familiares / Dinásticos Modelados**: **{len(clan_records)}** componentes conexas familiares.",
        f"- **Sujetos Integrados en Redes de Parentesco Explícito**: **{len(adj_fam)}** nodos de tipo `persona`.",
        f"- **Aristas de Parentesco Bidireccionales (`vinculos_familiares`)**: **{len(fam_edges)} pares familiares** ({len(fam_edges)*2} aristas dirigidas en el grafo).",
        f"- **Patrimonio Total Asociado a Clanes Familiares en Aristas Reificadas**: **`{fmt_clp(total_clan_clp)} CLP`** a través de **{len(all_clan_trxs)} transacciones reificadas**.",
        "",
        "---",
        "",
        "## 2. El Triángulo Piñera – Chadwick – Hermosilla (Arista Caso Audios y Acusación Constitucional)",
        "",
        "Uno de los casos paradigmáticos de acoplamiento entre **parentesco político-familiar** y **operadores extraprocesales** en la bóveda es la tríada conformada por [[Sebastian Pinera Echenique]], su primo hermano [[Andres Chadwick Pinera]] y el abogado penalista [[Luis Hermosilla Osorio]]:",
        "",
        "1. **Consanguinidad y Poder Ejecutivo (`Clan Piñera–Chadwick`)**: [[Sebastian Pinera Echenique]] y [[Andres Chadwick Pinera]] son **primos hermanos** (la madre de Chadwick, Paulette Piñera Carvallo, era hermana de José Piñera Carvallo, padre del expresidente). Durante ambos gobiernos de Piñera (2010–2014 y 2018–2022), Chadwick ocupó el corazón político de La Moneda como Ministro Secretario General de Gobierno y Ministro del Interior y Seguridad Pública, mientras [[Luis Hermosilla Osorio]] actuó como asesor penal externo de Interior y abogado de confianza del oficialismo.",
        "2. **Defensa en la Acusación Constitucional (`Diciembre de 2019`) financiada por [[Factop SpA]]**: Cuando [[Andres Chadwick Pinera]] enfrentó la Acusación Constitucional ante el [[Senado de la Republica de Chile]] (aprobada el 11 de diciembre de 2019 con inhabilitación por 5 años), su abogado defensor principal fue [[Luis Hermosilla Osorio]]. Los peritajes del [[Caso Audios]] demostraron que el informe en derecho del jurista alemán Kai Ambos utilizado en esa defensa parlamentaria fue pagado directamente con fondos del *factoring* [[Factop SpA]] de los hermanos Sauer.",
        "3. **Comunidad de Oficina en Alonso de Córdova y Transferencias por `$190.000.000 CLP` (`2020–2023`)**: Tras salir del gobierno, [[Andres Chadwick Pinera]] compartió oficina privada con [[Luis Hermosilla Osorio]] en Alonso de Córdova 3788 (Vitacura) —el mismo lugar donde se grabó [[Audio-Reunion-Edificio-Alonso-2023]]—. Entre 2020 y 2023, Hermosilla transfirió más de **`$190.000.000 CLP`** a Chadwick con cargo a fondos provenientes de [[Factop SpA]] ([[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]), período en que se investigan gestiones de [[Trafico de Influencias]] para destrabar el proyecto *Parque Capital* (Grupo Patio) y coordinaciones en nombramientos judiciales en la [[Corte Suprema de Chile]] junto a la exministra [[Angela Vivanco Martinez]] ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]).",
        "",
        "```mermaid",
        "flowchart TD",
        '    subgraph CLAN_PC["Clan Familiar Piñera-Chadwick"]',
        '        SP["Sebastian Pinera Echenique<br/>(Ex Presidente RN / Grupo Bancard)"] <-->|"Primos Hermanos<br/>(vinculos_familiares)"| AC["Andres Chadwick Pinera<br/>(Ex Ministro del Interior / UDI)"]',
        "    end",
        '    subgraph RED_AUDIOS["Red Alonso de Córdova / Caso Audios"]',
        '        LH["Luis Hermosilla Osorio<br/>(Abogado Defensor AC y Socio de Oficina)"]',
        '        FAC["Factop SpA<br/>(Factoring Hnos. Sauer)"]',
        '        AV["Angela Vivanco Martinez<br/>(Ex Ministra Corte Suprema)"]',
        "    end",
        '    FAC -->|"Caja Negra y Financiamiento<br/>Informe Kai Ambos + Remesas"| LH',
        '    LH -->|"TRX-2019-12-11 ($190.000.000 CLP)<br/>Defensa AC Senado y Pagos 2020-2023"| AC',
        '    LH <-->|"TRX-2023-02-09<br/>Nombramientos y Gestiones CS"| AV',
        '    AC -.->|"Lobby Nombramientos Judiciales<br/>y Arista Parque Capital"| AV',
        '    SP -->|"Bancard / US$152M Dominga"| DOM["Caso Minera Dominga / LAN / Exalmar / SQM"]',
        "```",
        "",
        "---",
        "",
        "## 3. Catálogo Forense de Clanes Familiares y Concentración Patrimonial",
        "",
        "| Clan Familiar / Dinástico | Tipo de Parentesco | Miembros (`persona`) | Macro-Causas Conectadas | N° TRX | Volumen Patrimonial Asociado (CLP) |",
        "| :--- | :--- | :--- | :--- | :---: | ---: |",
    ]

    for c in clan_records:
        members_links = ", ".join(f"[[{m}]]" for m in c["members"])
        causes_links = ", ".join(f"[[{ca}]]" for ca in c["causes"])
        lines.append(
            f"| **{c['nombre_clan']}** | {c['tipo_parentesco']} | {members_links} | {causes_links} | {len(c['trxs'])} | **{fmt_clp(c['monto_clan'])}** |"
        )

    lines.extend([
        "",
        "### Detalle Estructural por Clan",
        "",
    ])

    for idx, c in enumerate(clan_records, 1):
        lines.append(f"#### 3.{idx}. {c['nombre_clan']}")
        lines.append(f"- **Vínculo Genealógico / Afinidad**: {c['tipo_parentesco']}.")
        lines.append(f"- **Integrantes en la Bóveda**: {', '.join(f'[[{m}]]' for m in c['members'])}.")
        lines.append(f"- **Macro-Causas Acopladas ({len(c['causes'])})**: {', '.join(f'[[{ca}]]' for ca in c['causes'])}.")
        lines.append(f"- **Aristas Reificadas Vinculadas ({len(c['trxs'])})**: {', '.join(f'[[{t}]]' for t in c['trxs'])}.")
        lines.append(f"- **Volumen Financiero Consolidado**: **`{fmt_clp(c['monto_clan'])} CLP`**.")
        lines.append(f"- **Síntesis de Captura de Red**: {c['descripcion']}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 4. Reducción de Distancia Geodésica ($\\Delta d$) por Atajos de Parentesco",
        "",
        "Para medir el impacto topológico de los vínculos familiares, comparamos la distancia geodésica más corta $d_{G}(u, v)$ en el grafo completo versus $d_{G \\setminus E_{\\text{fam}}}(u, v)$ cuando se remueven las aristas `vinculos_familiares`:",
        "",
        "| Nodo Origen ($u$) | Nodo Destino ($v$) | $d(u,v)$ Sin Parentesco | $d(u,v)$ Con Parentesco | Reducción $\\Delta d$ | Ruta Geodésica Mínima con Parentesco |",
        "| :--- | :--- | :---: | :---: | :---: | :--- |",
    ])

    for sr in shortcut_results:
        d_wo = str(sr["d_without"]) if sr["d_without"] is not None else "∞"
        d_w = str(sr["d_with"]) if sr["d_with"] is not None else "∞"
        delta_str = f"-{sr['delta']} saltos" if (sr["delta"] is not None and sr["delta"] > 0) else "0 saltos"
        path_str = " → ".join(f"[[{p}]]" for p in sr["path_with"]) if sr["path_with"] else "N/A"
        lines.append(
            f"| [[{sr['u']}]] | [[{sr['v']}]] | `{d_wo}` | **`{d_w}`** | **{delta_str}** | {path_str} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 5. Otros Nexos de Parentesco e Influencia Familiar Documentados en Causas",
        "",
        "Además de los clanes que conectan múltiples nodos `persona` entre distintas causas, la bóveda registra aristas donde el parentesco opera al interior de una misma causa o sociedad vehículo:",
        "- **[[Caso Caval]] ([[Natalia Compagnon Soto]])**: Socia del 50% de [[Exportadora y de Gestion Caval Ltda]], cónyuge de Sebastián Dávalos Bachelet y nuera de la entonces Presidenta de la República Michelle Bachelet Jeria, vínculo familiar decisivo en la reunión privada con la vicepresidencia de [[Banco de Chile]] para obtener el crédito de `$6.500.000.000 CLP` ([[TRX-2013-11-06-Reunion-Luksic-Compagnon-01]] y [[TRX-2014-02-07-Credito-BancoDeChile-Caval-01]]).",
        "- **[[Caso Pinocheques]] y [[Caso Riggs]] (Sucesión Pinochet–Hiriart)**: Utilización de cuentas mancomunadas, pasaportes ideológicamente falsos y sociedades *offshore* familiares en [[Riggs Bank y Sociedades Offshore Ashburton]] para distribuir fondos reservados entre el grupo familiar directo de [[Augusto Pinochet Ugarte]], [[Lucia Hiriart Rodriguez]] y [[Augusto Pinochet Hiriart]].",
        "",
    ])

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[OK] Vista analítica de parentesco generada en: {OUTPUT_MD}")
    print(f"     Clanes detectados: {len(clan_records)} | Pares familiares: {len(fam_edges)} | Monto clanes: {fmt_clp(total_clan_clp)}")


if __name__ == "__main__":
    main()
