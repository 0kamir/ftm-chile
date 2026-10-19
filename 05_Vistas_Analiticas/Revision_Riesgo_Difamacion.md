---
tipo_nodo: vista_analitica
tags:
  - vista/revision-legal
---

# Revisión Preliminar de Riesgo de Difamación

> Triaje automático con el modelo local `qwen3:14b` (Ollama). **No es un dictamen**: cada hallazgo debe contrastarse con las fuentes antes de editar la nota. Se descartaron 35 frases que el modelo no copió literalmente.

> **Revisión editorial (2026-10-19, segunda pasada):** de 189 hallazgos, 110 ya habían sido revisados en la primera pasada. De los 79 nuevos, la mayoría marca redacción ya atribuida a la Fiscalía ('habría', 'según') o condenas firmes, y se descartaron como falsos positivos. Se corrigieron 13 frases: Cerimedo (indiciado por la Policía Federal de Brasil, no acusado ante el STF), Bancard (la sanción de la SVS fue a Piñera), Fuente-Alba, KDM, Milicogate (rango de Santic y monto estimado), el vínculo Hermosilla–Chadwick, y las cifras sin fuente de CEMA y Lucía Hiriart. Este listado corresponde al estado previo a esas correcciones.

Notas revisadas: 223 · Notas con hallazgos: 116 · Riesgo alto: 75

## [[Agustin Edwards Eastman]]
- **medio** — Usa el término 'acreditó' para afirmar un hecho como probado, sin indicar que la situación procesal no es condenado o que la causa no tiene sentencia.
  - Frase: “Según acreditó oficialmente el Informe de la Comisión Church del Senado de EE.UU. (1975)”
  - Sugerencia: Reemplazar 'acreditó' por un término más neutral, como 'indicó' o 'documentó', para evitar la impresión de que el hecho está probado.

## [[Andres Chadwick Pinera]]
- **medio** — La frase afirma como hecho probado la inhabilitación, sin mencionar que se trata de una decisión del Senado, lo que podría interpretarse como una condena firme, aunque en el contexto de una Acusación Constitucional, no es equivalente a una condena penal.
  - Frase: “fue destituido e inhabilitado por 5 años por el [[Senado de la Republica de Chile]] al aprobarse la Acusación Constitucional en su contra.”
  - Sugerencia: Aclarar que la inhabilitación fue decidida por el Senado y no constituye una condena penal.

## [[Angela Vivanco Martinez]]
- **medio** — Afirman como hecho probado un delito ('tipificadas bajo hipótesis de...') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “En la arista judicial del [[Caso Audios]], el Ministerio Público investiga las comunicaciones y gestiones sostenidas con el abogado [[Luis Hermosilla Osorio]] ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]) relativas a nombramientos judiciales y consultas sobre causas radicadas en la Tercera Sala, tipificadas bajo hipótesis de [[Trafico de Influencias]], [[Negociacion Incompatible]] y [[Cohecho]]”
  - Sugerencia: Evitar afirmar como hechos probados delitos que aún no han sido resueltos judicialmente. Utilizar lenguaje más cauteloso, como 'se investiga' o 'se considera que podrían estar relacionados con'.

## [[Augusto Pinochet Ugarte]]
- **medio** — uso de lenguaje peyorativo ('secretas') que puede interpretarse como calificativo no judicial
  - Frase: “mantuvo más de 125 cuentas bancarias secretas”
  - Sugerencia: revisar el uso de términos como 'secretas' para evitar interpretaciones no judiciales

## [[Bruno Villalobos Krumm]]
- **medio** — Usa el término 'procesado' sin especificar si se trata de una acusación formal o si existe una condena, lo que puede generar una impresión de certeza sobre el delito cuando no está acreditado.
  - Frase: “procesado por la justicia militar y civil por la presunta malversación de más de `$600.000.000 CLP` en gastos reservados institucionales.”
  - Sugerencia: Reemplazar 'procesado' por 'acusado' o 'formalizado' para reflejar adecuadamente la situación procesal actual.

## [[Camila Flores Oporto]]
- **medio** — uso de lenguaje peyorativo o calificativo no judicial ('fraude al Fisco reiterado') sobre una persona investigada sin condena
  - Frase: “investigada penalmente por la Unidad Regional Anticorrupción (URAC) de la Fiscalía de Valparaíso y el OS9 de Carabineros por presunto fraude al Fisco reiterado”
  - Sugerencia: reemplazar 'fraude al Fisco reiterado' por 'presunto fraude al Fisco reiterado' para mantener el rigor legal y respetar la presunción de inocencia

## [[Camila Polizzi Fonceca]]
- **medio** — Usa el verbo 'habría' que sugiere una presunción sin haberse acreditado como hecho probado, lo que podría violar el principio de presunción de inocencia.
  - Frase: “habría gestionado la adjudicación del convenio [[TRX-2022-12-20-Convenio-EnTi-01]] con el [[GORE Biobio]] (encabezado por [[Rodrigo Diaz Worner]]) utilizando la personalidad jurídica de [[Fundacion En Ti]] por **$250.635.000 CLP** según consta en la [[Resolucion-GORE-Biobio-EnTi-2022]]”
  - Sugerencia: Revisar el uso de 'habría' y reemplazarlo por un lenguaje más neutral y compatible con la situación procesal de formalizado.

## [[Cathy Barriga Guerra]]
- **alto** — Afirma como hecho probado delitos ('fraude al fisco', 'falsificación de instrumento público') cuando la situación procesal es 'formalizado' y no hay condena.
  - Frase: “Fue formalizada por la Fiscalía Metropolitana Oriente en el [[Caso Municipalidad de Maipu]] por delitos reiterados de [[Fraude al Fisco]] y falsificación de instrumento público por un perjuicio patrimonial de **$30.972.000.000 CLP** ([[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]), según el [[Informe-Contraloria-Municipalidad-Maipu-2021]]”
  - Sugerencia: Reemplazar afirmaciones de hechos probados por términos como 'acusada de', 'imputada por' o 'formalizada por'.

## [[Daniel Andrade Schwarze]]
- **alto** — Afirma como hecho probado un delito ('fraude al fisco reiterado') cuando la situación procesal es 'formalizado' y no hay condena.
  - Frase: “Se encuentra formalizado en la causa [[Caso Convenios]] por fraude al fisco reiterado.”
  - Sugerencia: Reemplazar 'por fraude al fisco reiterado' por 'por fraude al fisco reiterado, según la acusación' o similar, para evitar afirmar como hecho probado un delito sin condena.

## [[Eduardo Guendelman Israel]]
- **medio** — Usa el término 'acreditó' para afirmar un hecho sin que exista una condena o sentencia judicial que respalde dicha afirmación.
  - Frase: “una investigación de la Unidad de Investigación de *BioBioChile* sobre los correos desclasificados por el Departamento de Justicia de EE. UU. ([[Publicacion-Archivos-DOJ-CasoEpstein-2026]]) acreditó que el profesor Guendelman mantuvo un intercambio de correos electrónicos con Jeffrey Epstein entre 2015 y 2019.”
  - Sugerencia: Reemplazar 'acreditó' por un término más neutro, como 'indicó' o 'sugirió', para evitar la impresión de que el hecho está probado judicialmente.

## [[Eliodoro Matte Larrain]]
- **alto** — uso de lenguaje peyorativo ('cartel') que sugiere una organización criminal sin que exista una condena judicial firme
  - Frase: “cartel del papel tissue”
  - Sugerencia: reemplazar por términos neutrales como 'acuerdo colusorio' o 'prácticas colusorias'

## [[Felipe Sanchez Perez]]
- **medio** — Atribuye hechos a una persona sin condena firme, usando datos de operaciones bloqueadas por la Contraloría, lo que puede interpretarse como una acusación sin fundamento legal.
  - Frase: “pactó la venta por trato directo del inmueble de calle Sierra Bella a la [[Municipalidad de Santiago]] ([[Iraci Hassler Jacob]]) por **$8.200.000.000 CLP** pocos meses después de haberlo adquirido por cerca de `$2.080.000.000 CLP` ([[TRX-2023-01-20-Compraventa-Clinica-SierraBella-01]]), operación bloqueada por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) en el [[Dictamen-CGR-SierraBella-2023]]”
  - Sugerencia: Revisar si la información se basa en hechos probados o en investigaciones en curso, y evitar afirmaciones que puedan interpretarse como calumnias o injurias.

## [[Fernando Leon Steffens]]
- **medio** — Usa el término 'imputó' que sugiere una acusación formal, pero no acredita un delito probado, lo que podría generar confusión sobre la situación procesal real.
  - Frase: “la Fiscalía Regional Metropolitana Occidente le imputó haber autorizado (imputación que terminó en una salida alternativa, sin condena)”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados, y reemplazarlos por lenguaje más preciso y neutral.

## [[Flavio Echeverria Cortez]]
- **alto** — Afirma como hecho probado un delito ('habría sustraído') cuando la situación procesal no es condenado y la causa no tiene sentencia firme.
  - Frase: “habría sustraído $28.348.928.198 CLP mediante depósitos ficticios de remuneraciones”
  - Sugerencia: Evitar afirmaciones de hechos como probados sin evidencia judicial. Usar términos como 'acusado de haber sustraído' en lugar de 'habría sustraído'.
