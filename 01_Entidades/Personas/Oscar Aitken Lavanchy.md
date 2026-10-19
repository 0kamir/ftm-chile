---
tipo_nodo: persona
rut: ""
aliases:
  - "Óscar Aitken"
  - "Oscar Aitken"
rol_principal: "Abogado, Albacea y Estructurador de Sociedades Offshore de Augusto Pinochet"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: "Sin medidas cautelares vigentes (Procesado por delito tributario y malversación en la instrucción del Caso Riggs)"
tags:
  - entidad/persona
  - caso-riggs
  - offshore
---

# Oscar Aitken Lavanchy

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis Forense
Abogado y exalbacea testamentario de [[Augusto Pinochet Ugarte]]. En la investigación del [[Caso Riggs]] instruida por el Ministro en Visita [[Sergio Munoz Gajardo]], según la investigación judicial, habría actuado como operador jurídico y fiduciario en la constitución y administración de sociedades de papel *offshore* en Islas Vírgenes Británicas, Bahamas y Panamá (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*), agrupadas bajo [[Riggs Bank y Sociedades Offshore Ashburton]], utilizadas para triangular caudales públicos provenientes de gastos reservados ([[TRX-2004-07-14-Desvio-Gastos-Reservados-Riggs-Pinochet-01]]) y ocultar rentas ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Evasion-Tributaria-Cuentas-Riggs-SII-01]]).

## Nexos y Transacciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```
