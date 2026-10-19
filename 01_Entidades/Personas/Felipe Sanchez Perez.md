---
tipo_nodo: persona
rut: ""
aliases:
  - "Felipe Sánchez"
rol_principal: "Representante Legal y Controlador de Inmobiliaria San Valentino SpA"
afiliacion_politica: "Independiente"
situacion_procesal: ninguna
medida_cautelar: "Sin cargos: la Fiscalía decidió no perseverar en la investigación (26-05-2025); nunca fue formalizado/a"
estado_verificacion: verificado
fuentes:
  - url: "https://www.24horas.cl/actualidad/nacional/hassler-sin-cargos-cooper-cierra-investigacion-por-compra-de-sierra-bella"
    titulo: "Hassler sin cargos: Cooper cierra investigación por compra de Sierra Bella"
    medio: "24 Horas"
    tipo: secundaria
    fecha: 2025-05-26
    consultado: 2026-10-19
tags:
  - entidad/persona
  - caso-sierra-bella
---

# Felipe Sanchez Perez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Inmobiliaria San Valentino SpA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Estado Procesal**: `= this.medida_cautelar`

## Síntesis Forense
Abogado y representante legal de [[Inmobiliaria San Valentino SpA]]. En el [[Caso Sierra Bella]], pactó la venta por trato directo del inmueble de calle Sierra Bella a la [[Municipalidad de Santiago]] ([[Iraci Hassler Jacob]]) por **$8.200.000.000 CLP** pocos meses después de haberlo adquirido por cerca de `$2.080.000.000 CLP` ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]), operación bloqueada por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) en el [[Dictamen-CGR-SierraBella-2023]].

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
