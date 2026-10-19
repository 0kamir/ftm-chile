.PHONY: all validate validate-strict sources links audit benford export percolation linkpred communities flowcut kcore spectral temporal motifs resistance kinship dot ftm cypher jsonld csv dossier web test

all: validate sources audit benford export percolation linkpred communities flowcut kcore spectral temporal motifs resistance kinship dot ftm cypher jsonld csv dossier web test

validate:
	python3 00_Meta/Scripts/validate_vault.py

validate-strict:
	python3 00_Meta/Scripts/validate_vault.py --estricto

sources:
	python3 00_Meta/Scripts/check_sources.py

links:
	python3 00_Meta/Scripts/check_sources.py --links

audit:
	python3 00_Meta/Scripts/forensic_audit.py

benford:
	python3 00_Meta/Scripts/benford_forensic.py

export:
	python3 00_Meta/Scripts/export_graph.py

percolation: export
	python3 00_Meta/Scripts/percolation_analysis.py

linkpred: export
	python3 00_Meta/Scripts/link_prediction.py

communities: export
	python3 00_Meta/Scripts/community_detection.py

flowcut:
	python3 00_Meta/Scripts/financial_flow_cut.py

kcore: export
	python3 00_Meta/Scripts/kcore_and_assortativity.py

spectral: export
	python3 00_Meta/Scripts/spectral_analysis.py

temporal: export
	python3 00_Meta/Scripts/temporal_evolution.py

motifs: export
	python3 00_Meta/Scripts/motif_and_triads.py

resistance: export
	python3 00_Meta/Scripts/effective_resistance.py

kinship: export
	python3 00_Meta/Scripts/kinship_and_clans.py

dot: export
	python3 00_Meta/Scripts/export_graphviz_dot.py

ftm:
	python3 00_Meta/Scripts/export_ftm_aleph.py

cypher:
	python3 00_Meta/Scripts/export_neo4j_cypher.py

jsonld:
	python3 00_Meta/Scripts/export_jsonld.py

csv:
	python3 00_Meta/Scripts/export_csv_tables.py

dossier:
	python3 00_Meta/Scripts/generate_dossier.py

web: export
	python3 00_Meta/Scripts/generate_web_viewer.py

test:
	python3 00_Meta/Scripts/test_vault.py
