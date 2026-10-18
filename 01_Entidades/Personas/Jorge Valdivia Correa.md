---
tipo_nodo: persona
rut: "14.289.310-K"
aliases:
  - "Jorge Valdivia"
  - "Jorge Valdivia Correa"
rol_principal: "Representante Legal de Consultora Gestión Pública SpA"
afiliacion_politica: "Independiente"
situacion_procesal: ninguna
medida_cautelar: ""
tags:
  - entidad/persona
  - compras-publicas
  - proveedor
---

# Jorge Valdivia Correa

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Consultora Gestion Publica SpA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal` *(Sujeto de interés en auditoría OSINT desformalizada)*
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Administrador y socio representante de [[Consultora Gestion Publica SpA]]. Registra la suscripción del trato directo [[TRX-2023-08-14-Trato-Directo-ChileCompra-01]] con [[Direccion ChileCompra]] por **$45.800.000 CLP**, respaldado por [[Orden-Compra-MercadoPublico-2023]] y analizado preventivamente en [[Caso Compras Publicas]] sin formalización judicial vigente (`situacion_procesal: ninguna`).

## Auditoría Contable: Montos Suscritos como Proveedor (`firmante_destino`)
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

dv.header(4, `Monto Total Adjudicado (firmante_destino): ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Órgano Comprador", "Sociedad", "Monto (CLP)", "Causa"],
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
