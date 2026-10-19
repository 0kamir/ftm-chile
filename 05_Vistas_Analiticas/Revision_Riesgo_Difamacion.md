---
tipo_nodo: vista_analitica
tags:
  - vista/revision-legal
---

# Revisión Preliminar de Riesgo de Difamación

> Triaje automático con el modelo local `qwen3:14b` (Ollama). **No es un dictamen**: cada hallazgo debe contrastarse con las fuentes antes de editar la nota. Se descartaron 34 frases que el modelo no copió literalmente.

> **Revisión editorial (2026-10-19):** se revisaron los 81 hallazgos de riesgo alto. Se corrigieron 25 frases que afirmaban como probados hechos sin sentencia (Chadwick/Hermosilla, Factop, Luminarias, Basura, Vitacura, Maipú, ProCultura/En Ti, CEMA, Pinocheques, entre otros) y se marcaron como no firmes las condenas de Operación Huracán. Se descartaron como falsos positivos: el término 'cartel' en colusiones condenadas por el TDLC y la Corte Suprema, frases ya atribuidas a la Fiscalía ('habría', 'según'), condenas ejecutoriadas y citas de dichos de terceros. Este listado corresponde al estado previo a esas correcciones; vuelve a ejecutar `make screen` para un triaje actualizado.

Notas revisadas: 226 · Notas con hallazgos: 124 · Riesgo alto: 81

## [[Agustin Edwards Eastman]]
- **medio** — Usa el término 'acreditó' para afirmar un hecho como probado, sin indicar que la situación procesal no es condenado o que la causa no tiene sentencia.
  - Frase: “Según acreditó oficialmente el Informe de la Comisión Church del Senado de EE.UU. (1975)”
  - Sugerencia: Reemplazar 'acreditó' por un término más neutral, como 'indicó' o 'documentó', para evitar la impresión de que el hecho está probado.

## [[Alex Smith Leay]]
- **medio** — uso de términos como 'supuesto' y 'ficticias' que pueden sugerir falta de evidencia o especulación, aunque no afirman hechos probados
  - Frase: “Fue el ideólogo del supuesto software espía «Antorcha» y «Tubicación», herramientas ficticias que según la plana mayor de Carabineros interceptaban conversaciones de mensajería cifrada.”
  - Sugerencia: revisar el uso de términos que puedan generar ambigüedad o interpretación errónea sobre la naturaleza de las herramientas

## [[Andres Chadwick Pinera]]
- **alto** — Afirma como hecho probado un delito ('acreditaron transferencias') cuando la situación procesal no es condenado, sino imputado.
  - Frase: “Las cartolas bancarias periciadas por la Fiscalía Oriente acreditaron transferencias desde cuentas de [[Luis Hermosilla Osorio]] (nutridas por [[Factop SpA]]) hacia [[Andres Chadwick Pinera]] por más de `$190.000.000 CLP` entre 2020 y 2023”
  - Sugerencia: Evitar afirmar hechos como probados cuando no hay sentencia condenatoria. Usar lenguaje como 'se han identificado transferencias' o 'se han encontrado indicios de transferencias'.

## [[Angela Vivanco Martinez]]
- **medio** — uso de título institucional que puede generar confusión sobre su situación actual
  - Frase: “exministra de la [[Corte Suprema de Chile]]”
  - Sugerencia: especificar si actualmente ocupa el cargo o si fue destituido
- **medio** — uso de término 'arista judicial' puede ser ambiguo y no estándar en contextos legales
  - Frase: “En la arista judicial del [[Caso Audios]]”
  - Sugerencia: reemplazar por un término más preciso como 'aspecto judicial' o 'área de investigación judicial'

## [[Augusto Pinochet Hiriart]]
- **medio** — Usa el verbo 'acreditaron' que sugiere certeza de un hecho, cuando en realidad se refiere a una investigación o acusación en curso, no a un hecho probado.
  - Frase: “el Ministro en Visita [[Sergio Munoz Gajardo]] y las querellas del [[Servicio Impuestos Internos]] acreditaron el flujo de esos recursos hacia cuentas en el extranjero vinculadas a [[Riggs Bank y Sociedades Offshore Ashburton]]”
  - Sugerencia: Reemplazar 'acreditaron' por 'sospechado' o 'indicado' para evitar dar la impresión de certeza sobre un hecho que aún no ha sido probado judicialmente.

## [[Augusto Pinochet Ugarte]]
- **medio** — uso de lenguaje peyorativo ('secretas') que no es judicial y puede interpretarse como calumnioso
  - Frase: “mantuvo más de 125 cuentas bancarias secretas”
  - Sugerencia: revisar el uso de términos no judiciales y reemplazarlos por lenguaje neutral
- **medio** — afirma como hecho probado un delito ('desviando') cuando la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “desviando gastos reservados del Ejército y de la Presidencia por US$ 17,86 millones sin justificación lícita”
  - Sugerencia: revisar la afirmación de hechos como probados y usar lenguaje condicional como 'se le imputa' o 'se le acusa de'

## [[Bruno Villalobos Krumm]]
- **alto** — Afirma como hecho probado un delito ('malversación') cuando la situación procesal es 'formalizado' y no hay condena.
  - Frase: “fue procesado por la justicia militar y civil por la malversación de más de `$600.000.000 CLP` en gastos reservados institucionales.”
  - Sugerencia: Reemplazar 'fue procesado por la justicia... malversación' por 'fue formalizado por la justicia... por presunta malversación'.

## [[Camila Flores Oporto]]
- **medio** — uso de término 'presunto' que indica una acusación sin haberse probado el delito, lo cual es compatible con la situación procesal de 'investigada', pero el uso de 'reiterado' puede sugerir una certeza no respaldada por la evidencia
  - Frase: “presunto fraude al Fisco reiterado”
  - Sugerencia: revisar el uso de 'reiterado' para evitar sugerir una certeza no respaldada por la evidencia

## [[Camila Polizzi Fonceca]]
- **medio** — Atribuye hechos probados a una persona formalizada, sin mencionar que no hay condena ni sentencia
  - Frase: “Gestionó la adjudicación del convenio [[TRX-2022-12-20-Convenio-EnTi-01]] con el [[GORE Biobio]] (encabezado por [[Rodrigo Diaz Worner]]) utilizando la personalidad jurídica de [[Fundacion En Ti]] por **$250.635.000 CLP** según consta en la [[Resolucion-GORE-Biobio-EnTi-2022]]”
  - Sugerencia: Revisar si los hechos mencionados son probados o solo son acusaciones, y ajustar el lenguaje para evitar afirmaciones que puedan interpretarse como hechos probados

## [[Cathy Barriga Guerra]]
- **alto** — Afirma como hecho probado un delito ('acreditado') cuando la situación procesal es 'formalizado' y no hay condena.
  - Frase: “acreditado en el [[Informe-Contraloria-Municipalidad-Maipu-2021]]”
  - Sugerencia: Evitar el uso de términos que sugieran que un delito ha sido probado, ya que la situación procesal indica que aún no hay sentencia.

## [[Daniel Andrade Schwarze]]
- **alto** — Afirma como hecho probado un delito ('fraude al fisco reiterado') cuando la situación procesal es 'formalizado' y no hay condena.
  - Frase: “Se encuentra formalizado en la causa [[Caso Convenios]] por fraude al fisco reiterado.”
  - Sugerencia: Reemplazar 'por fraude al fisco reiterado' por 'por fraude al fisco reiterado, según la acusación' o similar, para evitar afirmar como hecho probado un delito sin condena.

## [[Eduardo Guendelman Israel]]
- **medio** — Usa el término 'acreditó' para afirmar un hecho sin que exista una condena o sentencia judicial que respalde dicha afirmación.
  - Frase: “una investigación de la Unidad de Investigación de *BioBioChile* sobre los correos desclasificados por el Departamento de Justicia de EE. UU. ([[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]) acreditó que el profesor Guendelman mantuvo un intercambio de correos electrónicos con Jeffrey Epstein entre 2015 y 2019.”
  - Sugerencia: Reemplazar 'acreditó' por un término más neutro, como 'indicó' o 'sugirió', para evitar la impresión de que el hecho está probado judicialmente.

## [[Eliodoro Matte Larrain]]
- **alto** — uso de lenguaje peyorativo ('cartel') que sugiere una organización criminal sin que exista una condena judicial firme
  - Frase: “cartel del papel tissue”
  - Sugerencia: reemplazar por términos neutrales como 'acuerdo colusorio' o 'prácticas colusorias'

## [[Fernando Cerimedo]]
- **medio** — Uso de término 'acreditada' que sugiere certeza de un hecho sin que exista una condena o formalización judicial
  - Frase: “Dicha presencia quedó acreditada mediante registros fotográficos exclusivos revelados por el medio The Clinic”
  - Sugerencia: Reemplazar 'acreditada' por 'revelada' o 'publicada' para evitar sugerir certeza judicial

## [[Fernando Leon Steffens]]
- **medio** — Usa el término 'imputó' que sugiere una acusación formal, pero no acredita un delito probado, lo que podría generar confusión sobre la situación procesal real.
  - Frase: “la Fiscalía Regional Metropolitana Occidente le imputó haber autorizado (imputación que terminó en una salida alternativa, sin condena)”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados, y reemplazarlos por lenguaje más preciso y neutral.

## [[Flavio Echeverria Cortez]]
- **alto** — Afirma como hecho probado un delito ('habría sustraído') cuando la situación procesal no es condenado y la causa no tiene sentencia firme.
  - Frase: “habría sustraído $28.348.928.198 CLP mediante depósitos ficticios de remuneraciones”
  - Sugerencia: Reemplazar 'habría sustraído' por 'se le imputa la sustracción' para evitar afirmar hechos como probados sin condena.
- **medio** — Usa el término 'señalado' que indica una acusación, lo cual es correcto, pero no debe usarse lenguaje que sugiera culpabilidad sin condena.
  - Frase: “señalado por la Fiscalía como líder del esquema del [[Caso Pacogate]]”
  - Sugerencia: Reemplazar 'señalado' por 'acusado' para mantener el rigor legal y la presunción de inocencia.

## [[Gonzalo Delaveau Swett]]
- **medio** — Usa lenguaje que puede interpretarse como peyorativo al mencionar sociedades *offshore* sin especificar si hay una condena o situación procesal relacionada
  - Frase: “figuraba personalmente como director, apoderado y secretario de al menos cinco sociedades *offshore* domiciliadas en Bahamas”
  - Sugerencia: Revisar si el uso de *offshore* es necesario o si se puede reemplazar con un término más neutral

## [[Guillermo Harding Alvarado]]
- **medio** — afirma como hecho probado un delito sin mencionar que la situación procesal no es condena firme
  - Frase: “coordinaron con [[Farmacias Salcobrand SA]] y [[Farmacias Ahumada SA]] el alza de precios de 222 medicamentos entre diciembre de 2007 y marzo de 2008”
  - Sugerencia: revisar si la frase refleja la situación procesal actual y evitar afirmar hechos como probados si no hay condena firme
- **medio** — afirma como hecho probado un delito sin mencionar que la situación procesal no es condena firme
  - Frase: “el Tribunal de Defensa de la Libre Competencia ([[Sentencia-TDLC-119-Colusion-Farmacias-2012]]) y la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-Colusion-Farmacias-2012]]) condenaron a la empresa al pago de la multa máxima de **20.000 UTA** (cerca de US$ 19 millones)”
  - Sugerencia: revisar si la frase refleja la situación procesal actual y evitar afirmar hechos como probados si no hay condena firme

