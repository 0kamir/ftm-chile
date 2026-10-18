---
tipo_nodo: entidad_privada
rut: "96.814.520-7"
razon_social: "Gestión Ambiental y Territorial S.A. (GESCAM S.A.)"
fecha_constitucion: "1996-05-14"
objeto_social: "Consultoría en ingeniería, gestión ambiental, estudios territoriales y asesoría vial"
representante_legal: "[[Roberto Lewin Valdivieso]]"
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
Empresa consultora (conocida por su sigla **GESCAM S.A.**) que operó como nodo central de triangulación financiera en el [[Caso MOP-Gate]]. A través de contratos adjudicados por el [[Ministerio de Obras Publicas]] bajo la dirección de [[Carlos Cruz Lorenzen]] ([[TRX-2001-08-20-Contratos-Simulados-MOP-GESCAM-01]]) y la emisión de facturas por estudios inexistentes o sobrevalorados ante el [[Servicio Impuestos Internos]] ([[TRX-2002-04-12-Facturas-Triangulacion-GESCAM-SII-01]]), reintegraba fondos en efectivo y cheques para financiar sobresueldos ministeriales, según acreditó la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-MOPGate-2016]].

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
