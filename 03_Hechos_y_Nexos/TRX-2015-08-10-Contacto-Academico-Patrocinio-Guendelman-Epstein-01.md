---
tipo_nodo: nexo_transaccion
fecha: 2015-08-10
tipo_nexo: solicitud_patrocinio
monto_clp: 0
entidad_origen: "[[Corte Suprema de Chile]]"
entidad_destino: "[[Corte Suprema de Chile]]"
firmante_origen: "[[Eduardo Guendelman Israel]]"
firmante_destino: "[[Eduardo Guendelman Israel]]"
causa_vinculada: "[[Caso Archivos Epstein Menciones Chile]]"
delito_imputado: "[[Trafico de Influencias]]"
evidencia_soporte: "[[Desclasificacion-Documentos-DOJ-CasoEpstein-2024]]"
tags:
  - nexo/desclasificacion
  - epstein-files
  - intercambio-academico
  - no-materializado
---

# TRX-2015-08-10-Contacto-Academico-Patrocinio-Guendelman-Epstein-01

## Ficha de Arista Reificada (Auditoría de Desclasificación / Solicitud Científica No Materializada)
- **Período de Mensajería**: `= this.fecha` *(Correspondencia entre 2015 y 2019)*
- **Tipo de Registro**: `= this.tipo_nexo` *(Intercambio epistolar estrictamente académico para financiamiento científico)*
- **Monto Imputado (CLP)**: `$`= regexreplace(string(this.monto_clp), "\B(?=(\d{3})+(?!\d))", ".")`` *(Donación no concretada / $0 CLP transferidos)*
- **Ámbito Institucional de Verificación**: `= this.entidad_origen`
- **Académico Solicitante**: `= this.firmante_origen`
- **Causa / Expediente Asociado**: `= this.causa_vinculada`
- **Ámbito Tipológico Evaluado**: `= this.delito_imputado` *(Descarte de cualquier conducta ilícita)*
- **Evidencia Soporte**: `= this.evidencia_soporte`

## Descripción Forense del Registro
La investigación de la Unidad de Investigación de *BioBioChile* sobre los correos desclasificados por el Departamento de Justicia de EE. UU. (DOJ) identificó que el físico teórico chileno-israelí [[Eduardo Guendelman Israel]] mantuvo correspondencia con Jeffrey Epstein entre 2015 y 2019 con el propósito de recabar aportes filantrópicos para organizar conferencias de física y un centro de investigación en las Bahamas.

**Determinación Forense**:
Los fondos solicitados nunca llegaron a transferirse ni a materializarse. El vínculo fue estrictamente epistolar y de carácter científico-académico, sin vinculación alguna con las actividades delictivas investigadas en la causa penal.
