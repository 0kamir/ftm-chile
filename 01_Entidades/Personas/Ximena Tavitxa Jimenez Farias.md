---
tipo_nodo: persona
rut: ""
aliases: []
rol_principal: "Imputada en la Operación Tributos; ex candidata a consejera regional"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: ""
historial_correcciones:
  - "Nombre y rol corregidos el 2026-10-19 según el listado publicado por la prensa; RUT eliminado por no constar en fuente pública."
estado_verificacion: parcial
fuentes:
  - "https://www.latercera.com/la-tercera-pm/noticia/expediente-secreto-del-sii-como-funcionaba-los-seis-clanes-que-crearon-el-mecanismo-del-fraude-tributario-mas-grande-de-la-historia/I4RBDAJD2JEZZJLGXGIDE7ZR6A/"
  - "https://www.latercera.com/nacional/noticia/el-listado-de-los-55-imputados-por-el-megafraude-tributario/JEH5YAOVRJHAPMLM5UIGN3N4CM/"
  - "https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml"
  - "https://www.latercera.com/nacional/noticia/megafraude-tributario-clan-de-pavez-canessa-vendia-facturas-falsas-y-contaba-con-un-notario-suplente-en-la-organizacion/552EKQIRDRFKBNGSSO2I3L2N3I/"
  - "https://cooperativa.cl/noticias/pais/judicial/denuncias-de-corrupcion/caso-tributos-fiscalia-pide-prision-preventiva-para-26-empresarios/2023-12-18/164214.html"
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - grupo-megafraude
---

# Ximena Tavitxa Jimenez Farias

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis
Figura en el listado de 55 imputados formalizados en diciembre de 2023 en el [[Caso Megafraude Tributario Operacion Tributos]]. Según La Tercera, la Fiscalía la señala como testaferra del denominado 'Clan Galaz' ([[Juan Victor Galaz Rojas]]); fue candidata a consejera regional por el Partido Republicano en 2021. Rige la presunción de inocencia: la causa no tiene sentencia.

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
| [Expediente secreto del SII: cómo funcionaban los seis clanes del fraude tributario](https://www.latercera.com/la-tercera-pm/noticia/expediente-secreto-del-sii-como-funcionaba-los-seis-clanes-que-crearon-el-mecanismo-del-fraude-tributario-mas-grande-de-la-historia/I4RBDAJD2JEZZJLGXGIDE7ZR6A/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/la-tercera-pm/noticia/expediente-secreto-del-sii-como-funcionaba-los-seis-clanes-que-crearon-el-mecanismo-del-fraude-tributario-mas-grande-de-la-historia/I4RBDAJD2JEZZJLGXGIDE7ZR6A/) |
| [El listado de los 55 imputados por el megafraude tributario](https://www.latercera.com/nacional/noticia/el-listado-de-los-55-imputados-por-el-megafraude-tributario/JEH5YAOVRJHAPMLM5UIGN3N4CM/) | La Tercera | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/el-listado-de-los-55-imputados-por-el-megafraude-tributario/JEH5YAOVRJHAPMLM5UIGN3N4CM/) |
| [SII confirma que 55 empresarios detenidos concretaron el mayor fraude de la historia contra el fisco](https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml) | BioBioChile | `secundaria` | 2023-12-15 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2023/12/15/sii-confirma-que-55-empresarios-detenidos-concretaron-el-mayor-fraude-de-la-historia-contra-el-fisco.shtml) |
| [Megafraude tributario: clan Pavez Canessa vendía facturas falsas](https://www.latercera.com/nacional/noticia/megafraude-tributario-clan-de-pavez-canessa-vendia-facturas-falsas-y-contaba-con-un-notario-suplente-en-la-organizacion/552EKQIRDRFKBNGSSO2I3L2N3I/) | La Tercera | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.latercera.com/nacional/noticia/megafraude-tributario-clan-de-pavez-canessa-vendia-facturas-falsas-y-contaba-con-un-notario-suplente-en-la-organizacion/552EKQIRDRFKBNGSSO2I3L2N3I/) |
| [Caso Tributos: Fiscalía pide prisión preventiva para 26 empresarios](https://cooperativa.cl/noticias/pais/judicial/denuncias-de-corrupcion/caso-tributos-fiscalia-pide-prision-preventiva-para-26-empresarios/2023-12-18/164214.html) | Cooperativa | `secundaria` | 2023-12-18 | [Wayback ↺](https://web.archive.org/web/*/https://cooperativa.cl/noticias/pais/judicial/denuncias-de-corrupcion/caso-tributos-fiscalia-pide-prision-preventiva-para-26-empresarios/2023-12-18/164214.html) |
