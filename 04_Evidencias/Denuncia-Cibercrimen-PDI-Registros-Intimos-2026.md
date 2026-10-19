---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-PDI-CIBERCRIMEN-REGISTROS-FLORES-2026"
tipo_documento: "Denuncia Penal y Parte Policial de la Brigada del Cibercrimen por Difusión No Consentida de Registros Íntimos"
fecha_emision: 2026-06-15
organismo_emisor: "[[Direccion de Inteligencia Policial de Carabineros]]"
fuente_osint: "Policía de Investigaciones de Chile (investigaciones.cl) / Fiscalía de Chile"
causa_vinculada: "[[Caso Asignaciones Parlamentarias y Cuota Flores]]"
nexo_respaldado: "[[TRX-2026-06-20-Extraccion-Difusion-Ilicita-Registros-Intimos-01]]"
estado_verificacion: verificado
fuentes:
  - url: "https://www.biobiochile.cl/noticias/nacional/chile/2026/06/09/percy-marin-responde-a-camila-flores-y-niega-responsabilidad-en-difusion-de-fotos-intimas.shtml"
    titulo: "Percy Marín responde a Camila Flores y niega responsabilidad en difusión de fotos íntimas"
    medio: "BioBioChile"
    tipo: secundaria
    fecha: 2026-06-09
    consultado: 2026-10-19
alertas_verificacion:
  - "PRIVACIDAD: hecho referido a la intimidad de una víctima, ajeno al eje de corrupción; el denunciado niega participación y no hay formalización. Se recomienda retirarlo del grafo."
tags:
  - evidencia/policial
  - cibercrimen
  - pdi
  - violencia-digital
  - registros-intimos
---

# Denuncia-Cibercrimen-PDI-Registros-Intimos-2026

## Metadatos de Fuente Primaria (Cadena de Custodia Legal)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Ingreso / Diligencia**: `= this.fecha_emision`
- **Unidad Policial Especializada**: Brigada Investigadora del Cibercrimen de la PDI
- **Fuente Oficial**: `= this.fuente_osint`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado`

## Contenido Probatorio y Relevancia
Parte policial y actas de investigación de la Brigada del Cibercrimen tras la denuncia penal presentada por [[Camila Flores Oporto]] por la sustracción de grabaciones de cámaras de seguridad del domicilio particular y la difusión ilícita de registros audiovisuales íntimos en plataformas de mensajería y redes sociales. El procedimiento motivó el allanamiento del domicilio de su exmarido [[Percy Marin Vera]] y el peritaje de servidores y dispositivos de almacenamiento.

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
