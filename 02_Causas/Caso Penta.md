---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2014
tribunal_o_fiscalia: "Fiscalía Nacional / Fiscalía Regional Metropolitana Oriente / 8° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Carlos Gajardo Pinto / Manuel Guerra Fuenzalida"
estado_judicial: cerrada_con_condena
delito_principal: "[[Delito Tributario]]"
estado_verificacion: verificado
fuentes:
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
  - "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
  - "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
  - "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
tags:
  - causa
  - financiamiento-politico
  - caso-penta
---

# Caso Penta

## Ficha Procesal y Ministerio Público
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscales Investigadores**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con [[Cohecho]] y [[Lavado de Activos]])

## Síntesis de la Causa
Investigación penal iniciada a partir de denuncias y querellas del [[Servicio Impuestos Internos]] por devoluciones fraudulentas de impuestos que destapó una estructura sistemática de financiamiento ilegal de campañas políticas de la [[Union Democrata Independiente]] mediante la emisión de boletas de honorarios y facturas ideológicamente falsas contra [[Empresas Penta SA]] ([[TRX-2013-07-15-Boletas-Penta-UDI-01]] y [[TRX-2013-09-20-Boletas-Penta-Novoa-01]]), dirigida por sus controladores [[Carlos Alberto Delano Abbott]] y [[Carlos Eugenio Lavin Garcia-Huidobro]] en beneficio de dirigentes como [[Pablo Longueira Montes]] y el exsenador [[Jovino Novoa Vasquez]] (primer político condenado en juicio abreviado en diciembre de 2015). Asimismo, documentó pagos periódicos de Penta al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]). En julio de 2018 la causa terminó en procedimientos abreviados por **delitos tributarios** ([[Sentencia-8Juzgado-Garantia-Penta-2018]]): la Fiscalía retiró las imputaciones de cohecho y soborno contra los controladores, y Wagner fue absuelto de cohecho y condenado por enriquecimiento ilícito y delitos tributarios.

## Transacciones y Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Lavín y Délano comenzaron las clases de ética tras condena del caso Penta](https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) | 24 Horas | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) |
| [Cartas: 'Good bye' a las clases de ética](https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) | CIPER Chile | `secundaria` | 2024-06-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) |
| [Caso Penta: Tribunal desecha argumentos del CDE y absuelve a exsubsecretario Wagner por cohecho](https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) | Emol | `secundaria` | 2018-07-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) |
| [Caso Penta deja condenas en juicios abreviados y suspensiones](https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) | T13 | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) |
