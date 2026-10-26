---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Sociedad Benefactora y Educacional Dignidad (Holding Villa Baviera / Cerro Florido S.A.)"
fecha_constitucion: 1961-09-20
objeto_social: "Beneficencia, educación, asistencia médica y explotación agrícola, forestal, industrial e inmobiliaria"
representante_legal: "[[Paul Schafer Schneider]]"
estado_verificacion: verificado
fuentes:
  - "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
  - "https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html"
  - "https://www.nbcnews.com/id/wbna23817827"
  - "https://irp.fas.org/cia/product/chile/index.html"
  - "https://nsarchive.gwu.edu/node/3113"
  - "https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash"
tags:
  - entidad/privada
  - caso-colonia-dignidad
  - holding-opaco
---

# Sociedad Benefactora y Educacional Dignidad

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion` (personalidad jurídica cancelada por Decreto Supremo N° 143 de 1991)
- **Objeto Social**: `= this.objeto_social`
- **Representante Legal / Controlador Histórico**: `= this.representante_legal` (y subdirector [[Hartmut Hopp Miottel]])

## Contexto en Investigaciones
Corporación de derecho privado constituida en 1961 en Parral (Región del Maule) por [[Paul Schafer Schneider]]. Bajo el amparo de franquicias aduaneras y exenciones impositivas, operó como un enclave territorial cerrado donde se perpetraron crímenes de lesa humanidad, trabajo esclavo de colonos no remunerados, abuso sexual sistemático de menores y acopio de armamento de guerra ([[TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01]]). Cuando el Estado canceló su personalidad jurídica en enero de 1991 en el marco del [[Caso Colonia Dignidad]], su directorio ejecutó un vaciamiento patrimonial masivo hacia más de 15 sociedades anónimas comerciales (*Inmobiliaria e Inversiones Cerro Florido S.A.*, *Agrícola Las Acacias S.A.*, *Villa Baviera*) registrado por el [[Servicio Impuestos Internos]] por evasión tributaria y ocultamiento de bienes afectos a comiso ([[TRX-1991-01-31-Movimientos-Patrimoniales-ColoniaDignidad-01]]), contando durante los años noventa con el respaldo político de dirigentes de la [[Union Democrata Independiente]] como el senador [[Hernan Larrain Fernandez]] ([[TRX-1996-06-12-Defensa-Politica-ColoniaDignidad-01]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Contraparte / Fiscalizador",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad](https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) | El Mostrador | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) |
| [Seis ex jerarcas de Colonia Dignidad fueron condenados a prisión por la Corte Suprema](https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) | Cooperativa | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) |
| [Ex-Nazi soldier gets more prison time in Chile](https://www.nbcnews.com/id/wbna23817827) | NBC News / AP | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.nbcnews.com/id/wbna23817827) |
| [CIA Activities in Chile (Informe Hinchey, 18-09-2000)](https://irp.fas.org/cia/product/chile/index.html) | CIA / Federation of American Scientists | `primaria` | 2000-09-18 | [Wayback ↺](https://web.archive.org/web/*/https://irp.fas.org/cia/product/chile/index.html) |
| [Documentos desclasificados sobre Chile](https://nsarchive.gwu.edu/node/3113) | National Security Archive | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://nsarchive.gwu.edu/node/3113) |
| [Chile's journalists' union kicked out powerful media mogul over CIA propaganda cash](https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) | The World (PRI) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) |
