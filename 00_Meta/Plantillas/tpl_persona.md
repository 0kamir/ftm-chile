---
tipo_nodo: persona
rut: ""
aliases: []
rol_principal: ""
afiliacion_politica: ""
situacion_procesal: ninguna # formalizado | testigo | condenado | ninguna
medida_cautelar: ""
vinculos_familiares: [] # Lista de wikilinks a parientes/afines: ["[[Nombre Apellido]]"]
estado_verificacion: pendiente # verificado | parcial | desactualizado | sin_fuente | pendiente
fuentes:
  - "https://"
tags:
  - entidad/persona
---

# {{title}}

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Auditoría Financiera (Aristas Reificadas)

### Como Firmante de Origen (Autorizador / Emisor)
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_origen && p.firmante_origen.path === dv.current().file.path);

let total = 0;
for (let p of pages) {
  total += Number(p.monto_clp || 0);
}

const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP' }).format(total);
dv.paragraph(`**Total autorizado como firmante de origen:** ${fmt} (${pages.length} registros)`);

if (pages.length > 0) {
  dv.table(
    ["Nexo / Transacción", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
    pages.sort(p => p.fecha, 'desc').map(p => [
      p.file.link,
      p.fecha,
      p.entidad_origen,
      p.entidad_destino,
      new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP' }).format(Number(p.monto_clp || 0)),
      p.causa_vinculada
    ])
  );
}
```

### Como Firmante de Destino (Receptor / Contraparte)
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => p.firmante_destino && p.firmante_destino.path === dv.current().file.path);

let total = 0;
for (let p of pages) {
  total += Number(p.monto_clp || 0);
}

const fmt = new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP' }).format(total);
dv.paragraph(`**Total suscrito como firmante de destino:** ${fmt} (${pages.length} registros)`);

if (pages.length > 0) {
  dv.table(
    ["Nexo / Transacción", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
    pages.sort(p => p.fecha, 'desc').map(p => [
      p.file.link,
      p.fecha,
      p.entidad_origen,
      p.entidad_destino,
      new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP' }).format(Number(p.monto_clp || 0)),
      p.causa_vinculada
    ])
  );
}
```

## Notas e Hitos Procesales
- 

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Título del documento o nota](https://) | Medio | `primaria` | YYYY-MM-DD | [copia](https://web.archive.org/) |
