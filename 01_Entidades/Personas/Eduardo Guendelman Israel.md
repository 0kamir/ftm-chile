---
tipo_nodo: persona
rut: "5.619.384-7"
aliases:
  - "Eduardo Guendelman"
  - "Eduardo I. Guendelman"
rol_principal: "Doctor en Física Teórica y Profesor Emérito del Departamento de Física de la Universidad Ben-Gurión del Néguev"
afiliacion_politica: "Independiente"
situacion_procesal: ninguna
medida_cautelar: "Sin medidas cautelares ni investigaciones penales vigentes (Correspondencia estrictamente académica para patrocinio científico no materializado)"
tags:
  - entidad/persona
  - academico
  - fisica-teorica
  - epstein-files
---

# Eduardo Guendelman Israel

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense y Auditoría de Menciones
Científico chileno-israelí, doctor en Física por la Universidad de California, Berkeley, y profesor emérito del Departamento de Física de la Universidad Ben-Gurión del Néguev (Israel), especializado en cosmología teórica, teoría de cuerdas y física de partículas. Su registro en esta bóveda forense se incorpora con fines de contextualización pericial rigurosa:

1. **Correspondencia Epistolar Directa en Desclasificaciones Epstein (`Búsqueda de Patrocinio Científico / Sin Delito`)**:
   - Una investigación de la Unidad de Investigación de *BioBioChile* sobre los correos desclasificados por el Departamento de Justicia de EE. UU. ([[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]) acreditó que el profesor Guendelman mantuvo un intercambio de correos electrónicos con Jeffrey Epstein entre 2015 y 2019.
   - **Objetivo de las comunicaciones**: Las gestiones tuvieron como fin exclusivo solicitar financiamiento filantrópico para organizar una conferencia académica internacional de física teórica e impulsar un instituto científico en las Bahamas. Este tipo de contactos era habitual en el circuito universitario internacional, dado que fundaciones vinculadas a Epstein donaron millones de dólares a departamentos de ciencias y matemáticas de instituciones como Harvard y el MIT.
   - **Conclusión pericial**: La propia evidencia desclasificada demuestra que **las donaciones y proyectos solicitados nunca se llegaron a concretar ni transferir** ([[TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01]]). La relación fue estrictamente epistolar y circunscrita al ámbito científico, sin existir ninguna imputación penal, sospecha delictual ni vínculo con actividades ilícitas.

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
