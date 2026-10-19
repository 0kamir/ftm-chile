---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2015
tribunal_o_fiscalia: "Corte Marcial (Ministra en Visita Romy Rutherford) / Fiscalía Centro Norte"
fiscal_a_cargo: "Romy Rutherford / Ximena Chong"
estado_judicial: cerrada
delito_principal: "[[Malversacion de Caudales Publicos]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/"
    titulo: "Los documentos secretos del Milicogate"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2015-08-18
    consultado: 2026-10-19
  - url: "https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html"
    titulo: "Procesan a general (r) por defraudar al fisco con cerca de 1.800 millones de pesos"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2018-02-11
    consultado: 2026-10-19
tags:
  - causa
  - caso-milicogate
  - ejercito
  - ley-reservada-del-cobre
---

# Caso Milicogate

## Ficha Procesal Penal
- **RUC**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Fiscalía**: `= this.tribunal_o_fiscalia`
- **Ministra en Visita / Fiscal a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial` *(Condenas ejecutoriadas en arista facturas CAF y fallos de la Corte Suprema)*
- **Delito Principal**: `= this.delito_principal` (junto a [[Fraude al Fisco]] y [[Lavado de Activos]])

## Resumen Ejecutivo
Investigación judicial sobre el desfalco de recursos provenientes de la Ley N° 13.196 Reservada del Cobre y de gastos reservados asignados al Ejército de Chile. En la arista de facturas falsas del [[Comando de Apoyo a la Fuerza del Ejercito]] (CAF), oficiales como el general (r) [[Jozo Santic Palomino]] fueron condenados por pagar servicios inexistentes a proveedores coludidos como [[Frasim Ltda]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]) por más de **$6.100.000.000 CLP**, mientras que en la arista gastos reservados fue procesado el ex Comandante en Jefe [[Juan Miguel Fuente-Alba Poblete]] según consta en el [[Procesamientos-Ministra-Rutherford-Milicogate]].

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Repartición Militar",
  entidad_destino AS "Proveedor / Destino",
  firmante_origen AS "Alto Mando",
  firmante_destino AS "Oficial Operador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
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
