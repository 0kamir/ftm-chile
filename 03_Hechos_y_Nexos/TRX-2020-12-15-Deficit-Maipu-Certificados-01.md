---
tipo_nodo: nexo_transaccion
fecha: 2020-12-15
tipo_nexo: transferencia
monto_clp: 30972000000
monto_origen: resolucion_administrativa
entidad_origen: "[[Municipalidad de Maipu]]"
entidad_destino: "[[Municipalidad de Maipu]]"
firmante_origen: "[[Cathy Barriga Guerra]]"
firmante_destino: "[[Cathy Barriga Guerra]]"
causa_vinculada: "[[Caso Municipalidad de Maipu]]"
delito_imputado: "[[Fraude al Fisco]]"
evidencia_soporte: "[[Informe-Contraloria-Municipalidad-Maipu-2021]]"
estado_verificacion: verificado
fuentes:
  - "https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/"
  - "https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/"
  - "https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/"
  - "https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html"
tags:
  - nexo/transaccion
  - fraude-municipal
  - caso-maipu
---

# TRX-2020-12-15-Deficit-Maipu-Certificados-01

## Ficha de Arista Reificada (Defraudación Presupuestaria y Certificados Ideológicamente Falsos)
- **Fecha del Hecho**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Entidad de Origen**: `= this.entidad_origen`
- **Entidad Afectada**: `= this.entidad_destino`
- **Autoridad Imputada**: `= this.firmante_origen`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Imputado**: `= this.delito_imputado`
- **Evidencia Documental**: `= this.evidencia_soporte`

## Descripción de la Operación
Déficit presupuestario, que la Fiscalía imputa como fraude al fisco, en la [[Municipalidad de Maipu]] bajo la administración de [[Cathy Barriga Guerra]] por **$30.972.000.000 CLP**, atribuido por la acusación a la emisión de Certificados de Disponibilidad Presupuestaria (CDP) sin respaldo contable, ocultamiento de pasivos devengados y desvío de fondos de uso exclusivo (como recursos de la sanitaria municipal SMAPA), según consta en el [[Informe-Contraloria-Municipalidad-Maipu-2021]] y la formalización del [[Caso Municipalidad de Maipu]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Expediente Cathy Barriga: las pruebas clave](https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-sabado/noticia/expediente-cathy-barriga-las-pruebas-clave-en-la-antesala-de-su-formalizacion-por-fraude-al-fisco/X3WAFR5PRNAJVPROK23QPVIHTM/) |
| [Formalización de Cathy Barriga: qué delitos le imputan](https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) | CNN Chile | `secundaria` | 2024-01-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formalizacion-cathy-barriga-que-delitos-imputan_20240116/) |
| [Exalcaldesa Cathy Barriga será formalizada en enero de 2024](https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) | El Mostrador | `secundaria` | 2023-11-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2023/11/28/exalcaldesa-cathy-barriga-sera-formalizada-en-enero-de-2024-por-fraude-al-fisco-y-corrupcion/) |
| [Caso Maipú: Fiscalía Oriente reformalizará a Cathy Barriga](https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) | Meganoticias | `secundaria` | 2024-08-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/456234-cathy-barriga-reformalizacion-maipu-fiscalia-mega-investiga-19-08-2024.html) |
