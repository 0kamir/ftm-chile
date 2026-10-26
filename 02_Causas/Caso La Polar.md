---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2011
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Centro Norte / 2° Juzgado de Garantía de Santiago / Corte Suprema"
fiscal_a_cargo: "José Morales Opazo / Andrés Montes Cruz"
estado_judicial: cerrada
delito_principal: "[[Lavado de Activos]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales"
  - "https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf"
  - "https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/"
tags:
  - causa
  - caso-la-polar
  - mercado-de-valores
  - lavado-de-activos
---

# Caso La Polar

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal`

## Resumen Ejecutivo
Megafraude corporativo y bursátil destapado el **9 de junio de 2011**, cuando la multitienda [[Empresas La Polar SA]] reconoció ante la Superintendencia de Valores y Seguros (hoy [[Comision para el Mercado Financiero]]) la aplicación sistemática y automatizada de **repactaciones unilaterales de deuda** sin consentimiento a cientos de miles de clientes morosos de su tarjeta de crédito ([[TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01]]). La maniobra ocultó la morosidad real de la cartera, infló artificialmente las utilidades contables y permitió a su plana ejecutiva percibir bonos millonarios y vender paquetes accionarios con información privilegiada antes del desplome bursátil.

En sede penal, el 2° Juzgado de Garantía de Santiago dictó en diciembre de 2015 sentencia condenatoria firme ([[Sentencia-Condenatoria-y-Fallo-CS-LaPolar-2015]]) contra el expresidente y exgerente general [[Pablo Alcalde Saavedra]], el exgerente de Productos Financieros [[Julian Moreno de Pablo]] y la exgerenta de Administración [[Maria Isabel Farah Silva]] a penas de 5 años de presidio (bajo libertad vigilada intensiva), comiso de bienes y multas por delitos reiterados de entrega de información falsa al mercado, declaración maliciosamente falsa, uso de información privilegiada (Farah y Moreno) y [[Lavado de Activos]]. Posteriormente, la [[Corte Suprema de Chile]] confirmó las multas regulatorias de la SVS/[[Comision para el Mercado Financiero]] y ratificó la condena civil solidaria contra los exejecutivos por **2.575.388 UF** (`$68.634.000.000 CLP` al valor de la época) por el perjuicio ocasionado a los fondos de pensiones, además de las compensaciones colectivas tramitadas junto al [[Servicio Nacional del Consumidor]].

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [La Polar: Fiscalía Centro Norte obtiene condena de principales ejecutivos por delitos de mercado de valores y lavado de activos](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales) | Fiscalía de Chile | `primaria` | 2015-12-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales) |
| [Sentencia Judicial sobre Sanciones SVS en Caso La Polar](https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf) | Poder Judicial (vía CIPER Chile) | `primaria` | 2014-09-03 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf) |
| [Corte Suprema confirma condena contra ex ejecutivos de La Polar y ordena indemnizar a AFP por pérdidas en fondos de pensiones](https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/) | Diario Constitucional | `secundaria` | 2026-03-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/) |
