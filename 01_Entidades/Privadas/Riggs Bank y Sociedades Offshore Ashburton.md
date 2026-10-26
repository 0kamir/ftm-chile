---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Riggs Bank N.A. & Estructuras Offshore (Ashburton Company Ltd. / Althorp Investment Co.)"
fecha_constitucion: 1994-03-22
objeto_social: "Banca privada internacional, fideicomisos offshore y vehículos de inversión en Bahamas, Islas Vírgenes Británicas y EE.UU."
representante_legal: "[[Oscar Aitken Lavanchy]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
  - "https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/"
  - "https://offshoreleaks.icij.org/"
  - "https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html"
  - "https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html"
tags:
  - entidad/privada
  - caso-riggs
  - offshore
  - lavado-activos
---

# Riggs Bank y Sociedades Offshore Ashburton

## Ficha Societaria e Institucional
- **RUT Inversionista Extranjero / Referencial**: `= this.rut`
- **Razón Social / Red Fiduciaria**: `= this.razon_social`
- **Fecha de Constitución Red Offshore**: `= this.fecha_constitucion` (operativa entre 1985 y 2004)
- **Objeto Social**: `= this.objeto_social`
- **Estructurador / Apoderado Fiduciario**: `= this.representante_legal` (en beneficio de [[Augusto Pinochet Ugarte]] y [[Lucia Hiriart Rodriguez]])

## Contexto en Investigaciones
Complejo bancario y societario *offshore* con centro en el **Riggs Bank** de Washington D.C. y ramificaciones en Bahamas, Islas Vírgenes Británicas, Panamá y Gibraltar (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*, *Sonder S.A.*). En el [[Caso Riggs]], el Subcomité de Investigaciones del Senado de EE.UU. y el Ministro en Visita [[Sergio Munoz Gajardo]] acreditaron que esta estructura albergó más de **125 cuentas secretas** y certificados de depósito de [[Augusto Pinochet Ugarte]] (bajo identidades falsas como *"Daniel López"*), nutriéndose de la malversación de gastos reservados del Ejército ([[TRX-2004-07-14-Gastos-Reservados-Riggs-01]]) y evadiendo impuestos ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]]). En 2018, la [[Corte Suprema de Chile]] decretó el comiso definitivo de los saldos y bienes asociados a favor del Fisco ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).

## Transacciones y Flujos Vinculados
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
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
| [The Panama Papers: los secretos de chilenos en paraísos fiscales](https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) | CIPER Chile | `secundaria` | 2016-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) |
| [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/) | ICIJ | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://offshoreleaks.icij.org/) |
| [Juez Valderrama sobreseyó arista de los 'Pinocheques' en caso Riggs](https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) | Cooperativa | `secundaria` | 2010-05-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) |
| [Frei descartó presiones militares para cerrar el caso de los 'pinocheques'](https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html) | Cooperativa | `secundaria` | 2004-12-07 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html) |
