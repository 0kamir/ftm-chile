#!/usr/bin/env python3
"""
Suite de Pruebas Automatizadas (Unit & Integration Tests) para el Vault OSINT de Corrupción en Chile.
Verifica:
1. Validación Módulo 11 de RUTs chilenos.
2. Integridad de esquemas YAML y enlaces internos (validate_vault.py).
3. Generación de reporte forense UTM, HHI, PageRank y detección de fraccionamiento (forensic_audit.py).
4. Auditoría Estadística de Ley de Benford y Sesgo de Montos Redondos (benford_forensic.py).
5. Exportación GraphML y JSON (export_graph.py).
6. Simulación de Percolación y Desarticulación de Nodos Clave (percolation_analysis.py).
7. Predicción de Vínculos Ocultos mediante Adamic-Adar y Jaccard (link_prediction.py).
8. Exportación a formato Graphviz DOT (export_graphviz_dot.py).
9. Exportación al estándar OCCRP Aleph FollowTheMoney (export_ftm_aleph.py).
10. Exportación al estándar ICIJ Neo4j Cypher (export_neo4j_cypher.py).
11. Exportación al estándar W3C JSON-LD Semántico (export_jsonld.py).
12. Exportación de planillas contables CSV (export_csv_tables.py).
13. Generación de Dossier Ejecutivo estático para PDF (generate_dossier.py).
14. Generación del Visor Web HTML5 autónomo (generate_web_viewer.py).
15. Buscador de caminos más cortos en el grafo (query_network.py).
16. Validez de referencias en Mapa_Forense_Redes.canvas.
17. Esquema de fuentes verificables y reporte de cobertura (add_source.py / check_sources.py).
"""

import json
import os
import subprocess
import sys
import unittest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))

import add_source  # noqa: E402
import validate_vault  # noqa: E402


