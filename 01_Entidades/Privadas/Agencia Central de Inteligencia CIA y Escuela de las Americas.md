---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Central Intelligence Agency (Comité 40 / Proyecto FUBELT) & U.S. Army School of the Americas (SOA)"
fecha_constitucion: 1947-09-18
objeto_social: "Operaciones de inteligencia exterior, acción política/económica encubierta y adiestramiento militar contrainsurgente (Fort Gulick, Panamá)"
representante_legal: "[[Manuel Contreras Sepulveda]]"
tags:
  - entidad/privada
  - proyecto-fubelt
  - cia
  - escuela-de-las-americas
---

# Agencia Central de Inteligencia CIA y Escuela de las Americas

## Ficha Institucional y de Archivo Desclasificado
- **RUT Entidad Extranjera / Referencial**: `= this.rut`
- **Denominación Oficial**: `= this.razon_social`
- **Fecha de Creación**: `= this.fecha_constitucion` (Escuela de las Américas fundada en Panamá en 1946; trasladada a Fort Benning en 1984)
- **Función Documentada en Chile**: `= this.objeto_social`
- **Enlace / Activo Remunerado en Chile (1974–1977)**: `= this.representante_legal` (según *Informe Hinchey* de 2000)

## Contexto en Investigaciones
Aparato de inteligencia y entrenamiento militar estadounidense cuyas operaciones encubiertas en Chile entre 1963 y 1977 fueron investigadas y acreditadas oficialmente por el Congreso de los Estados Unidos en el **Informe de la Comisión Church (1975)** y el **Informe Hinchey (2000)** ([[Informe-Comision-Church-1975-y-Hinchey-CIA-2000]]) dentro del [[Caso Operacion FUBELT Intervencion CIA y DINA]]:
1. **Financiamiento a [[Empresa El Mercurio SAP]]**: Desembolso de **US$ 1.950.000** (`$9.500.000.000 CLP`) aprobado por el *Comité 40* en favor del grupo periodístico de [[Agustin Edwards Eastman]] ([[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]]).
2. **Operaciones de Desestabilización y Paros Gremiales / Camioneros**: Canalización de más de **US$ 6 millones** adicionales (`$14.800.000.000 CLP`) hacia organizaciones políticas opositoras, prensa y gremios empresariales que sostuvieron los paros de transportistas y comercio de 1972–1973 ([[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]]).
3. **Adiestramiento en Tortura en la Escuela de las Américas y Pagos a la DINA**: Instrucción de oficiales chilenos en Fort Gulick (Panamá) mediante los manuales del *Proyecto X* (desclasificados por el Pentágono en 1996) y pago de estipendios como activo de la CIA al director de la DINA [[Manuel Contreras Sepulveda]] entre 1974 y 1977 ([[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Receptor en Chile",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
