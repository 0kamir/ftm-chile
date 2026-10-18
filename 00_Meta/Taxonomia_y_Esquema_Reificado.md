---
tipo_nodo: meta_taxonomia
version_esquema: "1.0.0"
estandar_referencia: "OCCRP FollowTheMoney (FtM) / ICIJ Graph Model"
tags:
  - meta/taxonomia
  - meta/esquema
---

# Taxonomía y Arquitectura de Grafos Reificados (Estándar Aleph / ICIJ)

## 1. Por qué Reificar las Aristas (`03_Hechos_y_Nexos/`)
En un grafo de conocimiento tradicional de Obsidian, un enlace directo `[[Seremi MINVU Antofagasta]] --> [[Fundacion Democracia Viva]]` es una arista simple sin propiedades: no permite almacenar fecha, monto en CLP, firmantes, delito imputado ni resolución exenta de respaldo.

Siguiendo el modelo **FollowTheMoney (OCCRP Aleph)** e **ICIJ Offshore Leaks**, cada transacción, convenio, pago, llamada o reunión de lobby se modela como un **nodo intermedio (arista reificada)** ubicado en `03_Hechos_y_Nexos/`.

```
[Entidad Origen] ──┐
                   ▼
[Firmante Origen] ─► ( TRX-YYYY-MM-DD-Convenio ) ◄── [Evidencia Soporte]
                   │              │
                   ▼              ▼
[Entidad Destino] ─┘      [Causa Judicial]
```

## 2. Vocabulario Controlado de Propiedades YAML

### `situacion_procesal` (en `tpl_persona.md`)
- `ninguna`: Sin imputación formal conocida.
- `testigo`: Declarante o sujeto de interés no formalizado.
- `formalizado`: Comunicación formal de cargos ante Juzgado de Garantía.
- `condenado`: Sentencia condenatoria ejecutoriada (procedimiento abreviado o juicio oral).

### `categoria` (en `tpl_entidad_publica.md`)
- `GORE`: Gobierno Regional.
- `Ministerio`: Ministerio, Subsecretaría, SEREMI o Servicio dependiente.
- `Municipio`: Municipalidad o Corporación Municipal.
- `Poder Judicial`: Tribunales, Cortes o Ministerio Público.

### `estado_judicial` (en `tpl_causa.md`)
- `investigacion`: Investigación desformalizada.
- `formalizada`: Investigación formalizada con plazo judicial vigente.
- `juicio_oral`: Acusación presentada / Auto de apertura de juicio oral.
- `cerrada`: Sobreseimiento definitivo, sentencia firme o archivo.

### `tipo_nexo` (en `tpl_nexo_transaccion.md`)
- `convenio_directo`: Asignación directa de fondos públicos a entidades privadas.
- `transferencia`: Traspaso bancario o remesa específica.
- `cohecho`: Soborno o beneficio económico ilícito.
- `llamada`: Comunicación telefónica o mensajería periciada.
- `reunion_lobby`: Audiencia registrada por Ley N° 20.730 o reunión extrainstitucional.
