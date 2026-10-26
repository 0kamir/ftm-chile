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
estado_verificacion: verificado
fuentes:
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
  - "https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/"
  - "https://offshoreleaks.icij.org/"
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

## Síntesis
Abogado y exalbacea testamentario de [[Augusto Pinochet Ugarte]]. En la investigación del [[Caso Riggs]] instruida por el Ministro en Visita [[Sergio Munoz Gajardo]], según la investigación judicial, habría actuado como operador jurídico y fiduciario en la constitución y administración de sociedades de papel *offshore* en Islas Vírgenes Británicas, Bahamas y Panamá (*Ashburton Company Ltd.*, *Althorp Investment Co.*, *Cornwall Overseas Corp.*), agrupadas bajo [[Riggs Bank y Sociedades Offshore Ashburton]], utilizadas para triangular caudales públicos provenientes de gastos reservados ([[TRX-2004-07-14-Gastos-Reservados-Riggs-01]]) y ocultar rentas ante el [[Servicio Impuestos Internos]] ([[TRX-2005-08-10-Querella-SII-Cuentas-Riggs-01]]).

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

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
| [The Panama Papers: los secretos de chilenos en paraísos fiscales](https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) | CIPER Chile | `secundaria` | 2016-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) |
| [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/) | ICIJ | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://offshoreleaks.icij.org/) |
