---
tipo_nodo: nexo_transaccion
fecha: 2019-12-11
tipo_nexo: transferencia
monto_clp: 190000000
entidad_origen: "[[Factop SpA]]"
entidad_destino: "[[Senado de la Republica de Chile]]"
firmante_origen: "[[Luis Hermosilla Osorio]]"
firmante_destino: "[[Andres Chadwick Pinera]]"
causa_vinculada: "[[Caso Audios]]"
delito_imputado: "[[Trafico de Influencias]]"
evidencia_soporte: "[[Audio-Reunion-Edificio-Alonso-2023]]"
tags:
  - nexo/transaccion
  - caso-audios
  - factop
  - trafico-influencias
  - clan-pinera-chadwick
---

# TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01

## Ficha de Arista Reificada (Financiamiento de Defensa en Acusación Constitucional y Remesas Hermosilla–Chadwick)
- **Fecha del Hito Inicial**: `= this.fecha` *(Votación de Acusación Constitucional en el Senado y posterior flujo de transferencias 2020–2023)*
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Auditado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Más de $190.000.000 CLP transferidos entre 2020 y 2023 desde cuentas de Luis Hermosilla, según la Fiscalía, además del pago desde Factop del informe en derecho de Kai Ambos por €26.000 para la Acusación Constitucional)*
- **Entidad de Origen**: `= this.entidad_origen`
- **Institución / Ámbito de Destino**: `= this.entidad_destino`
- **Operador Emisor**: `= this.firmante_origen`
- **Receptor / Beneficiario**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense de la Operación
Arista financiera y política del [[Caso Audios]] que documenta el vínculo profesional y financiero entre el abogado [[Luis Hermosilla Osorio]] y el exministro del Interior [[Andres Chadwick Pinera]] (primo hermano del expresidente [[Sebastian Pinera Echenique]]):
1. **Financiamiento de la defensa ante el [[Senado de la Republica de Chile]] (`diciembre de 2019`)**: Durante la Acusación Constitucional contra [[Andres Chadwick Pinera]], su defensa estuvo a cargo de [[Luis Hermosilla Osorio]]. Los peritajes contables a [[Factop SpA]] y a las comunicaciones extraídas a raíz de [[Audio-Reunion-Edificio-Alonso-2023]] acreditaron que los honorarios del jurista alemán Kai Ambos por el informe en derecho presentado ante el Senado habrían sido costeados, según la Fiscalía, con fondos de [[Factop SpA]] (Hermosilla declaró que Daniel Sauer solo actuó como intermediario y que le reembolsó; CIPER señala que no se sabe con certeza quién financió finalmente la defensa).
2. **Comunidad de oficina en Alonso de Córdova y remesas por `$190.000.000 CLP` (`2020–2023`)**: Tras instalarse ambos en la oficina de Alonso de Córdova 3788 (Vitacura), [[Luis Hermosilla Osorio]] habría realizado, según la Fiscalía, transferencias periódicas a [[Andres Chadwick Pinera]] por un total superior a **`$190.000.000 CLP`**, que Chadwick atribuye a servicios profesionales; la Fiscalía investiga si provenían de fondos de [[Factop SpA]], período en el cual se investigan gestiones de [[Trafico de Influencias]] para la obtención acelerada de certificados de factibilidad del proyecto *Parque Capital* (Grupo Patio) y coordinaciones en nombramientos de la [[Corte Suprema de Chile]] junto a [[Angela Vivanco Martinez]].
