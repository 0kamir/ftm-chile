---
tipo_nodo: partido_politico
rut: ""
sigla: "UDI"
fecha_fundacion: "1983-09-24"
coalicion: "Chile Vamos"
estado_registro: "Vigente"
tags:
  - entidad/partido
  - chile-vamos
---

# Union Democrata Independiente

## Ficha de Organización Política
- **RUT**: `= this.rut`
- **Sigla**: `= this.sigla`
- **Fecha de Fundación**: `= this.fecha_fundacion`
- **Coalición**: `= this.coalicion`
- **Estado de Registro**: `= this.estado_registro`

## Contexto en Investigaciones Forenses y Registro OSINT
Colectividad fundada en 1983 cuyos dirigentes históricos ("coroneles") y parlamentarios aparecen vinculados en múltiples causas estructurales de la bóveda: financiamiento ilegal de campañas en el [[Caso Penta]] ([[TRX-2013-07-15-Boletas-Falsas-Penta-UDI-01]] y [[TRX-2013-09-20-Boletas-Falsas-Penta-Novoa-01]]), la acusación por cohecho en el [[Caso SQM]] contra [[Pablo Longueira Montes]] (absuelto en 2025, con recursos de nulidad pendientes) y el [[Caso Corpesca]] ([[Jaime Orpis Bouchon]]), y red de protección parlamentaria en el [[Caso Colonia Dignidad]] ([[Hernan Larrain Fernandez]], [[TRX-1996-06-12-Blindaje-Politico-Judicial-ColoniaDignidad-01]]). Asimismo, en el registro hemerográfico sobre la interna partidaria, consta la entrevista televisiva de agosto de 2017 de la excandidata a diputada UDI [[Loreto Letelier]] (*"Con las Manos en la Masa"*, Vía X), quien al recordar su etapa en la Juventud UDI describió las celebraciones en los *"retiros espirituales"* del partido en **Punta de Tralca**, donde dirigentes como [[Jovino Novoa Vasquez]] y Juan Antonio Coloma terminaban *"bailando arriba de las mesas"* con las corbatas en la cabeza, antes de ser pasada al Tribunal Supremo y marginada de la colectividad en septiembre de 2017.

## Militantes y Autoridades Vinculadas en el Vault
```dataview
TABLE WITHOUT ID
  file.link AS "Persona",
  rol_principal AS "Rol Principal",
  situacion_procesal AS "Situación Procesal",
  medida_cautelar AS "Medida Cautelar"
FROM "01_Entidades/Personas"
WHERE contains(string(afiliacion_politica), this.file.name)
```
