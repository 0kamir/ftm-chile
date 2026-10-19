---
tipo_nodo: persona
rut: ""
aliases:
  - "Pía Guzmán"
  - "María Pía Guzmán Mena"
rol_principal: "Ex Diputada de la República e Integrante de la Comisión de Familia"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: sobreseido
medida_cautelar: "Sin medidas cautelares (Desaforada en 2004 por querella de injurias y posteriormente sobreseída tras acuerdo judicial)"
tags:
  - entidad/persona
  - caso-spiniak
  - ex-diputada
---

# Pia Guzman Mena

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Abogada y exdiputada de [[Renovacion Nacional]]. El 10 de octubre de 2003 realizó una conferencia de prensa afirmando tener antecedentes de que tres senadores de la República (dos de oposición pertenecientes a la [[Union Democrata Independiente]] y uno oficialista) participaban en las fiestas de la red de [[Claudio Spiniak Vilensky]] en el [[Caso Spiniak]]. Sus declaraciones desencadenaron una crisis institucional de proporciones entre [[Renovacion Nacional]] y la [[Union Democrata Independiente]] —encabezada por [[Pablo Longueira Montes]] y [[Jovino Novoa Vasquez]]—, derivando en su desafuero parlamentario por querellas de injurias y calumnias y en la apertura de la arista político-judicial instruida por el ministro [[Sergio Munoz Gajardo]] ([[TRX-2003-11-05-Operacion-Politico-Judicial-Spiniak-01]]), documentada en [[Sentencia-Corte-Suprema-CasoSpiniak-2008]].

## Nexos y Actuaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Actuación",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```
