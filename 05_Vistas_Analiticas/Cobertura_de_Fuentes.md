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
| `04_Evidencias` | 42 | 42 | 100% |
| `03_Hechos_y_Nexos` | 73 | 73 | 100% |

## Estado de Verificación (Causas y Evidencias)
| Estado | Notas |
| :--- | ---: |
| `desactualizado` | 5 |
| `parcial` | 11 |
| `verificado` | 59 |

## Alertas de Verificación Pendientes (40)

- **[[Acuerdo-Judicial-Restitucion-CEMAChile-2019]]**: No se encontró un 'acuerdo judicial de restitución' de 2019; la prensa describe el traspaso de bienes y la disolución vía CDE en 2021.
- **[[Audio-Reunion-Edificio-Alonso-2023]]**: Agregar el reportaje original de CIPER (14-11-2023) como fuente primaria periodística.
- **[[Auto-Procesamiento-Ministra-Rutherford-2019]]**: La fuente encontrada es un procesamiento de feb-2018 (general (r) Héctor Ureta); no se ubicó el auto de 2019 citado.
- **[[Caso Archivos Epstein Menciones Chile]]**: ALTO RIESGO REPUTACIONAL: las fuentes indican menciones referenciales, sin imputación ni contacto directo acreditado con Velasco o Luksic. La publicación masiva del DOJ es de diciembre 2025 a enero 2026, no 2024 como dice la evidencia. Considerar retirar las aristas TRX de 'mención'.
- **[[Caso Asignaciones Parlamentarias y Cuota Flores]]**: Investigación desformalizada: no hay imputación formal. La arista de registros íntimos (TRX-2026-06-20) trata a Flores como VÍCTIMA de un delito contra la intimidad, no de corrupción: evaluar retirarla del grafo por privacidad.
- **[[Caso Basura]]**: Arista Maipú: condenado el exconcejal Marcelo Torres; el exalcalde Christian Vittori fue absuelto. Arista Cerro Navia: condena a Luis Plaza (dic-2024). Verificar situacion_procesal de cada persona.
- **[[Caso CEMA Chile]]**: No se encontró condena penal: el vault marca 'cerrada_con_condena'. Lo documentado es querella (2016), embargo de propiedades, traspaso de bienes y disolución vía CDE (2021). Revisar estado_judicial.
- **[[Caso Cascadas]]**: La multa a Ponce Lerou (UF 1.700.000) fue rebajada a ~UF 75.000 tras fallo del TC; confirmar montos usados en TRX-2011-12-19.
- **[[Caso Caval]]**: Prensa: TOP Rancagua condenó a Compagnon solo por delito tributario (541 días remitidos, multa); Mauricio Valero y la sociedad Caval fueron absueltos y no hubo condena por soborno. Revisar TRX-2014-02-18-Soborno-Caval-Machali-01 y situacion_procesal de Valero.
- **[[Caso Colonia Dignidad]]**: El fallo CS de enero 2013 condenó por complicidad en abusos sexuales a menores; la condena de Schäfer por armas es de 2006. Revisar TRX-2005-06-14-Arsenal y la evidencia 'Sentencia-Corte-Suprema-ColoniaDignidad-2013'.
- **[[Caso Colusion del Papel Tissue]]**: La Corte Suprema (06-01-2020) revocó el beneficio de delación compensada de CMPC y le impuso 20.000 UTA, igual que a SCA. Verificar que las notas de CMPC lo reflejen.
- **[[Caso Convenios]]**: ProCultura: formalización arista RM (fraude al fisco, feb-2026, 7° JG Santiago) y arista Biobío (apropiación indebida, 05-08-2026). Actualizar estado de Larraín.
- **[[Caso Corpesca]]**: La sentencia con penas es de 16-04-2021 (veredicto 02-12-2020) y fue confirmada por la Corte de Apelaciones el 06-01-2022. La evidencia se titula 'Sentencia-3TOP-Santiago-Corpesca-2020'.
- **[[Caso LAN Informacion Privilegiada y Banco de Talca]]**: Resolución Exenta SVS N° 306 (06-07-2007) sancionó infracción al deber de abstención (art. 165 Ley 18.045), multa 19.740 UF; Piñera no apeló. Arista Banco de Talca (1982) sin fuente específica todavía.
- **[[Caso Luminarias LED]]**: Sentencia-TOP-Chillan-Luminarias-2023 y TRX-2020-07-08 (Itelecom-Hermosilla) retirados el 2026-10-19 por falta de fuente. Verificar el monto de $3.200 millones del TRX-2019-05-14.
- **[[Caso MOP-Gate]]**: La prensa identifica a la empresa como GATE (Gestión Ambiental y Territorial S.A.). El vault usa 'GESCAM' en TRX-2001-08-20 y TRX-2002-04-12: verificar nombre.
- **[[Caso Megafraude Tributario Operacion Tributos]]**: La prensa identifica como líder a José Antonio Pavez Canessa. La persona 'Carlos Pavez Tolosa' del vault no aparece en las fuentes revisadas: verificar identidad antes de publicar.
- **[[Caso Minera Dominga Pandora Papers]]**: Fiscalía pidió sobreseimiento definitivo en enero de 2024; no se confirmó la resolución del tribunal.
- **[[Caso Municipalidad de Maipu]]**: La formalización es de enero de 2024 ante el 9° JG de Santiago; el vault indica Fiscalía Oriente: verificar fiscalía a cargo.
- **[[Caso Operacion FUBELT Intervencion CIA y DINA]]**: El RUC '7000150970-K' no puede existir (el sistema RUC nace con la reforma procesal penal de 2000). Revisar identificadores de causas anteriores a 2000.
- **[[Caso Operacion Huracan]]**: Veredicto 09-01-2026 y sentencia 02-04-2026, con recursos de nulidad pendientes (mayo 2026): la sentencia no está firme. La evidencia se titula '...-2024'.
- **[[Caso Operaciones Digitales e Injerencia Electoral]]**: La investigación se abrió en septiembre de 2026 (el vault indica año_inicio 2024 y un RUC de 2024). Según The Clinic, RN afirma que Cerimedo nunca fue contratado por el partido.
- **[[Caso Pacogate]]**: Veredicto del juicio oral: abril de 2026 (25 de 28 condenados; se descartó asociación ilícita). Las penas se conocerán en la sentencia (prensa: feb-2027). La evidencia 'Sentencia-TOP-Santiago-Pacogate-2021' no coincide con esa cronología.
- **[[Caso Panama Papers Chile]]**: Aparecer en Panama Papers no implica ilegalidad (CIPER 2016: 'aún no hay evidencias de ilegalidades'). No se encontró fuente para la actuación del SII/UAF ni para el RUC indicado.
- **[[Caso Penta]]**: Prensa: la condena de 2018 (procedimiento abreviado) fue por delitos tributarios; CIPER señala que nadie fue condenado por cohecho. Revisar TRX-2011-03-10-Soborno-Penta-Wagner-01.
- **[[Caso Riggs]]**: La CS condenó a tres exmilitares (Vergara, Mac Lean, Castillo) por malversación de US$ 6,47 millones y ordenó comiso de US$ 1,62 millones. Pinochet murió (2006) sin condena.
- **[[Caso SQM]]**: CRÍTICO: el vault marca estado_judicial=juicio_oral, pero el 3° TOP de Santiago absolvió a los ocho acusados (Longueira, Enríquez-Ominami, Contesse y otros) en octubre de 2025. Actualizar estado y situacion_procesal de las personas; presunción de inocencia aplica.
- **[[Caso Sierra Bella]]**: La municipalidad no perseveró en la compra tras el informe de Contraloría. Verificar si TRX-2023-01-20-Compraventa-Clinica-SierraBella-01 registra un pago que no ocurrió, y la fiscalía a cargo (el vault dice Coquimbo).
- **[[Caso Spiniak]]**: Spiniak falleció en marzo de 2026: actualizar ficha de persona.
- **[[Caso Vitacura]]**: La formalización es de junio de 2023 (4° JG Santiago); el vault indica año_inicio 2021. Prensa: 29 delitos de fraude al fisco por ~$766,9 millones.
- **[[Denuncia-Cibercrimen-PDI-Registros-Intimos-2026]]**: PRIVACIDAD: hecho referido a la intimidad de una víctima, ajeno al eje de corrupción; el denunciado niega participación y no hay formalización. Se recomienda retirarlo del grafo.
- **[[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]**: La publicación del DOJ es de dic-2025 a ene-2026 (Epstein Files Transparency Act, nov-2025), no 2024.
- **[[Informe-ICIJ-SII-PanamaPapers-Chile-2016]]**: No se encontró un informe del SII asociado; la parte ICIJ/CIPER sí está documentada.
- **[[Querella-SII-Boletas-SQM-2015]]**: Los acusados del juicio oral fueron absueltos (oct-2025); el tribunal no dio por acreditada la falsedad ideológica de boletas y facturas.
- **[[Registro-Audiencia-InfoLobby-Biobio-2022]]**: Falta el enlace directo al registro de audiencia en leylobby.gob.cl.
- **[[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]]**: Falta el enlace a la Resolución Exenta 306 en cmfchile.cl.
- **[[Sentencia-Corte-Suprema-Colusion-Pollos-2015]]**: El rol del fallo publicado por la FNE es 27.181-2014; la nota usa 27.175-2014 en id_evidencia.
- **[[Sentencia-TOP-Santiago-Pacogate-2021]]**: El juicio oral se postergó en 2021 y el veredicto es de abril de 2026: una 'sentencia 2021' del TOP no calza con las fuentes (podría ser un abreviado). Verificar.
- **[[Sentencia-TOP-Temuco-OperacionHuracan-2024]]**: La sentencia es del 02-04-2026, no de 2024; renombrar la nota y corregir fecha_emision.
- **[[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]**: Monto de $3.200 millones sin respaldo en las fuentes revisadas; la prensa reporta un pago de $37 millones en efectivo a Campos.

## Notas sin Fuente Verificable

