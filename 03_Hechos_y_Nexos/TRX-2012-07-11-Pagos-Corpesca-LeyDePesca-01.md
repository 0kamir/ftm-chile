---
tipo_nodo: nexo_transaccion
fecha: 2012-07-11
tipo_nexo: cohecho
monto_clp: 233000000
monto_origen: sentencia
entidad_origen: "[[Corpesca SA]]"
entidad_destino: "[[Senado de la Republica de Chile]]"
firmante_origen: "[[Francisco Mujica Ortuzar]]"
firmante_destino: "[[Jaime Orpis Bouchon]]"
causa_vinculada: "[[Caso Corpesca]]"
delito_imputado: "[[Cohecho]]"
evidencia_soporte: "[[Sentencia-3TOP-Santiago-Corpesca-2021]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html"
tags:
  - nexo/transaccion
  - cohecho
  - caso-corpesca
  - captura-legislativa
---

# TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01

## Ficha de Arista Reificada (Soborno Parlamentario en Tramitación de Ley de Pesca)
- **Fecha de Votación / Período Clave**: `= this.fecha`
- **Tipo de Nexo**: `= this.tipo_nexo`
- **Monto Involucrado Consolidado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")``
- **Empresa Sobornante**: `= this.entidad_origen`
- **Órgano Público Afectado**: `= this.entidad_destino`
- **Ejecutivo Autorizador**: `= this.firmante_origen`
- **Parlamentario Receptor**: `= this.firmante_destino`
- **Causa Judicial Vinculada**: `= this.causa_vinculada`
- **Delito Condenado**: `= this.delito_imputado` (en concurso con [[Delito Tributario]])
- **Evidencia / Sentencia Firme**: `= this.evidencia_soporte`

## Descripción de la Operación
Pagos ilícitos reiterados por un total acreditado en juicio oral de **$233.000.000 CLP** efectuados entre 2009 y 2013 por [[Corpesca SA]] (bajo instrucción de su gerente general [[Francisco Mujica Ortuzar]]) a favor del entonces senador [[Jaime Orpis Bouchon]] ([[Union Democrata Independiente]]) mediante boletas de honorarios ideológicamente falsas emitidas por terceros, con el objeto de asegurar su actuación y voto favorable a los intereses de la pesquera durante la tramitación de la Ley General de Pesca y Acuicultura en el [[Senado de la Republica de Chile]], hechos condenados mediante [[Sentencia-3TOP-Santiago-Corpesca-2021]] en el [[Caso Corpesca]].

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Corpesca: Jaime Orpis fue condenado por fraude al Fisco y cohecho](https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html) | Cooperativa | `secundaria` | 2020-12-02 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20201202/pags-amp/20201202131131.html) |
| [Ex senador Jaime Orpis irá a la cárcel por fraude al Fisco y cohecho](https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html) | Cooperativa | `secundaria` | 2021-04-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20210416/pags-amp/20210416121129.html) |
| [Corte confirmó la pena de cárcel para el ex senador Jaime Orpis](https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html) | Cooperativa | `secundaria` | 2022-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20220106/pags-amp/20220106164027.html) |
