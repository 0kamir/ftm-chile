---
tipo_nodo: entidad_privada
rut: "89.807.200-2"
razon_social: "Farmacias Cruz Verde S.A. (Socofar)"
fecha_constitucion: 1984-01-05
objeto_social: "Distribución, droguería, importación y venta al por menor de medicamentos e insumos médicos"
representante_legal: "Eduardo Castillo Castillo"
estado_verificacion: parcial
fuentes:
  - url: "https://www.portalchile.org/empresa/farmacias-cruz-verde-spa-89807200"
    titulo: "Registro de RUT: Farmacias Cruz Verde"
    medio: "PortalChile (datos SII)"
    tipo: secundaria
    consultado: 2026-10-19
historial_correcciones:
  - "RUT corregido el 2026-10-19: el vault registraba 96.677.000-7, que no corresponde a la empresa; el RUT verificado es 89.807.200-2."
tags:
  - entidad/privada
  - farmacias
  - cruz-verde
  - colusion-farmacias
---

# Farmacias Cruz Verde SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Fundada por [[Guillermo Harding Alvarado]] (Grupo Socofar), posteriormente adquirida por la multinacional mexicana FEMSA

## Contexto en Investigaciones Forenses
Cadena de farmacias líder en cobertura a nivel nacional. En el [[Caso Colusion de las Farmacias]], coordinó junto a [[Farmacias Salcobrand SA]] y [[Farmacias Ahumada SA]] alzas simultáneas y concertadas de precios en 222 medicamentos entre diciembre de 2007 y marzo de 2008 mediante contactos triangulados con laboratorios proveedores farmacéuticos ([[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]). Fue condenada por el TDLC ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) y confirmada por la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]) a pagar la multa máxima de **20.000 UTA** (aproximadamente US$ 19 millones), y en sede civil al pago de compensaciones directas a los consumidores afectados ([[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]).

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
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
