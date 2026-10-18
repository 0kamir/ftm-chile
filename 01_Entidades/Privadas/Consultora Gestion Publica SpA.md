---
tipo_nodo: entidad_privada
rut: "77.314.890-2"
razon_social: "Consultora Gestión Pública y Estudios SpA"
fecha_constitucion: "2023-03-10"
objeto_social: "Asesorías en gestión pública, transformación digital y estudios estratégicos"
representante_legal: "[[Jorge Valdivia Correa]]"
tags:
  - entidad/privada
  - proveedor-estado
  - compras-publicas
---

# Consultora Gestion Publica SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`

## Contexto Forense y Societario
Sociedad por acciones constituida en marzo de 2023 en el registro "Tu Empresa en un Día" y adjudicataria de trato directo 157 días después ([[TRX-2023-08-14-Trato-Directo-ChileCompra-01]]) por **$45.800.000 CLP**, documentado en [[Orden-Compra-MercadoPublico-2023]] y monitoreado en el [[Caso Compras Publicas]] bajo hipótesis preliminar de [[Negociacion Incompatible]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Compradora",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```
