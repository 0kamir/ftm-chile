---
tipo_nodo: evidencia_documental
id_evidencia: "EVD-TOP-TEM-2024-HUR"
tipo_documento: "Sentencia Condenatoria Definitiva del Tribunal de Juicio Oral en lo Penal de Temuco en Caso Operación Huracán (RIT 180-2020)"
fecha_emision: 2026-04-02
organismo_emisor: "[[Corte Suprema de Chile]]"
fuente_osint: "Poder Judicial de Chile (pjud.cl) / Fiscalía de Chile / Tribunal de Juicio Oral en lo Penal de Temuco"
causa_vinculada: "[[Caso Operacion Huracan]]"
nexo_respaldado: "[[TRX-2017-09-23-Detencion-Montaje-OperacionHuracan-01]]"
estado_verificacion: desactualizado
fuentes:
  - url: "https://www.eldinamo.cl/pais/2026/04/02/el-profesor-smith-condenado-a-12-anos-de-carcel-por-montaje-en-operacion-huracan/"
    titulo: "El 'profesor' Smith condenado a 12 años de cárcel"
    medio: "El Dínamo"
    tipo: secundaria
    fecha: 2026-04-02
    consultado: 2026-10-19
tags:
  - evidencia/sentencia
  - operacion-huracan
  - top-temuco
  - condena-efectiva
---

# Sentencia-TOP-Temuco-OperacionHuracan-2026

## Metadatos de Fuente Primaria (Cadena de Custodia Judicial)
- **ID Evidencia**: `= this.id_evidencia`
- **Tipo de Documento**: `= this.tipo_documento`
- **Fecha de Sentencia**: `= this.fecha_emision`
- **Tribunal Emisor**: Tribunal de Juicio Oral en lo Penal de Temuco
- **Órgano Jurisdiccional Superior**: `= this.organismo_emisor`
- **Estado de Verificación**: `= this.estado_verificacion`
- **Causa Vinculada**: `= this.causa_vinculada`
- **Nexo Respaldado**: `= this.nexo_respaldado` (junto a [[TRX-2018-01-25-Peritaje-Cibercrimen-Descarte-Antorcha-01]] y [[TRX-2017-10-15-Remuneracion-Fondos-Reservados-Smith-Antorcha-01]])

## Extracto y Relevancia Probatoria
Fallo condenatorio unánime dictado por el Tribunal de Juicio Oral en lo Penal de Temuco que dio por acreditado el montaje policial y la implantación de pruebas falsas perpetrado por la plana mayor de la [[Direccion de Inteligencia Policial de Carabineros]] (UIOE):
1. **Condena a Prisión Efectiva**: Sentenció a **12 años de presidio efectivo** al creador civil de «Antorcha», [[Alex Smith Leay]], y a **10 años de presidio efectivo** al excapitán [[Leonardo Osses Sandoval]] por delitos reiterados de [[Falsificacion de Instrumento Publico]], [[Obstruccion a la Investigacion]] y uso malicioso de instrumento público falso.
2. **Condenas a Mandos de Inteligencia**: Condenó al exgeneral director de Inteligencia [[Gonzalo Blu Rodriguez]] y al exmayor jefe de operaciones [[Patricio Marin Lazo]] a **5 años de presidio** cada uno (bajo libertad vigilada intensiva), y al excoronel [[Marcelo Teuber Munoz]] a **3 años y un día más 100 días**.
3. **Acreditación del Montaje**: El tribunal concluyó que los oficios policiales e informes de inteligencia entregados al Ministerio Público contenían falsedades sustanciales, habiéndose adulterado e insertado manualmente los supuestos mensajes de WhatsApp en los dispositivos de los comuneros sobreseídos.

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
