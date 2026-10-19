---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Andes Iron SpA (Titular del Proyecto Minero-Portuario Dominga)"
fecha_constitucion: 2010-08-05
objeto_social: "Exploración, explotación minera de hierro y cobre, y desarrollo de infraestructura portuaria y desaladora en La Higuera"
representante_legal: "[[Carlos Alberto Delano Abbott]]"
tags:
  - entidad/privada
  - caso-dominga
  - pandora-papers
  - grupo-penta
---

# Andes Iron SpA

## Ficha Societaria e Institucional
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Controlador Principal**: `= this.representante_legal` (socio controlador de [[Empresas Penta SA]])

## Contexto en Investigaciones Forenses
Sociedad minera y portuaria controlada por la familia de [[Carlos Alberto Delano Abbott]] (condenado en el [[Caso Penta]]). En diciembre de 2010, a través de contratos firmados en Chile y en las Islas Vírgenes Británicas revelados por los *Pandora Papers* en el [[Caso Minera Dominga Pandora Papers]], adquirió de [[Bancard Inversiones Ltda]] (sociedad de la familia del entonces Presidente de la República [[Sebastian Pinera Echenique]]) la participación en el proyecto **Minera Dominga** por **US$ 152 millones** (`$75.500.000.000 CLP`), pactando en la cláusula tercera del contrato *offshore* que el último pago de US$ 9,9 millones sólo se realizaría si el Gobierno de Chile no declaraba la zona de La Higuera / Punta de Choros como área de protección ambiental ([[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]] y [[Contrato-Offshore-BVI-PandoraPapers-Dominga-2010]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```
