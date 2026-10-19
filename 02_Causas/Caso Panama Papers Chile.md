---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2016
tribunal_o_fiscalia: "Servicio de Impuestos Internos (Subdirección de Fiscalización Internacional) / Unidad de Análisis Financiero / Fiscalía Nacional"
fiscal_a_cargo: "Subdirección de Fiscalización SII / Unidad Especializada Anticorrupción y Lavado de Activos (UNAC)"
estado_judicial: en_investigacion
delito_principal: "[[Delito Tributario]]"
estado_verificacion: parcial
fuentes:
  - url: "https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/"
    titulo: "The Panama Papers: los secretos de chilenos en paraísos fiscales salen a la luz"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2016-04-04
    consultado: 2026-10-19
  - url: "https://offshoreleaks.icij.org/"
    titulo: "ICIJ Offshore Leaks Database"
    medio: "ICIJ"
    tipo: primaria
    consultado: 2026-10-19
historial_correcciones:
  - "Aparecer en Panama Papers no implica ilegalidad (CIPER 2016: 'aún no hay evidencias de ilegalidades'). No se encontró fuente para la actuación del SII/UAF ni para el RUC indicado."
tags:
  - causa
  - panama-papers
  - offshore
  - mossack-fonseca
  - icij
---

# Caso Panama Papers Chile

## Ficha Procesal, Tributaria y de Inteligencia Financiera
- **RUC / Expediente de Fiscalización**: `= this.ruc`
- **Año de Inicio**: `= this.año_inicio` (Publicación mundial del Consorcio Internacional de Periodistas de Investigación —ICIJ— y CIPER Chile el 3 de abril de 2016)
- **Órganos Investigadores**: `= this.tribunal_o_fiscalia`
- **Unidades a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial / Administrativo**: `= this.estado_judicial` (Auditorías tributarias de repatriación y reliquidación ante el SII, renuncias institucionales y cruces con causas de lavado de activos)
- **Delito / Infracción Principal**: `= this.delito_principal` (en concurso con [[Lavado de Activos]], elusión fiscal transfronteriza y ocultamiento de beneficiarios finales)

## Síntesis de la Causa
Capítulo chileno de la filtración global **Panama Papers** (11,5 millones de documentos internos del bufete panameño **Mossack Fonseca**, procesados en abril de 2016 por **ICIJ**, el diario alemán *Süddeutsche Zeitung* y en Chile por **CIPER**), que dejó al descubierto cerca de **200 sociedades *offshore* vinculadas a empresarios, estudios jurídicos y figuras públicas chilenas** constituidas en paraísos fiscales como Panamá, Bahamas, Islas Vírgenes Británicas y Seychelles, agrupadas en el nodo [[Mossack Fonseca y Sociedades Offshore Panama]].

Las cuatro aristas principales acreditadas en Chile ([[Filtracion-ICIJ-PanamaPapers-Chile-2016]]) son:
1. **Caída del Presidente de *Chile Transparente* y Estructuras Mineras en Bahamas (`Turnbrook / Andes Copper`)**: La filtración reveló que el abogado [[Gonzalo Delaveau Swett]] —quien hasta ese momento ejercía como **Presidente de *Chile Transparente*** (el capítulo chileno de Transparencia Internacional)— actuaba simultáneamente como agente e intermediario de [[Mossack Fonseca y Sociedades Offshore Panama]], gestionando y administrando al menos cinco sociedades *offshore* domiciliadas en Bahamas (*Turnbrook Corporation*, *DKL Holdings*, *Westquarter Limited*, *Mining Press Holdings* y *Turnbrook Mining Ltd.*) articuladas en torno al proyecto minero *Andes Copper* ([[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]]), lo que forzó su renuncia inmediata el 4 de abril de 2016.
2. **Fundaciones Privadas y Sociedades de la Élite Empresarial (`Edwards / Ovalle / CPC`)**: Los registros de Mossack Fonseca documentaron la creación de las fundaciones de interés privado *Ashton Foundation* y *Kintyre Foundation* en Panamá por parte del propietario de *El Mercurio*, [[Agustin Edwards Eastman]], así como las sociedades *Sierra Leona S.A.* y *Railton Foundation* vinculadas al expresidente de la Confederación de la Producción y del Comercio (CPC) y de la SONAMI, [[Alfredo Ovalle Rodriguez]] ([[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]]).
3. **Conexión con las Sociedades *Offshore* de Augusto Pinochet (`Caso Riggs`)**: Los archivos internos de [[Mossack Fonseca y Sociedades Offshore Panama]] confirmaron que el bufete panameño prestó servicios registrales a sociedades de papel en las Islas Vírgenes Británicas conectadas con la red fiduciaria de [[Riggs Bank y Sociedades Offshore Ashburton]], operada por [[Augusto Pinochet Ugarte]] y [[Oscar Aitken Lavanchy]] en el [[Caso Riggs]] ([[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]]).
4. **Fiscalización Masiva del SII y la UAF**: El [[Servicio Impuestos Internos]] y la [[Unidad de Analisis Financiero]] abrieron auditorías especiales sobre la nómina de 200 entidades chilenas de los *Panama Papers*, cruzándolas con la declaración extraordinaria de bienes y rentas en el extranjero (artículo 24 transitorio de la Reforma Tributaria Ley N° 20.780) y con los directorios investigados en el [[Caso SQM]] y [[Caso Penta]].

## Transacciones y Nexos Reificados Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
