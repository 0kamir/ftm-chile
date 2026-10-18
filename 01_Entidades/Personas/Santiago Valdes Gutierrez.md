---
tipo_nodo: persona
rut: "8.412.935-6"
aliases:
  - "Santiago Valdés"
rol_principal: "Ex Gerente de Administración y Finanzas de Bancard y Administrador Electoral Campaña Presidencial 2009"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: formalizado
medida_cautelar: "Formalizado por delitos tributarios reiterados en Caso SQM / Penta (sobreseído tras contienda de rectificatorias y prescripción parcial)"
tags:
  - entidad/persona
  - caso-sqm
  - caso-penta
  - caso-exalmar
  - bancard
---

# Santiago Valdes Gutierrez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal` ([[Bancard Inversiones Ltda]])
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Ingeniero comercial, hombre de confianza financiera de [[Sebastian Pinera Echenique]], gerente de administración y finanzas de [[Bancard Inversiones Ltda]] y administrador electoral de la campaña presidencial de Piñera en 2009. En el [[Caso SQM]] y el [[Caso Penta]], tras querellas y denuncias del [[Servicio Impuestos Internos]], fue formalizado ante el 8° Juzgado de Garantía de Santiago por delitos tributarios reiterados tras acreditarse la emisión de facturas ideológicamente falsas desde [[Bancard Inversiones Ltda]] y empresas proveedoras hacia [[SQM SA]] (autorizadas por [[Patricio Contesse Gonzalez]]) y *Aguas Andinas* por **$340.000.000 CLP** para financiar gastos de la campaña presidencial de 2009 ([[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]]). Asimismo, participó en la ejecución de las inversiones *offshore* de *Bancard International Investment Inc.* en la pesquera peruana *Exalmar S.A.* en el [[Caso Exalmar y Fideicomiso Ciego]] ([[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]]).

## Auditoría Contable: Montos Operados en Aristas Reificadas
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

dv.header(4, `Monto Total Asociado: ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
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
