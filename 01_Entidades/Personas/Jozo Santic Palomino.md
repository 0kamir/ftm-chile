---
tipo_nodo: persona
rut: ""
aliases:
  - "Jozo Santic"
  - "Coronel Jozo Santic Palomino"
rol_principal: "Ex Coronel Jefe de Finanzas del Comando de Apoyo a la Fuerza (CAF)"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condenado por la Corte Marcial (arista Tecnodata II) a 5 años y un día de presidio efectivo por falsedad en materia de administración militar; en primera instancia (nov-2019) la ministra Rutherford le había impuesto 10 años y un día y 3 años y un día"
historial_correcciones:
  - "Corregido el 2026-10-19: la Corte Marcial no revocó su condena, la redujo a 5 años y un día (falsedad); se descartó la condena por fraude al fisco."
estado_verificacion: verificado
fuentes:
  - "https://vlex.cl/vid/corte-marcial-revoca-condena-844999287"
  - "https://www.elciudadano.com/?p=683869"
  - "https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html"
  - "https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/"
tags:
  - entidad/persona
  - caso-milicogate
  - condenado
---

# Jozo Santic Palomino

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Comando de Apoyo a la Fuerza del Ejercito]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis
Ex Coronel del Ejército de Chile a cargo del área de finanzas en el [[Comando de Apoyo a la Fuerza del Ejercito]]. Fue condenado en el [[Caso Milicogate]] como pieza clave del pago de facturas ideológicamente falsas a proveedores como [[Frasim Ltda]] con cargo a la Ley Reservada del Cobre ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]), documentado en [[Procesamientos-Ministra-Rutherford-Milicogate]].

## Montos Operados como Firmante de Destino
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

dv.header(4, `Monto Total Operado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Repartición", "Proveedor", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
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
| [Corte Marcial revoca condena por fraude a general (r) Santic](https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) | vLex Chile | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://vlex.cl/vid/corte-marcial-revoca-condena-844999287) |
| [Fraude en el Ejército: Corte Marcial disminuye condenas a cuatro uniformados](https://www.elciudadano.com/?p=683869) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=683869) |
| [Procesan a general (r) por defraudar al fisco con cerca de 1.800 millones](https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) | Cooperativa | `secundaria` | 2018-02-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.cooperativa.cl/noticias/site/artic/20180211/pags-amp/20180211185247.html) |
| [Los documentos secretos del Milicogate](https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) | The Clinic | `secundaria` | 2015-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2015/08/18/los-documentos-secretos-del-milicogate/) |
