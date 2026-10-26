---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Farmacias Ahumada S.A. (FASA)"
fecha_constitucion: 1968-11-20
objeto_social: "Comercialización, distribución y venta minorista de productos farmacéuticos, medicinales y artículos de tocador"
representante_legal: "Juan Pablo Corvalán Kramer"
estado_verificacion: verificado
fuentes:
  - "https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf"
  - "https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion"
  - "https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html"
tags:
  - entidad/privada
  - farmacias
  - colusion-farmacias
  - retail-farmaceutico
---

# Farmacias Ahumada SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Fundada por [[Jose Codner Chijner]], posteriormente vendida al consorcio mexicano Casa Saba y luego a Walgreens Boots Alliance

## Contexto en Investigaciones
Cadena de farmacias que junto a [[Farmacias Cruz Verde SA]] y [[Farmacias Salcobrand SA]] conformaba el oligopolio de más del 90% del mercado farmacéutico chileno. En el [[Caso Colusion de las Farmacias]], participó entre diciembre de 2007 y marzo de 2008 en un mecanismo coordinado de alzas de precios en 222 medicamentos críticos para enfermedades crónicas ([[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]). En marzo de 2009, su directorio liderado por [[Jose Codner Chijner]] firmó un acuerdo conciliatorio con la [[Fiscalia Nacional Economica]] admitiendo la colusión e indemnizando con US$ 1 millón ([[Acuerdo-Conciliatorio-FNE-FASA-2009]]), lo que sirvió de prueba decisiva para sancionar a sus competidoras.

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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Sentencia TDLC N° 119/2012 y fallo Corte Suprema Rol 2578-2012](https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) | CentroCompetencia (copia del fallo) | `primaria` | 2012-09-07 | [Wayback ↺](https://web.archive.org/web/*/https://centrocompetencia.com/wp-content/uploads/2022/03/Sentencia_119_Corte_Suprema.pdf) |
| [Suprema confirma acuerdo entre FNE y FASA por caso colusión](https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) | Diario Financiero | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.df.cl/empresas/suprema-confirma-acuerdo-entre-fne-y-fasa-por-caso-colusion) |
| [Grandes cadenas de farmacias deberán pagar compensaciones a clientes tras colusión](https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) | Cooperativa | `secundaria` | 2019-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20191220/pags-amp/20191220104347.html) |
