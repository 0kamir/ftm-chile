---
tipo_nodo: persona
rut: ""
aliases:
  - "Jozo Santic"
  - "Coronel Jozo Santic Palomino"
rol_principal: "Ex Coronel Jefe de Finanzas del Comando de Apoyo a la Fuerza (CAF)"
afiliacion_politica: "Independiente"
situacion_procesal: condenado
medida_cautelar: "Condenado en primera instancia a 13 años por la ministra Romy Rutherford; la Corte Marcial revocó la condena por fraude al fisco en la arista Tecnodata II"
estado_verificacion: parcial
fuentes:
  - url: "https://vlex.cl/vid/corte-marcial-revoca-condena-844999287"
    titulo: "Corte Marcial revoca condena por fraude a general (r) Santic"
    medio: "vLex Chile"
    tipo: secundaria
    consultado: 2026-10-19
alertas_verificacion:
  - "La Corte Marcial revocó su condena por fraude al fisco en la arista Tecnodata II; verificar si su situación es 'condenado' en otras aristas."
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

## Síntesis Forense
Ex Coronel del Ejército de Chile a cargo del área de finanzas en el [[Comando de Apoyo a la Fuerza del Ejercito]]. Fue condenado en el [[Caso Milicogate]] como pieza clave del pago de facturas ideológicamente falsas a proveedores como [[Frasim Ltda]] con cargo a la Ley Reservada del Cobre ([[TRX-2014-05-20-Facturas-LeyReservadaCobre-01]]), documentado en [[Procesamientos-Ministra-Rutherford-Milicogate]].

## Auditoría Contable: Montos Operados como Firmante de Destino
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
