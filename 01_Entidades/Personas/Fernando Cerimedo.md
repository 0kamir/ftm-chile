---
tipo_nodo: persona
rut: ""
aliases:
  - "Fernando Cerimedo"
  - "Fernando Cerimedo Numen"
rol_principal: "Consultor de Comunicación Digital, Fundador de Numen y La Derecha Diario"
afiliacion_politica: "Independiente / Estratega Digital de Derecha Radical"
situacion_procesal: investigado
medida_cautelar: "Indiciado por la Policía Federal de Brasil (nov-2024) sin ser acusado por la PGR; investigado en Chile por la Fiscalía Centro Norte (sin formalización)"
estado_verificacion: parcial
fuentes:
  - "https://apublica.org/2025/09/julgamento-stf-quem-foi-indiciado-mas-nao-deve-ser-julgado/"
  - "https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/"
  - "https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/"
  - "https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html"
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

## Síntesis y Vínculos en Chile
Consultor político, publicista digital y estratega electoral argentino, propietario de la agencia [[Numen Publicidad SpA]] y fundador del portal de noticias *La Derecha Diario*. Ha coordinado estrategias de redes sociales y campañas de amplificación algorítmica para liderazgos de derecha en América Latina, incluyendo a Javier Milei en Argentina y Jair Bolsonaro en Brasil.

### 1. Actuación en Campañas Electorales Chilenas
En 2020 constituyó la filial de su agencia en Chile junto a socios locales. De cara al Plebiscito de Salida de septiembre de 2022, Cerimedo reconoció públicamente en diversos medios haber participado activamente en la estrategia digital de la opción **Rechazo**, gestionando microsegmentación, viralización de contenidos y presunto uso de infraestructuras automatizadas ("granjas de bots") en redes sociales. 

### 2. Vínculo y Presencia en la Sede de Renovación Nacional
El 4 de septiembre de 2022, en la noche del triunfo electoral del Rechazo, Cerimedo estuvo físicamente presente en la sede nacional del partido [[Renovacion Nacional]] (ubicada en Antonio Varas 454, Providencia). 

Dicha presencia consta en registros fotográficos revelados por el medio *The Clinic* (RN sostiene que nunca lo contrató) ([[Fotografia-Cerimedo-Sede-Renovacion-Nacional-2022]]), en los cuales aparece en dependencias de la sede partidaria junto al entonces prosecretario de RN, Manuel José Errázuriz, su socio en Numen Enrique García Arancibia, y colaboradoras ligadas a centros de estudios del sector como Teresa Zañartu ([[TRX-2022-09-04-Presencia-Cerimedo-Sede-Renovacion-Nacional-01]]).

### 3. Indagatorias Judiciales y Parlamentarias
- **Fiscalía Centro Norte**: Abrió causa penal para determinar eventuales infracciones a la Ley 19.884 sobre Control del Gasto Electoral y la Ley de Delitos Informáticos, ante la falta de reportes financieros en las rendiciones del Servel.
- **Cámara de Diputadas y Diputados**: Aprobó la creación de una Comisión Especial Investigadora sobre la participación de agencias digitales internacionales y desinformación en los plebiscitos chilenos.
- **Operación Tempus Veritatis (Brasil)**: En noviembre de 2024 la Policía Federal de Brasil lo incluyó entre los indiciados de la investigación sobre la intentona golpista de 2022, por una transmisión en la que difundió supuestas fraudes en las urnas electrónicas. La Procuraduría General de la República no lo incluyó en la acusación de febrero de 2025, por lo que no es acusado ante el STF.

## Registros Reificados
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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Julgamento no STF: quem foi indiciado mas não deve ser julgado](https://apublica.org/2025/09/julgamento-stf-quem-foi-indiciado-mas-nao-deve-ser-julgado/) | Agência Pública | `secundaria` | 2025-09-01 | [Wayback ↺](https://web.archive.org/web/*/https://apublica.org/2025/09/julgamento-stf-quem-foi-indiciado-mas-nao-deve-ser-julgado/) |
| [El día que el 'rey de los trolls' llegó a la sede de RN](https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/) | The Clinic | `secundaria` | 2026-08-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/) |
| [Fiscalía Centro Norte abre investigación por presuntos delitos informáticos vinculados a Fernando Cerimedo](https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/) | CNN Chile | `secundaria` | 2026-09-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/) |
| [Fiscalía Centro Norte abre investigación por eventual intervención de Cerimedo en procesos electorales](https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html) | Pauta | `secundaria` | 2026-09-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html) |