- **medio** — Usa el término 'señalado' que indica una acusación, lo cual es correcto dado que la situación procesal es 'acusado', pero podría interpretarse como una afirmación de hecho sin suficiente evidencia.
  - Frase: “señalado por la Fiscalía como líder del esquema del [[Caso Pacogate]]”
  - Sugerencia: Considerar reemplazar 'señalado' por 'acusado' para mayor precisión legal.

## [[Gonzalo Blu Rodriguez]]
- **medio** — la frase sugiere una formalización sin mencionar si fue absuelto o condenado, lo que podría generar confusión con la situación procesal actual
  - Frase: “fue dado de baja y formalizado por el Ministerio Público”
  - Sugerencia: especificar que fue formalizado y posteriormente condenado, según la sentencia no firme mencionada en los metadatos

## [[Gonzalo Delaveau Swett]]
- **alto** — Afirma hechos como si fueran probados sin mencionar que no hay una condena o sentencia judicial que respalde dicha afirmación
  - Frase: “figuraba personalmente como director, apoderado y secretario de al menos cinco sociedades offshore domiciliadas en Bahamas”
  - Sugerencia: Añadir un calificador como 'según los documentos revelados por Mossack Fonseca' para evitar afirmaciones directas de hechos sin evidencia judicial
- **medio** — Usa lenguaje que puede interpretarse como peyorativo al mencionar su rol en Chile Transparente, una organización anticorrupción, sin contextualizar adecuadamente el conflicto de interés
  - Frase: “Abogado especialista en derecho corporativo y minero que ejercía como Presidente de Chile Transparente”
  - Sugerencia: Revisar el lenguaje para evitar interpretaciones que puedan ser consideradas calumniosas o injustas

## [[Guillermo Harding Alvarado]]
- **medio** — Atribuye logros empresariales a la persona sin evidencia directa de su liderazgo en el hecho mencionado.
  - Frase: “Bajo su liderazgo, la compañía se transformó en la mayor cadena farmacéutica de Chile.”
  - Sugerencia: Revisar si hay evidencia concreta que vincule directamente a Guillermo Harding Alvarado con la transformación de la compañía en la mayor cadena farmacéutica de Chile.

## [[Hartmut Hopp Miottel]]
- **medio** — La frase sugiere que la sentencia no estaba ejecutoriada en el momento de la fuga, lo cual podría contradecir la situación procesal declarada en METADATOS que indica que fue condenado.
  - Frase: “fugándose del país hacia Krefeld (Alemania) en mayo de 2011 antes de que la sentencia quedara ejecutoriada.”
  - Sugerencia: Verificar si la sentencia ya estaba ejecutoriada en mayo de 2011 y ajustar la frase en consecuencia.

## [[Iraci Hassler Jacob]]
- **medio** — Usa lenguaje que sugiere responsabilidad directa de la Contraloría General de la República y de Jorge Bermudez Soto sin acreditar que sean responsables del paralelismo de pagos, lo que podría interpretarse como una imputación injustificada
  - Frase: “operación cuyos pagos fueron paralizados por la [[Contraloria General de la Republica]] ([[Jorge Bermudez Soto]]) mediante el [[Dictamen-CGR-SierraBella-2023]] al constatarse que el precio cuadruplicaba el avalúo fiscal y el valor de compra previa sin justificación técnica verificable”
  - Sugerencia: Revisar y reemplazar frases que sugieran responsabilidad directa de terceros sin evidencia suficiente

## [[Jaime Paz Meneses]]
- **alto** — Afirma como hecho probado un delito ('habría sustraído') cuando la situación procesal no es condenado y la causa no tiene sentencia firme.
  - Frase: “señalado como figura clave del esquema del [[Caso Pacogate]], que según la acusación habría sustraído $28.348.928.198 CLP mediante depósitos ficticios de remuneraciones”
  - Sugerencia: Reemplazar 'habría sustraído' por 'se le imputa la sustracción de' para evitar afirmar hechos como probados.
- **medio** — Menciona un veredicto condenatorio sin aclarar que no está firme, lo que puede generar confusión sobre la situación procesal real.
  - Frase: “veredicto condenatorio contra 25 de los 28 acusados que llegaron a juicio por malversación de caudales públicos reiterada y lavado de activos”
  - Sugerencia: Añadir una aclaración como 'veredicto condenatorio que no está firme' para reflejar correctamente la situación procesal.

## [[Javier Cruz Tamburrino]]
- **medio** — afirma un delito como hecho probado sin indicar que la situación procesal es condenado o la causa tiene sentencia
  - Frase: “Lavado de Activos”
  - Sugerencia: utilizar términos como 'presunto lavado de activos' o 'acusado de lavado de activos'
- **medio** — afirma como hecho probado un delito asociado a un caso sin indicar que la situación procesal es condenado o la causa tiene sentencia
  - Frase: “Caso Milicogate”
  - Sugerencia: utilizar términos como 'presunto caso Milicogate' o 'acusación relacionada con el caso Milicogate'
- **medio** — afirma como hecho probado un delito asociado a un caso sin indicar que la situación procesal es condenado o la causa tiene sentencia
  - Frase: “Caso Pacogate”
  - Sugerencia: utilizar términos como 'presunto caso Pacogate' o 'acusación relacionada con el caso Pacogate'

## [[Jose Antonio Pavez Canessa]]
- **alto** — uso de lenguaje peyorativo ('clan') que no es judicial y sugiere una organización criminal sin condena
  - Frase: “líder del denominado 'Clan Canessa'”
  - Sugerencia: reemplazar por 'uno de los imputados' o 'persona formalizada'
- **alto** — uso de lenguaje peyorativo ('clan') y 'sindica' sugiere una acusación sin condena
  - Frase: “la Fiscalía lo sindica como líder del denominado 'Clan Canessa'”
  - Sugerencia: reemplazar por 'la Fiscalía lo imputa como uno de los líderes de...'
- **medio** — uso de 'habría' indica una acusación sin prueba probada, lo que contradice la presunción de inocencia
  - Frase: “habría creado 16 sociedades de papel que vendían facturas falsas a cambio de comisión”
  - Sugerencia: reemplazar por 'se le atribuye la creación de...' o 'se le imputa la creación de...'

## [[Jose Codner Chijner]]
- **alto** — uso de lenguaje peyorativo ('cartel') que no es judicial y sugiere culpabilidad sin condena
  - Frase: “cartel de alza de precios de 222 medicamentos”
  - Sugerencia: reemplazar por términos neutrales como 'acuerdo de alza de precios' o 'concertación de precios'

## [[Juan Miguel Fuente-Alba Poblete]]
- **alto** — Afirma como hecho probado un delito ('desfalco') cuando la situación procesal no es condenado
  - Frase: “Durante su período de mando operó asimismo el desfalco de la Ley Reservada del Cobre”
  - Sugerencia: Reemplazar 'operó asimismo el desfalco' por 'se le imputa el desfalco' o 'se le acusa de desfalco' para evitar afirmar como hecho probado un delito
- **medio** — Usa lenguaje que sugiere una responsabilidad directa de la Ministra en Visita sin acreditar que haya actuado en ese rol de forma directa o decisiva
  - Frase: “Fue sometido a proceso por la Ministra en Visita Romy Rutherford”
  - Sugerencia: Revisar el rol exacto de la Ministra en Visita Romy Rutherford en el proceso y rephraser la frase para evitar sugerir responsabilidad directa no acreditada

## [[Juan Miguel Ovalle Garces]]
- **medio** — Usa el término 'sancionado' que sugiere una decisión judicial o administrativa definitiva, sin aclarar si se trata de una sanción provisional o pendiente de resolución
  - Frase: “coordinador del acuerdo colusorio sancionado por el TDLC”
  - Sugerencia: Revisar el uso del término 'sancionado' y aclarar si se refiere a una decisión definitiva o provisional
- **medio** — La frase sugiere un hecho concluido y definitivo, sin especificar si la disolución forzosa fue confirmada judicialmente o si aún está pendiente de resolución
  - Frase: “culminó en la disolución judicial forzosa del gremio”
  - Sugerencia: Aclarar si la disolución forzosa fue confirmada judicialmente o si aún está en proceso

## [[Juan Victor Galaz Rojas]]
- **alto** — uso de lenguaje peyorativo o calificativo no judicial ('clan') sobre una persona sin condena
  - Frase: “líder del denominado 'Clan Galaz'”
  - Sugerencia: evitar el uso de términos como 'clan' que pueden ser interpretados como calificativos no judiciales
- **medio** — uso de 'habría' que sugiere una afirmación de hecho sin estar probado
  - Frase: “habría declarado exportaciones falsas de teléfonos”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria y no probada de los hechos
- **medio** — exposición de montos sin estar relacionados con una condena firme
  - Frase: “perjuicio fiscal estimado de $11.594.172.879”
  - Sugerencia: evitar mencionar montos sin contexto legal o judicial claro

## [[Leon Marcelo Lefort Hernandez]]
- **alto** — Afirma como hecho probado un delito ('soborno a funcionarios') sin que exista una sentencia condenatoria, lo que viola la presunción de inocencia.
  - Frase: “Imputado en el [[Caso Luminarias LED]] por soborno a funcionarios de al menos 24 instituciones públicas, según la Fiscalía”
  - Sugerencia: Reemplazar 'por soborno' con 'acusado de soborno' o 'presunto soborno' para reflejar la situación procesal actual.
