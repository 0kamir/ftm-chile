---
tipo_nodo: persona
rut: "6.849.201-7"
aliases:
  - "Andrés Velasco"
  - "Andrés Velasco Brañes"
rol_principal: "Economista, Ex Ministro de Hacienda (2006–2010) y Decano de la Escuela de Políticas Públicas de LSE"
afiliacion_politica: "Independiente (Ex precandidato presidencial y fundador de Fuerza Pública / Ciudadanos)"
situacion_procesal: ninguna
medida_cautelar: "Sin medidas cautelares ni procesos judiciales vigentes (Sobreseído definitivamente en Caso Penta; mención referencial de terceros en archivos Epstein sin contacto acreditado)"
tags:
  - entidad/persona
  - ex-ministro
  - economista
  - epstein-files
---

# Andres Velasco Branes

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense y Auditoría de Menciones
Economista y académico chileno, ministro de Hacienda durante el primer gobierno de Michelle Bachelet (2006–2010), excandidato presidencial en las primarias de 2013 y actual decano de la Escuela de Políticas Públicas de la London School of Economics (LSE). Su registro en esta bóveda forense analiza dos antecedentes verificados:

1. **Auditoría de Desclasificaciones Judiciales del Caso Epstein (`Mención Referencial de Terceros / Sin Imputación`)**:
   - En los archivos desclasificados por el Departamento de Justicia de EE. UU. ([[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]), su nombre figura en una comunicación remitida por el escritor y curador británico Adrian Dannatt a un destinatario no identificado, con el asunto *«Future President of Chile etc.»*.
   - El mensaje describe a Velasco como un *«brillante economista y profesor de Harvard»* y menciona informalmente una cena o encuentro en Londres en el marco de su precandidatura presidencial de 2013 para reunir adherentes en el extranjero.
   - **Conclusión pericial**: Los antecedentes del tribunal estadounidense **no acreditan ninguna interacción, correo directo, reunión, aporte financiero ni vínculo societario entre Andrés Velasco y Jeffrey Epstein** ([[TRX-2013-05-20-Mencion-Referencial-Epstein-Dannatt-Velasco-01]]), tratándose estrictamente de un comentario social de un tercero sobre política internacional.

2. **Antecedentes en el Grafo Nacional (`Caso Penta / Sobreseimiento Definitivo`)**:
   - En el [[Caso Penta]], el Ministerio Público investigó aportes de campaña vinculados a un almuerzo profesional sostenido con los controladores de [[Empresas Penta SA]] ([[Carlos Alberto Delano Abbott]] y [[Carlos Eugenio Lavin Garcia-Huidobro]]). Tras la investigación judicial, los tribunales decretaron el **sobreseimiento definitivo** a su favor, acreditándose la inexistencia de delito tributario o financiamiento ilegal en su actuación.

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
