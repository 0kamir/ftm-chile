---
tipo_nodo: vista_analitica
tags:
  - vista/fuentes
  - meta/verificacion
---

# Cobertura de Fuentes y Alertas de Verificación

> Generado por `check_sources.py` el 2026-10-26. Una arista TRX se considera cubierta si su evidencia soporte tiene fuentes.

## Cobertura por Carpeta
| Carpeta | Notas | Con fuente | Cobertura |
| :--- | ---: | ---: | ---: |
| `01_Entidades` | 196 | 196 | 100% |
| `02_Causas` | 45 | 45 | 100% |
| `03_Hechos_y_Nexos` | 81 | 81 | 100% |
| `04_Evidencias` | 54 | 54 | 100% |
| `00_Meta/Delitos` | 12 | 12 | 100% |
| `06_Anexos` | 1 | 1 | 100% |

## Estado de Verificación (Causas y Evidencias)
| Estado | Notas |
| :--- | ---: |
| `desactualizado` | 2 |
| `parcial` | 10 |
| `verificado` | 87 |

## Montos por Origen
> Una cifra de sentencia o resolución está acreditada; una de acusación, estimación o prensa no. No se suman como si tuvieran la misma calidad.

| Origen del monto | Hechos | Monto (CLP) |
| :--- | ---: | ---: |
| `sentencia` | 21 | $325.359.171.520 |
| `resolucion_administrativa` | 6 | $134.198.000.000 |
| `estimacion_oficial` | 2 | $240.417.000.000 |
| `acusacion` | 18 | $49.748.563.198 |
| `prensa` | 4 | $89.200.000.000 |
| `no_verificado` | 3 | $2.282.000.000 |
| `sin_monto` | 27 | $0 |

## Alertas de Verificación Pendientes (9)

- **[[Caso Pacogate]]**: Veredicto del juicio oral: abril de 2026 (25 de 28 condenados; se descartó asociación ilícita). Las penas se conocerán en la sentencia (prensa: feb-2027). La evidencia 'Veredicto-TOP-Santiago-Pacogate-2026' no coincide con esa cronología.
- **[[Corporacion Chile Ambiente]]**: El monto de $57 millones y el destino del 90% de los fondos no constan en las fuentes citadas (la prensa menciona $66 millones en facturas de la Corporación Innovación y Democracia a Chile Ambiente). Falta confirmarlos en la sentencia.
- **[[Flavio Echeverria Cortez]]**: Verificar en la sentencia (feb-2027) si figura entre los condenados y su pena.
- **[[Jaime Paz Meneses]]**: Verificar en la sentencia (feb-2027) si figura entre los condenados y su pena.
- **[[Manuel Arancibia Morales]]**: La condena (541 días, 21-12-2007) y el segundo apellido 'Morales' constan en una nota de Emol ubicada solo como extracto del buscador; falta la URL directa de esa nota.
- **[[Patricio Rodrigo Salinas]]**: El monto de las facturas ($57 millones en la nota del hecho) no coincide con las cifras de prensa ($66 millones en facturas de la Corporación Innovación y Democracia a Chile Ambiente); falta confirmarlo en la sentencia. La fecha exacta (7 o 27 de junio de 2017) también está por confirmar.
- **[[TRX-2011-10-05-Facturas-SQM-ChileAmbiente-PPD-01]]**: El monto de $57 millones y el destino del 90% de los fondos no constan en las fuentes citadas (la prensa menciona $66 millones en facturas de la Corporación Innovación y Democracia a Chile Ambiente). Falta confirmarlos en la sentencia.
- **[[TRX-2014-07-24-Sanciones-SVS-CS-Auditorias-PwC-LaPolar-Cascadas-01]]**: El total de 80.000 UF / $2.100 millones no consta en las fuentes citadas; falta desglosar multas y condenas civiles con su fuente.
- **[[TRX-2018-09-12-Sobornos-Itelecom-Licitacion-Iquique-01]]**: El monto de $125 millones no aparece en las fuentes citadas; la Fiscalía solo menciona facturas falsas por más de $171 millones emitidas para ocultar dinero de los sobornos. Falta la cifra de la sentencia.

## Notas sin Fuente Verificable

