---
tipo_nodo: persona
rut: ""
aliases:
  - "Agustín Edwards"
  - "Agustin Edwards"
rol_principal: "Empresario y Ex Propietario de Empresa El Mercurio S.A.P."
afiliacion_politica: "Independiente (Derecha Conservadora)"
situacion_procesal: testigo_clave
medida_cautelar: "Fallecido en abril de 2017 (Auditado por el SII en el marco de las fundaciones panameñas Ashton Foundation y Kintyre Foundation)"
tags:
  - entidad/persona
  - panama-papers
  - offshore
---

# Agustin Edwards Eastman

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal / Tributaria**: `= this.situacion_procesal`
- **Estado / Fiscalización**: `= this.medida_cautelar`

## Síntesis Forense
Empresario y propietario histórico de [[Empresa El Mercurio SAP]]. En el mapa forense conecta dos grandes expedientes documentales:
1. **[[Caso Operacion FUBELT Intervencion CIA y DINA]] (`1970–1973`)**: Tras el triunfo electoral de Salvador Allende el 4 de septiembre de 1970, viajó a Washington D.C. y se reunió el 14 y 15 de septiembre de 1970 con el director de la CIA, Richard Helms, y con Henry Kissinger, desencadenando la orden del presidente Richard Nixon de iniciar el *Proyecto FUBELT*. Según acreditó oficialmente el **Informe de la Comisión Church del Senado de EE.UU. (1975)** ([[Informe-Comision-Church-1975-y-Hinchey-CIA-2000]]), el *"Comité 40"* autorizó transferencias encubiertas de la [[Agencia Central de Inteligencia CIA y Escuela de las Americas]] por **US$ 1.950.000** (`$9.500.000.000 CLP` en [[TRX-1971-09-09-Financiamiento-Encubierto-CIA-ElMercurio-Edwards-01]]) hacia [[Empresa El Mercurio SAP]], además de articular las operaciones de desestabilización y paros gremiales/camioneros de 1972–1973 ([[TRX-1972-10-12-Fondos-Desestabilizacion-Gremios-ParoCamioneros-CIA-01]]).
2. **[[Caso Panama Papers Chile]] (`2016`)**: La filtración de los archivos de [[Mossack Fonseca y Sociedades Offshore Panama]] ([[Filtracion-ICIJ-PanamaPapers-Chile-2016]]) reveló la constitución de dos fundaciones de interés privado en Panamá —*Ashton Foundation* y *Kintyre Foundation*— estructuradas para resguardar activos familiares fuera de la jurisdicción tributaria ordinaria chilena, motivando la revisión del [[Servicio Impuestos Internos]] y la [[Unidad de Analisis Financiero]] ([[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]]).

## Nexos y Operaciones Vinculadas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Operación",
  fecha AS "Fecha",
  entidad_origen AS "Entidad Origen",
  entidad_destino AS "Entidad Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto Auditado (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(firmante_origen), this.file.name) OR contains(string(firmante_destino), this.file.name)
SORT fecha ASC
```
