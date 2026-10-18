---
tipo_nodo: entidad_privada
rut: "70.012.450-9"
razon_social: "Fundación de Centros de Madres CEMA Chile"
fecha_constitucion: 1954-10-05
objeto_social: "Asistencia social, capacitación artesanal y administración de centros de madres"
representante_legal: "[[Lucia Hiriart Rodriguez]]"
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

## Contexto en Investigaciones Forenses
Corporación de derecho privado cuya dirección fue ejercida a perpetuidad por [[Lucia Hiriart Rodriguez]], cónyuge de [[Augusto Pinochet Ugarte]], tras una reforma estatutaria realizada antes del fin de la dictadura en 1989. En el [[Caso CEMA Chile]], el Ministro en Visita Guillermo de la Barra y el Consejo de Defensa del Estado acreditaron que la entidad recibió gratuitamente más de **135 inmuebles fiscales, municipales y del SERVIU**, procediendo entre 1990 y 2016 a enajenar comercialmente decenas de propiedades por más de `$8.900.000.000 CLP` y a distraer fondos de su giro social. Tras el embargo judicial y las acciones ante la [[Corte Suprema de Chile]], la fundación fue disuelta y obligada a restituir al Estado **108 bienes raíces y la totalidad de sus fondos líquidos**, valorizados en más de **`$10.500.000.000 CLP`** ([[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]] y [[Acuerdo-Judicial-Restitucion-CEMAChile-2019]]).

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
