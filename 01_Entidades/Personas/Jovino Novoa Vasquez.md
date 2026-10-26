---
tipo_nodo: persona
rut: ""
aliases:
  - "Jovino Novoa"
rol_principal: "Ex Senador de la República, Ex Presidente del Senado y Ex Presidente de la UDI"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: condenado
medida_cautelar: "Fallecido en 2021 (Condenado en 2015 a 3 años de pena remitida en Caso Penta; sobreseído en Caso Spiniak en 2004)"
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/"
  - "https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640"
  - "https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/"
  - "https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html"
  - "https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones"
  - "https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html"
tags:
  - entidad/persona
  - caso-spiniak
  - caso-penta
  - ex-senador
---

# Jovino Novoa Vasquez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis (Nodo Puente Caso Spiniak — Caso Penta)
Abogado, fundador y expresidente de la [[Union Democrata Independiente]] y expresidente del [[Senado de la Republica de Chile]]. En la topología histórica de causas político-judiciales en Chile, actúa como un **nodo puente inter-temporal** entre dos macro-causas:
1. **[[Caso Spiniak]] (2003–2004)**: Tras las declaraciones de la diputada de [[Renovacion Nacional]], [[Pia Guzman Mena]], fue objeto de una imputación de falso testimonio por parte de Gema Bueno y el sacerdote José Luis Artiagoitía ([[TRX-2003-11-05-Arista-Politica-Spiniak-01]]). La investigación del Ministro en Visita [[Sergio Munoz Gajardo]] demostró que las imputaciones eran falsas, dictando el sobreseimiento definitivo de Novoa y condenando a sus acusadores por falso testimonio ([[Sentencia-Corte-Suprema-CasoSpiniak-2008]]).
2. **[[Caso Penta]] y [[Caso SQM]] (2014–2015)**: Una década después, la investigación de la Fiscalía y las querellas del [[Servicio Impuestos Internos]] acreditaron que Novoa articuló el financiamiento ilegal de campañas de la [[Union Democrata Independiente]] mediante la emisión de facturas y boletas ideológicamente falsas a través de su sociedad *Inversiones y Mandatos S.A.* hacia [[Empresas Penta SA]] —autorizadas por [[Carlos Alberto Delano Abbott]]— y [[SQM SA]] ([[TRX-2013-09-20-Boletas-Penta-Novoa-01]]). El 2 de diciembre de 2015, el 8° Juzgado de Garantía de Santiago lo condenó en procedimiento abreviado a 3 años de presidio remitido, multa e inhabilitación por delitos tributarios reiterados ([[Sentencia-8Juzgado-Garantia-Penta-2018]]).
3. **Declaración Pública de [[Loreto Letelier]] sobre Encuentros Partidarios en Punta de Tralca (`2017`)**: En agosto de 2017, durante una entrevista en el programa televisivo *"Con las Manos en la Masa"* (Vía X), la entonces candidata a diputada de la [[Union Democrata Independiente]], [[Loreto Letelier]], relató sus inicios de militancia en la Juventud UDI y describió los denominados *"retiros espirituales políticos"* organizados por la colectividad en **Punta de Tralca**, señalando que tras las jornadas políticas se realizaban celebraciones nocturnas en las que dirigentes y senadores históricos del partido —mencionando a [[Jovino Novoa Vasquez]] y a Juan Antonio Coloma— terminaban *"bailando arriba de las mesas"* con las corbatas en la cabeza. Documentalmente, esta anécdota sobre la vida partidaria interna corresponde a un episodio distinto e independiente del expediente judicial de 2003.

## Montos Imputados en Nexos Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)) ||
              (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Asociado en Aristas Reificadas: ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
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
| [Délano y Lavín terminaron clases de ética](https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) | CNN Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/delano-lavin-terminaron-clases-etica/) |
| [Lavín y Délano comenzaron las clases de ética tras condena del caso Penta](https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) | 24 Horas | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.24horas.cl/politica/lavin-y-delano-comenzaron-las-clases-de-etica-tras-condena-del-caso-penta-3218640) |
| [Cartas: 'Good bye' a las clases de ética](https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) | CIPER Chile | `secundaria` | 2024-06-07 | [Wayback ↺](https://web.archive.org/web/*/https://www.ciperchile.cl/2024/06/07/cartas-clases-de-etica/) |
| [Caso Penta: Tribunal desecha argumentos del CDE y absuelve a exsubsecretario Wagner por cohecho](https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) | Emol | `secundaria` | 2018-07-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2018/07/06/912366/Caso-Penta-Tribunal-desecha-argumentos-del-CDE-y-absuelve-a-exsubsecretario-Wagner-por-cohecho.html) |
| [Caso Penta deja condenas en juicios abreviados y suspensiones](https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) | T13 | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.t13.cl/noticia/politica/caso-penta-deja-condenas-juicios-abreviados-y-suspensiones) |
| [Claudio Spiniak fue condenado a cinco años y un día de cárcel](https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) | Cooperativa | `secundaria` | 2006-08-10 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) |
