---
tipo_nodo: persona
rut: ""
aliases:
  - "Carlos Alberto Délano"
  - "Choclo Délano"
rol_principal: "Cofundador y Controlador de Empresas Penta S.A."
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Condena cumplida en libertad vigilada, multa fiscal y clases de ética empresarial"
estado_verificacion: verificado
fuentes:
  - "https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/"
  - "https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/"
  - "https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html"
  - "https://www.eldinamo.cl/pais/2024/05/09/caso-minera-dominga-tribunal-sobresee-definitivamente-causa-que-involucraba-a-sebastian-pinera/"
  - "https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/"
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
tags:
  - entidad/persona
  - caso-penta
  - condenado
---

# Carlos Alberto Delano Abbott

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Empresas Penta SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Cofundador y controlador de [[Empresas Penta SA]] junto a [[Carlos Eugenio Lavin Garcia-Huidobro]], y controlador de [[Andes Iron SpA]]. Fue condenado en procedimiento abreviado en el [[Caso Penta]] ([[Sentencia-8Juzgado-Garantia-Penta-2018]]) por delitos tributarios reiterados tras incorporar en la contabilidad del holding cientos de boletas de honorarios y facturas ideológicamente falsas para desviar fondos hacia campañas políticas de la [[Union Democrata Independiente]] y dirigentes como [[Pablo Longueira Montes]] y [[Jovino Novoa Vasquez]] ([[TRX-2013-07-15-Boletas-Penta-UDI-01]] y [[TRX-2013-09-20-Boletas-Penta-Novoa-01]]). Adicionalmente, en el [[Caso Minera Dominga Pandora Papers]], adquirió a través de [[Andes Iron SpA]] la participación de [[Bancard Inversiones Ltda]] (familia de [[Sebastian Pinera Echenique]]) en el proyecto Dominga por **US$ 152 millones** (`$75.500.000.000 CLP`), firmando en las Islas Vírgenes Británicas la cláusula que condicionó el último pago a que el Gobierno de Chile no declarara zona de exclusión ambiental en La Higuera ([[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] y [[Contrato-Offshore-BVI-PandoraPapers-Dominga-2010]]).

## Montos Autorizados como Firmante de Origen
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && (
    p.firmante_origen.path === dv.current().file.path ||
    String(p.firmante_origen).includes(dv.current().file.name)
  ));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Autorizado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Origen", "Destino", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Pandora Papers: Piñera vendió Minera Dominga a Délano en Islas Vírgenes Británicas](https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/) | Radio Agricultura | `secundaria` | 2021-10-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.radioagricultura.cl/noticias/nacional/pandora-papers-investigacion-asegura-que-pinera-vendio-minera-dominga-a-delano-en-islas-virgenes-britanicas_20211003/) |
| [Fiscalía cierra investigación por el caso Dominga y solicita sobreseimiento definitivo](https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/) | La Tercera | `secundaria` | 2024-01-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/fiscalia-cierra-investigacion-por-el-caso-dominga-y-solicita-sobreseimiento-definitivo/ETCJHQKLVNFKVBX3M7Y7SJGK6I/) |
| [Pandora Papers: venta de Minera Dominga en Islas Vírgenes](https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html) | Meganoticias | `secundaria` | 2021-10-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.meganoticias.cl/nacional/354151-sebastian-pinera-presidente-pandora-papers-proyecto-minera-dominga-venta-paraiso-fiscal-islas-virgenes-05-10-2021.html) |
| [Caso Minera Dominga: tribunal sobresee definitivamente causa que involucraba a Sebastián Piñera](https://www.eldinamo.cl/pais/2024/05/09/caso-minera-dominga-tribunal-sobresee-definitivamente-causa-que-involucraba-a-sebastian-pinera/) | El Dínamo | `secundaria` | 2024-05-09 | [Wayback ↺](https://web.archive.org/web/*/https://www.eldinamo.cl/pais/2024/05/09/caso-minera-dominga-tribunal-sobresee-definitivamente-causa-que-involucraba-a-sebastian-pinera/) |
| [Délano y Lavín terminaron clases de ética](https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) |
| [Lavín y Délano comenzaron las clases de ética tras condena del caso Penta](https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) | 24 Horas | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) |
