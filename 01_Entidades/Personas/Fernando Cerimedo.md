---
tipo_nodo: persona
rut: ""
aliases:
  - "Fernando Cerimedo"
  - "Fernando Cerimedo Numen"
rol_principal: "Consultor de Comunicación Digital, Fundador de Numen y La Derecha Diario"
afiliacion_politica: "Independiente / Estratega Digital de Derecha Radical"
situacion_procesal: investigado
medida_cautelar: "Imputado en Brasil por el STF por desinformación electoral; investigado penalmente en Chile por Fiscalía Centro Norte"
tags:
  - entidad/persona
  - consultor-digital
  - redes-sociales
  - cerimedo
  - rechazo
  - renovacion-nacional
---

# Fernando Cerimedo

> [!NOTE] Disclaimer Jurídico y Procesal en Chile
> En Chile, **Fernando Cerimedo no ha sido formalizado ni condenado penalmente**. El Ministerio Público (Fiscalía Metropolitana Centro Norte) mantiene diligencias de investigación desformalizadas respecto de presuntas irregularidades en el financiamiento u operaciones de propaganda digital durante los procesos constitucionales. Los partidos aludidos, dirigentes de [[Renovacion Nacional]] y el excandidato presidencial José Antonio Kast han negado formalmente haber suscrito contratos institucionales o emitido pagos electorales a su nombre.

## Perfil Biográfico e Institucional
- **RUT Provisorio / Registro Extranjero**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medidas Cautelares / Procesos Internacionales**: `= this.medida_cautelar`

## Síntesis Forense y Vínculos en Chile
Consultor político, publicista digital y estratega electoral argentino, propietario de la agencia [[Numen Publicidad SpA]] y fundador del portal de noticias *La Derecha Diario*. Ha coordinado estrategias de redes sociales y campañas de amplificación algorítmica para liderazgos de derecha en América Latina, incluyendo a Javier Milei en Argentina y Jair Bolsonaro en Brasil.

### 1. Actuación en Campañas Electorales Chilenas
En 2020 constituyó la filial de su agencia en Chile junto a socios locales. De cara al Plebiscito de Salida de septiembre de 2022, Cerimedo reconoció públicamente en diversos medios haber participado activamente en la estrategia digital de la opción **Rechazo**, gestionando microsegmentación, viralización de contenidos y presunto uso de infraestructuras automatizadas ("granjas de bots") en redes sociales. 

### 2. Vínculo y Presencia en la Sede de Renovación Nacional
El 4 de septiembre de 2022, en la noche del triunfo electoral del Rechazo, Cerimedo estuvo físicamente presente en la sede nacional del partido [[Renovacion Nacional]] (ubicada en Antonio Varas 454, Providencia). 

Dicha presencia consta en registros fotográficos revelados por el medio *The Clinic* (RN sostiene que nunca lo contrató) ([[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]]), en los cuales aparece en dependencias de la sede partidaria junto al entonces prosecretario de RN, Manuel José Errázuriz, su socio en Numen Enrique García Arancibia, y colaboradoras ligadas a centros de estudios del sector como Teresa Zañartu ([[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]).

### 3. Indagatorias Judiciales y Parlamentarias
- **Fiscalía Centro Norte**: Abrió causa penal para determinar eventuales infracciones a la Ley 19.884 sobre Control del Gasto Electoral y la Ley de Delitos Informáticos, ante la falta de reportes financieros en las rendiciones del Servel.
- **Cámara de Diputadas y Diputados**: Aprobó la creación de una Comisión Especial Investigadora sobre la participación de agencias digitales internacionales y desinformación en los plebiscitos chilenos.
- **Operación Tempus Veritatis (Brasil)**: En febrero de 2024, la Policía Federal de Brasil y el Supremo Tribunal Federal (STF) lo imputaron dentro del núcleo de desinformación por difundir ataques contra el sistema de votación electrónica brasileño.

## Auditoría Contable: Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Delito", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    p.delito_imputado,
    p.causa_vinculada
  ])
);
```
