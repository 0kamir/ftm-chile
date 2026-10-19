---
tipo_nodo: causa_judicial
ruc: ""
año_inicio: 2026
tribunal_o_fiscalia: "Fiscalía Regional Metropolitana Centro Norte / 7° Juzgado de Garantía de Santiago"
fiscal_a_cargo: "Fiscalía Metropolitana Centro Norte / Comisión Investigadora Cámara de Diputados"
estado_judicial: investigacion_desformalizada
delito_principal: "[[Fraude al Fisco]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/"
    titulo: "Fiscalía Centro Norte abre investigación por presuntos delitos informáticos vinculados a Fernando Cerimedo"
    medio: "CNN Chile"
    tipo: secundaria
    fecha: 2026-09-03
    consultado: 2026-10-19
  - url: "https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html"
    titulo: "Fiscalía Centro Norte abre investigación por eventual intervención de Cerimedo en procesos electorales"
    medio: "Pauta"
    tipo: secundaria
    fecha: 2026-09-04
    consultado: 2026-10-19
  - url: "https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/"
    titulo: "El día que el 'rey de los trolls' llegó a la sede de RN"
    medio: "The Clinic"
    tipo: secundaria
    fecha: 2026-08-28
    consultado: 2026-10-19
tags:
  - causa
  - desinformacion
  - redes-sociales
  - servel
  - injerencia-electoral
  - cerimedo
  - rechazo
  - bots
---

# Caso Operaciones Digitales e Injerencia Electoral

## Ficha Procesal, Regulatoria y Sancionatoria
- **Rol de Causa / Registro Persecutor**: `= this.ruc` *(Investigación penal abierta ante Fiscalía Metropolitana Centro Norte)*
- **Año de Apertura / Indagatoria Pública**: `= this.año_inicio` (Período de operaciones investigadas: 2020–2023)
- **Instancias Investigadoras**: `= this.tribunal_o_fiscalia` y Comisión Especial Investigadora de la Cámara de Diputadas y Diputados
- **Fiscales y Órganos Fiscalizadores**: `= this.fiscal_a_cargo` en coordinación técnica con el [[Servicio Electoral]]
- **Estado Procesal**: `= this.estado_judicial` (Diligencias periciales de trazabilidad financiera y digital)
- **Delito / Infracción Principal**: `= this.delito_principal` (con investigación de infracciones a la Ley 19.884 sobre Control del Gasto Electoral y Ley de Delitos Informáticos)

## Resumen Ejecutivo de la Causa
Indagatoria penal y fiscalización parlamentaria en torno al despliegue de operaciones de desinformación, amplificación coordinada mediante cuentas automatizadas ("granjas de bots") y presunto financiamiento irregular u opaco de campañas electorales en Chile, asociadas a agencias digitales extranjeras y en particular a [[Fernando Cerimedo]] y su firma [[Numen Publicidad SpA]].

La causa aborda tres ejes principales:
1. **Despliegue Digital en el Plebiscito Constitucional 2022**: Reconocimiento público de Cerimedo sobre la coordinación de campañas de microsegmentación, viralización y difusión de contenidos en redes sociales durante la campaña del Rechazo, contrastado con la ausencia de registros de facturación o pagos directos reportados en las rendiciones oficiales del gasto electoral ante el Servel.
2. **Nexos Políticos y Presencia en Sedes Partidarias**: Registros fotográficos difundidos por The Clinic muestran a Cerimedo en la sede nacional del partido (RN niega haberlo contratado) [[Renovacion Nacional]] el 4 de septiembre de 2022 durante las celebraciones de la victoria del Rechazo, junto a dirigentes partidarios y operadores de campaña ([[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]]).
3. **Imputaciones Internacionales y Seguridad Electoral**: La causa cobró urgencia tras la imputación formal de Cerimedo en Brasil por la Policía Federal y el Supremo Tribunal Federal por su rol en los ataques de desinformación contra las urnas electrónicas en la trama golpista de 2022-2023, activando requerimientos de cooperación judicial internacional y la creación de una Comisión Investigadora en la Cámara de Diputados de Chile.

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
