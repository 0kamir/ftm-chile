---
tipo_nodo: tipo_penal
articulo_cp: "Artículo 27 de la Ley N° 19.913 (UAF)"
bien_juridico: "Orden público económico y administración de justicia"
pena_referencial: "Presidio mayor en sus grados mínimo a medio y multa de 200 a 1.000 UTM"
prescripcion_anos: 10
tags:
  - delito/lavado-de-activos
---

# Lavado de Activos

## Tipificación Legal en Chile
- **Norma**: `= this.articulo_cp`
- **Bien Jurídico Protegido**: `= this.bien_juridico`
- **Marco Penal**: `= this.pena_referencial`

Ocultamiento o disimulación del origen ilícito de determinados bienes, a sabiendas de que proceden, directa o indirectamente, de la perpetración de delitos base (incluyendo fraude al fisco, cohecho, malversación de caudales públicos y delitos tributarios o de la Ley de Mercado de Valores).

## Nexos e Imputaciones Vinculadas a este Delito
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(delito_imputado), this.file.name)
SORT fecha DESC
```
