---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PDI-BRILAC-TRIBUTOS-2023"
tipo_documento: "Informe Policial y Actas de Allanamiento Masivo de la Brigada de Lavado de Activos (BRILAC)"
fecha_emision: 2023-12-14
organismo_emisor: "[[Direccion de Inteligencia Policial de Carabineros]]"
fuente_osint: "Policía de Investigaciones de Chile (investigaciones.cl) / Fiscalía de Chile"
causa_vinculada: "[[Caso Megafraude Tributario Operacion Tributos]]"
nexo_respaldado: "[[TRX-2023-12-15-Lavado-Activos-Bienes-Inmuebles-Clan-Pavez-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml"
    titulo: "SII confirma que 55 empresarios detenidos concretaron el mayor fraude"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2023-12-15
    consultado: 2026-10-19
tags:
  - evidencia/policial
  - pdi
  - brilac
  - allanamientos
  - operacion-tributos
---

# Informe-BRILAC-PDI-Operacion-Tributos-2023

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Emisión**: `= this.fecha_emision`
- **Organismo Policial Ejecutor**: Brigada Investigadora de Lavado de Activos (BRILAC) - PDI
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Informe de resultados del operativo simultáneo nacional llevado a cabo el 14 de diciembre de 2023 en 83 inmuebles distribuidos en 10 regiones del país. En el operativo se incautaron automóviles de alta gama, armas de fuego, más de $2.000 millones en efectivo y divisas, lingotes de oro, dispositivos electrónicos con trazabilidad contable y billeteras frías de criptoactivos vinculadas al esquema de blanqueo de [[Jose Antonio Pavez Campillay]] y las empresas pantalla.

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
