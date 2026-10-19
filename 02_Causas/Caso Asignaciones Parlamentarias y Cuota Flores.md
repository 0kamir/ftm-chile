---
tipo_nodo: causa_judicial
ruc: "RUC-2500819421-2"
año_inicio: 2025
tribunal_o_fiscalia: "Juzgado de Garantía de Valparaíso / Unidad Regional Anticorrupción (URAC) Fiscalía de Valparaíso"
fiscal_a_cargo: "Claudia Perivancich Hoyuelos / OS9 y Cibercrimen de la PDI"
estado_judicial: investigacion_desformalizada_con_allanamientos
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2026/04/09/1196710/camila-flores-investigacion-fraude-fisco.html"
    titulo: "Camila Flores: investigación por fraude al fisco"
    medio: "Emol"
    tipo: secundaria
    fecha: 2026-04-09
    consultado: 2026-10-19
  - url: "https://www.ciperchile.cl/2026/05/06/fiscalia-ingresa-al-senado-por-investigacion-contra-camila-flores-por-posible-fraude-al-fisco/"
    titulo: "Fiscalía ingresa al Senado por investigación contra Camila Flores"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2026-05-06
    consultado: 2026-10-19
  - url: "https://www.diarioconstitucional.cl/2026/05/09/rn-remite-a-camila-flores-al-tribunal-supremo-en-medio-de-investigacion-por-presunto-fraude-al-fisco/"
    titulo: "RN remite a Camila Flores al Tribunal Supremo"
    medio: "Diario Constitucional"
    tipo: secundaria
    fecha: 2026-05-09
    consultado: 2026-10-19
alertas_verificacion:
  - "Investigación desformalizada: no hay imputación formal. La arista de registros íntimos (TRX-2026-06-20) trata a Flores como VÍCTIMA de un delito contra la intimidad, no de corrupción: evaluar retirarla del grafo por privacidad."
tags:
  - causa
  - asignaciones-parlamentarias
  - cuota-flores
  - camila-flores
  - percy-marin
  - rn
  - valparaiso
---

# Caso Asignaciones Parlamentarias y Cuota Flores

## Ficha Procesal, Regulatoria y Sancionatoria
- **Rol de Causa / Identificador Persecutor**: `= this.ruc` *(Investigación penal a cargo de la URAC Valparaíso)*
- **Año de Apertura**: `= this.año_inicio` (Pesquisas y diligencias públicas desarrolladas durante 2025–2026)
- **Tribunales e Instancias Intervinientes**: `= this.tribunal_o_fiscalia` (con recursos de cautela ante la Corte Suprema)
- **Fiscales e Investigadores Policiales**: `= this.fiscal_a_cargo` en coordinación con el OS9 de Carabineros y la Brigada del Cibercrimen
- **Estado Procesal**: `= this.estado_judicial` (Allanamiento de dependencias legislativas, peritajes digitales y solicitud de querella al CDE)
- **Delito Principal**: `= this.delito_principal` (con concurrencia de delitos contra la intimidad personal y violencia digital)

## Resumen Ejecutivo de la Causa
Investigación penal de alta connotación institucional dirigida contra la senadora de [[Renovacion Nacional]] [[Camila Flores Oporto]] (ex diputada por el Distrito 6) por presuntos delitos reiterados de fraude al Fisco, desvío de caudales públicos y vulneración de normas laborales y de probidad en el Congreso Nacional.

La causa se estructura en dos aristas complementarias:

1. **Arista "Cuota Flores" (Fraude al Fisco por Diezmos Parlamentarios)**:
   A raíz de denuncias de excolaboradores y personal de apoyo financiado con cargo a asignaciones parlamentarias del [[Senado de la Republica de Chile]], la Fiscalía Regional de Valparaíso indaga la exigencia sistemática a asesores legislativos de entregar en efectivo un porcentaje recurrente de sus remuneraciones mensuales ([[TRX-2025-10-15-Denuncia-Retencion-Sueldos-Asesores-Flores-01]]). En abril de 2026, el OS9 de Carabineros ejecutó allanamientos e incautaciones de computadores y celulares en dependencias del Congreso y en el domicilio de la parlamentaria ([[Orden-Entrada-Registro-Congreso-Caso-Flores-2026]]).

2. **Arista Registros Íntimos y Disputa Conyugal**:
   Paralelamente, a mediados de 2026 se abrió una causa penal en la Brigada del Cibercrimen de la PDI tras la denuncia de Camila Flores por la obtención, sustracción y difusión no consentida de registros audiovisuales íntimos y privados grabados por cámaras de seguridad en su hogar ([[Denuncia-Cibercrimen-PDI-Registros-Intimos-2026]]), apuntando a su exmarido [[Percy Marin Vera]] ([[TRX-2026-06-20-Extraccion-Difusion-Ilicita-Registros-Intimos-01]]). Este hecho derivó además en la interposición de recursos de cautela de garantía por parte de la defensa ante el Juzgado de Garantía y la Corte Suprema para evitar la filtración de material de índole estrictamente privada requisado en los dispositivos incautados.

## Hechos y Nexos Vinculados a la Causa
```dataview
TABLE WITHOUT ID
  file.link AS "Hecho / Nexo",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo de Nexo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Infracción / Delito",
  evidencia_soporte AS "Evidencia"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(causa_vinculada), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