class TestForensicVault(unittest.TestCase):
    def test_modulo_11_rut_validator(self):
        self.assertTrue(validate_vault.validar_rut_chileno("61.812.000-7"))
        self.assertTrue(validate_vault.validar_rut_chileno("60.201.000-7"))
        self.assertTrue(validate_vault.validar_rut_chileno("96.893.820-7"))
        self.assertTrue(validate_vault.validar_rut_chileno("7.018.430-3"))
        self.assertTrue(validate_vault.validar_rut_chileno("6.194.820-1"))
        self.assertFalse(validate_vault.validar_rut_chileno("15.482.910-4"))
        self.assertFalse(validate_vault.validar_rut_chileno("invalido"))

    def test_source_schema_validation(self):
        errors, warnings = [], []
        meta_ok = {
            "tipo_nodo": "causa_judicial",
            "estado_verificacion": "verificado",
            "fuentes": [{"url": "https://www.pjud.cl/x", "titulo": "Fallo", "medio": "PJUD", "tipo": "primaria"}],
        }
        validate_vault.validar_fuentes("ok.md", meta_ok, True, errors, warnings)
        self.assertEqual(errors, [])

        meta_mal = {
            "tipo_nodo": "evidencia_documental",
            "estado_verificacion": "verificado",
            "fuentes": [{"url": "pjud.cl", "titulo": "", "medio": "PJUD", "tipo": "otra"}],
        }
        validate_vault.validar_fuentes("mal.md", meta_mal, False, errors, warnings)
        self.assertEqual(len(errors), 3)

        with self.assertRaises(ValueError):
            add_source.validar_fuente({"url": "ftp://x", "titulo": "t", "medio": "m", "tipo": "primaria"})

    def test_sources_coverage_report(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/check_sources.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Reporte de cobertura de fuentes generado", res.stdout)
        self.assertTrue(
            os.path.isfile(os.path.join(ROOT_DIR, "05_Vistas_Analiticas/Cobertura_de_Fuentes.md"))
        )

    def test_vault_schema_and_links_integrity(self):
        rc = validate_vault.main()
        self.assertEqual(rc, 0, "validate_vault.py detectó errores en el vault")

    def test_forensic_audit_and_utm_fractioning(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/forensic_audit.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Fraccionamientos CGR detectados: 1", res.stdout)
        report_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Reporte_Auditoria_Automatizada.md"
        )
        self.assertTrue(os.path.isfile(report_path))

    def test_benford_statistical_audit(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/benford_forensic.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Auditoría Benford y Redondeo generada", res.stdout)
        benford_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Auditoria_Benford_y_Montos.md"
        )
        self.assertTrue(os.path.isfile(benford_md))

    def test_graphml_and_json_export(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/export_graph.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        json_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/metricas_red.json"
        )
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # 751.189.363.198 + 35.000.000 (Cuota Flores) = 751.224.363.198
        self.assertEqual(data["resumen"]["monto_total_clp"], 751224363198)

    def test_percolation_simulation(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/percolation_analysis.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Simulación de Percolación generada", res.stdout)
        perc_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Simulacion_Desarticulacion_Red.md"
        )
        self.assertTrue(os.path.isfile(perc_md))

    def test_link_prediction_adamic_adar(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/link_prediction.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Predicción de Vínculos Ocultos generada", res.stdout)
        lp_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Prediccion_Vinculos_Ocultos.md"
        )
        self.assertTrue(os.path.isfile(lp_md))

    def test_community_detection_modularity(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/community_detection.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Reporte de Comunidades Operativas generado", res.stdout)
        comm_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Deteccion_Comunidades_Operativas.md"
        )
        self.assertTrue(os.path.isfile(comm_md))

    def test_financial_flow_min_cut(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/financial_flow_cut.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Análisis de Flujo Financiero y Corte Mínimo generado", res.stdout)
        flow_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Analisis_Flujo_Financiero_y_Corte_Minimo.md"
        )
        self.assertTrue(os.path.isfile(flow_md))

    def test_kcore_and_assortativity(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/kcore_and_assortativity.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Análisis k-Core, Asortatividad", res.stdout)
        kcore_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Nucleos_KCore_y_Asortatividad.md"
        )
        self.assertTrue(os.path.isfile(kcore_md))

    def test_spectral_fiedler_analysis(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/spectral_analysis.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Análisis Espectral y Fiedler generado", res.stdout)
        spec_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Analisis_Espectral_y_Fiedler.md"
        )
        self.assertTrue(os.path.isfile(spec_md))

    def test_temporal_evolution_phase_transition(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/temporal_evolution.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Evolución Temporal y Transición de Fase generada", res.stdout)
        temp_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Evolucion_Temporal_y_Transicion_de_Fase.md"
        )
        self.assertTrue(os.path.isfile(temp_md))

    def test_motif_and_triadic_census(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/motif_and_triads.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Censo Triádico y Motivos Superiores generado", res.stdout)
        motif_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Censo_Triadico_y_Motivos_Superiores.md"
        )
        self.assertTrue(os.path.isfile(motif_md))

    def test_effective_resistance_kirchhoff(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/effective_resistance.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Resistencia Efectiva y Tiempos de Impacto generados", res.stdout)
        res_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Resistencia_Efectiva_y_Tiempos_de_Impacto.md"
        )
        self.assertTrue(os.path.isfile(res_md))

    def test_graphviz_dot_export(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/export_graphviz_dot.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        dot_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/red_corrupcion_chile.dot"
        )
        self.assertTrue(os.path.isfile(dot_path))

    def test_aleph_ftm_jsonl_export(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/export_ftm_aleph.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        ftm_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/aleph_entities.ftm.jsonl"
        )
        self.assertTrue(os.path.isfile(ftm_path))

    def test_icij_neo4j_cypher_export(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/export_neo4j_cypher.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        cypher_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/icij_neo4j_import.cypher"
        )
        self.assertTrue(os.path.isfile(cypher_path))

    def test_jsonld_semantic_export(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/export_jsonld.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        jsonld_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/red_corrupcion_chile.jsonld"
        )
        self.assertTrue(os.path.isfile(jsonld_path))

    def test_csv_tables_export(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/export_csv_tables.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        for name in (
            "peritaje_transacciones.csv",
            "peritaje_imputados.csv",
            "peritaje_entidades.csv",
        ):
            p = os.path.join(ROOT_DIR, "05_Vistas_Analiticas/Exportaciones", name)
            self.assertTrue(os.path.isfile(p))

    def test_dossier_generation(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/generate_dossier.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        dossier_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/Dossier_Ejecutivo_Completo.md"
        )
        self.assertTrue(os.path.isfile(dossier_path))

    def test_shortest_path_query(self):
        res = subprocess.run(
            [
                sys.executable,
                os.path.join(ROOT_DIR, "00_Meta/Scripts/query_network.py"),
                "--shortest-path",
                "Jaime Orpis Bouchon",
                "Pablo Longueira Montes",
            ],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("CAMINO FORENSE MÁS CORTO", res.stdout)
        self.assertIn("Union Democrata Independiente", res.stdout)

    def test_web_viewer_generation(self):
        subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/generate_web_viewer.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        html_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Exportaciones/visor_forense.html"
        )
        self.assertTrue(os.path.isfile(html_path))

    def test_canvas_files_exist(self):
        canvas_path = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Mapa_Forense_Redes.canvas"
        )
        with open(canvas_path, "r", encoding="utf-8") as f:
            canvas = json.load(f)
        for node in canvas.get("nodes", []):
            if node.get("type") == "file":
                target = os.path.join(ROOT_DIR, node["file"])
                self.assertTrue(
                    os.path.isfile(target),
                    f"Nodo Canvas apunta a archivo inexistente: {node['file']}",
                )

    def test_kinship_and_clans_analysis(self):
        res = subprocess.run(
            [sys.executable, os.path.join(ROOT_DIR, "00_Meta/Scripts/kinship_and_clans.py")],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Vista analítica de parentesco generada", res.stdout)
        kin_md = os.path.join(
            ROOT_DIR, "05_Vistas_Analiticas/Redes_Parentesco_y_Clanes_Familiares.md"
        )
        self.assertTrue(os.path.isfile(kin_md))


if __name__ == "__main__":
    unittest.main(verbosity=2)