- **alto** — Afirma como hecho probado ('entregar presuntamente') un delito sin que exista una sentencia condenatoria, lo que viola la presunción de inocencia.
  - Frase: “fue detenido el 05-05-2020 tras entregar presuntamente $37 millones en efectivo”
  - Sugerencia: Reemplazar 'entregar presuntamente' con 'acusado de entregar' o 'presunto entregar' para reflejar la situación procesal actual.
- **alto** — Usa lenguaje que sugiere un hecho probado ('habría anticipado') sin que exista una sentencia condenatoria, lo que viola la presunción de inocencia.
  - Frase: “habría anticipado las bases técnicas de la licitación a [[Itelecom Holding Chile SpA]]”
  - Sugerencia: Reemplazar 'habría anticipado' con 'acusado de anticipar' o 'presunto anticipar' para reflejar la situación procesal actual.
- **medio** — Menciona una función profesional sin indicar si está relacionada con el hecho investigado, lo que podría generar confusión sobre su relevancia en el caso.
  - Frase: “Ingeniero y controlador de [[Itelecom Holding Chile SpA]]”
  - Sugerencia: Aclarar si el rol de ingeniero y controlador está vinculado directamente con los hechos investigados.

## [[Leonarda Villalobos Muth]]
- **alto** — Afirma como hecho probado un pago de $100.000.000 CLP, cuando no hay sentencia ni condena que acredite dicha afirmación.
  - Frase: “se mencionaron pagos por **$100.000.000 CLP** ([[TRX-2023-06-22-Reunion-Audios-01]]) desde el entorno de [[Factop SpA]] hacia funcionarios del [[Servicio Impuestos Internos]]”
  - Sugerencia: Reemplazar 'se mencionaron pagos' por 'se mencionó la posibilidad de pagos' o similar, para evitar la impresión de que el pago fue acreditado como hecho probado.
- **medio** — Usa el término 'formalizada' que puede interpretarse como una condena, cuando en realidad la situación procesal es 'formalizado', lo que indica que aún no hay sentencia.
  - Frase: “Abogada formalizada en el [[Caso Audios]] por [[Cohecho]], [[Lavado de Activos]] y delitos tributarios.”
  - Sugerencia: Reemplazar 'formalizada' por 'formalizado' para alinear con la situación procesal declarada en los metadatos.

## [[Leonardo Osses Sandoval]]
- **alto** — Afirma como hecho probado un delito ('acreditó') cuando la situación procesal NO es condenado firme, ya que la sentencia no es firme y hay recursos de nulidad pendientes.
  - Frase: “el tribunal acreditó que Osses remitió por correo electrónico borradores de los textos que luego aparecieron falsamente atribuidos a los comuneros mapuche”
  - Sugerencia: Evitar el uso de términos que sugieran certeza en la comisión del delito, ya que la sentencia no es firme.

## [[Loreto Letelier]]
- **alto** — Atribuye a las víctimas del Caso Quemados un hecho que contradice sentencias judiciales ejecutoriadas que acreditan la responsabilidad de patrullas militares.
  - Frase: “se habían quemado a sí mismas con bombas molotov”
  - Sugerencia: Revisar la afirmación para evitar contradicción con sentencias judiciales ejecutoriadas.

## [[Lucia Hiriart Rodriguez]]
- **medio** — afirma como hecho probado la disolución de la entidad y el traspaso de sus bienes al Fisco, sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “encabezó la venta a privados de decenas de terrenos e inmuebles donados gratuitamente por el Fisco, SERVIU y municipalidades, desviando recursos y manteniendo más de un centenar de propiedades públicas bajo control privado hasta que la acción del Consejo de Defensa del Estado y de los tribunales obligó a la disolución de la entidad y a el traspaso de sus bienes al Fisco y a fundaciones de beneficencia”
  - Sugerencia: revisar la formulación para evitar afirmar hechos como si fueran probados, usando términos como 'se ha determinado' o 'según la Fiscalía'

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

## [[Olga Paz Barraza Quezada]]
- **alto** — uso de lenguaje peyorativo o calificativo no judicial ('clan') sobre una persona formalizada pero no condenada
  - Frase: “líder del denominado 'Clan Barraza'”
  - Sugerencia: evitar el uso de términos como 'clan' que pueden ser interpretados como calificativos no judiciales y que no tienen base en la situación procesal
- **medio** — afirma como hecho probado un delito ('obtenido devoluciones') cuando la situación procesal no es condenado y la causa no tiene sentencia
  - Frase: “habría obtenido devoluciones del impuesto específico al diésel por $2.489 millones”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria de la información, como 'se le imputa' o 'se le atribuye', en lugar de afirmar hechos como si estuvieran probados

## [[Oscar Aitken Lavanchy]]
- **medio** — Usa lenguaje que sugiere hechos probados sin mencionar que la situación procesal es formalizado, no condenado. Además, menciona documentos de investigación judicial sin aclarar si son evidencia probada.
  - Frase: “habría actuado como operador jurídico y fiduciario en la constitución y administración de sociedades de papel *offshore* en Islas Vírgenes Británicas, Bahamas y Panamá (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*), agrupadas bajo [[Riggs Bank y Sociedades Offshore Ashburton]], utilizadas para triangular caudales públicos provenientes de gastos reservados ([[TRX-2004-07-14-Gastos-Reservados-Riggs-01]]) y ocultar rentas ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]])”
  - Sugerencia: Revisar el uso de términos como 'habría actuado' y 'utilizadas para' para evitar sugerir certeza sobre hechos que no están probados. Se recomienda usar lenguaje más cauteloso como 'se le atribuye' o 'se le imputa'.

## [[Osvaldo Mario Luis Sacco Croxatto]]
- **alto** — uso de lenguaje peyorativo o calificativo no judicial ('clan') sobre una persona sin condena
  - Frase: “líder del denominado 'Clan Croxatto'”
  - Sugerencia: evitar el uso de términos como 'clan' que pueden ser interpretados como calificativos no judiciales
- **medio** — afirma como hecho probado un delito ('generado pérdidas fiscales por... facturas falsas') cuando la situación procesal no es condenado
  - Frase: “habría generado pérdidas fiscales por $422.727.859 mediante seis empresas proveedoras de facturas falsas”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria de la situación, como 'se le imputa' o 'se le atribuye'

## [[Pablo Wagner San Martin]]
- **medio** — afirma como hecho probado la recepción de pagos sin mencionar que la situación procesal no es condena total, sino condena parcial y absolución en otros delitos
  - Frase: “recibió pagos bimensuales de `$3.000.000 CLP` (`$42.000.000 CLP` en total) de [[Empresas Penta SA]] mientras ejercía funciones públicas, documentados con boletas de terceros”
  - Sugerencia: precisar que los pagos son acreditados como hechos, pero no se ha probado que fueran a cambio de favores según la Fiscalía
- **medio** — menciona una afirmación de la Fiscalía que no se encuentra en los datos procesales proporcionados
  - Frase: “la propia Fiscalía reconoció no haber acreditado que los pagos fueran a cambio de favores”
  - Sugerencia: verificar si la Fiscalía efectivamente reconoció dicha situación y, en caso afirmativo, citar la fuente específica

## [[Patricio Marin Lazo]]
- **alto** — La sentencia no es firme, ya que existen recursos de nulidad pendientes (2026), por lo que no puede afirmarse que esté condenado definitivamente.
  - Frase: “sentenciado a 5 años de presidio menor en su grado máximo por [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]]”
  - Sugerencia: Se debe indicar que la sentencia no es firme y que existen recursos pendientes.

## [[Percy Marin Vera]]
- **medio** — Usa el término 'objetó' que sugiere una afirmación de hecho, sin aclarar que se trata de una objeción de la Contraloría y no de una condena o resolución judicial definitiva
  - Frase: “una auditoría de la Contraloría al Consejo Regional de Valparaíso objetó el cobro de más de $9 millones en viáticos y combustible por no acreditar su residencia”
  - Sugerencia: Revisar el uso de 'objetó' para evitar dar la impresión de que el hecho está probado, y aclarar que se trata de una objeción de la Contraloría
- **medio** — Menciona una acción del Tribunal Regional de RN sin aclarar si se trata de una decisión política o disciplinaria, lo que podría interpretarse como una condena o resolución judicial
  - Frase: “En junio de 2020 el Tribunal Regional de RN lo suspendió del partido”
  - Sugerencia: Aclarar que la suspensión fue una decisión política o disciplinaria del Tribunal Regional de RN, no una resolución judicial

## [[Raul Torrealba del Pedregal]]
- **medio** — Usa términos que sugieren hechos probados (delitos) sin haberse dictado sentencia, lo que contradice la situación procesal de 'formalizado'.
  - Frase: “Fue formalizado en el [[Caso Vitacura]] por 29 delitos de [[Fraude al Fisco]] / [[Malversacion de Caudales Publicos]], asociación ilícita, delitos tributarios y [[Lavado de Activos]]”
  - Sugerencia: Reemplazar términos como 'por 29 delitos' con 'acusado de 29 delitos' para reflejar correctamente su situación procesal.

## [[Roberto Belloni Pechini]]
- **alto** — uso de lenguaje peyorativo o calificativo no judicial ('cartel') sobre una persona sin condena
  - Frase: “cartel”
  - Sugerencia: evitar el uso de términos como 'cartel' que no son judiciales y pueden ser considerados difamatorios

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

