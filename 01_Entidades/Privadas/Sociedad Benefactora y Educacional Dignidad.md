---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Sociedad Benefactora y Educacional Dignidad (Holding Villa Baviera / Cerro Florido S.A.)"
fecha_constitucion: 1961-09-20
objeto_social: "Beneficencia, educación, asistencia médica y explotación agrícola, forestal, industrial e inmobiliaria"
representante_legal: "[[Paul Schafer Schneider]]"
tags:
  - entidad/privada
  - caso-colonia-dignidad
  - holding-opaco
---

# Sociedad Benefactora y Educacional Dignidad

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion` (personalidad jurídica cancelada por Decreto Supremo N° 143 de 1991)
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Controlador Histórico**: `= this.representante_legal` (y subdirector [[Hartmut Hopp Miottel]])

## Contexto en Investigaciones Forenses
Corporación de derecho privado constituida en 1961 en Parral (Región del Maule) por [[Paul Schafer Schneider]]. Bajo el amparo de franquicias aduaneras y exenciones impositivas, operó como un enclave territorial cerrado donde se perpetraron crímenes de lesa humanidad, trabajo esclavo de colonos no remunerados, abuso sexual sistemático de menores y acopio de armamento de guerra ([[TRX-2005-06-14-Arsenal-Clandestino-AsociacionIlicita-ColoniaDignidad-01]]). Cuando el Estado canceló su personalidad jurídica en enero de 1991 en el marco del [[Caso Colonia Dignidad]], su directorio ejecutó un vaciamiento patrimonial masivo hacia más de 15 sociedades anónimas comerciales (*Inmobiliaria e Inversiones Cerro Florido S.A.*, *Agrícola Las Acacias S.A.*, *Villa Baviera*) auditado por el [[Servicio Impuestos Internos]] por evasión tributaria y ocultamiento de bienes afectos a comiso ([[TRX-1991-01-31-Vaciamiento-Patrimonial-Evasion-ColoniaDignidad-01]]), contando durante los años noventa con el respaldo político de dirigentes de la [[Union Democrata Independiente]] como el senador [[Hernan Larrain Fernandez]] ([[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte / Fiscalizador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
