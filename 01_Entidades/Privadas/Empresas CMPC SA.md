---
tipo_nodo: entidad_privada
rut: "90.222.000-3"
razon_social: "Empresas CMPC S.A. (CMPC Tissue)"
fecha_constitucion: 1920-03-12
objeto_social: "Fabricación, transformación, comercialización y exportación de celulosa, maderas, papeles y productos tissue"
representante_legal: "Francisco Ruiz-Tagle Edwards"
estado_verificacion: parcial
fuentes:
  - url: "https://mercantil.com/empresa/empresa-cmpc-sa/santiago/300000090/esp"
    titulo: "Registro de RUT: Empresas CMPC S.A."
    medio: "Mercantil.com"
    tipo: secundaria
    consultado: 2026-10-19
tags:
  - entidad/privada
  - cmpc
  - grupo-matte
  - caso-colusion-tissue
---

# Empresas CMPC SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Grupo Controlador**: Grupo Matte (liderado históricamente por [[Eliodoro Matte Larrain]])

## Contexto en Investigaciones Forenses
Matriz forestal y papelera del Grupo Matte. En el [[Caso Colusion del Papel Tissue]], su filial CMPC Tissue protagonizó junto a [[SCA Chile SA]] un cartel que operó entre 2000 y 2015 para fijar precios de venta y repartirse cuotas en el mercado del papel higiénico, servilletas y toallas de papel ([[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]). Tras acogerse a la delación compensada ante la [[Fiscalia Nacional Economica]], pactó con el [[Servicio Nacional del Consumidor]] el desembolso de un fondo reparatorio histórico de **$97.500.000.000 CLP** ([[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]]), siendo posteriormente sancionada por la [[Corte Suprema de Chile]] con una multa de 20.000 UTA al determinarse que había coaccionado a su competidora para sostener el acuerdo.

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