## [[Hartmut Hopp Miottel]]
- **medio** — La frase sugiere que la sentencia no estaba ejecutoriada en el momento de la fuga, lo cual podría generar confusión sobre el estado procesal del caso.
  - Frase: “fugándose del país hacia Krefeld (Alemania) en mayo de 2011 antes de que la sentencia quedara ejecutoriada.”
  - Sugerencia: Se recomienda aclarar el estado procesal de la sentencia en el momento de la fuga para evitar malentendidos.

## [[Iraci Hassler Jacob]]
- **medio** — afirma hechos como probados sin mencionar que la situación procesal no es condena, sino investigación penal desformalizada y sumario de Contraloría
  - Frase: “operación cuyos pagos fueron paralizados por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) mediante el [[Dictamen-CGR-SierraBella-2023]] al constatarse que el precio cuadruplicaba el avalúo fiscal y el valor de compra previa sin justificación técnica verificable.”
  - Sugerencia: revisar el lenguaje para evitar afirmar hechos como probados sin evidencia judicial

## [[Jaime Paz Meneses]]
- **alto** — Afirma como hecho probado un delito ('habría sustraído') cuando la situación procesal no es condenado
  - Frase: “habría sustraído $28.348.928.198 CLP mediante depósitos ficticios de remuneraciones”
  - Sugerencia: Reemplazar por 'se le imputa haber sustraído' o similar, para evitar afirmar hechos como probados sin sentencia firme
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales ('figura clave') sobre una persona acusada sin condena
  - Frase: “señalado como figura clave del esquema del [[Caso Pacogate]]”
  - Sugerencia: Reemplazar por 'acusado como figura clave' o similar, para mantener el rigor legal y respetar la presunción de inocencia

## [[Javier Cruz Tamburrino]]
- **medio** — afirma un delito como hecho probado sin indicar que la situación procesal es condenado o la causa tiene sentencia
  - Frase: “Lavado de Activos”
  - Sugerencia: utilizar términos como 'presunto lavado de activos' o 'acusado de lavado de activos'
- **medio** — atribuye hechos de terceros a una persona sin condena
  - Frase: “Flavio Echeverria Cortez”
  - Sugerencia: verificar si los hechos mencionados están relacionados directamente con Flavio Echeverria Cortez y usar lenguaje preciso

## [[Jose Antonio Pavez Canessa]]
- **alto** — uso de lenguaje peyorativo ('clan') que no es judicial y sugiere una organización criminal sin condena
  - Frase: “líder del denominado 'Clan Canessa'”
  - Sugerencia: reemplazar por 'uno de los imputados' o 'figura en el listado de imputados'
- **medio** — uso de 'habría' indica una acusación sin prueba probada, lo que contradice la presunción de inocencia
  - Frase: “habría creado 16 sociedades de papel que vendían facturas falsas a cambio de comisión”
  - Sugerencia: reemplazar por 'se le atribuye la creación de 16 sociedades de papel que vendían facturas falsas a cambio de comisión'

## [[Jose Codner Chijner]]
- **alto** — uso de lenguaje peyorativo ('cartel') que no es judicial y sugiere culpabilidad sin condena
  - Frase: “cartel de alza de precios de 222 medicamentos”
  - Sugerencia: reemplazar por términos neutrales como 'acuerdo de alza de precios' o 'concertación de precios'

## [[Jovino Novoa Vasquez]]
- **alto** — Menciona una condena específica, pero no se alinea con la situación procesal declarada en METADATOS que indica 'condenado en 2015 a 3 años de pena remitida en Caso Penta'
  - Frase: “El 2 de diciembre de 2015, el 8° Juzgado de Garantía de Santiago lo condenó en procedimiento abreviado a 3 años de presidio remitido, multa e inhabilitación por delitos tributarios reiterados”
  - Sugerencia: Verificar si la condena mencionada en la nota corresponde exactamente a la situación procesal declarada en METADATOS y ajustar la redacción si es necesario

## [[Juan Miguel Fuente-Alba Poblete]]
- **medio** — Usa lenguaje que sugiere una responsabilidad directa sin mencionar que es un proceso formalizado, lo que puede generar una impresión de culpabilidad no probada.
  - Frase: “Fue sometido a proceso por la Ministra en Visita Romy Rutherford”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como una condena o responsabilidad directa, incluso si el proceso es formalizado.

## [[Juan Miguel Ovalle Garces]]
- **alto** — Usa lenguaje peyorativo ('cartel') sobre una persona sin condena
  - Frase: “lo identificaron como el artífice técnico y coordinador cotidiano del cartel”
  - Sugerencia: Evitar el uso de términos como 'cartel' que pueden ser interpretados como calificativos no judiciales

## [[Juan Victor Galaz Rojas]]
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre una persona sin condena
  - Frase: “líder del denominado 'Clan Galaz'”
  - Sugerencia: evitar el uso de términos como 'clan' que pueden ser interpretados como calificativos no judiciales
- **medio** — uso de 'habría' que sugiere una afirmación de hecho sin estar probado
  - Frase: “habría declarado exportaciones falsas de teléfonos”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria y no probada de los hechos
- **medio** — exposición de montos sin estar relacionados directamente con una condena o sentencia
  - Frase: “perjuicio fiscal estimado de $11.594.172.879”
  - Sugerencia: evitar mencionar montos sin contexto legal o judicial claro

## [[Leon Marcelo Lefort Hernandez]]
- **alto** — Afirma como hecho probado un delito ('soborno a funcionarios') sin que exista una sentencia condenatoria, lo que viola la presunción de inocencia.
  - Frase: “Imputado en el [[Caso Luminarias LED]] por soborno a funcionarios de al menos 24 instituciones públicas, según la Fiscalía”
  - Sugerencia: Reemplazar 'por soborno' con 'acusado de soborno' o 'presunto soborno' para reflejar la situación procesal actual.
- **alto** — Afirma como hecho probado ('entregar') un acto que no ha sido probado judicialmente, lo que viola la presunción de inocencia.
  - Frase: “fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo”
  - Sugerencia: Utilizar lenguaje como 'habría entregado' o 'presuntamente entregado' para reflejar la naturaleza acusatoria de la información.
- **alto** — Usa lenguaje que sugiere un hecho probado ('habría anticipado') sin que exista una sentencia condenatoria, lo que viola la presunción de inocencia.
  - Frase: “habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]”
  - Sugerencia: Reemplazar 'habría anticipado' con 'presuntamente anticipado' o 'acusado de anticipar' para reflejar la situación procesal actual.
- **medio** — Menciona una función profesional sin indicar si está relacionada con el hecho investigado, lo que podría generar confusión sobre su relevancia en el caso.
  - Frase: “Ingeniero y controlador de [[Itelecom Holding Chile SpA]]”
  - Sugerencia: Aclarar si el rol de ingeniero y controlador está vinculado directamente con los hechos investigados.

## [[Leonarda Villalobos Muth]]
- **alto** — Afirma como hecho probado la canalización de pagos de $100.000.000 CLP sin mencionar que se trata de una acusación o presunta actividad, lo que puede interpretarse como una afirmación de hecho probado.
  - Frase: “Registró y participó en la reunión del edificio Alonso de Córdova ([[Audio-Reunion-Edificio-Alonso-2023]]) con [[Luis Hermosilla Osorio]], donde se detalló la canalización de pagos por **$100.000.000 CLP** ([[TRX-2023-06-22-Reunion-Audios-01]]) desde el entorno de [[Factop SpA]] hacia funcionarios del [[Servicio Impuestos Internos]]”
  - Sugerencia: Revisar la frase para evitar afirmar hechos como probados sin evidencia judicial.
- **medio** — Usa términos que sugieren culpabilidad sin mencionar que la situación procesal es 'formalizado', lo que implica que aún no hay condena.
  - Frase: “Abogada formalizada en el [[Caso Audios]] por [[Cohecho]], [[Lavado de Activos]] y delitos tributarios.”
  - Sugerencia: Revisar el lenguaje para evitar sugerir culpabilidad antes de una condena.

## [[Loreto Letelier]]
- **alto** — Afirma como hecho probado un delito sin que exista una condena o sentencia ejecutoriada, lo cual contradice la situación procesal declarada en METADATOS.
  - Frase: “se habían quemado a sí mismas con bombas molotov”
  - Sugerencia: Evitar afirmar hechos como si fueran probados cuando no hay condena o sentencia ejecutoriada. Se recomienda usar términos como 'afirmó' o 'declaró' en lugar de presentarlos como hechos probados.

