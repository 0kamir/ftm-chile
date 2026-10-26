---
tipo_nodo: persona
rut: ""
aliases:
  - "Manuel Contreras"
  - "Mamo Contreras"
rol_principal: "General (R) de Ejército y Ex Director Ejecutivo de la Dirección de Inteligencia Nacional (DINA)"
afiliacion_politica: "Militar / Dictadura Cívico-Militar (Subordinado directo de Augusto Pinochet Ugarte)"
situacion_procesal: condenado
medida_cautelar: "Fallecido en agosto de 2015 en el Hospital Militar cumpliendo condenas ejecutoriadas por más de 529 años de presidio efectivo"
estado_verificacion: verificado
fuentes:
  - "https://irp.fas.org/cia/product/chile/index.html"
  - "https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile"
  - "https://nsarchive.gwu.edu/node/3113"
  - "https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash"
  - "https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/"
  - "https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html"
tags:
  - entidad/persona
  - proyecto-fubelt
  - dina
  - caso-colonia-dignidad
  - condenado
---

# Manuel Contreras Sepulveda

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación / Dependencia**: `= this.afiliacion_politica` ([[Augusto Pinochet Ugarte]])
- **Situación Procesal**: `= this.situacion_procesal`
- **Condenas Ejecutoriadas**: `= this.medida_cautelar`

## Síntesis
General de Ejército e ingeniero militar, fundador y director ejecutivo de la **Dirección de Inteligencia Nacional (DINA)** entre noviembre de 1973 y agosto de 1977 bajo dependencia directa de [[Augusto Pinochet Ugarte]]. En la red conecta tres estructuras documentadas:
1. **Vínculo Remunerado con la CIA y Escuela de las Américas ([[Caso Operacion FUBELT Intervencion CIA y DINA]])**: Formado en academias militares estadounidenses en Fort Belvoir y vinculado a la doctrina de inteligencia de la **Escuela de las Américas (SOA)**, el **Informe Hinchey al Congreso de EE.UU. (19 de septiembre de 2000)** ([[Informe-Comision-Church-1975-y-Hinchey-CIA-2000]]) reveló oficialmente que Contreras mantuvo una relación operativa con la [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] entre 1974 y 1977 y recibió pagos monetarios directos de la agencia estadounidense como activo registrado ([[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]]).
2. **Alianza Operativa y Armamentística con Colonia Dignidad ([[Caso Colonia Dignidad]])**: Mantuvo una estrecha colaboración logística y de inteligencia con [[Paul Schafer Schneider]] en el enclave de [[Sociedad Benefactora y Educacional Dignidad]] en Parral, utilizando el recinto como centro clandestino de detención, tortura, exterminio y desarrollo de armamento y toxinas ([[TRX-2005-06-14-Hallazgo-Arsenal-ColoniaDignidad-01]]).
3. **Condenas Históricas de la [[Corte Suprema de Chile]]**: Acumuló más de **529 años de presidio efectivo** en sentencias definitivas dictadas por la [[Corte Suprema de Chile]] por asociación ilícita, secuestro calificado, homicidio calificado (incluyendo los asesinatos del general Carlos Prats en Buenos Aires y del excanciller Orlando Letelier en Washington D.C.) y apremios ilegítimos.

## Montos Registrados y Procesal: Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto Registrado (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [CIA Activities in Chile (Informe Hinchey)](https://irp.fas.org/cia/product/chile/index.html) | CIA / FAS | `primaria` | 2000-09-18 | [Wayback ↺](https://web.archive.org/web/*/https://irp.fas.org/cia/product/chile/index.html) |
| [Hinchey Report on CIA Activities in Chile](https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile) | Transnational Institute | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.tni.org/en/article/hinchey-report-on-cia-activities-in-chile) |
| [Documentos desclasificados sobre Chile](https://nsarchive.gwu.edu/node/3113) | National Security Archive | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://nsarchive.gwu.edu/node/3113) |
| [Chile's journalists' union kicked out powerful media mogul over CIA propaganda cash](https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) | The World (PRI) | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://theworld.org/stories/2016/07/30/chiles-journalists-union-kicked-out-powerful-media-mogul-over-cia-propaganda-cash) |
| [Corte Suprema decreta prisión para seis ex líderes de Colonia Dignidad](https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) | El Mostrador | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2013/01/28/corte-suprema-decreta-prision-para-seis-ex-lideres-de-colonia-dignidad/) |
| [Seis ex jerarcas de Colonia Dignidad fueron condenados a prisión por la Corte Suprema](https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) | Cooperativa | `secundaria` | 2013-01-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20130128/pags-amp/20130128100305.html) |
