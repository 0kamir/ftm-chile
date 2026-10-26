---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio
region: "Nacional (Sede Santiago)"
superior_jerarquico: "Ejército de Chile / Ministerio de Defensa Nacional"
estado_verificacion: verificado
fuentes:
  - "https://irp.fas.org/cia/product/chile/index.html"
  - "https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile"
  - "https://nsarchive.gwu.edu/node/3113"
  - "https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash"
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html"
tags:
  - entidad/publica
  - ejercito
  - caso-milicogate
---

# Comando de Apoyo a la Fuerza del Ejercito

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Contexto en Investigaciones
Unidad logística del Ejército de Chile encargada de la gestión de adquisiciones y mantenimiento con cargo a los fondos de la Ley Reservada del Cobre. En el [[Caso Milicogate]], se acreditó la operación de un mecanismo de pago de facturas ideológicamente falsas a empresas proveedoras como [[Frasim Ltda]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]) por **$6.100.000.000 CLP**, con participación del coronel (r) [[Jozo Santic Palomino]] y bajo el período de mando institucional de [[Juan Miguel Fuente-Alba Poblete]] ([[Procesamientos-Ministra-Rutherford-Milicogate]]).

## Nexos y Operaciones Registradas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Desfalco",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Proveedor",
  firmante_destino AS "Oficial Condenado",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [CIA Activities in Chile (Informe Hinchey)](https://irp.fas.org/cia/product/chile/index.html) | CIA / FAS | `primaria` | 2000-09-18 | [Wayback ↺](https://web.archive.org/web/*/https://irp.fas.org/cia/product/chile/index.html) |
| [Hinchey Report on CIA Activities in Chile](https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile) | Transnational Institute | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile) |
| [Documentos desclasificados sobre Chile](https://nsarchive.gwu.edu/node/3113) | National Security Archive | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://nsarchive.gwu.edu/node/3113) |
| [Chile's journalists' union kicked out powerful media mogul over CIA propaganda cash](https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) | The World (PRI) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Juez Valderrama sobreseyó arista de los 'Pinocheques' en caso Riggs](https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) | Cooperativa | `secundaria` | 2010-05-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20100507/pags-amp/20100507182039.html) |
