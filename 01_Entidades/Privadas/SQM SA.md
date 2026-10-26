---
tipo_nodo: entidad_privada
rut: "93.007.000-9"
razon_social: "Sociedad Química y Minera de Chile S.A. (SQM)"
fecha_constitucion: "1968-06-29"
objeto_social: "Explotación minera no metálica, producción de litio, yodo y fertilizantes de especialidad"
representante_legal: "[[Patricio Contesse Gonzalez]]"
estado_verificacion: parcial
fuentes:
  - "https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTMwTwMDcwMDAtOQ-jTw/nombre-y-rut/SQM-S.A.-93007000-9"
  - "https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/"
  - "https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/"
  - "https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/"
  - "https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml"
tags:
  - entidad/privada
  - minera
  - caso-sqm
---

# SQM SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Gerente General en Período Investigado**: `= this.representante_legal`

## Contexto y Societario
Empresa minera investigada en el [[Caso SQM]] tras las denuncias y querellas del [[Servicio Impuestos Internos]] ([[Querella-SII-Boletas-SQM-2015]]) por contabilizar como gastos necesarios para producir la renta miles de boletas de honorarios y facturas ideológicamente falsas ([[Delito Tributario]]), empleadas para financiar campañas políticas y pagar beneficios económicos ([[Cohecho]]) asociados a la tramitación del artículo de invariabilidad tributaria del Royalty Minero ([[TRX-2010-08-19-Correo-Royalty-SQM-01]]). La empresa reconoció ante la SEC y el DOJ de EE.UU. pagos indebidos por unos US$ 14,75 millones. En el juicio oral, el 3° TOP de Santiago absolvió en octubre de 2025 a los ocho acusados, incluidos su ex gerente general [[Patricio Contesse Gonzalez]] y [[Pablo Longueira Montes]]; hay recursos de nulidad pendientes.

## Historial de Nexos y Pagos Investigados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Ejecutivo Origen",
  firmante_destino AS "Destinatario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Registro de RUT: SQM S.A.](https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTMwTwMDcwMDAtOQ-jTw/nombre-y-rut/SQM-S.A.-93007000-9) | Genealog (datos SII) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTMwTwMDcwMDAtOQ-jTw/nombre-y-rut/SQM-S.A.-93007000-9) |
| [Fiscalía reconstruye los pasos de Manuel Guerra: así se selló la salida del administrador electoral de Piñera del caso Penta](https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) | CIPER Chile | `secundaria` | 2024-11-10 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/) |
| [Facturas de SQM aterrizan en campaña de Piñera: pagos de 2009 suman $103 millones](https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) | The Clinic | `secundaria` | 2017-09-26 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2017/09/26/facturas-truchas-sqm-aterrizan-campana-pinera-pagos-sqm-2009-suman-103-millones/) |
| [Juicio oral caso SQM tras 8 años de espera](https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) | The Clinic | `secundaria` | 2023-02-13 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2023/02/13/juicio-oral-caso-sqm-8-anos-espera/) |
| [Caso SQM: tribunal absuelve a Pablo Longueira, ME-O, Patricio Contesse y el resto de acusados](https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) | La Tercera | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/caso-sqm-tribunal-absuelve-a-pablo-longueira-me-o-patricio-contesse-y-el-resto-de-acusados-tras-casi-tres-anos-de-juicio/) |
| [Todos absueltos: tribunal da golpe a Fiscalía y dicta veredicto en caso SQM](https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) | BioBioChile | `secundaria` | 2025-10-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2025/10/22/todos-absueltos-tribuanal-da-golpe-a-fiscalia-y-dicta-veredicto-en-caso-sqm.shtml) |