## [[Agricola Don Pollo Limitada]]
- **alto** — afirma como hecho probado un delito sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “fue condenada por formar parte del cartel oligopólico”
  - Sugerencia: revisar si la condena es firme y si se debe usar lenguaje que refleje la situación procesal actual
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales sobre una entidad sin condena
  - Frase: “cartel oligopólico”
  - Sugerencia: evitar el uso de términos peyorativos que no estén respaldados por una condena judicial

## [[Andes Iron SpA]]
- **alto** — Afirma como hecho probado que Carlos Alberto Delano Abbott fue condenado, sin mencionar si la condena es firme o si se encuentra en apelación.
  - Frase: “controlada por la familia de [[Carlos Alberto Delano Abbott]] (condenado en el [[Caso Penta]]).”
  - Sugerencia: Revisar si la condena mencionada es definitiva y, en caso contrario, reemplazar 'condenado' por 'acusado' o 'presunto'.

## [[Bancard Inversiones Ltda]]
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al referirse al grupo de Sebastian Pinera Echenique como 'grupo' sin condena
  - Frase: “Matriz de inversiones y *family office* del grupo de [[Sebastian Pinera Echenique]] y su familia”
  - Sugerencia: Evitar calificativos no judiciales o que puedan interpretarse como acusaciones sin fundamento legal
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al referirse a filiales como 'brazo offshore' sin condena
  - Frase: “integrada por sus filiales chilenas *Inversiones Santa Cecilia S.A.*, *Inversiones Mediterráneo* y su brazo *offshore* en las Islas Vírgenes Británicas *Bancard International Investment Inc.*”
  - Sugerencia: Evitar calificativos no judiciales o que puedan interpretarse como acusaciones sin fundamento legal
- **medio** — Afirma como hecho probado un delito o situación procesal sin condena o sentencia
  - Frase: “condicionando la última cuota a que el gobierno de Piñera no declarara zona de exclusión ambiental en La Higuera”
  - Sugerencia: Utilizar lenguaje que refleje la naturaleza presunta de las acusaciones
- **medio** — Afirma como hecho probado un delito o situación procesal sin condena o sentencia
  - Frase: “sancionada por la [[Comision para el Mercado Financiero]]”
  - Sugerencia: Utilizar lenguaje que refleje la naturaleza presunta de las acusaciones
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al referirse a empresas como 'empresas zombis'
  - Frase: “adquirir "empresas zombis" con pérdidas arrastradas fiscalizadas por el [[Servicio Impuestos Internos]]”
  - Sugerencia: Evitar calificativos no judiciales o que puedan interpretarse como acusaciones sin fundamento legal
- **medio** — Afirma como hecho probado un delito o situación procesal sin condena o sentencia
  - Frase: “mientras Chile litigaba con Perú ante la Corte Internacional de Justicia de La Haya”
  - Sugerencia: Utilizar lenguaje que refleje la naturaleza presunta de las acusaciones
- **medio** — Afirma como hecho probado un delito o situación procesal sin condena o sentencia
  - Frase: “la Fiscalía presumió ideológicamente falsas”
  - Sugerencia: Utilizar lenguaje que refleje la naturaleza presunta de las acusaciones
- **medio** — Afirma como hecho probado un delito o situación procesal sin condena o sentencia
  - Frase: “la investigación terminó con el sobreseimiento por prescripción de [[Santiago Valdes Gutierrez]] en 2019”
  - Sugerencia: Utilizar lenguaje que refleje la naturaleza presunta de las acusaciones

## [[Corpesca SA]]
- **alto** — Afirma como hecho probado un delito ('condenada penalmente') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “Empresa pesquera industrial condenada penalmente como persona jurídica (bajo la Ley N° 20.393)”
  - Sugerencia: Revisar si la condena es firme y si se menciona correctamente en los METADATOS. Si no es condena firme, reemplazar 'condenada' por 'acusada' o 'formalizada' según corresponda.

## [[Empresas CMPC SA]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre una entidad sin condena firme
  - Frase: “cartel que operó entre 2000 y 2015 para fijar precios de venta y repartirse cuotas en el mercado del papel higiénico, servilletas y toallas de papel”
  - Sugerencia: reemplazar 'cartel' por términos neutrales como 'acuerdo' o 'colusión'
- **medio** — afirma como hecho probado una sanción sin mencionar si fue condena firme o si la causa está formalizada
  - Frase: “sancionada por la [[Corte Suprema de Chile]] con una multa de 20.000 UTA al determinarse que había coaccionado a su competidora para sostener el acuerdo”
  - Sugerencia: precisar si la sanción fue confirmada en una sentencia firme o si se encuentra en trámite

## [[Empresas Penta SA]]
- **medio** — Usa lenguaje que sugiere una imputación retirada, lo cual puede interpretarse como una negación de hechos sin estar respaldado por una condena o sentencia
  - Frase: “sin condena por cohecho: la imputación de soborno fue retirada en 2018”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como afirmaciones de hechos sin estar respaldados por una sentencia judicial

## [[Exportadora y de Gestion Caval Ltda]]
- **medio** — Afirma como hecho probado un delito ('soborno', 'delitos tributarios') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “operación por la que fue acusada de soborno al Director de Obras de la [[Municipalidad de Machali]] [[Jorge Silva Menares]] ([[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]]) y de delitos tributarios ([[TRX-2015-01-29-Facturas-Caval-SII-01]]).”
  - Sugerencia: Reemplazar 'acusada de soborno' y 'acusada de delitos tributarios' por 'acusada de haber cometido soborno' y 'acusada de haber cometido delitos tributarios' para evitar la impresión de que los delitos han sido probados.

## [[Factop SpA]]
- **alto** — Usa lenguaje peyorativo o calificativos no judiciales sobre una entidad sin condena
  - Frase: “emisión de facturas ideológicamente falsas”
  - Sugerencia: Evitar calificar hechos como 'ideológicamente falsas' sin una base judicial
- **alto** — Usa lenguaje peyorativo o calificativos no judiciales sobre una entidad sin condena
  - Frase: “Lavado de Activos”
  - Sugerencia: Evitar mencionar delitos específicos como 'Lavado de Activos' sin una condena o sentencia
- **medio** — Usa lenguaje que sugiere hechos probados sin que exista una condena o sentencia firme
  - Frase: “habrían estructurado, según la Fiscalía, un fondo para sobornos”
  - Sugerencia: Revisar el uso de términos que implican responsabilidad legal sin que exista una resolución judicial

## [[Fundacion CEMA Chile]]
- **alto** — afirma como hecho probado la recepción de inmuebles sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “la entidad recibió gratuitamente más de 135 inmuebles fiscales, municipales y del SERVIU”
  - Sugerencia: revisar si la recepción de los inmuebles fue acreditada judicialmente y usar lenguaje más cauteloso
- **alto** — afirma como hecho probado la enajenación de propiedades sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “procediendo entre 1990 y 2016 a enajenar comercialmente decenas de propiedades por más de `$8.900.000.000 CLP`”
  - Sugerencia: revisar si la enajenación fue acreditada judicialmente y usar lenguaje más cauteloso
- **alto** — afirma como hecho probado la distracción de fondos sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “distraer fondos de su giro social”
  - Sugerencia: revisar si la distracción de fondos fue acreditada judicialmente y usar lenguaje más cauteloso
- **alto** — afirma como hecho probado la disolución y restitución de bienes sin mencionar que la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “la fundación fue disuelta y obligada a restituir al Estado 108 bienes raíces y la totalidad de sus fondos líquidos”
  - Sugerencia: revisar si la disolución y restitución fueron acreditadas judicialmente y usar lenguaje más cauteloso

## [[KDM Empresas SA]]
- **alto** — afirma como hecho probado la existencia de sobornos sin mencionar si hay condena o absolución
  - Frase: “canalizaron sobornos para asegurar la adjudicación del contrato”
  - Sugerencia: utilizar lenguaje que refleje la naturaleza acusatoria de la información, como 'se acusó que'
- **medio** — uso de término 'imputó' que sugiere una acusación formal, pero no se menciona si hay condena o absolución
  - Frase: “la Fiscalía Regional Metropolitana Occidente imputó que a través de su ejecutivo”
  - Sugerencia: revisar si se ha dictado sentencia o si la acusación sigue vigente

## [[Riggs Bank y Sociedades Offshore Ashburton]]
- **alto** — Afirma como hecho probado un delito ('acreditaron') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el Subcomité de Investigaciones del Senado de EE.UU. y el Ministro en Visita [[Sergio Munoz Gajardo]] acreditaron que esta estructura albergó más de 125 cuentas secretas”
  - Sugerencia: Evitar el uso de términos que sugieran certeza sobre hechos que no han sido probados judicialmente.

## [[SQM SA]]
- **medio** — Atribuye hechos probados a la empresa sin mencionar que la situación procesal no es condena firme.
  - Frase: “La empresa reconoció ante la SEC y el DOJ de EE.UU. pagos indebidos por unos US$ 14,75 millones.”
  - Sugerencia: Revisar si la frase refleja una condena o acuerdo judicial, y en caso contrario, reemplazar por un lenguaje más preciso como 'reconoció haber realizado pagos indebidos según declaraciones ante la SEC y el DOJ'.

