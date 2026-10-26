---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2003
tribunal_o_fiscalia: "33° Juzgado del Crimen de Santiago / Corte de Apelaciones de Santiago / Corte Suprema de Chile (Causa Rol 9.327-2003)"
fiscal_a_cargo: "Ministro en Visita Sergio Muñoz Gajardo (tras inhabilitación de Juez Daniel Calvo Flores)"
estado_judicial: cerrada_con_condena
delito_principal: "[[Lavado de Activos]]"
estado_verificacion: verificado
fuentes:
  - "https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html"
  - "https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html"
  - "https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz"
tags:
  - causa
  - poder-judicial
  - caso-spiniak
---

# Caso Spiniak

## Ficha Procesal y Judicial
- **RUC / Rol Judicial**: `= this.ruc` (Rol Crimen N° `9.327-2003`)
- **Año de Inicio**: `= this.año_inicio`
- **Tribunal / Ministro Instructor**: `= this.tribunal_o_fiscalia`
- **Magistrado a Cargo**: `= this.fiscal_a_cargo`
- **Estado Judicial**: `= this.estado_judicial`
- **Delito Principal**: `= this.delito_principal` (en concurso con asociación ilícita, explotación sexual comercial de menores, producción de material pornográfico, falso testimonio y [[Delito Tributario]])

## Síntesis de la Causa
Macro-proceso judicial e institucional iniciado el 30 de septiembre de 2003 tras la detención del empresario [[Claudio Spiniak Vilensky]] en sus instalaciones de calle El Bosque Norte, operadas a través de [[Inversiones El Bosque Ltda]]. Aunque su núcleo penal primario fue una red de explotación sexual de menores y producción de pornografía infantil (por la cual Spiniak fue condenado definitivamente a 12 años de presidio efectivo en [[Sentencia-Corte-Suprema-CasoSpiniak-2008]]), el caso desencadenó tres aristas de alto impacto sobre el sistema político, tributario y el Poder Judicial chileno:

1. **Arista Patrimonial y Tributaria (SII / Sociedad Fachada)**: Auditoría y fiscalización del [[Servicio Impuestos Internos]] sobre [[Inversiones El Bosque Ltda]] ([[TRX-2003-10-15-Patrimonio-ElBosque-Spiniak-01]]), acreditando el desvío de flujos societarios, gastos rechazados y evasión impositiva para sostener la infraestructura clandestina del gimnasio *Go Fitness* y residencias en El Arrayán.
2. **Arista de Captura y Extorsión al Poder Judicial (Operación Cámara Oculta)**: En noviembre de 2003, el primer ministro en visita, juez Daniel Calvo Flores, fue objeto de una operación de extorsión y grabación subrepticia con cámara oculta difundida televisivamente, lo que forzó al Pleno de la [[Corte Suprema de Chile]] a removerlo de la causa, sancionarlo disciplinariamente y designar con dedicación exclusiva al ministro de la Corte Suprema [[Sergio Munoz Gajardo]].
3. **Arista Político-Parlamentaria y Montaje de Falso Testimonio (RN vs. UDI)**: El 10 de octubre de 2003, la diputada de [[Renovacion Nacional]], [[Pia Guzman Mena]], denunció públicamente que tres senadores integraban la red de Spiniak, desatando una fractura institucional en la coalición opositora con la [[Union Democrata Independiente]] —presidida por [[Pablo Longueira Montes]]— y querellas cruzadas ([[TRX-2003-11-05-Arista-Politica-Spiniak-01]]). En 2004, la investigación del ministro [[Sergio Munoz Gajardo]] acreditó científicamente la falsedad de los testimonios de Gema Bueno y del sacerdote José Luis Artiagoitía contra el senador UDI [[Jovino Novoa Vasquez]], condenando a los denunciantes por falso testimonio y sobreseyendo a Novoa en esta causa (quien una década más tarde sería condenado penalmente en el [[Caso Penta]] mediante [[TRX-2013-09-20-Boletas-Penta-Novoa-01]]).

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

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Claudio Spiniak fue condenado a cinco años y un día de cárcel](https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) | Cooperativa | `secundaria` | 2006-08-10 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/caso-spiniak/claudio-spiniak-fue-condenado-a-cinco-anos-y-un-dia-de-car/2006-08-10/084046.html) |
| [Muere Claudio Spiniak](https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) | Emol | `secundaria` | 2026-03-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2026/03/14/1194273/muere-claudio-spiniak-abuso-menores.html) |
| [Jovino Novoa, caso Spiniak e investigación del juez Sergio Muñoz](https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) | Pauta | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/politica/jovino-novoa-caso-spiniak-udi-investigacion-sergio-munoz) |
