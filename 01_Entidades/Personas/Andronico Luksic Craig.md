---
tipo_nodo: persona
rut: "5.781.429-2"
aliases:
  - "Andrónico Luksic"
  - "Andrónico Luksic Craig"
rol_principal: "Empresario y Ex Presidente del Holding Quiñenco S.A. y Banco de Chile"
afiliacion_politica: "Independiente"
situacion_procesal: ninguna
medida_cautelar: "Sin medidas cautelares ni procesos judiciales vigentes (Mención indirecta de terceros en archivos Epstein descartada sin contacto)"
tags:
  - entidad/persona
  - empresario
  - quinenco
  - caso-caval
  - epstein-files
---

# Andronico Luksic Craig

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense y Auditoría de Menciones
Empresario chileno, ex líder del consorcio empresarial Quiñenco S.A. y figura central del sector financiero y minero en Chile. Su registro en esta bóveda forense abarca dos dimensiones diferenciadas:

1. **Auditoría de Desclasificaciones Judiciales del Caso Epstein (`Mención Indirecta de Terceros / Sin Imputación`)**:
   - En las desclasificaciones masivas de correos del tribunal federal de Nueva York (SDNY) relativas a Jeffrey Epstein ([[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]), su nombre figura de manera incidental en un correo electrónico enviado por el empresario emiratí Sultan Ahmed bin Sulayem (presidente de *DP World*) a Epstein.
   - En dicho mensaje, Bin Sulayem adjuntó el currículum de Luksic y consultó: *«¿Sabes algo sobre este tipo?»*, en el marco de la coordinación protocolar de una reunión comercial en Dubái con ejecutivos de *DP World*.
   - **Conclusión pericial**: Los registros desclasificados **no contienen ninguna evidencia de que haya existido una reunión, llamada o comunicación directa entre Luksic y Epstein**, descartándose cualquier relación ilícita o societaria ([[TRX-2015-11-14-Mencion-Indirecta-Epstein-BinSulayem-Luksic-01]]). Luksic desmintió públicamente cualquier vínculo.

2. **Antecedentes en el Grafo Nacional (`Caso Caval`)**:
   - En el ámbito corporativo nacional, en noviembre de 2013 sostuvo en la casa matriz del banco una reunión con [[Natalia Compagnon Soto]] y Sebastián Dávalos Bachelet en el marco de la tramitación de un crédito por `$6.500.000.000 CLP` solicitado por [[Exportadora y de Gestion Caval Ltda]] para la compra de terrenos en Machalí, arista investigada en el [[Caso Caval]] donde prestó declaración en calidad de testigo sin formulación de cargos penales en su contra.

## Auditoría Contable: Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Monto (CLP)", "Causa / Ámbito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