## [[Lucia Hiriart Rodriguez]]
- **medio** — Atribuye un monto total a una causa colectiva sin especificar si corresponde exclusivamente a la persona mencionada.
  - Frase: “restitución al Estado de 108 inmuebles y fondos líquidos por más de `$10.500.000.000 CLP`”
  - Sugerencia: Precisar si el monto corresponde exclusivamente a Lucia Hiriart Rodriguez o si forma parte de un acuerdo colectivo.

## [[Luis Hermosilla Osorio]]
- **alto** — Atribuye un monto específico a una persona sin haber sido condenado o probado judicialmente, lo que puede constituir calumnia o difamación.
  - Frase: “transfiriéndole más de `$190.000.000 CLP` desde fondos originados en [[Factop SpA]]”
  - Sugerencia: Evitar mencionar montos concretos sin evidencia judicial o condena firme.

## [[Manuel Ariztia Ruiz]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre una persona o entidad sin condena criminal
  - Frase: “cartel avícola sancionado en el [[Caso Colusion de los Pollos]]”
  - Sugerencia: reemplazar 'cartel' por un término neutral, como 'grupo' o 'organización'

## [[Marcelo Campos Henriquez]]
- **medio** — Usa el verbo 'habría' que sugiere una acción probada, pero no se menciona una condena ni sentencia, lo que podría generar una impresión de culpabilidad sin fundamento legal.
  - Frase: “habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]”
  - Sugerencia: Revisar el uso de 'habría' y reemplazarlo por un lenguaje más neutral, como 'se le atribuye haber anticipado'.
- **medio** — El uso de 'presuntamente' es correcto, pero la frase sugiere una acción probada al mencionar el monto en efectivo, lo que podría interpretarse como un hecho confirmado.
  - Frase: “fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo a [[Marcelo Campos Henriquez]]”
  - Sugerencia: Aclarar que el monto es una acusación y no un hecho probado, usando términos como 'se le atribuye haber entregado presuntamente'.

## [[Olga Paz Barraza Quezada]]
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('Clan Barraza') sobre una persona sin condena
  - Frase: “líder del denominado 'Clan Barraza'”
  - Sugerencia: evitar el uso de términos que puedan generar estigmatización o asociación con grupos delictivos sin evidencia judicial
- **medio** — afirma como hecho probado un delito ('obtenido devoluciones') cuando la situación procesal no es condenado
  - Frase: “habría obtenido devoluciones del impuesto específico al diésel por $2.489 millones”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria de la información, como 'se le imputa' o 'se le atribuye'

## [[Oscar Aitken Lavanchy]]
- **alto** — Afirman como hecho probado un delito ('se acreditó') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “se acreditó que actuó como operador jurídico y fiduciario en la constitución y administración de sociedades de papel *offshore* en Islas Vírgenes Británicas, Bahamas y Panamá (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*), agrupadas bajo [[Riggs Bank y Sociedades Offshore Ashburton]], utilizadas para triangular caudales públicos provenientes de gastos reservados ([[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]]) y ocultar rentas ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]])”
  - Sugerencia: Evitar afirmaciones de hechos probados sin que exista una sentencia condenatoria. Utilizar términos como 'se ha señalado' o 'se le imputa' en su lugar.

## [[Osvaldo Mario Luis Sacco Croxatto]]
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('Clan Croxatto') sobre una persona sin condena
  - Frase: “líder del denominado 'Clan Croxatto'”
  - Sugerencia: evitar el uso de términos peyorativos o calificativos no judiciales, como 'Clan Croxatto', en ausencia de una condena judicial
- **medio** — afirma como hecho probado un delito ('habría generado pérdidas fiscales por...') cuando la situación procesal no es condenado
  - Frase: “habría generado pérdidas fiscales por $422.727.859 mediante seis empresas proveedoras de facturas falsas”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria de la información, como 'se le imputa haber generado pérdidas fiscales...'

## [[Pablo Wagner San Martin]]
- **medio** — afirma como hecho probado el pago de dinero sin mencionar que la situación procesal no es condena firme, sino absolutoria en algunos delitos
  - Frase: “recibió pagos bimensuales de `$3.000.000 CLP` (`$42.000.000 CLP` en total) de [[Empresas Penta SA]] mientras ejercía funciones públicas, documentados con boletas de terceros”
  - Sugerencia: revisar si los montos y pagos son hechos probados o solo presuntos, y ajustar el lenguaje para evitar afirmaciones definitivas sin base procesal
- **medio** — menciona una afirmación de la Fiscalía que no es un hecho probado, pero podría interpretarse como una admisión de falta de pruebas, lo que requiere precisión en el lenguaje
  - Frase: “la propia Fiscalía reconoció no haber acreditado que los pagos fueran a cambio de favores”
  - Sugerencia: revisar el uso de la frase 'reconoció no haber acreditado' para evitar ambigüedades y asegurar que se refleje la situación procesal correctamente

## [[Patricio Marin Lazo]]
- **alto** — Afirmación de autoría probada sin mencionar si la condena fue firme o si se encuentra en apelación
  - Frase: “Durante el juicio oral ([[Sentencia-TOP-Temuco-OperacionHuracan-2024]]), el tribunal acreditó su autoría en la remisión de informes falsificados dirigidos al Ministerio Público y a tribunales con el objeto de inducir detenciones y medidas cautelares”
  - Sugerencia: Especificar si la condena es firme o si se encuentra en apelación
- **alto** — Afirmación de condena sin aclarar si se encuentra en apelación o si es firme
  - Frase: “siendo sentenciado a **5 años de presidio** menor en su grado máximo por [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]]”
  - Sugerencia: Especificar si la condena es firme o si se encuentra en apelación
- **medio** — Usa lenguaje que sugiere responsabilidad directa sin aclarar si fue formalizado o condenado en dicha causa
  - Frase: “Coordinó en terreno la ejecución de la [[Caso Operacion Huracan]]”
  - Sugerencia: Aclarar si fue formalizado o condenado en el caso mencionado
- **medio** — Usa el término 'supuesto' que sugiere incertidumbre, pero la frase en general puede interpretarse como afirmación de hechos
  - Frase: “gestionó el pago de fondos reservados para financiar el supuesto software «Antorcha»”
  - Sugerencia: Revisar si el pago de fondos reservados fue acreditado judicialmente

## [[Percy Marin Vera]]
- **medio** — Usa el término 'objetó' que sugiere una afirmación de hecho, sin aclarar que se trata de una objeción de la Contraloría y no de una condena o resolución judicial definitiva.
  - Frase: “una auditoría de la Contraloría al Consejo Regional de Valparaíso objetó el cobro de más de $9 millones en viáticos y combustible por no acreditar su residencia”
  - Sugerencia: Revisar el uso del verbo 'objetó' para evitar la impresión de que el hecho está probado, y aclarar que se trata de una objeción de la Contraloría.

## [[Raul Torrealba del Pedregal]]
- **alto** — Afirman como hecho probado un delito ('desvío sistemático de subvenciones municipales') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “tras acreditarse mediante la autodenuncia de [[Domingo Prieto Urrejola]] ([[Declaracion-Judicial-Prieto-Vitacura-2021]]) el desvío sistemático de subvenciones municipales otorgadas a [[Vita Deportes]] ([[TRX-2021-04-15-Subvencion-VitaDeportes-01]])”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

## [[Roberto Belloni Pechini]]
- **alto** — uso de lenguaje peyorativo o calificativo no judicial ('cartel') sobre una persona sin condena
  - Frase: “cartel”
  - Sugerencia: reemplazar el término 'cartel' por un término neutral y descriptivo, como 'acuerdo' o 'colusión'

## [[Santiago Valdes Gutierrez]]
- **medio** — Usa el término 'delitos tributarios' sin aclarar que no hay condena ni sentencia que lo declare culpable, lo que podría dar la impresión de que el delito fue probado.
  - Frase: “Fue formalizado en 2015 en el [[Caso Penta]] por delitos tributarios vinculados a facturas emitidas a [[SQM SA]]”
  - Sugerencia: Aclarar que se trata de una acusación formalizada, no de un delito probado.
- **medio** — Aunque es correcto mencionar la ausencia de sentencia, el enunciado puede interpretarse como una afirmación de que no hay evidencia de falsedad, lo que podría ser ambiguo.
  - Frase: “no existe sentencia que declare falsas las facturas”
  - Sugerencia: Reforzar que la presunción de inocencia rige y que no hay sentencia condenatoria.

## [[Sebastian Pinera Echenique]]
- **medio** — Usa lenguaje que sugiere una intención o acción directa sin evidencia de condena o sentencia judicial que respalde dicha afirmación.
  - Frase: “supeditando el último pago de US$ 9,9 millones a que su propio gobierno no declarara zona de exclusión ambiental en La Higuera”
  - Sugerencia: Revisar si hay pruebas judiciales o administrativas que respalden la afirmación y reemplazar con un lenguaje más neutral.
- **medio** — Atribuye una acción específica a una persona sin evidencia de condena o sentencia judicial que respalde dicha afirmación.
  - Frase: “vendió en las Islas Vírgenes Británicas el proyecto minero-portuario Dominga a [[Andes Iron SpA]]”
  - Sugerencia: Verificar si hay pruebas judiciales o administrativas que respalden la afirmación y reemplazar con un lenguaje más neutral.

## [[Ximena Tavitxa Jimenez Farias]]
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre una persona sin condena
  - Frase: “denominado 'Clan Galaz'”
  - Sugerencia: evitar el uso de términos como 'clan' que pueden ser interpretados como calificativos no judiciales

## [[Agencia Central de Inteligencia CIA y Escuela de las Americas]]
- **alto** — afirma hechos probados sobre una institución sin mencionar si hay una condena o sentencia judicial
  - Frase: “pagos a la DINA”
  - Sugerencia: revisar si existe una condena judicial o sentencia que respalde dicha afirmación y reemplazar por lenguaje más neutral si no es el caso