## [[Sociedad Benefactora y Educacional Dignidad]]
- **alto** — Afirman como hecho probado delitos sin que la situación procesal indique condena o sentencia
  - Frase: “perpetraron crímenes de lesa humanidad, trabajo esclavo de colonos no remunerados, abuso sexual sistemático de menores y acopio de armamento de guerra”
  - Sugerencia: Revisar y reemplazar por términos que reflejen la naturaleza de las investigaciones o acusaciones, sin asumir la culpabilidad

## [[Sociedad de Inversiones Pampa Calichera SA]]
- **alto** — Afirma como hecho probado un delito ('acreditó', 'irrogando un perjuicio multimillonario') cuando la situación procesal NO es condenado o la causa no tiene sentencia.
  - Frase: “la [[Comision para el Mercado Financiero]] (entonces SVS) acreditó que [[Sociedad de Inversiones Pampa Calichera SA]] vendió paquetes accionarios a precios subvalorados a sociedades relacionadas con su propio controlador para luego recomprarlos a sobreprecio, irrogando un perjuicio multimillonario a los accionistas minoritarios y AFPs”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria o resolución judicial que lo respalde.

## [[Valmoval Ltda]]
- **alto** — La frase afirma hechos como si fueran probados sin mencionar que se trata de una investigación o acusación, lo que puede implicar difamación si no hay sentencia condenatoria.
  - Frase: “girándose tres cheques por cerca de US$ 3 millones ($2.950.000.000 CLP actualizados) directamente a nombre de su hijo”
  - Sugerencia: Reemplazar con términos como 'se habría girado' o 'según la investigación, se habrían girado' para evitar afirmar hechos como probados.
- **medio** — La frase sugiere una situación legal concluida sin indicar si la quiebra fue confirmada judicialmente, lo que podría generar confusión sobre el estado actual de la empresa.
  - Frase: “declarada en quiebra”
  - Sugerencia: Utilizar términos más neutrales como 'en proceso de quiebra' o 'sometida a quiebra' si no se ha confirmado judicialmente.

## [[Caso Asignaciones Parlamentarias y Cuota Flores]]
- **medio** — Usa el término 'presuntos delitos' lo cual es correcto, pero la frase menciona delitos de forma general sin especificar si están acreditados o no, lo que puede generar ambigüedad.
  - Frase: “presuntos delitos reiterados de fraude al Fisco, desvío de caudales públicos y vulneración de normas laborales y de probidad en el Congreso Nacional.”
  - Sugerencia: Aclarar que se trata de delitos presuntos y no acreditados, y evitar generalizaciones sin evidencia.

## [[Caso Basura]]
- **alto** — uso de lenguaje peyorativo ('corrupción') sin condena judicial explícita
  - Frase: “red transversal de corrupción municipal”
  - Sugerencia: reemplazar por términos neutrales como 'situación de interés público' o 'hechos investigados'
- **medio** — exposición de datos económicos sin vincularlos directamente a una condena judicial
  - Frase: “multimillonarios contratos de recolección, transporte y disposición final de residuos domiciliarios”
  - Sugerencia: evitar mencionar montos o características específicas de contratos sin evidencia judicial
