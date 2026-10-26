---
tipo_nodo: entidad_privada
rut: ""
razon_social: "SCA Chile S.A. (ex Papeles Industriales S.A. - PISA)"
fecha_constitucion: 1978-08-14
objeto_social: "Fabricación y comercialización de productos de papel tissue, pañales y productos absorbentes"
representante_legal: "Gonzalo Eguiguren Correa"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html"
  - "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml"
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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [TDLC dicta sentencia en caso Tissue](https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) | Emol | `secundaria` | 2017-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) |
| [Suprema condena a CMPC y SCA por colusión](https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) | Emol | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) |
| [CMPC tendrá que pagar una millonaria multa por la colusión del papel](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) | BioBioChile | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) |