- **medio** — afirma hechos como si fueran probados sin mencionar si hay una condena o sentencia judicial
  - Frase: “instrucción de oficiales chilenos en Fort Gulick (Panamá) mediante los manuales del Proyecto X”
  - Sugerencia: verificar si hay una condena judicial o sentencia que respalde dicha afirmación y reemplazar por lenguaje más neutral si no es el caso

## [[Agricola Don Pollo Limitada]]
- **alto** — afirma como hecho probado un delito sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “fue condenada por formar parte del cartel oligopólico”
  - Sugerencia: revisar si la condena es firme y si se debe usar lenguaje judicial como 'condenada' o 'absuelta' según el estado procesal
- **alto** — afirma como hecho probado un delito sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “la [[Corte Suprema de Chile]] le impuso una multa de 12.000 UTA”
  - Sugerencia: verificar si la multa fue impuesta y si se debe usar lenguaje judicial como 'condenada' o 'absuelta' según el estado procesal
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales sobre una entidad sin condena
  - Frase: “cartel oligopólico”
  - Sugerencia: evitar el uso de términos como 'cartel' si no hay una condena firme

## [[Andes Iron SpA]]
- **alto** — Afirma como hecho probado que Carlos Alberto Delano Abbott fue condenado, sin mencionar si la condena es firme o si se encuentra en apelación.
  - Frase: “controlada por la familia de [[Carlos Alberto Delano Abbott]] (condenado en el [[Caso Penta]]).”
  - Sugerencia: Revisar si la condena mencionada es definitiva y, en caso contrario, reemplazar 'condenado' por 'acusado' o 'presunto'.

## [[Bancard Inversiones Ltda]]
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al referirse al grupo de Sebastian Pinera Echenique como 'grupo' sin evidencia de delito probado.
  - Frase: “Matriz de inversiones y *family office* del grupo de [[Sebastian Pinera Echenique]] y su familia”
  - Sugerencia: Evitar calificativos no judiciales como 'grupo' o 'familia' sin evidencia de delito probado.
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al referirse a filiales como 'brazo offshore' sin evidencia de delito probado.
  - Frase: “integrada por sus filiales chilenas *Inversiones Santa Cecilia S.A.*, *Inversiones Mediterráneo* y su brazo *offshore* en las Islas Vírgenes Británicas *Bancard International Investment Inc.*”
  - Sugerencia: Evitar calificativos no judiciales como 'brazo offshore' sin evidencia de delito probado.

## [[Corpesca SA]]
- **alto** — Afirma como hecho probado un delito ('condenada penalmente') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “Empresa pesquera industrial condenada penalmente como persona jurídica (bajo la Ley N° 20.393)”
  - Sugerencia: Revisar si la condena se encuentra declarada en METADATOS y si es posible sustituir 'condenada' por 'acusada' o 'formalizada' según corresponda.

## [[Empresas CMPC SA]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre una entidad sin condena firme
  - Frase: “cartel que operó entre 2000 y 2015 para fijar precios de venta y repartirse cuotas en el mercado del papel higiénico, servilletas y toallas de papel”
  - Sugerencia: reemplazar 'cartel' por términos neutrales como 'acuerdo' o 'colusión'
- **medio** — afirma como hecho probado una sanción sin mencionar si fue condena firme o si la causa está formalizada
  - Frase: “sancionada por la [[Corte Suprema de Chile]] con una multa de 20.000 UTA al determinarse que había coaccionado a su competidora para sostener el acuerdo”
  - Sugerencia: precisar si la sanción fue confirmada en una sentencia firme o si se encuentra en trámite

## [[Empresas Penta SA]]
- **medio** — afirma que la imputación de soborno fue retirada en 2018, lo que sugiere que no hay condena, pero no se menciona explícitamente que el pago no haya sido probado como delito
  - Frase: “realizar pagos bimensuales (sin condena por cohecho: la imputación de soborno fue retirada en 2018) al entonces Subsecretario de Minería [[Pablo Wagner San Martin]] ([[TRX-2011-03-10-Pagos-Penta-Wagner-01]]), según [[Sentencia-8Juzgado-Garantia-Penta-2018]]”
  - Sugerencia: evitar afirmar hechos como probados si no hay condena firme, y usar lenguaje más cauteloso

## [[Factop SpA]]
- **alto** — Afirma como hecho probado la existencia de un fondo de sobornos sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “estructuraron el fondo de sobornos [[TRX-2023-06-22-Reunion-Audios-01]] dirigido a funcionarios del [[Servicio Impuestos Internos]]”
  - Sugerencia: Evitar afirmar hechos como probados sin evidencia judicial concluyente.

## [[Frasim Ltda]]
- **alto** — Atribuye hechos a la sociedad sin establecer que haya sido condenada o que los hechos hayan sido probados judicialmente
  - Frase: “Sociedad proveedora utilizada en el [[Caso Milicogate]] para emitir facturas por servicios y suministros inexistentes pagados con fondos de la Ley Reservada del Cobre desde el [[Comando de Apoyo a la Fuerza del Ejercito]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]), en coordinación con el coronel (r) [[Jozo Santic Palomino]] y documentado en [[Auto-Procesamiento-Ministra-Rutherford-2019]]”
  - Sugerencia: Revisar si los hechos mencionados han sido probados judicialmente y evitar afirmar como hechos probados situaciones que aún no estén resueltas en el proceso

## [[Fundacion CEMA Chile]]
- **alto** — Afirma como hecho probado un delito ('acreditaron') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el Ministro en Visita Guillermo de la Barra y el Consejo de Defensa del Estado acreditaron que la entidad recibió gratuitamente más de 135 inmuebles fiscales, municipales y del SERVIU”
  - Sugerencia: Evitar el uso de términos que sugieran certeza de hechos sin una sentencia condenatoria.

## [[Gestion Ambiental y Territorial SA]]
- **alto** — Afirma como hecho probado un delito ('reintegraba fondos en efectivo y cheques para financiar sobresueldos ministeriales') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “reintegraba fondos en efectivo y cheques para financiar sobresueldos ministeriales, según acreditó la [[Corte Suprema de Chile]] en [[Sentencia-Corte-Suprema-MOPGate-2016]]”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

## [[Inmobiliaria San Valentino SpA]]
- **medio** — Uso de lenguaje que sugiere una acción negativa o irregular sin haberse establecido una condena o responsabilidad legal probada.
  - Frase: “activó la bandera roja de Constitución Societaria Reciente (`< 365 días`)”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como valorativos o que sugieran irregularidades sin evidencia judicial.

## [[Riggs Bank y Sociedades Offshore Ashburton]]
- **alto** — Afirma como hecho probado un delito ('acreditaron') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el Subcomité de Investigaciones del Senado de EE.UU. y el Ministro en Visita [[Sergio Munoz Gajardo]] acreditaron que esta estructura albergó más de 125 cuentas secretas”
  - Sugerencia: Evitar el uso de términos que sugieran certeza sobre hechos que no han sido probados judicialmente.

## [[SQM SA]]
- **medio** — Atribuye hechos probados a la empresa sin mencionar que la situación procesal no es condena firme.
  - Frase: “La empresa reconoció ante la SEC y el DOJ de EE.UU. pagos indebidos por unos US$ 14,75 millones.”
  - Sugerencia: Revisar si la frase refleja una condena o acuerdo judicial, y en caso contrario, reemplazar por un lenguaje más preciso como 'reconoció haber realizado pagos indebidos según declaraciones ante la SEC y el DOJ'.

## [[Sociedad Benefactora y Educacional Dignidad]]
- **alto** — Afirma como hechos probados delitos graves sin mencionar que la situación procesal no es condena firme o que la causa no tiene sentencia.
  - Frase: “perpetraron crímenes de lesa humanidad, trabajo esclavo de colonos no remunerados, abuso sexual sistemático de menores y acopio de armamento de guerra”
  - Sugerencia: Revisar y reemplazar con términos que reflejen la naturaleza procesal de las acusaciones, como 'acusado de' o 'presunto'.

## [[Sociedad de Inversiones Pampa Calichera SA]]
- **alto** — Afirma como hecho probado un delito ('acreditó', 'irrogando un perjuicio multimillonario') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “la [[Comision para el Mercado Financiero]] (entonces SVS) acreditó que [[Sociedad de Inversiones Pampa Calichera SA]] vendió paquetes accionarios a precios subvalorados a sociedades relacionadas con su propio controlador para luego recomprarlos a sobreprecio, irrogando un perjuicio multimillonario a los accionistas minoritarios y AFPs”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria o resolución judicial que lo respalde.

## [[Valmoval Ltda]]
- **medio** — Usa un término que puede implicar responsabilidad sin mencionar una condena o sentencia judicial
  - Frase: “declarada en quiebra”
  - Sugerencia: Revisar si la declaración en quiebra fue judicialmente establecida y usar lenguaje más preciso
- **medio** — Atribuye una acción a una persona sin evidencia judicial concluyente
  - Frase: “activos fueron adquiridos en enero de 1989 por las Fábricas y Maestranzas del Ejército (FAMAE / [[Comando de Apoyo a la Fuerza del Ejercito]]) bajo el mando de [[Augusto Pinochet Ugarte]]”
  - Sugerencia: Verificar si hay pruebas judiciales que respalden esta afirmación y usar lenguaje más cauteloso
- **medio** — Asume como hecho probado una transacción sin mencionar una condena o sentencia judicial
  - Frase: “girándose tres cheques por cerca de US$ 3 millones (`$2.950.000.000 CLP` actualizados) directamente a nombre de su hijo [[Augusto Pinochet Hiriart]]”
  - Sugerencia: Revisar si la transacción fue judicialmente establecida y usar lenguaje más preciso
- **medio** — Asume una omisión de la Contraloría sin evidencia judicial concluyente
  - Frase: “sin toma de razón de la [[Contraloria General de la Republica]]”
  - Sugerencia: Verificar si hay pruebas judiciales que respalden esta afirmación y usar lenguaje más cauteloso

