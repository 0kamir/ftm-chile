---
tipo_nodo: persona
rut: ""
aliases:
  - "Sergio Muñoz"
  - "Ministro Sergio Muñoz Gajardo"
rol_principal: "Ex Ministro y Ex Presidente de la Corte Suprema de Chile (Ministro en Visita Caso Spiniak y Caso Riggs)"
afiliacion_politica: "Independiente"
situacion_procesal: testigo_clave
medida_cautelar: "Sin medidas cautelares penales (destituido en acusación constitucional parlamentaria en 2024)"
tags:
  - entidad/persona
  - poder-judicial
  - caso-spiniak
---

# Sergio Munoz Gajardo

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Magistrado de la [[Corte Suprema de Chile]] (y presidente del máximo tribunal entre 2014 y 2016). Actuó como juez instructor en dos de las mayores investigaciones judiciales del país:
1. **[[Caso Spiniak]] (2003–2005)**: En noviembre de 2003 fue designado por el Pleno de la [[Corte Suprema de Chile]] como Ministro en Visita extraordinario con dedicación exclusiva luego de la remoción del juez Daniel Calvo Flores tras una operación de extorsión con cámara oculta ([[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]]). Su instrucción junto al [[Servicio Impuestos Internos]] acreditó la estructura ilícita de [[Claudio Spiniak Vilensky]] e [[Inversiones El Bosque Ltda]] ([[TRX-2003-10-15-Ocultamiento-Patrimonial-ElBosque-Spiniak-01]]) y desmontó el montaje de falso testimonio contra el senador [[Jovino Novoa Vasquez]] ([[Sentencia-Corte-Suprema-CasoSpiniak-2008]]).
2. **[[Caso Riggs]] y antecedentes del [[Caso CEMA Chile]] (2004–2005)**: Como primer Ministro en Visita del [[Caso Riggs]], descubrió la red de más de 125 cuentas secretas y sociedades *offshore* en [[Riggs Bank y Sociedades Offshore Ashburton]], los pasaportes falsos de [[Augusto Pinochet Ugarte]], la participación fiduciaria de [[Oscar Aitken Lavanchy]], la evasión tributaria denunciada por el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]]) y los primeros desvíos desde la [[Fundacion CEMA Chile]] presidida por [[Lucia Hiriart Rodriguez]] ([[TRX-2016-08-12-Enajenacion-Inmuebles-Fiscales-CEMAChile-01]]), cimentando el comiso definitivo dictado en [[Sentencia-Corte-Suprema-CasoRiggs-2018]].

## Auditoría Contable y Procesal: Causas y Nexos Instruidos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Actuación",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto Auditado (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_destino), this.file.name) OR contains(string(firmante_origen), this.file.name)
SORT fecha ASC
```
