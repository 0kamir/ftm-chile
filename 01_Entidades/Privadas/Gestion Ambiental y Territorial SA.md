---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Gestión Ambiental y Territorial S.A. (GATE)"
fecha_constitucion: ""
objeto_social: "Consultoría en ingeniería, gestión ambiental, estudios territoriales y asesoría vial"
representante_legal: "[[Hector Pena Veliz]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
    titulo: "Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas"
    medio: "Emol"
    tipo: secundaria
    fecha: 2016-06-29
    consultado: 2026-10-19
historial_correcciones:
  - "RUT y fecha de constitución eliminados por no constar en fuente pública."
tags:
  - entidad/privada
  - consultora-ingenieria
  - caso-mop-gate
---

# Gestion Ambiental y Territorial SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal y Controlador**: `= this.representante_legal`

## Contexto Forense y Societario
Empresa consultora (conocida por su sigla **GATE**) que operó como nodo central de triangulación financiera en el [[Caso MOP-Gate]]. A través de contratos adjudicados por el [[Ministerio de Obras Publicas]] bajo la dirección de [[Carlos Cruz Lorenzen]] ([[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]), reintegraba fondos en efectivo y cheques para financiar sobresueldos ministeriales, según acreditó la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-MOPGate-2016]].

## Historial de Contratos y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

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
