---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Presidencia de la República de Chile"
autoridad_vinculada: "[[Carlos Cruz Lorenzen]]"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
  - "https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html"
  - "https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/"
  - "https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html"
  - "https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/"
  - "https://www.biobiochile.cl/noticias/2013/07/16/victor-manuel-rebolledo-baja-candidatura-tras-criticas-por-su-condena-en-el-caso-coimas.shtml"
tags:
  - entidad/publica
  - ministerio
  - caso-mop-gate
---

# Ministerio de Obras Publicas

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Autoridad Vinculada**: `= this.autoridad_vinculada`

## Contexto en Investigaciones
Secretaría de Estado encargada de la infraestructura vial y concesiones públicas. En el [[Caso MOP-Gate]], la investigación judicial acreditó que bajo la gestión del ex Ministro [[Carlos Cruz Lorenzen]] se suscribieron contratos simulados o con sobreprecios deliberados con consultoras privadas como [[Gestion Ambiental y Territorial SA]] ([[Hector Pena Veliz]]) por **$1.253.000.000 CLP** para desviar caudales fiscales hacia el pago de sobresueldos y gastos extrapresupuestarios ([[TRX-2001-08-20-Contratos-MOP-GATE-01]], [[Sentencia-Corte-Suprema-MOPGate-2016]]).

## Historial de Nexos y Contratos Registrados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Consultora / Contraparte",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas](https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html) | Emol | `secundaria` | 2016-06-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html) |
| [Corte de Apelaciones ratificó condenas en el caso MOP-Gate](https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html) | Cooperativa | `secundaria` | 2014-08-12 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html) |
| [Fraude al fisco: el delito por el cual Jorge Quiroz fue condenado y luego absuelto por la Suprema](https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/) | El Mostrador | `secundaria` | 2026-06-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2026/06/09/fraude-al-fisco-el-delito-por-el-cual-jorge-quiroz-fue-condenado-y-luego-absuelto-por-la-suprema/) |
| [Caso MOP-Gate: ex ministro Carlos Cruz condenado a tres años de pena remitida](https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html) | Emol | `secundaria` | 2010-07-01 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/nacional/2010/07/01/422053/caso-mop-gate-ex-ministro-carlos-cruz-condenado-a-tres-anos-de-pena-remitida.html) |
| [Caso Coimas: Corte Suprema condena a tres exdiputados](https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/) | El Mostrador | `secundaria` | 2007-05-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2007/05/10/corte-suprema-condena-a-tres-ex-diputados-y-absuelve-a-patricio-tombolini/) |
| [Víctor Manuel Rebolledo y las condenas ejecutoriadas del Caso Coimas](https://www.biobiochile.cl/noticias/2013/07/16/victor-manuel-rebolledo-baja-candidatura-tras-criticas-por-su-condena-en-el-caso-coimas.shtml) | BioBioChile | `secundaria` | 2013-07-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/2013/07/16/victor-manuel-rebolledo-baja-candidatura-tras-criticas-por-su-condena-en-el-caso-coimas.shtml) |
