---
tipo_nodo: vista_analitica
titulo: "Redes de Parentesco, Grupos familiares y Puentes Familiares"
actualizacion_automatica: true
tags:
  - vista-analitica
  - parentesco
  - clanes-familiares
  - caso-audios
  - grafos-multiplex
---

# Redes de Parentesco y Puentes Familiares ($G_{\text{fam}}$)

> [!WARNING] Análisis exploratorio, no prueba de responsabilidad
> Este reporte aplica métricas de análisis de redes a los datos del vault. Sus resultados describen la estructura del grafo, no hechos: una cercanía, un agrupamiento o un par similar no indica que exista una relación, un acuerdo ni un delito. Los datos tienen calidades distintas (ver `monto_origen` y `estado_verificacion`) y pueden contener errores. Toda persona mencionada se presume inocente mientras no exista sentencia condenatoria firme. No citar estos resultados como prueba ni como acusación.
>
> Un vínculo familiar **no implica participación** en ningún hecho. Se registra solo cuando consta en fuentes públicas y es relevante para entender la red.


> **Modelamiento Matemático de Parentesco en Grafos Multiplex**: En el análisis de redes, los lazos de consanguinidad (padres, hijos, primos hermanos) y afinidad (cónyuges, suegros, yernos, cuñados) conforman una capa estructural independiente ($E_{\text{fam}}$) que se superpone a la red de transacciones financieras ($E_{\text{trx}}$) y militancias políticas ($E_{\text{pol}}$). Mediante el atributo YAML `vinculos_familiares` en el esquema `persona`, el motor de grafos cuantifica cómo los grupos familiares reducen la distancia geodésica ($\Delta d$) entre macro-causas judiciales y concentran flujos patrimoniales.

## 1. Resumen Ejecutivo de la Capa de Parentesco (`vinculos_familiares`)
- **Grupos familiares / Familiares Modelados**: **2** componentes conexas familiares.
- **Sujetos Integrados en Redes de Parentesco Explícito**: **6** nodos de tipo `persona`.
- **Aristas de Parentesco Bidireccionales (`vinculos_familiares`)**: **6 pares familiares** (12 aristas dirigidas en el grafo).
- **Montos Registrados en Hechos con Integrantes de Grupos Familiares**: **`$110.440.000.000 CLP`** a través de **13 transacciones reificadas**.

---

## 2. Grupos Familiares Registrados

| Grupo familiar / Familiar | Tipo de Parentesco | Miembros (`persona`) | Macro-Causas Conectadas | N° TRX | Volumen Patrimonial Asociado (CLP) |
| :--- | :--- | :--- | :--- | :---: | ---: |
| **Grupo familiar Piñera–Chadwick** | Primos hermanos (hijos de hermanos Piñera Carvallo) | [[Andres Chadwick Pinera]], [[Sebastian Pinera Echenique]] | [[Caso Audios]], [[Caso Exalmar y Fideicomiso Ciego]], [[Caso LAN Informacion Privilegiada y Banco de Talca]], [[Caso Minera Dominga Pandora Papers]] | 5 | **$89.240.000.000** |
| **Grupo familiar Pinochet–Hiriart** | Cónyuges, hijo y exyerno (Julio Ponce Lerou estuvo casado con Verónica Pinochet Hiriart) | [[Augusto Pinochet Hiriart]], [[Augusto Pinochet Ugarte]], [[Julio Ponce Lerou]], [[Lucia Hiriart Rodriguez]] | [[Caso CEMA Chile]], [[Caso Cascadas]], [[Caso Operacion FUBELT Intervencion CIA y DINA]], [[Caso Panama Papers Chile]], [[Caso Pinocheques]], [[Caso Riggs]] | 8 | **$21.200.000.000** |

### Detalle por Grupo Familiar

#### 3.1. Grupo familiar Piñera–Chadwick
- **Vínculo Genealógico / Afinidad**: Primos hermanos (hijos de hermanos Piñera Carvallo).
- **Integrantes en la Bóveda**: [[Andres Chadwick Pinera]], [[Sebastian Pinera Echenique]].
- **Macro-Causas Acopladas (4)**: [[Caso Audios]], [[Caso Exalmar y Fideicomiso Ciego]], [[Caso LAN Informacion Privilegiada y Banco de Talca]], [[Caso Minera Dominga Pandora Papers]].
- **Aristas Reificadas Vinculadas (5)**: [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]], [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]], [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]], [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]], [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]].
- **Volumen Financiero Consolidado**: **`$89.240.000.000 CLP`**.
- **Síntesis de Captura de Red**: Parentesco de conocimiento público. No implica participación conjunta en los hechos registrados.

