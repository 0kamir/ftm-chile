---
tipo_nodo: entidad_privada
rut: ""
razon_social: "SCA Chile S.A. (ex Papeles Industriales S.A. - PISA)"
fecha_constitucion: 1978-08-14
objeto_social: "Fabricación y comercialización de productos de papel tissue, pañales y productos absorbentes"
representante_legal: "Gonzalo Eguiguren Correa"
tags:
  - entidad/privada
  - sca-chile
  - pisa
  - caso-colusion-tissue
---

# SCA Chile SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal**: `= this.representante_legal`
- **Controlador Histórico**: Fundada como PISA por [[Gabriel Ruiz-Tagle Serrano]], posteriormente adquirida por la multinacional sueca SCA (actual Essity)

## Contexto en Investigaciones
Fabricante de papel tissue que operó bajo el nombre de PISA hasta su venta al grupo internacional SCA. En el [[Caso Colusion del Papel Tissue]], concertó a partir del año 2000 con [[Empresas CMPC SA]] un esquema ilícito de reparto de cuotas de mercado y fijación de precios ([[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]), estructurado en reuniones clandestinas en hoteles y clubes de golf. Fue sancionada por el TDLC ([[Sentencia-TDLC-160-Colusion-Tissue-2017]]) y ratificada por la [[Corte Suprema de Chile]] con una multa de 20.000 UTA (aproximadamente US$ 15 millones).

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  firmante_origen AS "Operador Origen",
  firmante_destino AS "Operador Destino",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
