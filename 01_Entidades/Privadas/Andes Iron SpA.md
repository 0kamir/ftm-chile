---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Andes Iron SpA (Titular del Proyecto Minero-Portuario Dominga)"
fecha_constitucion: 2010-08-05
objeto_social: "Exploración, explotación minera de hierro y cobre, y desarrollo de infraestructura portuaria y desaladora en La Higuera"
representante_legal: "[[Carlos Alberto Delano Abbott]]"
estado_verificacion: verificado
fuentes:
  - "https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/"
  - "https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/"
  - "https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html"
  - "https://www.eldinamo.cl/pais/2024/05/09/caso-minera-dominga-tribunal-sobresee-definitivamente-causa-que-involucraba-a-sebastian-pinera/"
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
  - "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
tags:
  - entidad/privada
  - caso-dominga
  - pandora-papers
  - grupo-penta
---

# Andes Iron SpA

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador Principal**: `= this.representante_legal` (socio controlador de [[Empresas Penta SA]])

## Contexto en Investigaciones
Sociedad minera y portuaria controlada por la familia de [[Carlos Alberto Delano Abbott]] (condenado en el [[Caso Penta]]). En diciembre de 2010, a través de contratos firmados en Chile y en las Islas Vírgenes Británicas revelados por los *Pandora Papers* en el [[Caso Minera Dominga Pandora Papers]], adquirió de [[Bancard Inversiones Ltda]] (sociedad de la familia del entonces Presidente de la República [[Sebastian Pinera Echenique]]) la participación en el proyecto **Minera Dominga** por **US$ 152 millones** (`$75.500.000.000 CLP`), pactando en la cláusula tercera del contrato *offshore* que el último pago de US$ 9,9 millones sólo se realizaría si el Gobierno de Chile no declaraba la zona de La Higuera / Punta de Choros como área de protección ambiental ([[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] y [[Contrato-Offshore-BVI-PandoraPapers-Dominga-2010]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Pandora Papers: Piñera vendió Minera Dominga a Délano en Islas Vírgenes Británicas](https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/) | Radio Agricultura | `secundaria` | 2021-10-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/) |
| [Fiscalía cierra investigación por el caso Dominga y solicita sobreseimiento definitivo](https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/) | La Tercera | `secundaria` | 2024-01-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/) |
| [Pandora Papers: venta de Minera Dominga en Islas Vírgenes](https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html) | Meganoticias | `secundaria` | 2021-10-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html) |
| [Caso Minera Dominga: tribunal sobresee definitivamente causa que involucraba a Sebastián Piñera](https://www.eldinamo.cl/pais/2024/05/09/caso-minera-dominga-tribunal-sobresee-definitivamente-causa-que-involucraba-a-sebastian-pinera/) | El Dínamo | `secundaria` | 2024-05-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/05/09/caso-minera-dominga-tribunal-sobresee-definitivamente-causa-que-involucraba-a-sebastian-pinera/) |
| [Lavín y Délano comenzaron las clases de ética tras condena del caso Penta](https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) | 24 Horas | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) |
| [Cartas: 'Good bye' a las clases de ética](https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) | CIPER Chile | `secundaria` | 2024-06-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) |
