---
tipo_nodo: persona
rut: ""
aliases:
  - "Alberto Larraín"
  - "Alberto Larraín Salas"
rol_principal: "Cofundador y Director Ejecutivo de Fundación ProCultura"
afiliacion_politica: "Independiente (Ex DC / Cercano Frente Amplio)"
situacion_procesal: formalizado
medida_cautelar: "Formalizado en arista RM (fraude al fisco, feb-2026) y arista Biobío (apropiación indebida, 05-08-2026, con arraigo nacional)"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html"
  - "https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml"
  - "https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/"
  - "https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/"
  - "https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/"
  - "https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html"
tags:
  - entidad/persona
  - caso-convenios
  - procultura
---

# Alberto Larrain Salas

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Fundacion ProCultura]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Médico psiquiatra y director ejecutivo de [[Fundacion ProCultura]]. En el marco del [[Caso Convenios]], suscribió convenios multirregionales tanto con la [[Seremi MINVU Antofagasta]] dirigida por [[Carlos Contreras Gutierrez]] ([[TRX-2022-10-28-Convenio-ProCultura-Antofagasta]]) como con el [[GORE Biobio]] dirigido por [[Rodrigo Diaz Worner]] ([[TRX-2022-11-18-Convenio-ProCultura-Biobio]]), actuando como **conector interregional** en el grafo.

## Montos Recibidos como Firmante de Destino
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && (
    p.firmante_destino.path === dv.current().file.path ||
    String(p.firmante_destino).includes(dv.current().file.name)
  ));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Suscrito (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Firmante Origen", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    p.firmante_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Alberto Larraín fue formalizado por la arista Biobío del caso ProCultura](https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) | Cooperativa | `secundaria` | 2026-08-05 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/pais/judicial/casos-emblematicos/alberto-larrain-fue-formalizado-por-la-arista-biobio-del-caso-procultura/2026-08-05/232613.html) |
| [Caso Democracia Viva: contratos evitaron revisión de Contraloría al ser pagados de forma parcializada](https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) | BioBioChile | `secundaria` | 2023-06-22 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2023/06/22/caso-democracia-viva-contratos-evitaron-revision-de-contraloria-al-ser-pagados-de-forma-parcializada.shtml) |
| [Tras informe sobre Democracia Viva, contralor afirma que hubo corrupción](https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) | La Tercera | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/tras-informe-sobre-democracia-viva-contralor-afirma-que-hubo-corrupcion-y-asegura-que-es-imposible-que-se-restituyan-los-dineros/YBJ555PO75H6FPOLMU5HOOF7KM/) |
| [Democracia Viva: Daniel Andrade y Carlos Contreras quedan en prisión preventiva](https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/democracia-viva-daniel-andrade-y-carlos-contreras-quedan-en-prision-preventiva/MKEUFESDTNEEZL44JWIARZAADM/) |
| [Formalización de Daniel Andrade y Carlos Contreras: delitos y convenios Minvu Antofagasta](https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) | CNN Chile | `secundaria` | 2023-12-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/formaliacion-daniel-andrade-carlos-contreras-caso-convenios-delitos-minvu-antofagasta/) |
| [Contraloría publica informe sobre Democracia Viva y faltas a la probidad](https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) | Emol | `secundaria` | 2023-08-31 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Nacional/2023/08/31/1105868/contraloria-informe-democracia-viva-probidad.html) |
