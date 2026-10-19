---
tipo_nodo: vista_analitica
tags:
  - vista/fuentes
  - meta/verificacion
---

# Cobertura de Fuentes y Alertas de Verificación

> Generado por `check_sources.py` el 2026-10-19. Una arista TRX se considera cubierta si su evidencia soporte tiene fuentes.

## Cobertura por Carpeta
| Carpeta | Notas | Con fuente | Cobertura |
| :--- | ---: | ---: | ---: |
| `02_Causas` | 33 | 33 | 100% |
| `04_Evidencias` | 41 | 41 | 100% |
| `03_Hechos_y_Nexos` | 71 | 71 | 100% |

## Estado de Verificación (Causas y Evidencias)
| Estado | Notas |
| :--- | ---: |
| `desactualizado` | 3 |
| `parcial` | 12 |
| `verificado` | 59 |

## Alertas de Verificación Pendientes (43)

- **[[Acuerdo-Judicial-Restitucion-CEMAChile-2019]]**: No se encontró un 'acuerdo judicial de restitución' de 2019; la prensa describe el traspaso de bienes y la disolución vía CDE en 2021.
- **[[Audio-Reunion-Edificio-Alonso-2023]]**: Agregar el reportaje original de CIPER (14-11-2023) como fuente primaria periodística.
- **[[Auto-Procesamiento-Ministra-Rutherford-2019]]**: La fuente encontrada es un procesamiento de feb-2018 (general (r) Héctor Ureta); no se ubicó el auto de 2019 citado.
- **[[Caso Archivos Epstein Menciones Chile]]**: ALTO RIESGO REPUTACIONAL: las fuentes indican menciones referenciales, sin imputación ni contacto directo acreditado con Velasco o Luksic. La publicación masiva del DOJ es de diciembre 2025 a enero 2026, no 2024 como dice la evidencia. Considerar retirar las aristas TRX de 'mención'.
- **[[Caso Asignaciones Parlamentarias y Cuota Flores]]**: Investigación desformalizada: no hay imputación formal. La arista de registros íntimos se retiró el 2026-10-19 por tratarse de la vida privada de una víctima, ajena al eje de corrupción.
- **[[Caso Basura]]**: Arista Maipú: condenado el exconcejal Marcelo Torres; el exalcalde Christian Vittori fue absuelto. Arista Cerro Navia: condena a Luis Plaza (dic-2024). Verificar situacion_procesal de cada persona.
- **[[Caso CEMA Chile]]**: estado_judicial corregido a cerrada_sin_condena (2026-10-19): la arista penal fue sobreseída temporalmente (2013) y la fundación se disolvió vía CDE (2021).
- **[[Caso Cascadas]]**: La multa a Ponce Lerou (UF 1.700.000) fue rebajada a ~UF 75.000 tras fallo del TC; confirmar montos usados en TRX-2011-12-19.
- **[[Caso Colonia Dignidad]]**: El fallo CS de enero 2013 condenó por complicidad en abusos sexuales a menores; la condena de Schäfer por armas es de 2006. Revisar TRX-2005-06-14-Arsenal y la evidencia 'Sentencia-Corte-Suprema-ColoniaDignidad-2013'.
- **[[Caso Colusion del Papel Tissue]]**: La Corte Suprema (06-01-2020) revocó el beneficio de delación compensada de CMPC y le impuso 20.000 UTA, igual que a SCA. Verificar que las notas de CMPC lo reflejen.
- **[[Caso Convenios]]**: ProCultura: formalización arista RM (fraude al fisco, feb-2026, 7° JG Santiago) y arista Biobío (apropiación indebida, 05-08-2026). Actualizar estado de Larraín.
- **[[Caso Corpesca]]**: La sentencia con penas es de 16-04-2021 (veredicto 02-12-2020) y fue confirmada por la Corte de Apelaciones el 06-01-2022. La evidencia se titula 'Sentencia-3TOP-Santiago-Corpesca-2020'.
- **[[Caso LAN Informacion Privilegiada y Banco de Talca]]**: Resolución Exenta SVS N° 306 (06-07-2007) sancionó infracción al deber de abstención (art. 165 Ley 18.045), multa 19.740 UF; Piñera no apeló. Arista Banco de Talca (1982) sin fuente específica todavía.
- **[[Caso Luminarias LED]]**: Sentencia-TOP-Chillan-Luminarias-2023 y TRX-2020-07-08 (Itelecom-Hermosilla) retirados el 2026-10-19 por falta de fuente. Verificar el monto de $3.200 millones del TRX-2019-05-14.
- **[[Caso MOP-Gate]]**: Corregido el 2026-10-19: la empresa es GATE y su dueño condenado es Héctor Peña Véliz; se retiró 'Roberto Lewin Valdivieso' por falta de fuente.
- **[[Caso Megafraude Tributario Operacion Tributos]]**: Personas renombradas el 2026-10-19 según el listado publicado por La Tercera (Pavez Canessa, Galaz Rojas, Sacco Croxatto, Jiménez Farías). Se retiraron dos sociedades y un TRX de lavado sin fuente.
- **[[Caso Minera Dominga Pandora Papers]]**: Fiscalía pidió sobreseimiento definitivo en enero de 2024; no se confirmó la resolución del tribunal.
- **[[Caso Municipalidad de Maipu]]**: La formalización es de enero de 2024 ante el 9° JG de Santiago; el vault indica Fiscalía Oriente: verificar fiscalía a cargo.
- **[[Caso Operacion FUBELT Intervencion CIA y DINA]]**: El RUC '7000150970-K' no puede existir (el sistema RUC nace con la reforma procesal penal de 2000). Revisar identificadores de causas anteriores a 2000.
- **[[Caso Operacion Huracan]]**: Veredicto 09-01-2026 y sentencia 02-04-2026, con recursos de nulidad pendientes (mayo 2026): la sentencia no está firme. La evidencia se titula '...-2024'.
- **[[Caso Operaciones Digitales e Injerencia Electoral]]**: La investigación se abrió en septiembre de 2026 (el vault indica año_inicio 2024 y un RUC de 2024). Según The Clinic, RN afirma que Cerimedo nunca fue contratado por el partido.
- **[[Caso Pacogate]]**: Veredicto del juicio oral: abril de 2026 (25 de 28 condenados; se descartó asociación ilícita). Las penas se conocerán en la sentencia (prensa: feb-2027). La evidencia 'Veredicto-TOP-Santiago-Pacogate-2026' no coincide con esa cronología.
- **[[Caso Panama Papers Chile]]**: Aparecer en Panama Papers no implica ilegalidad (CIPER 2016: 'aún no hay evidencias de ilegalidades'). No se encontró fuente para la actuación del SII/UAF ni para el RUC indicado.
- **[[Caso Riggs]]**: La CS condenó a tres exmilitares (Vergara, Mac Lean, Castillo) por malversación de US$ 6,47 millones y ordenó comiso de US$ 1,62 millones. Pinochet murió (2006) sin condena.
- **[[Caso Sierra Bella]]**: La municipalidad no perseveró en la compra tras el informe de Contraloría. Verificar si TRX-2023-01-20-Compraventa-Clinica-SierraBella-01 registra un pago que no ocurrió, y la fiscalía a cargo (el vault dice Coquimbo).
- **[[Caso Spiniak]]**: Spiniak falleció en marzo de 2026: actualizar ficha de persona.
- **[[Caso Vitacura]]**: La formalización es de junio de 2023 (4° JG Santiago); el vault indica año_inicio 2021. Prensa: 29 delitos de fraude al fisco por ~$766,9 millones.
- **[[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]**: La publicación del DOJ es de dic-2025 a ene-2026 (Epstein Files Transparency Act, nov-2025), no 2024.
- **[[Informe-ICIJ-SII-PanamaPapers-Chile-2016]]**: No se encontró un informe del SII asociado; la parte ICIJ/CIPER sí está documentada.
- **[[Querella-SII-Boletas-SQM-2015]]**: Los acusados del juicio oral fueron absueltos (oct-2025); el tribunal no dio por acreditada la falsedad ideológica de boletas y facturas.
- **[[Registro-Audiencia-InfoLobby-Biobio-2022]]**: Falta el enlace directo al registro de audiencia en leylobby.gob.cl.
- **[[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]]**: Falta el enlace a la Resolución Exenta 306 en cmfchile.cl.
- **[[Sentencia-Corte-Suprema-Colusion-Pollos-2015]]**: El rol del fallo publicado por la FNE es 27.181-2014; la nota usa 27.175-2014 en id_evidencia.
- **[[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]**: Prensa: perjuicio de 'más de $1.200 millones' en honorarios; verificar cifra exacta de $1.253 millones.
- **[[TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01]]**: Sin fuente específica para el monto de $450 millones ni para facturas ante el SII; la condena del caso es por fraude al fisco.
- **[[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]]**: Hecho no adjudicado: investigación cerrada por prescripción (2019).
- **[[TRX-2010-08-19-Correo-Royalty-SQM-01]]**: Absolución en primera instancia (22-10-2025); monto de $730 millones corresponde a la acusación.
- **[[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]]**: Mención documental sin imputación: se eliminó delito_imputado (2026-10-19). Aparecer en los archivos Epstein no constituye delito.
- **[[TRX-2014-02-18-Soborno-Caval-Machali-01]]**: Monto de $140 millones corresponde a la acusación; no verificado en sentencia.
- **[[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]]**: Mención documental sin imputación: se eliminó delito_imputado (2026-10-19). Aparecer en los archivos Epstein no constituye delito.
- **[[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]]**: Mención documental sin imputación: se eliminó delito_imputado (2026-10-19). Aparecer en los archivos Epstein no constituye delito.
- **[[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]**: Monto de $3.200 millones sin respaldo en las fuentes revisadas; la prensa reporta un pago de $37 millones en efectivo a Campos.
- **[[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]**: Se eliminó delito_imputado (2026-10-19): la presencia en una sede partidaria no es un delito imputado. RN afirma que Cerimedo nunca fue contratado.

## Notas sin Fuente Verificable

