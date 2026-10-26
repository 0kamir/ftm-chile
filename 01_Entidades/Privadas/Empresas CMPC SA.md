---
tipo_nodo: entidad_privada
rut: "90.222.000-3"
razon_social: "Empresas CMPC S.A. (CMPC Tissue)"
fecha_constitucion: 1920-03-12
objeto_social: "Fabricación, transformación, comercialización y exportación de celulosa, maderas, papeles y productos tissue"
representante_legal: "Francisco Ruiz-Tagle Edwards"
estado_verificacion: parcial
fuentes:
  - "https://mercantil.com/empresa/empresa-cmpc-sa/santiago/300000090/esp"
  - "https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html"
  - "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml"
  - "https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html"
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

## Contexto en Investigaciones
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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Registro de RUT: Empresas CMPC S.A.](https://mercantil.com/empresa/empresa-cmpc-sa/santiago/300000090/esp) | Mercantil.com | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://mercantil.com/empresa/empresa-cmpc-sa/santiago/300000090/esp) |
| [TDLC dicta sentencia en caso Tissue](https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) | Emol | `secundaria` | 2017-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) |
| [Suprema condena a CMPC y SCA por colusión](https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) | Emol | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) |
| [CMPC tendrá que pagar una millonaria multa por la colusión del papel](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) | BioBioChile | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) |
| [Acuerdo por colusión tissue: CMPC pagará US$150 millones para compensar a consumidores](https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) | Emol | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) |
| [CMPC pagará compensación de 150 millones de dólares: por consumidor serán 7.000 pesos](https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) | Cooperativa | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) |
