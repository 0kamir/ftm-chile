---
tipo_nodo: entidad_privada
rut: "87.107.000-8"
razon_social: "Empresas Penta S.A."
fecha_constitucion: "1986-09-12"
objeto_social: "Holding financiero, inversiones previsionales, seguros, salud e inmobiliaria"
representante_legal: "[[Carlos Alberto Delano Abbott]]"
historial_correcciones:
  - "RUT corregido el 2026-10-19: el vault registraba 96.714.830-K, que no corresponde a la empresa; el RUT verificado es 87.107.000-8."
estado_verificacion: parcial
fuentes:
  - "https://www.portalchile.org/empresa/empresas-penta-spa-87107000"
  - "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
  - "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
  - "https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/"
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
  - "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
tags:
  - entidad/privada
  - holding-financiero
  - caso-penta
---

# Empresas Penta SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador y Representante**: `= this.representante_legal` (junto a [[Carlos Eugenio Lavin Garcia-Huidobro]])

## Contexto y Societario
Holding financiero cuyos controladores [[Carlos Alberto Delano Abbott]] y [[Carlos Eugenio Lavin Garcia-Huidobro]] articularon en el [[Caso Penta]] un mecanismo de rebaja fraudulenta de base imponible ante el [[Servicio Impuestos Internos]] mediante la contabilización de boletas y facturas ideológicamente falsas para financiar campañas de la [[Union Democrata Independiente]] y de [[Pablo Longueira Montes]] ([[TRX-2013-07-15-Boletas-Penta-UDI-01]]), además de realizar pagos bimensuales (sin condena por cohecho: la imputación de soborno fue retirada en 2018) al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]), según [[Sentencia-8Juzgado-Garantia-Penta-2018]].

## Historial de Desembolsos y Nexos Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Destinatario",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Registro de RUT: Empresas Penta](https://www.portalchile.org/empresa/empresas-penta-spa-87107000) | PortalChile (datos SII) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.portalchile.org/empresa/empresas-penta-spa-87107000) |
| [Caso Penta: Tribunal desecha argumentos del CDE y absuelve a exsubsecretario Wagner por cohecho](https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) | Emol | `secundaria` | 2018-07-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) |
| [Caso Penta deja condenas en juicios abreviados y suspensiones](https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) | T13 | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) |
| [Délano y Lavín terminaron clases de ética](https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) |
| [Lavín y Délano comenzaron las clases de ética tras condena del caso Penta](https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) | 24 Horas | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) |
| [Cartas: 'Good bye' a las clases de ética](https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) | CIPER Chile | `secundaria` | 2024-06-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) |