## [[Caso Asignaciones Parlamentarias y Cuota Flores]]
- **medio** — Usa el término 'presuntos delitos' lo cual es correcto, pero la frase menciona delitos de forma general sin especificar si están acreditados o no, lo que puede generar ambigüedad.
  - Frase: “presuntos delitos reiterados de fraude al Fisco, desvío de caudales públicos y vulneración de normas laborales y de probidad en el Congreso Nacional.”
  - Sugerencia: Aclarar que se trata de delitos presuntos y no acreditados, y evitar generalizaciones sin evidencia.

## [[Caso Audios]]
- **medio** — afirma como hecho probado un delito ('aristas estructurales de trafico de influencias') cuando la situación procesal no es condenado
  - Frase: “la incautación del teléfono de [[Luis Hermosilla Osorio]] abrió además aristas estructurales de [[Trafico de Influencias]]”
  - Sugerencia: revisar el lenguaje para evitar afirmaciones de hechos probados sin evidencia judicial
- **medio** — afirma como hecho probado un delito ('pagos desde Factop SpA') cuando la situación procesal no es condenado
  - Frase: “los pagos desde [[Factop SpA]] para financiar la defensa en la Acusación Constitucional de 2019”
  - Sugerencia: revisar el lenguaje para evitar afirmaciones de hechos probados sin evidencia judicial

## [[Caso Basura]]
- **alto** — uso de lenguaje peyorativo ('corrupción') sin condena judicial explícita
  - Frase: “red transversal de corrupción municipal”
  - Sugerencia: reemplazar por términos neutrales y evitar calificativos no judiciales
- **medio** — exposición de datos económicos sin vincularlos directamente a una condena judicial
  - Frase: “multimillonarios contratos de recolección, transporte y disposición final de residuos domiciliarios”
  - Sugerencia: contextualizar la información dentro del marco procesal y evitar generalizaciones
- **medio** — mencionar entidades sin indicar si han sido condenadas o no
  - Frase: “consorcio [[KDM Empresas SA]] (representado por [[Fernando Leon Steffens]]”
  - Sugerencia: especificar el estado judicial de las entidades mencionadas

## [[Caso CEMA Chile]]
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales sobre una persona sin condena
  - Frase: “entidad privada presidida a perpetuidad hasta agosto de 2016 por [[Lucia Hiriart Rodriguez]]”
  - Sugerencia: Evitar calificativos no judiciales como 'presidida a perpetuidad' que pueden interpretarse como valoraciones negativas sin base legal
- **medio** — Exponen datos personales o de la vida íntima/familiar ajenos al hecho de interés público
  - Frase: “cónyuge de [[Augusto Pinochet Ugarte]]”
  - Sugerencia: Evitar mencionar relaciones personales a menos que sean relevantes para el hecho investigado
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “mecanismo forense acreditado en la causa operó en tres fases”
  - Sugerencia: Utilizar lenguaje más cauteloso como 'se investigó' en lugar de 'acreditado'
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “recaudando más de `$8.900.000.000 CLP`”
  - Sugerencia: Evitar afirmaciones de montos económicos como si fueran hechos probados sin evidencia judicial
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “sufragar gastos y asignaciones vinculadas a [[Lucia Hiriart Rodriguez]] y su entorno familiar”
  - Sugerencia: Utilizar lenguaje más cauteloso como 'se investigó' en lugar de afirmaciones directas
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “restituir al Estado de Chile 108 inmuebles fiscales y municipales más sus fondos bancarios remanentes”
  - Sugerencia: Evitar afirmaciones de hechos como si fueran probados sin evidencia judicial

## [[Caso Colusion de las Farmacias]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre personas o entidades sin condena explícita en el texto, aunque la causa está cerrada con condena
  - Frase: “formación de un cartel de precios entre las tres principales cadenas farmacéuticas del país”
  - Sugerencia: reemplazar 'cartel' por términos neutrales como 'acuerdo' o 'colusión'

## [[Caso Colusion de los Pollos]]
- **alto** — uso de lenguaje peyorativo ('cartel delictivo') sobre una asociación gremial sin condena firme de su naturaleza delictiva, ya que la sentencia menciona su disolución forzada por haber sido instrumentalizada, pero no afirma explícitamente que sea un cartel delictivo
  - Frase: “instrumentalizada como cartel delictivo”
  - Sugerencia: reemplazar 'cartel delictivo' por 'asociación gremial instrumentalizada en prácticas anticompetitivas' para evitar lenguaje no judicial
- **medio** — uso de término 'cartel' para referirse a una investigación, lo cual puede interpretarse como lenguaje peyorativo o calificativo no judicial
  - Frase: “Cartel de los Supermercados”
  - Sugerencia: reemplazar 'Cartel de los Supermercados' por 'investigación sobre prácticas anticompetitivas en los supermercados' para mantener un lenguaje neutral y judicial

## [[Caso Colusion del Papel Tissue]]
- **alto** — Usa el término 'condena histórica' sin especificar si se trata de una condena firme o si aún está en apelación, lo que puede generar una impresión errónea de certeza en el hecho probado.
  - Frase: “condena histórica por colusión y formación de cartel empresarial”
  - Sugerencia: Reemplazar por 'condena por colusión y formación de cartel empresarial' o 'condena en primera instancia por colusión y formación de cartel empresarial' según corresponda.
- **medio** — Atribuye una caracterización general a las empresas sin mencionar si esta afirmación está respaldada por evidencia judicial o si es una interpretación subjetiva.
  - Frase: “protagonizado por las dos empresas dominantes que concentraban más del 90% del mercado chileno”
  - Sugerencia: Añadir una referencia a la evidencia judicial que respalde la afirmación de que las empresas concentraban más del 90% del mercado chileno.

## [[Caso Convenios]]
- **medio** — exposición de montos sin acreditar su vinculación con delitos, lo que puede generar impresión de culpabilidad
  - Frase: “el monto total transferido bajo el Programa de Asentamientos Precarios alcanzó los $426.000.000 CLP”
  - Sugerencia: revisar si el monto está relacionado con hechos probados o si se debe usar lenguaje más cauteloso como 'se transfirieron' en lugar de 'alcanzó los'
- **medio** — afirmación de un delito como probado cuando la causa está formalizada, no condenada
  - Frase: “el Consejo de Defensa del Estado (CDE) presentó querella criminal por el delito de fraude al fisco reiterado”
  - Sugerencia: reemplazar 'presentó querella criminal por el delito de fraude al fisco reiterado' por 'presentó querella criminal por presunto delito de fraude al fisco reiterado'

## [[Caso Corpesca]]
- **alto** — Afirma como hecho probado un delito ("acreditarse que recibió $233.000.000 CLP") cuando la situación procesal es cerrada, no necesariamente condena firme
  - Frase: “El 3° Tribunal de Juicio Oral en lo Penal de Santiago ([[Sentencia-3TOP-Santiago-Corpesca-2020]]) condenó al exsenador de [[Union Democrata Independiente]], [[Jaime Orpis Bouchon]], a 5 años y un día de presidio efectivo por [[Cohecho]] y [[Fraude al Fisco]] en el [[Senado de la Republica de Chile]], tras acreditarse que recibió **$233.000.000 CLP** ([[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]]) desde la pesquera [[Corpesca SA]], autorizados por su gerente general [[Francisco Mujica Ortuzar]], para representar los intereses de la compañía en las votaciones legislativas.”
  - Sugerencia: Revisar si la sentencia mencionada es firme y si el monto mencionado es definitivo según la sentencia
- **medio** — Usa lenguaje peyorativo como "corrupción" sin necesidad, aunque se menciona condena, no se considera calificativo no judicial en este contexto
  - Frase: “Primera causa en la historia judicial chilena en que un parlamentario en ejercicio y una gran empresa fueron condenados en juicio oral por delitos de corrupción asociados a la tramitación de una ley de la República ("Ley de Pesca")”
  - Sugerencia: Revisar si el uso de "corrupción" es necesario o si se puede reemplazar por un término más neutral

## [[Caso Exalmar y Fideicomiso Ciego]]
- **medio** — atribuye a una empresa hechos vinculados a un fallo judicial sin establecer una conexión directa probada con el sujeto investigado
  - Frase: “empresa directamente beneficiada por los derechos de pesca en el triángulo marítimo adjudicado a Perú en el fallo de enero de 2014”
  - Sugerencia: revisar y precisar la relación entre la empresa y el sujeto investigado, evitando afirmaciones no verificables
- **medio** — usa lenguaje que sugiere una vinculación directa y beneficiosa sin evidencia judicial concluyente
  - Frase: “empresa directamente beneficiada por los derechos de pesca en el triángulo marítimo adjudicado a Perú en el fallo de enero de 2014”
  - Sugerencia: reformular la frase para evitar interpretaciones que puedan ser consideradas calumnias o injurias

## [[Caso Luminarias LED]]
- **alto** — Afirma como hecho probado un delito ('pagó sobornos') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “pagó sobornos a directivos y asesores municipales —como el administrador municipal de la [[Municipalidad de Chillan]], [[Marcelo Campos Henriquez]]— para manipular las bases técnicas y adjudicarse contratos”
  - Sugerencia: Reemplazar por lenguaje que refleje la naturaleza acusatoria de la investigación, como 'se le imputa haber pagado sobornos'.
- **medio** — Usa lenguaje que sugiere certeza sobre hechos que aún no han sido probados.
  - Frase: “según la hipótesis de la Fiscalía”
  - Sugerencia: Mantener el uso de 'según la hipótesis de la Fiscalía' para reflejar la naturaleza acusatoria de la investigación.
- **medio** — Usa lenguaje que sugiere certeza sobre hechos que aún no han sido probados.
  - Frase: “habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]”
  - Sugerencia: Reemplazar 'habría' por 'se le imputa haber anticipado' para reflejar la naturaleza acusatoria de la investigación.

