---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 97 N° 4 del Código Tributario (D.L. N° 830)"
bien_juridico: "Hacienda Pública y orden público tributario"
pena_referencial: "Presidio menor en su grado medio a máximo y multa del 50% al 300% de lo defraudado"
prescripcion_anos: 5
tags:
  - delito/tributario
---

# Delito Tributario

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Declaraciones maliciosamente incompletas o falsas que puedan inducir a la liquidación de un impuesto inferior al que corresponda, o la facilitación de boletas de honorarios y facturas ideológicamente falsas para rebajar artificialmente la base imponible del Impuesto de Primera Categoría (mecanismo empleado en el financiamiento ilegal de campañas políticas y en redes de factoring).

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(delito_imputado), this.file.name)
SORT fecha DESC
```
