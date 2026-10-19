---
tipo_nodo: persona
rut: ""
aliases:
  - "Alfredo Ovalle"
rol_principal: "Empresario Minero, Ex Presidente de la CPC y Ex Presidente de la SONAMI"
afiliacion_politica: "Independiente (Dirigente Gremial Empresarial)"
situacion_procesal: testigo_clave
medida_cautelar: "Fallecido en julio de 2021 (Incluido en las auditorías del SII por sociedades offshore en Panamá e Islas Vírgenes Británicas)"
tags:
  - entidad/persona
  - panama-papers
  - offshore
  - gremios-empresariales
---

# Alfredo Ovalle Rodriguez

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal / Tributaria**: `= this.situacion_procesal`
- **Estado / Fiscalización**: `= this.medida_cautelar`

## Síntesis
Abogado, empresario minero, expresidente de la Sociedad Nacional de Minería (SONAMI) y expresidente de la Confederación de la Producción y del Comercio (CPC, 2006–2008). En el [[Caso Panama Papers Chile]], los archivos de [[Mossack Fonseca y Sociedades Offshore Panama]] revelaron su vinculación con la sociedad *offshore* panameña *Sierra Leona S.A.* y con *Railton Foundation*, estructuradas en coordinación con su asesor jurídico Humberto Julio Reyes (exintegrante de aparatos de inteligencia militar), operaciones que fueron incorporadas en el catastro de fiscalización del [[Servicio Impuestos Internos]] y la [[Unidad de Analisis Financiero]] ([[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]] y [[Filtracion-ICIJ-PanamaPapers-Chile-2016]]).

## Nexos y Operaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto Registrado (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```
