---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Mossack Fonseca & Co. y Red de 200 Sociedades Offshore Chilenas (Turnbrook Corp. / Ashton Foundation / Sierra Leona S.A.)"
fecha_constitucion: 1977-03-18
objeto_social: "Servicios jurídicos fiduciarios, incorporación de sociedades offshore y fundaciones de interés privado en Panamá, Bahamas e Islas Vírgenes Británicas"
representante_legal: "[[Gonzalo Delaveau Swett]]"
estado_verificacion: verificado
fuentes:
  - "https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/"
  - "https://offshoreleaks.icij.org/"
  - "https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/"
  - "https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/"
tags:
  - entidad/privada
  - panama-papers
  - offshore
  - mossack-fonseca
---

# Mossack Fonseca y Sociedades Offshore Panama

## Ficha Societaria e Institucional
- **RUT Inversionista Extranjero / Referencial**: `= this.rut`
- **Razón Social / Red Fiduciaria**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion` (disuelta en marzo de 2018 tras el escándalo mundial de los *Panama Papers*)
- **Objeto Social**: `= this.objeto_social`
- **Agente / Intermediario Principal en Chile**: `= this.representante_legal`

## Contexto en Investigaciones
Bufete panameño fundado por Jürgen Mossack y Ramón Fonseca Mora que protagonizó en abril de 2016 la filtración global **Panama Papers** (ICIJ). En el [[Caso Panama Papers Chile]], sus archivos internos revelaron cerca de **200 sociedades *offshore* vinculadas a Chile**, entre ellas:
1. Las cinco sociedades en Bahamas (*Turnbrook Corporation*, *DKL Holdings*, *Westquarter Limited*, *Mining Press Holdings* y *Turnbrook Mining Ltd.*) administradas por [[Gonzalo Delaveau Swett]], entonces presidente de *Chile Transparente* ([[TRX-2016-04-03-Estructuracion-Offshore-MossackFonseca-Delaveau-01]]).
2. Las fundaciones panameñas *Ashton Foundation* y *Kintyre Foundation* de [[Agustin Edwards Eastman]] y las sociedades *Sierra Leona S.A.* y *Railton Foundation* de [[Alfredo Ovalle Rodriguez]] ([[TRX-2016-04-05-Fundaciones-Offshore-MossackFonseca-Edwards-Ovalle-01]]).
3. Vehículos corporativos en Islas Vírgenes Británicas interconectados con [[Riggs Bank y Sociedades Offshore Ashburton]], utilizados por [[Augusto Pinochet Ugarte]] y [[Oscar Aitken Lavanchy]] en el [[Caso Riggs]] ([[TRX-2016-04-15-Cruce-Offshore-MossackFonseca-Riggs-Pinochet-01]]).

## Transacciones y Flujos Vinculados
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Origen",
  entidad_destino AS "Destino",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  delito_imputado AS "Delito"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha ASC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [The Panama Papers: los secretos de chilenos en paraísos fiscales](https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) | CIPER Chile | `secundaria` | 2016-04-04 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/2016/04/04/the-panama-papers-los-secretos-de-chilenos-en-paraisos-fiscales-salen-a-la-luz/) |
| [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/) | ICIJ | `primaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://offshoreleaks.icij.org/) |
| [Caso Riggs fue cerrado por la Corte Suprema tras 14 años](https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) | CNN Chile | `secundaria` | 2018-08-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/caso-riggs-fue-cerrado-por-la-corte-suprema-tras-14-anos/) |
| [Ordenan decomiso de bienes de Pinochet](https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) | The Clinic | `secundaria` | 2018-08-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.theclinic.cl/2018/08/25/ordenan-decomiso-de-bienes-de-pinochet-por-mas-de-us-16-millones/) |