- **medio** — mencionar nombres de personas o empresas sin vincularlos a una condena judicial
  - Frase: “consorcio [[KDM Empresas SA]] (representado por [[Fernando Leon Steffens]]”
  - Sugerencia: utilizar términos como 'presunto' o 'acusado' si no hay condena judicial

## [[Caso CEMA Chile]]
- **medio** — Usa lenguaje peyorativo o calificativos no judiciales al describir a una persona sin condena
  - Frase: “entidad privada presidida a perpetuidad hasta agosto de 2016 por [[Lucia Hiriart Rodriguez]]”
  - Sugerencia: Evitar calificativos no judiciales como 'presidida a perpetuidad' que pueden interpretarse como valoraciones negativas sin base judicial
- **medio** — Exponen datos personales o de la vida íntima/familiar ajenos al hecho de interés público
  - Frase: “cónyuge de [[Augusto Pinochet Ugarte]]”
  - Sugerencia: Evitar mencionar relaciones personales a menos que sean relevantes para el hecho investigado
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “según la querella, más de $8.900.000.000 CLP”
  - Sugerencia: Utilizar términos como 'según la querella' para evitar dar la impresión de que los hechos son probados
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “según los querellantes, gastos y asignaciones vinculadas a [[Lucia Hiriart Rodriguez]]”
  - Sugerencia: Utilizar términos como 'según los querellantes' para evitar dar la impresión de que los hechos son probados
- **medio** — Afirman como hecho probado un delito cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “según Emol, el Estado recuperó más de $18.000 millones”
  - Sugerencia: Utilizar términos como 'según Emol' para evitar dar la impresión de que los hechos son probados

## [[Caso Colusion de las Farmacias]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre personas o entidades sin condena explícita en el texto, aunque la causa está cerrada con condena
  - Frase: “formación de un cartel de precios entre las tres principales cadenas farmacéuticas del país”
  - Sugerencia: reemplazar 'cartel' por términos neutrales como 'acuerdo' o 'colusión'

## [[Caso Colusion de los Pollos]]
- **alto** — uso de lenguaje peyorativo ('cartel delictivo') sobre una asociación gremial sin condena firme de su naturaleza delictiva, ya que la sentencia menciona su disolución forzada por haber sido instrumentalizada como cartel, pero no afirma explícitamente que sea un cartel delictivo en sí misma
  - Frase: “instrumentalizada como cartel delictivo”
  - Sugerencia: revisar el uso de términos calificativos y reemplazarlos por descripciones neutras basadas en la sentencia
- **medio** — uso de lenguaje peyorativo ('Cartel') para referirse a una investigación, lo cual puede interpretarse como una valoración no judicial
  - Frase: “Cartel de los Supermercados”
  - Sugerencia: evitar el uso de términos como 'cartel' para referirse a investigaciones o causas judiciales, a menos que estén respaldados por condenas firmes

## [[Caso Colusion del Papel Tissue]]
- **alto** — Usa el término 'condena histórica' sin especificar si se trata de una condena firme o si aún está en apelación, lo que puede generar ambigüedad sobre la situación procesal.
  - Frase: “condena histórica por colusión y formación de cartel empresarial”
  - Sugerencia: Precisar si la condena es firme o si se encuentra en fase de apelación, según lo indicado en los METADATOS.
- **alto** — El término 'cartel' es calificativo peyorativo y no judicial, utilizado sin una condena firme.
  - Frase: “formación de cartel empresarial”
  - Sugerencia: Evitar el uso de términos no judiciales como 'cartel' y reemplazarlos con descripciones neutras y basadas en hechos probados.

## [[Caso Convenios]]
- **medio** — exposición de montos sin acreditar su vinculación con delitos, lo que puede generar impresión de responsabilidad penal sin fundamento procesal
  - Frase: “el monto total transferido bajo el Programa de Asentamientos Precarios alcanzó los $426.000.000 CLP”
  - Sugerencia: revisar si el monto está relacionado con hechos investigados y evitar su mención sin contexto legal
- **medio** — menciona un delito sin indicar si ha sido acreditado o si existe sentencia condenatoria
  - Frase: “el Consejo de Defensa del Estado (CDE) presentó querella criminal por el delito de fraude al fisco reiterado”
  - Sugerencia: precisar que la querella es una acusación formal y no un hecho probado
- **medio** — menciona una investigación sin indicar si ha concluido o si hay condena
  - Frase: “investigación penal iniciada de oficio en junio de 2023 por la Fiscalía Regional de Antofagasta”
  - Sugerencia: especificar que la investigación está en trámite y no ha concluido con sentencia

## [[Caso Corpesca]]
- **alto** — Afirma como hecho probado que un parlamentario y una empresa fueron condenados, sin mencionar que la causa está cerrada y verificada, lo que podría implicar que la condena es firme, pero no se especifica si se refiere a la condena de los acusados mencionados en la nota.
  - Frase: “Primera causa en la historia judicial chilena en que un parlamentario en ejercicio y una gran empresa fueron condenados en juicio oral por delitos de corrupción asociados a la tramitación de una ley de la República ("Ley de Pesca")”
  - Sugerencia: Verificar si la condena mencionada corresponde a los individuos y empresas citados, y si es posible añadir más contexto sobre el estado de la causa judicial.
- **medio** — Aunque menciona una condena, no se especifica si la causa está cerrada y verificada, lo que podría generar ambigüedad sobre la firmeza de la condena.
  - Frase: “El 3° Tribunal de Juicio Oral en lo Penal de Santiago ([[Sentencia-3TOP-Santiago-Corpesca-2021]]) condenó al exsenador de [[Union Democrata Independiente]], [[Jaime Orpis Bouchon]], a 5 años y un día de presidio efectivo por [[Cohecho]] y [[Fraude al Fisco]] en el [[Senado de la Republica de Chile]], tras acreditarse que recibió **$233.000.000 CLP** ([[TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01]]) desde la pesquera [[Corpesca SA]], autorizados por su gerente general [[Francisco Mujica Ortuzar]], para representar los intereses de la compañía en las votaciones legislativas.”
  - Sugerencia: Añadir información sobre el estado final de la causa judicial y verificar si la condena mencionada es definitiva.

## [[Caso Exalmar y Fideicomiso Ciego]]
- **medio** — Usa el término 'según los querellantes', lo que indica una afirmación no probada, pero no se considera un riesgo alto ya que se menciona la fuente de la afirmación.
  - Frase: “empresa que, según los querellantes, se beneficiaría de los derechos de pesca en el triángulo marítimo adjudicado a Perú en el fallo de enero de 2014”
  - Sugerencia: Considerar reemplazar 'según los querellantes' por 'según se afirma' para mayor precisión y neutralidad.

## [[Caso Luminarias LED]]
- **medio** — Usa lenguaje que sugiere hechos probados sin que exista una sentencia condenatoria, lo que contradice la presunción de inocencia.
  - Frase: “habría pagado sobornos”
  - Sugerencia: Reemplazar por frases que reflejen la naturaleza acusatoria de la investigación, como 'se le imputa haber pagado sobornos'.
- **medio** — Usa lenguaje que sugiere hechos probados sin que exista una sentencia condenatoria, lo que contradice la presunción de inocencia.
  - Frase: “habría anticipado las bases técnicas”
  - Sugerencia: Reemplazar por frases que reflejen la naturaleza acusatoria de la investigación, como 'se le imputa haber anticipado las bases técnicas'.

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

## [[Caso Milicogate]]
- **alto** — Afirma como hecho probado un delito ('fueron condenados') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “oficiales como el coronel (r) [[Jozo Santic Palomino]] fueron condenados por pagar servicios inexistentes a proveedores coludidos como [[Frasim Ltda]]”
  - Sugerencia: Evitar afirmar condenas sin que estén declaradas en los METADATOS o en fuentes verificables.
- **alto** — Afirma como hecho probado un delito ('fueron condenados') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “en la arista de facturas falsas del [[Comando de Apoyo a la Fuerza del Ejercito]] (CAF), oficiales como el coronel (r) [[Jozo Santic Palomino]] fueron condenados por pagar servicios inexistentes a proveedores coludidos como [[Frasim Ltda]]”
  - Sugerencia: Evitar afirmar condenas sin que estén declaradas en los METADATOS o en fuentes verificables.

## [[Caso Minera Dominga Pandora Papers]]
- **alto** — afirma como hecho probado un delito ('condenado') cuando la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “condenado en el [[Caso Penta]] por delitos tributarios y enriquecimiento ilícito (absuelto de cohecho)”
  - Sugerencia: revisar la frase para evitar afirmar como hecho probado un delito sin evidencia de condena firme
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales ('íntimo amigo') sobre una persona sin condena
  - Frase: “socio fundador de [[Empresas Penta SA]] e íntimo amigo del entonces Presidente de la República [[Sebastian Pinera Echenique]]”
  - Sugerencia: reemplazar 'íntimo amigo' por un término neutral, como 'conocido' o 'relacionado'
- **medio** — puede interpretarse como una afirmación de hecho sin suficiente acreditación
  - Frase: “habilitándose el cobro de la cuota final”
  - Sugerencia: precisar que la acción fue autorizada o permitida, sin asumir responsabilidad directa

## [[Caso Municipalidad de Maipu]]
- **alto** — Afirma como hecho probado un delito (perjuicio fiscal) cuando la situación procesal es formalizada, no condenado.
  - Frase: “perjuicio fiscal imputado por el Ministerio Público y el Consejo de Defensa del Estado asciende a $30.972.000.000 CLP”
  - Sugerencia: Evitar afirmar montos o hechos como si fueran probados, ya que la causa no ha sido condenada.

## [[Caso Operaciones Digitales e Injerencia Electoral]]
- **alto** — Usa lenguaje que sugiere una condena o resolución judicial firme (imputación formal) sin aclarar que se trata de una situación procesal en curso o sin indicar que no hay sentencia condenatoria
  - Frase: “imputación formal de Cerimedo en Brasil por la Policía Federal y el Supremo Tribunal Federal”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como confirmación de hechos probados, y aclarar el estado procesal actual de la imputación en Brasil

## [[Caso Pacogate]]
- **alto** — Afirma como hecho probado un delito con un monto específico sin que la situación procesal indique una condena firme.
  - Frase: “habrían sustraído $28.348.928.198 CLP”
  - Sugerencia: Evitar afirmar montos o hechos como si fueran probados cuando la causa no tiene sentencia firme.
- **medio** — Menciona un veredicto condenatorio sin mencionar que no está firme, lo que puede generar confusión sobre el estado real del proceso.
  - Frase: “dictó veredicto condenatorio contra 25 de los 28 acusados”
  - Sugerencia: Aclarar que el veredicto no está firme y que la sentencia aún no se ha dictado.

## [[Caso Panama Papers Chile]]
- **medio** — Afirma como hecho probado la gestión de sociedades offshore sin mencionar que no hay condena o sentencia en la causa judicial
  - Frase: “La filtración reveló que el abogado [[Gonzalo Delaveau Swett]] —quien hasta ese momento ejercía como Presidente de *Chile Transparente*** (el capítulo chileno de Transparencia Internacional)— actuaba simultáneamente como agente e intermediario de [[Mossack Fonseca y Sociedades Offshore Panama]], gestionando y administrando al menos cinco sociedades *offshore* domiciliadas en Bahamas (*Turnbrook Corporation*, *DKL Holdings*, *Westquarter Limited*, *Mining Press Holdings* y *Turnbrook Mining Ltd.*) articuladas en torno al proyecto minero *Andes Copper*”
  - Sugerencia: Revisar si la información se basa en pruebas judiciales concluyentes o si se trata de suposiciones o hallazgos preliminares de la investigación
- **medio** — Afirma como hecho probado la creación de fundaciones y sociedades offshore sin mencionar que no hay condena o sentencia en la causa judicial
  - Frase: “Los registros de Mossack Fonseca documentaron la creación de las fundaciones de interés privado *Ashton Foundation* y *Kintyre Foundation* en Panamá por parte del propietario de *El Mercurio*, [[Agustin Edwards Eastman]], así como las sociedades *Sierra Leona S.A.* y *Railton Foundation* vinculadas al expresidente de la Confederación de la Producción y del Comercio (CPC) y de la SONAMI, [[Alfredo Ovalle Rodriguez]]”
  - Sugerencia: Revisar si la información se basa en pruebas judiciales concluyentes o si se trata de suposiciones o hallazgos preliminares de la investigación
- **medio** — Afirma como hecho probado la conexión con sociedades offshore sin mencionar que no hay condena o sentencia en la causa judicial
  - Frase: “Los archivos internos de [[Mossack Fonseca y Sociedades Offshore Panama]] confirmaron que el bufete panameño prestó servicios registrales a sociedades de papel en las Islas Vírgenes Británicas conectadas con la red fiduciaria de [[Riggs Bank y Sociedades Offshore Ashburton]], operada por [[Augusto Pinochet Ugarte]] y [[Oscar Aitken Lavanchy]] en el [[Caso Riggs]]”
  - Sugerencia: Revisar si la información se basa en pruebas judiciales concluyentes o si se trata de suposiciones o hallazgos preliminares de la investigación

## [[Caso Penta]]
- **alto** — Afirma como hecho probado un delito (condenado) cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “primer político condenado en juicio abreviado en diciembre de 2015”
  - Sugerencia: Evitar afirmar con certeza la condena de un político sin verificar que la causa tenga sentencia firme.

## [[Caso Riggs]]
- **medio** — uso de lenguaje peyorativo o calificativo no judicial al describir una red de cuentas bancarias sin mencionar si fue probado judicialmente
  - Frase: “estructuró y ocultó una red de más de 125 cuentas bancarias secretas”
  - Sugerencia: revisar si el término 'estructuró y ocultó' se basa en pruebas judiciales o si se puede reemplazar por un lenguaje más neutral
- **medio** — uso de lenguaje peyorativo al calificar las cédulas como 'ideológicamente falsas' sin mencionar si fue probado judicialmente
  - Frase: “abrió cuentas secretas utilizando pasaportes diplomáticos y cédulas chilenas ideológicamente falsas”
  - Sugerencia: revisar si el término 'ideológicamente falsas' se basa en pruebas judiciales o si se puede reemplazar por un lenguaje más neutral

## [[Caso SQM]]
- **medio** — Atribuye a SQM un hecho sin mencionar que sea probado judicialmente, lo que puede generar una impresión de culpabilidad sin base legal.
  - Frase: “La propia SQM reconoció ante la SEC y el Departamento de Justicia de EE.UU. pagos indebidos por unos US$ 14,75 millones.”
  - Sugerencia: Revisar si el reconocimiento de SQM fue judicialmente acreditado o si se trata de una admisión en un ámbito no judicial, para evitar una interpretación errónea.

## [[TRX-1975-08-15-Pagos-CIA-Entrenamiento-SOA-DINA-Contreras-01]]
- **alto** — Afirma como hecho probado una condena sin mencionar si la causa tiene sentencia firme o si se encuentra en apelación, lo que podría ser contradictorio con la situación procesal real.
  - Frase: “la [[Corte Suprema de Chile]] condenó posteriormente a Contreras a más de 529 años de presidio efectivo”
  - Sugerencia: Revisar si la condena mencionada es definitiva y si se encuentra respaldada por una sentencia firme. En caso contrario, se debe evitar afirmar con certeza la condena.

## [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]]
- **medio** — afirma como hecho probado un delito o consecuencia sin que exista una sentencia condenatoria o resolución judicial que lo acredite
  - Frase: “provocó la insolvencia e intervención estatal de la institución financiera”
  - Sugerencia: revisar si existe una sentencia o resolución judicial que acredite la insolvencia e intervención estatal como consecuencia directa del hecho auditado
- **medio** — afirma como hecho probado la fuga del imputado sin que exista una sentencia condenatoria o resolución judicial que lo acredite
  - Frase: “permaneció 24 días prófugo”
  - Sugerencia: revisar si existe una sentencia o resolución judicial que acredite la fuga del imputado
- **medio** — afirma como hecho probado la existencia de una orden de detención sin que exista una sentencia condenatoria o resolución judicial que lo acredite
  - Frase: “el juez Luis Correa Bulo dictó encargatoria de reo y orden de detención”
  - Sugerencia: revisar si existe una sentencia o resolución judicial que acredite la encargatoria de reo y la orden de detención

## [[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]
- **medio** — exposición de datos personales (nombre completo) de una persona sin que se haya establecido una condena firme
  - Frase: “máximos ejecutivos de [[Empresas CMPC SA]] (CMPC Tissue) y el fundador y controlador de PISA ([[SCA Chile SA]]), [[Gabriel Ruiz-Tagle Serrano]]”
  - Sugerencia: evitar mencionar nombres completos de personas sin condena firme
- **medio** — afirmación de hechos como probados sin mencionar que se trata de una imputación o acusación
  - Frase: “acordaron poner fin a una guerra comercial de precios y dividirse artificialmente el mercado del papel higiénico y servilletas en Chile”
  - Sugerencia: utilizar términos como 'presunto' o 'acusado de' para evitar dar por ciertos hechos que aún no han sido probados

## [[TRX-2001-08-20-Contratos-MOP-GATE-01]]
- **alto** — Afirma como hecho probado la existencia de un delito (desvío de caudales públicos y pago de sobresueldos) sin haberse establecido una condena o sentencia judicial.
  - Frase: “deliberadamente abultado en `$1.253.000.000 CLP` para desviar caudales públicos hacia el pago de sobresueldos de funcionarios y directivos ministeriales.”
  - Sugerencia: Reemplazar frases que afirman hechos como probados con términos que reflejen la naturaleza de la investigación, como 'se ha señalado' o 'se ha identificado una posible irregularidad'.

## [[TRX-2007-11-01-Colusion-Precios-Medicamentos-Farmacias-01]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre personas sin condena
  - Frase: “cartel operó contactando a los laboratorios farmacéuticos para que actuaran como supervisores del cumplimiento de las listas de precios infladas”
  - Sugerencia: reemplazar 'cartel' por términos neutrales como 'grupo' o 'organización'

## [[TRX-2008-01-15-Colusion-Cuotas-Produccion-Pollos-01]]
- **alto** — uso de lenguaje peyorativo ('Cartel') que sugiere una organización criminal sin que exista una condena o sentencia que lo acredite
  - Frase: “Cartel-Pollos-01”
  - Sugerencia: evitar el uso de términos como 'cartel' que pueden ser interpretados como calificativos no judiciales y que no están respaldados por una condena judicial

## [[TRX-2009-11-18-Facturas-Bancard-SQM-2009-01]]
- **medio** — Usa el término 'presumió' que indica una acusación sin prueba concluyente, lo cual es compatible con la presunción de inocencia, pero podría interpretarse como una afirmación de hecho probado si no se contextualiza adecuadamente.
  - Frase: “la Fiscalía presumió ideológicamente falsas por no existir servicios que las justificaran”
  - Sugerencia: Aclarar que la Fiscalía solo ha formulado una presunción, no una prueba concluyente de falsedad de las facturas.
- **medio** — Aunque es correcto señalar que no hay sentencia, el enunciado podría interpretarse como una afirmación de hecho probado si no se enfatiza la ausencia de condena.
  - Frase: “no existe sentencia que declare falsas las facturas”
  - Sugerencia: Reforzar que la ausencia de sentencia confirma la presunción de inocencia y que no hay condena firme.

## [[TRX-2010-06-15-Informe-Economico-Peritaje-Defensa-Salcobrand-01]]
- **alto** — Afirma como hecho probado un delito ('acreditando la concertación ilícita') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “acreditando la concertación ilícita horizontal entre las farmacias”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

## [[TRX-2010-08-19-Correo-Royalty-SQM-01]]
- **medio** — Usa el verbo 'habría' que sugiere una acción no probada, pero no afirma directamente un hecho como probado. Sin embargo, menciona un monto específico que podría interpretarse como un hecho concreto.
  - Frase: “la empresa habría canalizado pagos por aproximadamente $730.000.000 CLP entre 2009 y 2015 a personas de su entorno mediante boletas y facturas”
  - Sugerencia: Evitar mencionar montos específicos sin aclarar que se trata de hipótesis acusatorias no acreditadas.

## [[TRX-2010-11-15-Pagos-KDM-Licitacion-Basura-Maipu-01]]
- **alto** — Afirma como hecho probado un delito ('acreditados') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el tribunal dio por acreditados pagos de KDM por $186,5 millones”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

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
  - Sugerencia: revisar el uso de la frase para evitar interpretaciones que puedan implicar una falta de rigor en la acreditación de hechos

## [[TRX-2012-07-11-Pagos-Corpesca-LeyDePesca-01]]
- **alto** — Afirma como hecho probado un delito ('acreditado en juicio oral') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “Pagos ilícitos reiterados por un total acreditado en juicio oral de $233.000.000 CLP”
  - Sugerencia: Evitar afirmar como probado un delito sin que exista una sentencia condenatoria firme.

## [[TRX-2013-07-15-Boletas-Penta-UDI-01]]
- **medio** — Atribuye a terceros (candidatos y dirigentes de la UDI) un hecho que no está probado ni vinculado directamente a la transacción auditada, lo que puede generar una presunción de culpabilidad injusta.
  - Frase: “financiar fuera del marco legal campañas electorales de candidatos y dirigentes de la [[Union Democrata Independiente]] como [[Pablo Longueira Montes]]”
  - Sugerencia: Revisar y reescribir la frase para evitar atribuir hechos no probados a terceros, manteniendo el enfoque en la transacción auditada.

## [[TRX-2013-09-20-Boletas-Penta-Novoa-01]]
- **alto** — Afirma como hecho probado un delito (condenado) cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el primer político condenado penalmente en el [[Caso Penta]]”
  - Sugerencia: Evitar afirmar con certeza la condena de una persona si no se ha declarado explícitamente en los metadatos.

## [[TRX-2014-02-18-Pagos-DOM-Machali-Caval-01]]
- **alto** — Afirma como hecho probado un delito (condenado) cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “Silva fue condenado en procedimiento abreviado (enero de 2018) a 818 días con remisión condicional por cohecho reiterado.”
  - Sugerencia: Revisar si la condena fue firme y si se menciona correctamente en los metadatos.
- **medio** — Usa lenguaje que podría implicar una condena o responsabilidad cuando se refiere a la absolución de Mauricio Valero Illanes y Caval.
  - Frase: “La acusación de soborno contra [[Mauricio Valero Illanes]] y la sociedad Caval fue rechazada: ambos fueron absueltos por el TOP de Rancagua en julio de 2018.”
  - Sugerencia: Asegurar que el lenguaje refleje correctamente la absolución y no deje lugar a ambigüedades.

## [[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]
- **alto** — Afirma como hecho probado un delito con un monto específico sin mencionar que la situación procesal no es condena
  - Frase: “defraudación patrimonial por un monto consolidado de $6.100.000.000 CLP”
  - Sugerencia: Revisar y reemplazar por un lenguaje que no afirme hechos como probados, por ejemplo: 'se le imputa una defraudación patrimonial por un monto consolidado de $6.100.000.000 CLP'

## [[TRX-2015-01-29-Facturas-Caval-SII-01]]
- **alto** — afirma como hecho probado un delito (condenó) cuando la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “el TOP de Rancagua condenó a [[Natalia Compagnon Soto]] por permitir que la contabilidad social incorporara facturas ideológicamente falsas por asesorías inexistentes en los años tributarios 2013, 2014 y 2015”
  - Sugerencia: revisar si la condena está acreditada como firme en la causa, y en caso contrario, reemplazar por lenguaje no concluyente
- **medio** — afirma como hecho probado un delito (generó una utilidad bruta) cuando la situación procesal no es condenado o la causa no tiene sentencia
  - Frase: “operación de compraventa especulativa de los predios de Machalí que generó una utilidad bruta de $2.500.000.000 CLP para [[Exportadora y de Gestion Caval Ltda]]”
  - Sugerencia: revisar si la utilidad bruta está acreditada como hecho probado en la causa, y en caso contrario, reemplazar por lenguaje no concluyente

## [[TRX-2015-08-14-GastosReservados-Ejercito-UAF-01]]
- **medio** — Usa lenguaje que sugiere responsabilidad directa sin haberse establecido una condena o sentencia
  - Frase: “atribuidas por la investigación a [[Juan Miguel Fuente-Alba Poblete]]”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como afirmaciones de hecho probado, y reemplazarlos con lenguaje más cauteloso, como 'presuntamente atribuidas' o 'asociadas según la investigación'.

## [[TRX-2015-10-29-Pago-Multas-Colusion-Pollos-01]]
- **alto** — uso de lenguaje peyorativo ('cartel') que no es judicial y sugiere criminalidad sin condena firme
  - Frase: “Cartel de los Pollos”
  - Sugerencia: reemplazar por términos neutrales y no calificativos, como 'grupo empresarial' o 'organización'

## [[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]
- **medio** — uso de calificativo no judicial ('vitaliciamente') que puede interpretarse como peyorativo
  - Frase: “presidida vitaliciamente por [[Lucia Hiriart Rodriguez]]”
  - Sugerencia: revisar el uso de términos que puedan interpretarse como calificativos no judiciales
- **medio** — afirma como hecho probado la devolución de activos sin mencionar la situación procesal o condena
  - Frase: “forzó la disolución de la fundación y la devolución al Fisco de 108 inmuebles fiscales y municipales más sus activos bancarios líquidos”
  - Sugerencia: especificar si la devolución fue resultado de una condena o acuerdo judicial

## [[TRX-2016-11-10-Fondos-Direccion-Finanzas-Carabineros-01]]
- **medio** — Usa un veredicto que no está firme como si fuera un hecho probado
  - Frase: “descartó la asociación ilícita”
  - Sugerencia: Se debe aclarar que el veredicto no está firme y que la asociación ilícita sigue siendo un cargo pendiente de resolución judicial
- **medio** — Afirma como hecho probado un delito sin que la situación procesal lo indique
  - Frase: “lavado de activos”
  - Sugerencia: Se debe usar lenguaje que indique que es un cargo imputado, no un hecho probado

## [[TRX-2017-03-06-Reportes-UAF-Carabineros-01]]
- **medio** — Usa un término que sugiere una decisión judicial definitiva, cuando el veredicto no está firme.
  - Frase: “descartó la asociación ilícita”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como decisiones definitivas, cuando el proceso aún no ha concluido.

## [[TRX-2017-09-23-Detenciones-OperacionHuracan-01]]
- **alto** — Afirma como hecho probado un delito ('acreditó') cuando la situación procesal no es condenado o la causa no tiene sentencia.
  - Frase: “el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]) acreditó que los supuestos chats fueron redactados e implantados manualmente en los teléfonos por [[Leonardo Osses Sandoval]] y sus subalternos tras las incautaciones”
  - Sugerencia: Evitar afirmar hechos como probados sin que exista una sentencia condenatoria firme.