## [[Caso Megafraude Tributario Operacion Tributos]]
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clanes') sobre personas sin condena
  - Frase: “clanes”
  - Sugerencia: reemplazar por términos neutrales y no calificativos
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre personas sin condena
  - Frase: “clan Canessa”
  - Sugerencia: reemplazar por términos neutrales y no calificativos
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre personas sin condena
  - Frase: “clan Galaz”
  - Sugerencia: reemplazar por términos neutrales y no calificativos
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre personas sin condena
  - Frase: “clan Barraza”
  - Sugerencia: reemplazar por términos neutrales y no calificativos
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre personas sin condena
  - Frase: “clan Croxatto”
  - Sugerencia: reemplazar por términos neutrales y no calificativos
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre personas sin condena
  - Frase: “clan Nexus”
  - Sugerencia: reemplazar por términos neutrales y no calificativos
- **alto** — uso de lenguaje peyorativo o calificativos no judiciales ('clan') sobre personas sin condena
  - Frase: “clan Barriga & Polanco”
  - Sugerencia: reemplazar por términos neutrales y no calificativos

## [[Caso Minera Dominga Pandora Papers]]
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales ('íntimo amigo') sobre una persona sin condena
  - Frase: “socio fundador de [[Empresas Penta SA]] e íntimo amigo del entonces Presidente de la República [[Sebastian Pinera Echenique]]”
  - Sugerencia: reemplazar 'íntimo amigo' por un término neutral, como 'conocido' o 'relacionado'
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales ('condenado') sobre una persona sin condena firme en el contexto de la causa actual
  - Frase: “condenado en el [[Caso Penta]] por delitos tributarios y enriquecimiento ilícito (absuelto de cohecho)”
  - Sugerencia: reemplazar 'condenado' por 'acusado' o 'imputado'
- **medio** — afirma como hecho probado la ausencia de gestiones sin evidencia suficiente
  - Frase: “no se encontró fuente que acredite gestiones suyas a favor del proyecto”
  - Sugerencia: revisar el uso de 'no se encontró fuente' y reemplazar por 'no se ha podido acreditar' para evitar afirmaciones definitivas

## [[Caso Municipalidad de Maipu]]
- **alto** — Afirma como hecho probado un delito (perjuicio fiscal) cuando la situación procesal es formalizada, no condenado.
  - Frase: “perjuicio fiscal imputado por el Ministerio Público y el Consejo de Defensa del Estado asciende a $30.972.000.000 CLP”
  - Sugerencia: Evitar afirmar montos o hechos como si fueran probados, ya que la causa no ha sido resuelta con sentencia condenatoria.

## [[Caso Operaciones Digitales e Injerencia Electoral]]
- **medio** — Uso del término 'acreditaron' sugiere certeza en un hecho que podría no estar probado judicialmente, lo que puede generar una impresión de certeza no respaldada por la situación procesal actual.
  - Frase: “Registros fotográficos y documentales acreditaron la presencia física de Cerimedo en la sede nacional del partido”
  - Sugerencia: Reemplazar 'acreditaron' por un término más neutro, como 'mostraron' o 'registraron', para evitar dar la impresión de certeza judicial.

## [[Caso Pacogate]]
- **alto** — Afirma como hecho probado un delito con un monto específico sin que la situación procesal indique una condena firme.
  - Frase: “habrían sustraído $28.348.928.198 CLP”
  - Sugerencia: Evitar afirmar montos o hechos como si fueran probados cuando la causa no tiene sentencia firme.
- **medio** — Menciona un veredicto condenatorio, pero el estado judicial indica que el veredicto no está firme.
  - Frase: “dictó veredicto condenatorio contra 25 de los 28 acusados”
  - Sugerencia: Precisar que el veredicto no es firme y que la sentencia aún no se ha dictado.

## [[Caso Panama Papers Chile]]
- **medio** — Afirma como hecho probado la gestión de sociedades offshore sin mencionar que no hay condena o sentencia en la causa judicial
  - Frase: “La filtración reveló que el abogado [[Gonzalo Delaveau Swett]] —quien hasta ese momento ejercía como Presidente de *Chile Transparente*** (el capítulo chileno de Transparencia Internacional)— actuaba simultáneamente como agente e intermediario de [[Mossack Fonseca y Sociedades Offshore Panama]], gestionando y administrando al menos cinco sociedades *offshore* domiciliadas en Bahamas (*Turnbrook Corporation*, *DKL Holdings*, *Westquarter Limited*, *Mining Press Holdings* y *Turnbrook Mining Ltd.*) articuladas en torno al proyecto minero *Andes Copper*”
  - Sugerencia: Revisar si la gestión de sociedades offshore fue acreditada judicialmente y evitar afirmaciones como hechos probados si no hay sentencia
- **medio** — Afirma como hecho probado la creación de fundaciones y sociedades offshore sin mencionar que no hay condena o sentencia en la causa judicial
  - Frase: “Los registros de Mossack Fonseca documentaron la creación de las fundaciones de interés privado *Ashton Foundation* y *Kintyre Foundation* en Panamá por parte del propietario de *El Mercurio*, [[Agustin Edwards Eastman]], así como las sociedades *Sierra Leona S.A.* y *Railton Foundation* vinculadas al expresidente de la Confederación de la Producción y del Comercio (CPC) y de la SONAMI, [[Alfredo Ovalle Rodriguez]]”
  - Sugerencia: Revisar si la creación de fundaciones y sociedades offshore fue acreditada judicialmente y evitar afirmaciones como hechos probados si no hay sentencia
- **medio** — Afirma como hecho probado la conexión con sociedades offshore sin mencionar que no hay condena o sentencia en la causa judicial
  - Frase: “Los archivos internos de [[Mossack Fonseca y Sociedades Offshore Panama]] confirmaron que el bufete panameño prestó servicios registrales a sociedades de papel en las Islas Vírgenes Británicas conectadas con la red fiduciaria de [[Riggs Bank y Sociedades Offshore Ashburton]], operada por [[Augusto Pinochet Ugarte]] y [[Oscar Aitken Lavanchy]] en el [[Caso Riggs]]”
  - Sugerencia: Revisar si la conexión con sociedades offshore fue acreditada judicialmente y evitar afirmaciones como hechos probados si no hay sentencia

## [[Caso Penta]]
- **alto** — Afirma como hecho probado un delito (condenado) cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “primer político condenado en juicio abreviado en diciembre de 2015”
  - Sugerencia: Evitar afirmar con certeza la condena de un político sin verificar que la causa tenga sentencia firme.

## [[Caso Riggs]]
- **medio** — uso de lenguaje que sugiere hechos probados sin mencionar la presunción de inocencia o la existencia de una condena firme
  - Frase: “estructuró y ocultó una red de más de 125 cuentas bancarias secretas”
  - Sugerencia: revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados sin evidencia judicial suficiente
- **medio** — uso de lenguaje que sugiere hechos probados sin mencionar la presunción de inocencia
  - Frase: “abrió cuentas secretas utilizando pasaportes diplomáticos y cédulas chilenas ideológicamente falsas”
  - Sugerencia: revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados sin evidencia judicial suficiente
- **medio** — uso de lenguaje que sugiere hechos probados sin mencionar la presunción de inocencia
  - Frase: “nutriéndolas con el desvío continuo de fondos públicos”
  - Sugerencia: revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados sin evidencia judicial suficiente
- **medio** — uso de lenguaje que sugiere hechos probados sin mencionar la presunción de inocencia
  - Frase: “declaraciones maliciosamente falsas e impuestos evadidos por más de $2.450.000.000 CLP”
  - Sugerencia: revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados sin evidencia judicial suficiente

## [[Caso SQM]]
- **medio** — Atribuye a SQM un hecho sin mencionar que sea probado judicialmente, lo que puede generar una impresión de culpabilidad sin base legal.
  - Frase: “La propia SQM reconoció ante la SEC y el Departamento de Justicia de EE.UU. pagos indebidos por unos US$ 14,75 millones.”
  - Sugerencia: Revisar si el reconocimiento de SQM fue judicialmente acreditado o si se trata de una admisión en un ámbito no judicial, y ajustar el lenguaje para evitar sugerir culpabilidad sin pruebas.

## [[Caso Sierra Bella]]
- **medio** — uso de lenguaje que puede implicar una atribución de responsabilidad sin haberse acreditado formalmente en el proceso
  - Frase: “encabezada por la alcaldesa [[Iraci Hassler Jacob]] ([[Partido Comunista de Chile]])”
  - Sugerencia: evitar mencionar atribuciones políticas o responsabilidades sin que estén respaldadas por la causa judicial
- **medio** — uso de lenguaje que puede implicar una atribución de responsabilidad sin haberse acreditado formalmente en el proceso
  - Frase: “representada por [[Felipe Sanchez Perez]]”
  - Sugerencia: evitar mencionar responsabilidades sin que estén respaldadas por la causa judicial
- **medio** — uso de lenguaje que puede implicar una atribución de responsabilidad sin haberse acreditado formalmente en el proceso
  - Frase: “tras detectarse tasaciones irregulares coordinadas entre peritos tasadores y funcionarios municipales”
  - Sugerencia: evitar mencionar responsabilidades sin que estén respaldadas por la causa judicial

## [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]]
- **medio** — afirma como hecho probado un delito o consecuencia sin que exista una sentencia condenatoria o resolución judicial que lo acredite
  - Frase: “provocó la insolvencia e intervención estatal de la institución financiera”
  - Sugerencia: revisar el uso de afirmaciones que implican responsabilidad directa sin evidencia judicial
- **medio** — afirma como hecho probado un delito o consecuencia sin que exista una sentencia condenatoria o resolución judicial que lo acredite
  - Frase: “permaneció 24 días prófugo”
  - Sugerencia: revisar el uso de afirmaciones que implican responsabilidad directa sin evidencia judicial

