---
tipo_nodo: persona
rut: ""
aliases:
  - "Gonzalo Blu"
  - "Gonzalo Blu Rodríguez"
rol_principal: "Ex General Inspector y Ex Director Nacional de Inteligencia, Drogas e Investigación Criminal de Carabineros"
afiliacion_politica: "Militar / Carabineros"
situacion_procesal: condenado
medida_cautelar: "Condenado a 5 años de presidio (libertad vigilada intensiva) por el TOP de Temuco — sentencia no firme: recursos de nulidad pendientes (2026)"
tags:
  - entidad/persona
  - caso-operacion-huracan
  - dipolcar
  - carabineros
  - condenado
---

# Gonzalo Blu Rodriguez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Direccion de Inteligencia Policial de Carabineros]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Condena Ejecutoriada / Cautelar**: `= this.medida_cautelar`

## Síntesis Forense
General inspector de Carabineros que ejerció como Director Nacional de Inteligencia, Drogas e Investigación Criminal. Fue el máximo responsable policial que validó institucionalmente ante el Gobierno y la Fiscalía los informes fraudulentos de la UIOE en la [[Caso Operacion Huracan]], defendiendo públicamente la eficacia del software «Antorcha» desarrollado por [[Alex Smith Leay]]. 

Tras destaparse la falsificación por parte de los peritajes de la PDI ([[Peritaje-Cibercrimen-PDI-SoftwareAntorcha-2018]]), fue dado de baja y formalizado por el Ministerio Público. En el juicio oral ante el Tribunal de Juicio Oral en lo Penal de Temuco ([[Sentencia-TOP-Temuco-OperacionHuracan-2026]]) fue condenado a **5 años de presidio** menor en su grado máximo por [[Falsificacion de Instrumento Publico]] y [[Obstruccion a la Investigacion]].

## Auditoría Contable: Registros Reificados
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

dv.header(4, `Monto Total Autorizado / Imputado: ${formattedTotal}`);
dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Monto (CLP)", "Delito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.delito_imputado
  ])
);
```