#### 3.2. Grupo familiar Pinochet–Hiriart
- **Vínculo Genealógico / Afinidad**: Cónyuges, hijo y exyerno (Julio Ponce Lerou estuvo casado con Verónica Pinochet Hiriart).
- **Integrantes en la Bóveda**: [[Augusto Pinochet Hiriart]], [[Augusto Pinochet Ugarte]], [[Julio Ponce Lerou]], [[Lucia Hiriart Rodriguez]].
- **Macro-Causas Acopladas (6)**: [[Caso CEMA Chile]], [[Caso Cascadas]], [[Caso Operacion FUBELT Intervencion CIA y DINA]], [[Caso Panama Papers Chile]], [[Caso Pinocheques]], [[Caso Riggs]].
- **Aristas Reificadas Vinculadas (8)**: [[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]], [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]], [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]], [[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]], [[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]], [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]], [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]], [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]].
- **Volumen Financiero Consolidado**: **`$21.200.000.000 CLP`**.
- **Síntesis de Captura de Red**: Parentesco de conocimiento público. No implica participación conjunta en los hechos registrados.

---

## 3. Reducción de Distancia Geodésica ($\Delta d$) por Atajos de Parentesco

Para medir el impacto topológico de los vínculos familiares, comparamos la distancia geodésica más corta $d_{G}(u, v)$ en el grafo completo versus $d_{G \setminus E_{\text{fam}}}(u, v)$ cuando se remueven las aristas `vinculos_familiares`:

| Nodo Origen ($u$) | Nodo Destino ($v$) | $d(u,v)$ Sin Parentesco | $d(u,v)$ Con Parentesco | Reducción $\Delta d$ | Ruta Geodésica Mínima con Parentesco |
| :--- | :--- | :---: | :---: | :---: | :--- |
| [[Sebastian Pinera Echenique]] | [[Luis Hermosilla Osorio]] | `4` | **`3`** | **-1 saltos** | [[Sebastian Pinera Echenique]] → [[Andres Chadwick Pinera]] → [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]] → [[Luis Hermosilla Osorio]] |
| [[Augusto Pinochet Ugarte]] | [[SQM SA]] | `5` | **`3`** | **-2 saltos** | [[Augusto Pinochet Ugarte]] → [[Julio Ponce Lerou]] → [[TRX-2011-12-19-Operaciones-Bursatiles-Cascadas-SQM-01]] → [[SQM SA]] |
| [[Caso Riggs]] | [[Caso Cascadas]] | `5` | **`5`** | **0 saltos** | [[Caso Riggs]] → [[Sentencia-Corte-Suprema-CasoRiggs-2018]] → [[Corte Suprema de Chile]] → [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]] → [[Negociacion Incompatible]] → [[Caso Cascadas]] |

---

## 4. Otros Nexos de Parentesco e Influencia Familiar Documentados en Causas

Además de los clanes que conectan múltiples nodos `persona` entre distintas causas, la bóveda registra aristas donde el parentesco opera al interior de una misma causa o sociedad vehículo:
- **[[Caso Caval]] ([[Natalia Compagnon Soto]])**: Socia del 50% de [[Exportadora y de Gestion Caval Ltda]], cónyuge de Sebastián Dávalos Bachelet y nuera de la entonces Presidenta de la República Michelle Bachelet Jeria, vínculo familiar decisivo en la reunión privada con la vicepresidencia de [[Banco de Chile]] para obtener el crédito de `$6.500.000.000 CLP` ([[TRX-2013-11-06-Reunion-Luksic-Compagnon-01]] y [[TRX-2014-02-07-Credito-BancoDeChile-Caval-01]]).
- **[[Caso Pinocheques]] y [[Caso Riggs]] (Sucesión Pinochet–Hiriart)**: Utilización de cuentas mancomunadas, pasaportes ideológicamente falsos y sociedades *offshore* familiares en [[Riggs Bank y Sociedades Offshore Ashburton]] para distribuir fondos reservados entre el grupo familiar directo de [[Augusto Pinochet Ugarte]], [[Lucia Hiriart Rodriguez]] y [[Augusto Pinochet Hiriart]].