## [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]]
- **medio** — Usa el término 'concluyentes' que sugiere certeza absoluta en un informe pericial, lo cual puede interpretarse como afirmación de hechos probados sin que exista una sentencia condenatoria.
  - Frase: “la Fiscalía Regional de La Araucanía remitió al Juzgado de Garantía de Temuco los resultados concluyentes del informe pericial”
  - Sugerencia: Revisar el uso de términos que sugieran certeza absoluta en contextos donde aún no se ha dictado una sentencia.

## [[TRX-2019-05-14-Licitacion-Luminarias-Chillan-01]]
- **medio** — Usa lenguaje que sugiere hechos probados sin que exista una sentencia conocida al 2026-10-19
  - Frase: “según la Fiscalía, se habría obtenido mediante el pago de sobornos”
  - Sugerencia: Revisar el uso de términos como 'habría obtenido' para evitar sugerir certeza sobre hechos que no han sido probados judicialmente
- **medio** — Menciona una hipótesis de la Fiscalía sin mencionar que no hay sentencia conocida al 2026-10-19, lo que puede generar confusión sobre el estado del proceso
  - Frase: “según la hipótesis de la Fiscalía en el [[Caso Luminarias LED]] (sin sentencia conocida al 2026-10-19)”
  - Sugerencia: Aclarar que no hay sentencia conocida al 2026-10-19 para evitar malinterpretaciones sobre el estado del caso

