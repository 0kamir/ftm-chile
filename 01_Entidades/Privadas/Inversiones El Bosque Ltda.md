---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Inversiones y Centro de Eventos El Bosque Limitada (Go Fitness)"
fecha_constitucion: 1998-04-14
objeto_social: "Inversiones inmobiliarias, administración de centros deportivos, gimnasios, estética y eventos"
representante_legal: "[[Claudio Spiniak Vilensky]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html"
  - "https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html"
  - "https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html"
  - "https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz"
tags:
  - entidad/privada
  - caso-spiniak
  - sociedad-pantalla
---

# Inversiones El Bosque Ltda

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`

## Contexto en Investigaciones
Sociedad instrumental controlada por [[Claudio Spiniak Vilensky]] a través de la cual operaba el gimnasio *Go Fitness* en calle El Bosque Norte (Las Condes) y propiedades en El Arrayán. En el marco del [[Caso Spiniak]], el [[Servicio Impuestos Internos]] y la instrucción judicial del ministro [[Sergio Munoz Gajardo]] auditaron el uso de la sociedad para encubrir egresos ilícitos, gastos rechazados y evasión tributaria ([[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]]), documentados en [[Sentencia-Corte-Suprema-CasoSpiniak-2008]].

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte / Fiscalizador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Falleció Claudio Spiniak, empresario condenado por liderar una red de pedofilia](https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) | Cooperativa | `secundaria` | 2026-03-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20260313/pags-amp/20260313185017.html) |
| [Claudio Spiniak fue condenado a cinco años y un día de cárcel](https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) | Cooperativa | `secundaria` | 2006-08-10 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) |
| [Muere Claudio Spiniak](https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) | Emol | `secundaria` | 2026-03-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) |
| [Jovino Novoa, caso Spiniak e investigación del juez Sergio Muñoz](https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) | Pauta | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) |
