---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Sociedad Industrial y Metalúrgica Valmoval Limitada (ex Proyectos Integrados / Nihon PSP)"
fecha_constitucion: 1984-06-15
objeto_social: "Fabricación metalmecánica, ensamblaje de armamento ligero (subfusiles PSP) y suministros militares"
representante_legal: "[[Augusto Pinochet Hiriart]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html"
  - "https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
tags:
  - entidad/privada
  - caso-pinocheques
  - industria-militar
---

# Valmoval Ltda

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Beneficiario / Controlador Real**: `= this.representante_legal`

## Contexto en Investigaciones
Empresa metalúrgica y armera declarada en quiebra cuyos activos fueron adquiridos en enero de 1989 por las Fábricas y Maestranzas del Ejército (FAMAE / [[Comando de Apoyo a la Fuerza del Ejercito]]) bajo el mando de [[Augusto Pinochet Ugarte]], girándose tres cheques por cerca de US$ 3 millones (`$2.950.000.000 CLP` actualizados) directamente a nombre de su hijo [[Augusto Pinochet Hiriart]] sin toma de razón de la [[Contraloria General de la Republica]], originando el [[Caso Pinocheques]] ([[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]]) y posterior triangulación hacia [[Riggs Bank y Sociedades Offshore Ashburton]] en el [[Caso Riggs]].

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
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
| [Juez Valderrama sobreseyó arista de los 'Pinocheques' en caso Riggs](https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) | Cooperativa | `secundaria` | 2010-05-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) |
| [Frei descartó presiones militares para cerrar el caso de los 'pinocheques'](https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html) | Cooperativa | `secundaria` | 2004-12-07 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/augusto-pinochet/frei-descarto-presiones-militares-para-cerrar-el-caso-de-los/2004-12-07/082825.html) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
