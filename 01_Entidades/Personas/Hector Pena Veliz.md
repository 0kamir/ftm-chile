---
tipo_nodo: persona
rut: ""
aliases: []
rol_principal: "Dueño de la consultora Gestión Ambiental y Territorial S.A. (GATE)"
afiliacion_politica: "Partido Socialista (según la prensa)"
situacion_procesal: condenado
medida_cautelar: "Condenado a 61 días de presidio por fraude al fisco; confirmado por la Corte Suprema (29-06-2016)"
estado_verificacion: verificado
fuentes:
  - url: "https://www.emol.com/noticias/Nacional/2016/06/29/810116/Corte-Suprema-dicta-sentencia-definitiva-en-el-caso-Mop-Gate-y-confirma-condenas.html"
    titulo: "Corte Suprema dicta sentencia definitiva en el caso MOP-Gate y confirma condenas"
    medio: "Emol"
    tipo: secundaria
    fecha: 2016-06-29
    consultado: 2026-10-19
  - url: "https://cooperativa.cl/noticias/pais/judicial/mop-sobresueldos/corte-de-apelaciones-ratifico-condenas-en-el-caso-mop-g/2014-08-12/113714.html"
    titulo: "Corte de Apelaciones ratificó condenas en el caso MOP-Gate"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2014-08-12
    consultado: 2026-10-19
historial_correcciones:
  - "Reemplaza a 'Roberto Lewin Valdivieso', persona sin respaldo en fuentes (2026-10-19)."
tags:
  - entidad/persona
  - caso-mop-gate
  - condenado
---

# Hector Pena Veliz

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Gestion Ambiental y Territorial SA]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Condena Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Dueño de la consultora [[Gestion Ambiental y Territorial SA]] (GATE). En el [[Caso MOP-Gate]] fue condenado como autor de [[Fraude al Fisco]] a 61 días de presidio, condena confirmada por la Corte de Apelaciones de Santiago (2014) y por la [[Corte Suprema de Chile]] el 29 de junio de 2016 ([[Sentencia-Corte-Suprema-MOPGate-2016]]), por los contratos con el [[Ministerio de Obras Publicas]] cuyos fondos se usaron para pagar sobresueldos ([[TRX-2001-08-20-Contratos-Simulados-MOP-GATE-01]]).

## Auditoría Contable: Montos Operados como Firmante
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

dv.header(4, `Monto Total Operado en Nexos: ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Origen", "Destino", "Monto (CLP)", "Causa"],
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
  elink(f.url, f.titulo) AS "Fuente",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  choice(f.archivo, elink(f.archivo, "copia"), "—") AS "Archivo"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
