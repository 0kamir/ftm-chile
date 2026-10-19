---
tipo_nodo: entidad_privada
rut: "90.193.000-7"
razon_social: "Empresa El Mercurio S.A.P."
fecha_constitucion: 1900-06-01
objeto_social: "Edición, impresión y distribución de periódicos, medios de comunicación y servicios informativos"
representante_legal: "[[Agustin Edwards Eastman]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.genealog.cl/Geneanexus/empresa/CHILE/TOTAxTwOTMwMDAtNw-jTw/nombre-y-rut/EL-MERCURIO-90193000-7"
    titulo: "Registro de RUT: Empresa El Mercurio S.A.P."
    medio: "Genealog (datos SII)"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - entidad/privada
  - proyecto-fubelt
  - el-mercurio
  - medios-comunicacion
---

# Empresa El Mercurio SAP

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador Histórico**: `= this.representante_legal`

## Contexto en Investigaciones Forenses y Archivos Desclasificados
Sociedad editora del diario *El Mercurio*, *Las Últimas Noticias* y *La Segunda*, presidida y controlada por [[Agustin Edwards Eastman]]. En el [[Caso Operacion FUBELT Intervencion CIA y DINA]], el **Informe de la Comisión Church del Senado de los Estados Unidos (1975)** ([[Informe-Comision-Church-1975-y-Hinchey-CIA-2000]]) documentó oficialmente que, tras las gestiones personales de [[Agustin Edwards Eastman]] en Washington en septiembre de 1970, el *"Comité 40"* del Consejo de Seguridad Nacional de EE.UU. autorizó transferencias encubiertas desde la [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] hacia [[Empresa El Mercurio SAP]] por **US$ 1.950.000** entre 1971 y 1973 (`$9.500.000.000 CLP` actualizados en [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]]) para financiar su operación editorial y campañas de desestabilización previas al golpe de Estado de 1973. Décadas más tarde, su controlador [[Agustin Edwards Eastman]] apareció en el [[Caso Panama Papers Chile]] como titular de fundaciones *offshore* estructuradas por [[Mossack Fonseca y Sociedades Offshore Panama]] ([[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
