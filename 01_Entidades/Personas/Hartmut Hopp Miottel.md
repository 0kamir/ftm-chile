---
tipo_nodo: persona
rut: ""
aliases:
  - "Hartmut Hopp"
rol_principal: "Director Médico, Vocero y Subdirector Administrativo de Colonia Dignidad (Villa Baviera)"
afiliacion_politica: "Independiente (Operador de relaciones políticas del enclave)"
situacion_procesal: condenado
medida_cautelar: "Prófugo de la justicia chilena en Alemania desde 2011 (Condenado a 5 años y 1 día de presidio efectivo por la Corte Suprema de Chile)"
tags:
  - entidad/persona
  - caso-colonia-dignidad
  - profugo
---

# Hartmut Hopp Miottel

## Perfil Biográfico e Institucional
- **RUT / Cédula Extranjería**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Médico, director del hospital de Villa Baviera y principal articulador político, financiero y público de [[Paul Schafer Schneider]] en [[Sociedad Benefactora y Educacional Dignidad]]. Durante los años noventa encabezó las relaciones institucionales del enclave con autoridades parlamentarias y dirigentes de la [[Union Democrata Independiente]] como el senador [[Hernan Larrain Fernandez]] para resistir la disolución jurídica de la corporación y obstaculizar los operativos policiales ([[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]]). En el [[Caso Colonia Dignidad]], fue condenado por el Ministro en Visita [[Jorge Zepeda Arancibia]] y ratificado en sentencia definitiva por la [[Corte Suprema de Chile]] a **5 años y un día de presidio efectivo** como cómplice de abusos sexuales reiterados de menores y miembro de asociación ilícita ([[Sentencia-Corte-Suprema-ColoniaDignidad-2013]]), fugándose del país hacia Krefeld (Alemania) en mayo de 2011 antes de que la sentencia quedara ejecutoriada.

## Nexos y Actuaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```
