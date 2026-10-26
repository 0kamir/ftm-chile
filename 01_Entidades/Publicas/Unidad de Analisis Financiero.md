---
tipo_nodo: entidad_publica
rut: ""
categoria: Servicio Público Fiscalizador
region: "Metropolitana de Santiago (Alcance Nacional)"
superior_jerarquico: "Ministerio de Hacienda"
autoridad_vinculada: "[[Javier Cruz Tamburrino]]"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html"
  - "https://vlex.cl/vid/corte-marcial-revoca-condena-844999287"
  - "https://www.elciudadano.com/?p=683869"
  - "https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/"
  - "https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/"
  - "https://offshoreleaks.icij.org/"
tags:
  - entidad/publica
  - inteligencia-financiera
  - uaf
  - lavado-activos
---

# Unidad de Analisis Financiero

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`
- **Ex Director Vinculado en Reportes**: `= this.autoridad_vinculada`

## Contexto en Investigaciones
Servicio público descentralizado encargado de prevenir e impedir la utilización del sistema financiero y de otros sectores de la actividad económica para la comisión de los delitos de [[Lavado de Activos]] y financiamiento del terrorismo (Ley N° 19.913). En el grafo actúa como nodo articulador de inteligencia patrimonial al haber emitido los **Reportes de Operaciones Sospechosas (ROS)** que permitieron al Ministerio Público y al Consejo de Defensa del Estado trazabilizar:
1. El blanqueo de gastos reservados en el [[Caso Milicogate]] por parte de [[Juan Miguel Fuente-Alba Poblete]] ([[TRX-2015-08-14-GastosReservados-Ejercito-UAF-01]]).
2. La red de testaferros y adquisición de bienes raíces con caudales sustraídos de la [[Direccion de Finanzas de Carabineros]] en el [[Caso Pacogate]] por [[Flavio Echeverria Cortez]] ([[TRX-2017-03-06-Reportes-UAF-Carabineros-01]]).
3. Las alertas de operaciones de factoring ficticio de [[Factop SpA]] y [[Luis Hermosilla Osorio]] en el [[Caso Audios]].

## Historial de Nexos y Reportes de Inteligencia Financiera
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación Reportada",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen del Flujo",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Procesan a general (r) por defraudar al fisco con cerca de 1.800 millones](https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) | Cooperativa | `secundaria` | 2018-02-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) |
| [Corte Marcial revoca condena por fraude a general (r) Santic](https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) | vLex Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) |
| [Fraude en el Ejército: Corte Marcial disminuye condenas a cuatro uniformados](https://www.elciudadano.com/?p=683869) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=683869) |
| [Los documentos secretos del Milicogate](https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) | The Clinic | `secundaria` | 2015-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) |
| [The Panama Papers: los secretos de chilenos en paraísos fiscales](https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) | CIPER Chile | `secundaria` | 2016-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) |
| [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/) | ICIJ | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://offshoreleaks.icij.org/) |
