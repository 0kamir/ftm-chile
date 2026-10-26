---
tipo_nodo: persona
rut: ""
aliases:
  - "Juan Miguel Fuente-Alba"
  - "General Fuente-Alba"
rol_principal: "Ex Comandante en Jefe del Ejército de Chile (2010-2014)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Procesado por malversación de gastos reservados (Justicia Militar / Ordinaria)"
estado_verificacion: verificado
fuentes:
  - "https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html"
  - "https://vlex.cl/vid/corte-marcial-revoca-condena-844999287"
  - "https://www.elciudadano.com/?p=683869"
  - "https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/"
tags:
  - entidad/persona
  - caso-milicogate
  - ejercito
---

# Juan Miguel Fuente-Alba Poblete

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Comando de Apoyo a la Fuerza del Ejercito]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
General de Ejército (r) y Comandante en Jefe entre 2010 y 2014. Fue sometido a proceso por la Ministra en Visita Romy Rutherford ([[Procesamientos-Ministra-Rutherford-Milicogate]]) en el [[Caso Milicogate]] por [[Malversacion de Caudales Publicos]] de gastos reservados y juzgado en la justicia ordinaria por [[Lavado de Activos]]. Durante su período de mando ocurrió además el fraude con fondos de la Ley Reservada del Cobre investigado en el Milicogate en el [[Comando de Apoyo a la Fuerza del Ejercito]] ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]).

## Montos Asociados como Mando de Origen
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && (
    p.firmante_origen.path === dv.current().file.path ||
    String(p.firmante_origen).includes(dv.current().file.name)
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

dv.header(4, `Monto Total Asociado (firmante_origen): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Repartición", "Operador Destino", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.firmante_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Procesan a general (r) por defraudar al fisco con cerca de 1.800 millones](https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) | Cooperativa | `secundaria` | 2018-02-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) |
| [Corte Marcial revoca condena por fraude a general (r) Santic](https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) | vLex Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) |
| [Fraude en el Ejército: Corte Marcial disminuye condenas a cuatro uniformados](https://www.elciudadano.com/?p=683869) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=683869) |
| [Los documentos secretos del Milicogate](https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) | The Clinic | `secundaria` | 2015-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) |
