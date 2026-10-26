---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Numen Publicidad SpA"
fecha_constitucion: 2020-07-15
objeto_social: "Servicios de publicidad, comunicación estratégica, marketing digital, análisis de redes sociales y sondeos de opinión"
representante_legal: "[[Fernando Cerimedo]]"
estado_verificacion: verificado
fuentes:
  - "https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/"
  - "https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/"
  - "https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html"
  - "https://apublica.org/2025/09/julgamento-stf-quem-foi-indiciado-mas-nao-deve-ser-julgado/"
tags:
  - entidad/privada
  - agencia-digital
  - numen
  - redes-sociales
  - cerimedo
---

# Numen Publicidad SpA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador / Fundador**: [[Fernando Cerimedo]] (junto a socios locales chilenos)

## Contexto en Investigaciones y Electorales
Filial chilena de la agencia de marketing digital fundada por el estratega argentino [[Fernando Cerimedo]]. La entidad operó en Chile realizando sondeos de opinión pública digital y coordinando campañas de difusión y posicionamiento en redes sociales durante los ciclos electorales de 2020 a 2022.

En el marco del [[Caso Operaciones Digitales e Injerencia Electoral]], la sociedad y sus cuentas bancarias e infraestructura informática han sido objeto de oficios del Congreso y requerimientos de la Fiscalía Centro Norte para verificar la trazabilidad de fondos, la ausencia de facturación en las rendiciones de partidos ante el Servel y la eventual prestación de servicios mediante redes automatizadas en la campaña del Plebiscito de 2022.

## Registros Reificados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito Imputado"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [El día que el 'rey de los trolls' llegó a la sede de RN](https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/) | The Clinic | `secundaria` | 2026-08-28 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2026/08/28/el-dia-que-el-rey-de-los-trolls-llego-a-la-sede-de-rn-la-viralizada-foto-con-cerimedo-que-reunio-a-figuras-ligadas-a-la-udi-parisi-y-el-actual-segundo-piso/) |
| [Fiscalía Centro Norte abre investigación por presuntos delitos informáticos vinculados a Fernando Cerimedo](https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/) | CNN Chile | `secundaria` | 2026-09-03 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/fiscalia-centro-norte-abre-investigacion-por-presuntos-delitos-informaticos-vinculados-a-fernando-cerimedo/) |
| [Fiscalía Centro Norte abre investigación por eventual intervención de Cerimedo en procesos electorales](https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html) | Pauta | `secundaria` | 2026-09-04 | [Wayback ↺](https://web.archive.org/web/*/https://www.pauta.cl/actualidad/2026/09/04/fiscalia-centro-norte-abre-investigacion-por-eventual-intervencion-de-fernando-cerimedo-en-procesos-electorales-en-chile.html) |
| [Julgamento no STF: quem foi indiciado mas não deve ser julgado](https://apublica.org/2025/09/julgamento-stf-quem-foi-indiciado-mas-nao-deve-ser-julgado/) | Agência Pública | `secundaria` | 2025-09-01 | [Wayback ↺](https://web.archive.org/web/*/https://apublica.org/2025/09/julgamento-stf-quem-foi-indiciado-mas-nao-deve-ser-julgado/) |