## [[TRX-1989-01-10-Emision-Pinocheques-Ejercito-Valmoval-01]]
- **alto** — Afirma como hecho probado un delito ('probó') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “probó que parte de estos fondos terminó depositada en cuentas extranjeras controladas por [[Augusto Pinochet Ugarte]] en [[Riggs Bank y Sociedades Offshore Ashburton]] ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).”
  - Sugerencia: Reemplazar 'probó' por un término más neutral, como 'indicó' o 'sugirió', para evitar afirmar hechos como probados sin una sentencia condenatoria.

## [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]
- **alto** — Afirma como hecho probado un delito sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “congelando cuotas del 76% para CMPC y 24% para PISA”
  - Sugerencia: Revisar si la frase se basa en una condena firme o en pruebas probatorias, y en caso de no ser así, reemplazar por un lenguaje más cauteloso como 'se acusó de congelar cuotas del 76% para CMPC y 24% para PISA'.

## [[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]
- **alto** — Afirma como hecho probado la existencia de un delito (desvío de caudales públicos y pago de sobresueldos) sin haberse establecido una condena o sentencia judicial.
  - Frase: “deliberadamente abultado en `$1.253.000.000 CLP` para desviar caudales públicos hacia el pago de sobresueldos de funcionarios y directivos ministeriales.”
  - Sugerencia: Reemplazar frases que afirman hechos como probados con términos que reflejen la naturaleza presunta de la información, como 'se habría abultado' o 'se habrían desviado caudales públicos'.

## [[TRX-2002-04-12-Facturas-Triangulacion-GATE-SII-01]]
- **alto** — Afirma como hecho probado la existencia de facturas ideológicamente falsas sin mencionar que la situación procesal no es condenado o que la causa no tiene sentencia.
  - Frase: “Contabilización de facturas y boletas de honorarios ideológicamente falsas por `$450.000.000 CLP`”
  - Sugerencia: Revisar el lenguaje para evitar afirmaciones que puedan interpretarse como hechos probados, utilizando términos como 'presunto' o 'acusado de'.

## [[TRX-2007-11-01-Coordinacion-Cartel-Precios-Medicamentos-Farmacias-01]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre personas sin condena
  - Frase: “cartel operó contactando a los laboratorios farmacéuticos para que actuaran como supervisores del cumplimiento de las listas de precios infladas”
  - Sugerencia: reemplazar 'cartel' por términos neutrales como 'grupo' o 'organización'

## [[TRX-2008-01-15-Pacto-Cuotas-Produccion-Cartel-Pollos-01]]
- **alto** — uso de lenguaje peyorativo ('Cartel') que sugiere una organización criminal sin que exista una condena o sentencia que lo acredite
  - Frase: “Cartel-Pollos-01”
  - Sugerencia: evitar el uso de términos como 'cartel' que pueden ser interpretados como calificativos no judiciales y que no están respaldados por una condena judicial

## [[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]]
- **medio** — Usa el término 'presumió' que indica una acusación sin prueba concluyente, lo cual es compatible con la presunción de inocencia, pero podría interpretarse como una afirmación de hecho probado si no se contextualiza adecuadamente.
  - Frase: “la Fiscalía presumió ideológicamente falsas por no existir servicios que las justificaran”
  - Sugerencia: Aclarar que la Fiscalía solo ha formulado una presunción, no una prueba concluyente de falsedad de las facturas.
- **medio** — Aunque es correcto señalar que no hay sentencia, el enunciado podría interpretarse como una afirmación de hecho probado si no se enfatiza la ausencia de condena.
  - Frase: “no existe sentencia que declare falsas las facturas”
  - Sugerencia: Reforzar que la ausencia de sentencia confirma la presunción de inocencia y que no se ha probado la falsedad de las facturas.

## [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]]
- **alto** — Afirma como hecho probado un delito ('acreditando la concertación ilícita') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “acreditando la concertación ilícita horizontal entre las farmacias”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

## [[TRX-2010-08-19-Correo-Royalty-SQM-01]]
- **medio** — Usa el verbo 'habría' que sugiere una acción no probada, pero no afirma directamente un hecho como probado. Sin embargo, menciona un monto específico sin aclarar que no está acreditado.
  - Frase: “la empresa habría canalizado pagos por aproximadamente $730.000.000 CLP entre 2009 y 2015 a personas de su entorno mediante boletas y facturas”
  - Sugerencia: Aclarar que el monto mencionado no está acreditado judicialmente y que se trata de una hipótesis acusatoria.

## [[TRX-2010-11-15-Soborno-Licitacion-Basura-Maipu-01]]
- **alto** — Afirma como hecho probado un delito ('acreditó transferencias trianguladas') sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “Fiscalía Regional Metropolitana Occidente acreditó transferencias trianguladas desde el ejecutivo [[Fernando Leon Steffens]] hacia el entonces concejal [[Marcelo Torres Ferrari]]”
  - Sugerencia: Reemplazar 'acreditó' por un término más neutro como 'indica' o 'señala' para evitar la impresión de que el hecho está probado.

## [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]]
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales al referirse a la familia del ex Presidente
  - Frase: “matriz de la familia del entonces Presidente de la República en ejercicio [[Sebastian Pinera Echenique]]”
  - Sugerencia: evitar calificar a la familia del ex Presidente con términos que puedan interpretarse como peyorativos
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales al referirse a una persona sin condena
  - Frase: “controlada por su amigo y socio [[Carlos Alberto Delano Abbott]] ([[Empresas Penta SA]]).”
  - Sugerencia: evitar calificar a terceros con términos que puedan interpretarse como peyorativos

## [[TRX-2011-03-10-Pagos-Penta-Wagner-01]]
- **medio** — afirma que la Fiscalía no acreditó un hecho, lo cual podría interpretarse como una afirmación de un delito sin prueba suficiente, aunque no se afirma directamente como probado
  - Frase: “la propia Fiscalía reconoció no haber acreditado que los pagos fueran a cambio de favores”
  - Sugerencia: revisar el uso de la frase para evitar interpretaciones que puedan implicar una afirmación de un delito sin evidencia suficiente

## [[TRX-2012-07-11-Soborno-LeyDePesca-Corpesca-01]]
- **alto** — Afirma como hecho probado un delito ('acreditado en juicio oral') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “Pagos ilícitos reiterados por un total acreditado en juicio oral de $233.000.000 CLP”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia firme.

## [[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]]
- **medio** — Atribuye a terceros (candidatos y dirigentes de la UDI) un hecho que no está probado ni vinculado directamente a la transacción auditada, lo que puede generar una presunción de culpabilidad injusta.
  - Frase: “financiar fuera del marco legal campañas electorales de candidatos y dirigentes de la [[Union Democrata Independiente]] como [[Pablo Longueira Montes]]”
  - Sugerencia: Revisar y reescribir la frase para evitar atribuir hechos no probados a terceros, manteniendo el enfoque en la transacción auditada.

## [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]]
- **alto** — Afirma como hecho probado un delito (condenado) cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el primer político condenado penalmente en el [[Caso Penta]]”
  - Sugerencia: Revisar si la condena mencionada corresponde a una sentencia firme y si se encuentra documentada en los METADATOS.

## [[TRX-2014-02-18-Soborno-Caval-Machali-01]]
- **alto** — Afirma como hecho probado un delito (condenado) sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “Silva fue condenado por cohecho reiterado en enero de 2018.”
  - Sugerencia: Revisar si la condena es firme y si se debe mencionar el estado actual del proceso judicial.
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al mencionar 'acusación de soborno' sin especificar que es una acusación formal.
  - Frase: “La acusación de soborno contra [[Mauricio Valero Illanes]] y la sociedad fue rechazada: ambos fueron absueltos por el TOP de Rancagua en julio de 2018.”
  - Sugerencia: Utilizar lenguaje más neutral, como 'acusación formal' en lugar de 'acusación de soborno'.

## [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]
- **medio** — Usa el término 'acreditada' que sugiere que el delito fue probado, sin mencionar si existe una sentencia condenatoria firme.
  - Frase: “acreditada en [[Auto-Procesamiento-Ministra-Rutherford-2019]] dentro del [[Caso Milicogate]]”
  - Sugerencia: Reemplazar 'acreditada' por un término más neutral, como 'relacionada' o 'vinculada', para evitar dar la impresión de que el delito fue probado sin una sentencia condenatoria.

## [[TRX-2015-01-29-Facturas-Falsas-Caval-SII-01]]
- **alto** — afirma como hecho probado un delito (condenó) cuando la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “TOP de Rancagua condenó a [[Natalia Compagnon Soto]] por permitir que la contabilidad social incorporara facturas ideológicamente falsas por asesorías inexistentes en los años tributarios 2013, 2014 y 2015”
  - Sugerencia: reemplazar por lenguaje que indique que se trata de una acusación o presunta condena, sin afirmar como hecho probado
- **medio** — afirma como hecho probado un delito (generó una utilidad bruta) cuando la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “operación de compraventa especulativa de los predios de Machalí que generó una utilidad bruta de $2.500.000.000 CLP para [[Exportadora y de Gestion Caval Ltda]]”
  - Sugerencia: reemplazar por lenguaje que indique que se trata de una acusación o presunta operación, sin afirmar como hecho probado

## [[TRX-2015-08-14-Lavado-GastosReservados-Ejercito-UAF-01]]
- **medio** — Atribuye hechos a una persona sin mencionar si hay una condena o si la situación procesal es formalizada, acusado o absuelto.
  - Frase: “realizadas por [[Juan Miguel Fuente-Alba Poblete]] con fondos provenientes de gastos reservados del Ejército y del [[Comando de Apoyo a la Fuerza del Ejercito]]”
  - Sugerencia: Se recomienda reemplazar con lenguaje que indique que son hechos imputados o presuntos, según la situación procesal.

## [[TRX-2015-10-29-Pago-Multas-Historicas-Cartel-Pollos-01]]
- **alto** — uso de lenguaje peyorativo ('cartel') que no es judicial y sugiere criminalidad sin condena firme
  - Frase: “Cartel de los Pollos”
  - Sugerencia: reemplazar por términos neutrales y no calificativos, como 'grupo empresarial' o 'organización'