## [[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]
- **medio** — uso de lenguaje peyorativo o calificativos no judiciales ('vínculo simbiótico') sobre personas sin condena
  - Frase: “Arista financiera y política del [[Caso Audios]] que documenta el vínculo simbiótico entre el abogado [[Luis Hermosilla Osorio]] y el exministro del Interior [[Andres Chadwick Pinera]] (primo hermano del expresidente [[Sebastian Pinera Echenique]]):”
  - Sugerencia: reemplazar 'vínculo simbiótico' por un término neutral y objetivo
- **medio** — afirma como hecho probado un delito ('gestiones de Trafico de Influencias') cuando la situación procesal NO es condenado o la causa no tiene sentencia
  - Frase: “la Fiscalía investiga si provenían de fondos de [[Factop SpA]], período en el cual se investigan gestiones de [[Trafico de Influencias]] para la obtención acelerada de certificados de factibilidad del proyecto *Parque Capital* (Grupo Patio) y coordinaciones en nombramientos de la [[Corte Suprema de Chile]] junto a [[Angela Vivanco Martinez]]”
  - Sugerencia: reemplazar 'gestiones de Trafico de Influencias' por 'posibles gestiones de Trafico de Influencias' o similar para reflejar la naturaleza investigativa del hecho

## [[TRX-2020-11-25-Compensacion-Indemnizatoria-Consumidores-Farmacias-01]]
- **alto** — uso de lenguaje peyorativo ('cartel') sobre una entidad sin condena judicial
  - Frase: “cartel farmacéutico”
  - Sugerencia: reemplazar por términos neutrales como 'grupo farmacéutico' o 'organización farmacéutica'

## [[TRX-2020-12-15-Deficit-Maipu-Certificados-01]]
- **alto** — Afirma como hecho probado un delito sin que la situación procesal indique una condena firme.
  - Frase: “fraude al fisco”
  - Sugerencia: Utilizar lenguaje que refleje la naturaleza acusatoria del caso, como 'presunto fraude al fisco' o 'acusado de fraude al fisco'.

## [[TRX-2021-04-15-Subvencion-VitaDeportes-01]]
- **medio** — Usa el verbo 'habrían sido' que sugiere una acción probada sin que exista una condena o sentencia firme.
  - Frase: “habrían sido desviadas por $759.000.000 CLP”
  - Sugerencia: Reemplazar por 'se habrían desviado' o 'se sospecha que fueron desviadas' para evitar afirmar como hecho probado un delito.

## [[TRX-2022-11-18-Convenio-ProCultura-Biobio]]
- **medio** — Usa el término 'por' para atribuir un delito sin haberse establecido una condena o sentencia
  - Frase: “investigado en el [[Caso Convenios]] por [[Fraude al Fisco]]”
  - Sugerencia: Reemplazar por 'investigado en el [[Caso Convenios]] por presunto [[Fraude al Fisco]]' o similar para mantener el rigor legal y la presunción de inocencia

## [[TRX-2022-11-29-Convenio-DV-03]]
- **medio** — Atribuye un delito a una causa colectiva sin especificar la participación individual de la persona mencionada.
  - Frase: “imputado como [[Fraude al Fisco]] reiterado en [[Caso Convenios]]”
  - Sugerencia: Revisar si el fraude al fisco se refiere específicamente a la persona mencionada o si se refiere a la causa colectiva, evitando generalizaciones.

## [[TRX-2022-12-20-Convenio-EnTi-01]]
- **medio** — Usa lenguaje que sugiere hechos probados sin mencionar que la situación procesal no es condena firme
  - Frase: “La investigación penal de la Fiscalía Regional del Biobío en el [[Caso Convenios]] sostiene que hubo desvío de fondos hacia sociedades instrumentales, gastos personales improcedentes y rendiciones con facturas ideológicamente falsas”
  - Sugerencia: Revisar el uso de términos que implican certeza sobre hechos que aún no han sido probados judicialmente

## [[TRX-2023-06-22-Reunion-Audios-01]]
- **medio** — Usa el término 'presuntamente' lo cual indica que no hay una prueba concluyente del delito, sin embargo, menciona específicamente el pago de sobornos, lo que puede interpretarse como una afirmación de hecho sin estar suficientemente respaldada.
  - Frase: “presuntamente destinado, según la Fiscalía, al pago de sobornos a funcionarios públicos del [[Servicio Impuestos Internos]] y la CMF en beneficio de [[Factop SpA]]”
  - Sugerencia: Revisar el uso de términos que puedan interpretarse como afirmaciones de hechos probados, incluso si están precedidos por 'presuntamente'.

## [[TRX-2023-12-14-Perjuicio-Fiscal-Operacion-Tributos-01]]
- **alto** — Exposición de un monto elevado de perjuicio fiscal sin mencionar que se trata de una estimación o hipótesis acusatoria, lo que puede dar una impresión de certeza cuando no existe sentencia condenatoria.
  - Frase: “perjuicio fiscal récord consolidado de $240.000.000.000 CLP cuantificado por el SII”
  - Sugerencia: Aclarar que el monto es una estimación del SII y no un hecho probado.

## [[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]
- **medio** — uso de lenguaje que sugiere hechos probados sin haberse establecido una condena o sentencia
  - Frase: “según el cual a funcionarios y asesores contratados con cargo a los fondos públicos de asignaciones del Congreso se les habría exigido la restitución en dinero en efectivo de parte significativa de sus salarios mensuales”
  - Sugerencia: revisar el uso de términos como 'habría exigido' para evitar la impresión de certeza sobre hechos que aún no han sido probados judicialmente

