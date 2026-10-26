---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Fundación de Centros de Madres CEMA Chile"
fecha_constitucion: 1954-10-05
objeto_social: "Asistencia social, capacitación artesanal y administración de centros de madres"
representante_legal: "[[Lucia Hiriart Rodriguez]]"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html"
  - "https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/"
  - "https://www.theclinic.cl/2016/12/29/lo-que-declaro-lucia-hiriart-por-el-caso-cema-chile-por-mi-no-pasaba-ni-un-centavo/"
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
tags:
  - entidad/privada
  - caso-cema-chile
  - fundacion
  - bienes-fiscales
---

# Fundacion CEMA Chile

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion` (estatutos privatizados en 1989; disuelta y liquidada a favor del Fisco en 2019)
- **Objeto Social**: `= this.objeto_social`
- **Presidenta Vitalicia (1973–2016)**: `= this.representante_legal`

## Contexto en Investigaciones
Corporación de derecho privado cuya dirección fue ejercida a perpetuidad por [[Lucia Hiriart Rodriguez]], cónyuge de [[Augusto Pinochet Ugarte]], tras una reforma estatutaria realizada antes del fin de la dictadura en 1989. En el [[Caso CEMA Chile]], el Ministro en Visita Guillermo de la Barra y el Consejo de Defensa del Estado señalaron que la entidad recibió gratuitamente más de **135 inmuebles fiscales, municipales y del SERVIU**, procediendo entre 1990 y 2016 a enajenar comercialmente decenas de propiedades por más de `$8.900.000.000 CLP` y a destinar fondos, según los querellantes, a fines ajenos a su giro social. Tras el embargo judicial y las acciones ante la [[Corte Suprema de Chile]], la fundación fue disuelta vía CDE (2021) tras traspasar sus bienes al Fisco y a fundaciones de beneficencia (según Emol, el Estado recuperó más de $18.000 millones; la cifra de $10.500 millones previa no tiene fuente) ([[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] y [[Disolucion-CDE-Fundacion-CEMAChile-2021]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte / Receptor",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Falleció Lucía Hiriart (menciona recuperación de bienes vía CDE)](https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html) | Emol | `secundaria` | 2021-12-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2021/12/16/1041401/fallecio-lucia-hiriart.html) |
| [Caso CEMA Chile: querella por fraude al fisco](https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/) | The Clinic | `secundaria` | 2016-08-23 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2016/08/23/caso-cema-chile-fraude-al-fisco/) |
| [Lo que declaró Lucía Hiriart por el caso CEMA Chile](https://www.theclinic.cl/2016/12/29/lo-que-declaro-lucia-hiriart-por-el-caso-cema-chile-por-mi-no-pasaba-ni-un-centavo/) | The Clinic | `secundaria` | 2016-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2016/12/29/lo-que-declaro-lucia-hiriart-por-el-caso-cema-chile-por-mi-no-pasaba-ni-un-centavo/) |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