## [[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]]
- **alto** — Afirma como hecho probado un delito ('probó que el bufete panameño administró y prestó servicios...') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “intersección documental acreditada en los archivos internos de [[Mossack Fonseca y Sociedades Offshore Panama]] ([[Informe-ICIJ-SII-PanamaPapers-Chile-2016]]) que probó que el bufete panameño administró y prestó servicios de agente residente en las Islas Vírgenes Británicas y Bahamas para sociedades de papel integradas en el circuito de [[Riggs Bank y Sociedades Offshore Ashburton]], estructuradas con intervención de [[Oscar Aitken Lavanchy]] para ocultar caudales de [[Augusto Pinochet Ugarte]] investigados en el [[Caso Riggs]] y posteriormente afectos al comiso de la [[Corte Suprema de Chile]] ([[Sentencia-Corte-Suprema-CasoRiggs-2018]]).”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria o resolución judicial que lo acredite.

## [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]
- **alto** — Afirma como hecho probado un delito ('acreditó ventas inmobiliarias') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “la reapertura judicial de 2016 en el [[Caso CEMA Chile]] acreditó ventas inmobiliarias por más de `$8.900.000.000 CLP`”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria o resolución judicial que lo respalde.

## [[TRX-2016-11-10-Desfalco-Intendencia-Carabineros-01]]
- **medio** — Usa un veredicto que no está firme como si fuera un hecho probado
  - Frase: “descartó la asociación ilícita”
  - Sugerencia: Se debe mencionar que el veredicto no está firme y que la asociación ilícita no fue descartada definitivamente
- **medio** — Afirma como hecho probado un delito sin que la situación procesal indique una condena firme
  - Frase: “lavado de activos”
  - Sugerencia: Se debe usar lenguaje que indique que es una acusación o presunta acción, no un hecho probado

## [[TRX-2017-03-06-Lavado-Activos-Carabineros-UAF-01]]
- **medio** — La frase indica que el veredicto no es firme, lo que contradice la presunción de inocencia al sugerir que hay un veredicto existente, aunque no definitivo.
  - Frase: “El veredicto no está firme.”
  - Sugerencia: Evitar mencionar el veredicto como algo existente si no es firme, para no generar confusión o impresión de culpabilidad.
- **medio** — La frase sugiere que un delito fue descartado, lo que puede interpretarse como un hecho probado, aunque en el contexto legal no se menciona una condena firme.
  - Frase: “descartó la asociación ilícita”
  - Sugerencia: Utilizar lenguaje más cauteloso, como 'no se encontró evidencia suficiente para considerar la asociación ilícita'.

## [[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]]
- **alto** — Afirma como hecho probado un delito ('acreditó') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2024]]) acreditó que los supuestos chats fueron redactados e implantados manualmente en los teléfonos por [[Leonardo Osses Sandoval]] y sus subalternos tras las incautaciones”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

## [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]]
- **medio** — Usa el término 'concluyentes' que sugiere certeza en los resultados del informe pericial, lo que podría interpretarse como afirmación de hechos probados sin que exista una sentencia o condena formal.
  - Frase: “la Fiscalía Regional de La Araucanía remitió al Juzgado de Garantía de Temuco los resultados concluyentes del informe pericial”
  - Sugerencia: Revisar el uso de términos que sugieran certeza absoluta en la ausencia de una sentencia judicial.

## [[TRX-2019-05-14-Soborno-Luminarias-Chillan-01]]
- **alto** — Afirma como hecho probado el pago de sobornos cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “obtenida mediante el pago de sobornos a [[Marcelo Campos Henriquez]] (integrante de la comisión evaluadora y administrador municipal)”
  - Sugerencia: Reemplazar por lenguaje presuntivo como 'presuntamente obtenida mediante el pago de sobornos'.

## [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]
- **alto** — afirma como hecho probado un monto total de transferencias sin mencionar que se trata de una estimación o acreditación obtenida a través de peritajes contables, lo que podría interpretarse como una afirmación de hecho sin suficiente fundamento procesal
  - Frase: “realizó transferencias periódicas a [[Andres Chadwick Pinera]] por un total superior a `$190.000.000 CLP`”
  - Sugerencia: revisar el uso de términos como 'superior a $190.000.000 CLP' y considerar el uso de términos más cautelosos como 'se acredita que el monto total de transferencias podría superar los $190.000.000 CLP'
- **medio** — afirma como hecho probado un pago realizado por Factop SpA sin mencionar que se trata de una acreditación obtenida a través de peritajes contables, lo que podría interpretarse como una afirmación de hecho sin suficiente fundamento procesal
  - Frase: “los honorarios del jurista alemán Kai Ambos por el informe en derecho presentado ante el Senado fueron costeados directamente con fondos de [[Factop SpA]]”
  - Sugerencia: revisar el uso de términos como 'fueron costeados directamente' y considerar el uso de términos más cautelosos como 'se acredita que los honorarios fueron cubiertos parcialmente por fondos de Factop SpA'

## [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]
- **alto** — uso de lenguaje peyorativo ('cartel') sin condena judicial firme
  - Frase: “cartel farmacéutico”
  - Sugerencia: reemplazar por términos neutrales como 'grupo de empresas' o 'organización'

## [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]
- **alto** — Afirman como hecho probado un delito ('defraudación patrimonial consolidada', 'ejecutada mediante...') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “Defraudación patrimonial consolidada en la [[Municipalidad de Maipu]] bajo la administración de [[Cathy Barriga Guerra]] por **$30.972.000.000 CLP**, ejecutada mediante la emisión de Certificados de Disponibilidad Presupuestaria (CDP) sin respaldo contable, ocultamiento de pasivos devengados y desvío de fondos de uso exclusivo (como recursos de la sanitaria municipal SMAPA), según consta en el [[Informe-Contraloria-Municipalidad-Maipu-2021]] y la formalización del [[Caso Municipalidad de Maipu]]”
  - Sugerencia: Evitar afirmar hechos como si fueran probados. Utilizar lenguaje que refleje la naturaleza acusatoria del proceso, como 'presunto' o 'acusado de'.

## [[TRX-2021-04-15-Subvencion-VitaDeportes-01]]
- **alto** — Afirma como hecho probado un delito (desvío de fondos) sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “desviadas por $759.000.000 CLP”
  - Sugerencia: Utilizar lenguaje que indique que se trata de una acusación o presunta acción, no de un hecho probado.

## [[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]
- **medio** — Usa el término 'acreditado' para afirmar un hecho como probado, sin que exista una sentencia o resolución judicial que lo respalde.
  - Frase: “Registro acreditado de la permanencia y participación del consultor político argentino [[Fernando Cerimedo]], titular de [[Numen Publicidad SpA]], en la sede central de [[Renovacion Nacional]] durante la jornada electoral y celebración de los resultados del Plebiscito Constitucional del 4 de septiembre de 2022.”
  - Sugerencia: Reemplazar 'acreditado' por un término más neutro, como 'documentado' o 'registrado', para evitar la impresión de que el hecho está probado judicialmente.

## [[TRX-2022-11-18-Convenio-ProCultura-Biobio]]
- **medio** — Usa el término 'fraude al fisco' como si fuera un delito probado, sin mencionar que la situación procesal no es condena ni que la causa no tiene sentencia.
  - Frase: “investigado en el [[Caso Convenios]] por [[Fraude al Fisco]]”
  - Sugerencia: Reemplazar 'por [[Fraude al Fisco]]' con 'por presunto fraude al fisco' o 'por investigación de fraude al fisco' para evitar afirmar como hecho probado un delito.

## [[TRX-2022-11-29-Convenio-DV-03]]
- **medio** — Atribuye un delito a una causa colectiva sin especificar la participación individual de la persona mencionada.
  - Frase: “imputado como [[Fraude al Fisco]] reiterado en [[Caso Convenios]]”
  - Sugerencia: Revisar si el fraude al fisco se refiere específicamente a la persona mencionada o si se refiere a la causa colectiva, evitando generalizaciones.

## [[TRX-2022-12-20-Convenio-EnTi-01]]
- **alto** — Afirma como hecho probado un delito ('acreditó el desvío de fondos') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “la investigación penal de la Fiscalía Regional del Biobío en el [[Caso Convenios]] acreditó el desvío de fondos hacia sociedades instrumentales, gastos personales improcedentes y rendiciones con facturas ideológicamente falsas”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria o resolución judicial que lo respalde.

## [[TRX-2023-06-22-Reunion-Audios-01]]
- **alto** — Afirma como hecho probado el pago de sobornos sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “destinado al pago de sobornos a funcionarios públicos del [[Servicio Impuestos Internos]] y la CMF en beneficio de [[Factop SpA]]”
  - Sugerencia: Revisar el lenguaje para evitar afirmaciones de hechos probados sin base judicial.

## [[TRX-2023-06-29-Auditoria-CGR-DemocraciaViva-01]]
- **alto** — Afirma como hecho probado un delito ('fraccionamiento doloso') sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “que acreditó el fraccionamiento doloso de los tres convenios transferidos”
  - Sugerencia: Reemplazar 'acreditó' por un término más neutro como 'se identificó' o 'se observó' para evitar la impresión de que el delito fue probado.

## [[TRX-2023-12-14-Emision-Facturas-Falsas-Fraude-SII-Operacion-Tributos-01]]
- **alto** — Afirma como hecho probado un delito (monto defraudado) cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “perjuicio fiscal récord consolidado de $240.000.000.000 CLP cuantificado por el SII”
  - Sugerencia: Evitar afirmar montos como hechos probados sin que exista una sentencia condenatoria.

## [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]
- **medio** — Usa lenguaje que sugiere hechos probados sin haberse establecido una condena o sentencia
  - Frase: “habría exigido la restitución en dinero en efectivo de parte significativa de sus salarios mensuales”
  - Sugerencia: Revisar el uso de términos como 'habría' para evitar la impresión de certeza sobre hechos que aún no han sido probados judicialmente

