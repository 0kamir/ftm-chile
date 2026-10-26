---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Consejo Local de Deportes Vitacura (Vita Deportes)"
fecha_constitucion: "2001-06-12"
objeto_social: "Fomento del deporte comunal y administración de recintos deportivos en Vitacura"
representante_legal: "[[Domingo Prieto Urrejola]]"
estado_verificacion: verificado
fuentes:
  - "https://www.ex-ante.cl/?p=152080"
  - "https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/"
  - "https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html"
tags:
  - entidad/privada
  - organizacion-comunitaria
  - caso-vitacura
---

# Vita Deportes

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`

## Contexto y Societario
Organización comunitaria funcional que recibía cuantiosas subvenciones anuales de la [[Municipalidad de Vitacura]]. En el [[Caso Vitacura]], su expresidente y representante legal [[Domingo Prieto Urrejola]] reveló mediante [[Declaracion-Judicial-Prieto-Vitacura-2021]] el mecanismo de extracción en efectivo de fondos provenientes de subvenciones municipales ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]]) entregados a [[Raul Torrealba del Pedregal]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_destino AS "Firmante Receptor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Audiencia de formalización de Raúl Torrealba](https://www.ex-ante.cl/?p=152080) | Ex-Ante | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.ex-ante.cl/?p=152080) |
| [Fiscalía formalizará a exalcalde Raúl Torrealba por fraude al fisco y asociación ilícita](https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) | La Tercera | `secundaria` | 2023-05-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-pm/noticia/fiscalia-formalizara-a-exalcalde-raul-torrealba-por-fraude-al-fisco-y-ademas-lo-imputara-como-lider-de-una-asociacion-ilicita-que-opero-en-vitacura/4Z5EW4AI5VFNRDG6YE6J4FFEI4/) |
| [Formalizan a exalcalde Raúl Torrealba](https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) | Pauta | `secundaria` | 2023-06-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2023/06/15/formalizan-a-exalcalde-raul-torrealba-yo-quiero-que-la-institucion.html) |
