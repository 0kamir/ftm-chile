---
tipo_nodo: persona
rut: ""
aliases:
  - "Eliodoro Matte"
  - "Eliodoro Matte Larraín"
rol_principal: "Ex Presidente del Directorio de Empresas CMPC S.A. y Patriarca del Grupo Matte"
afiliacion_politica: "Independiente (Vinculado a centros de pensamiento de centroderecha / CEP)"
situacion_procesal: descarte_procesal_sin_imputacion
medida_cautelar: "Renuncia obligada a la presidencia de CMPC en abril de 2016 tras estallar el Cartel del Confort"
estado_verificacion: verificado
fuentes:
  - "https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html"
  - "https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml"
  - "https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html"
  - "https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html"
tags:
  - entidad/persona
  - empresario
  - grupo-matte
  - cmpc
  - caso-colusion-tissue
---

# Eliodoro Matte Larrain

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Empresas CMPC SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Consecuencia Institucional**: `= this.medida_cautelar`

## Síntesis
Ingeniero civil industrial, empresario y cabeza histórica del Grupo Matte, uno de los conglomerados económicos más influyentes del país (con intereses en el sector forestal, financiero y energético) y expresidente del Centro de Estudios Públicos (CEP). 

Ejerció la presidencia del directorio de [[Empresas CMPC SA]] durante todo el período en que operó el cartel del papel tissue (2000–2015). Al hacerse pública la delación compensada y el requerimiento de la [[Fiscalia Nacional Economica]] en octubre de 2015, afirmó inicialmente desconocer las prácticas colusorias de la plana ejecutiva; no obstante, la gravedad del escándalo de colusión coordinada con [[SCA Chile SA]] ([[TRX-2000-05-15-Pacto-Colusion-Precios-Cuotas-CMPC-PISA-01]]) forzó su renuncia indeclinable a la presidencia de la compañía en abril de 2016, tras lo cual la papelera suscribió el acuerdo indemnizatorio histórico con el [[Servicio Nacional del Consumidor]] ([[TRX-2017-03-03-Compensacion-Historica-Consumidores-CMPC-SERNAC-01]]).

## Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Asociado a Entidades Controladas: ${formattedTotal}`);
dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [TDLC dicta sentencia en caso Tissue](https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) | Emol | `secundaria` | 2017-12-29 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/12/29/889225/TDLC-dicta-sentencia-en-caso-Tissue-Multa-a-SCA-con-US18-millones-y-exime-a-CMPC.html) |
| [Suprema condena a CMPC y SCA por colusión](https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) | Emol | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2020/01/06/972511/Suprema-condena-CMPC-SCA-colusion.html) |
| [CMPC tendrá que pagar una millonaria multa por la colusión del papel](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) | BioBioChile | `secundaria` | 2020-01-06 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2020/01/06/cmpc-tendra-que-pagar-una-millonaria-multa-por-la-colusion-del-papel.shtml) |
| [Acuerdo por colusión tissue: CMPC pagará US$150 millones para compensar a consumidores](https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) | Emol | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.emol.com/noticias/Economia/2017/01/27/842148/Acuerdo-por-colusion-tissue-CMPC-pagara-US150-millones-para-compensar-a-consumidores.html) |
| [CMPC pagará compensación de 150 millones de dólares: por consumidor serán 7.000 pesos](https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) | Cooperativa | `secundaria` | 2017-01-27 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20170127/pags-amp/20170127103630.html) |
