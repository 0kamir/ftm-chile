---
tipo_nodo: persona
rut: ""
aliases:
  - "Andrés Chadwick"
  - "Andrés Pío Bernardino Chadwick Piñera"
rol_principal: "Ex Ministro del Interior y Seguridad Pública (2012–2014 y 2018–2019), Ex Senador UDI y Socio de Comunidad de Oficina con Luis Hermosilla"
afiliacion_politica: "[[Union Democrata Independiente]]"
situacion_procesal: en_investigacion
medida_cautelar: "Inhabilitado por 5 años para ejercer cargos públicos por el Senado (Acusación Constitucional 2019); imputado en aristas Parque Capital y nombramientos judiciales del Caso Audios"
vinculos_familiares:
  - "[[Sebastian Pinera Echenique]]"
tags:
  - entidad/persona
  - caso-audios
  - udi
  - ex-ministro
  - clan-pinera-chadwick
---

# Andres Chadwick Pinera

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Primo hermano de [[Sebastian Pinera Echenique]])*
- **Situación Procesal**: `= this.situacion_procesal`
- **Sanción Constitucional / Cautelar**: `= this.medida_cautelar`

## Síntesis Forense
Abogado, dirigente histórico de la [[Union Democrata Independiente]] (exdiputado y exsenador en el [[Senado de la Republica de Chile]]) y hombre clave de los dos gobiernos de su primo hermano [[Sebastian Pinera Echenique]], en los que ejerció como Ministro Secretario General de Gobierno (2011–2012) y Ministro del Interior y Seguridad Pública (2012–2014 y 2018–2019). En la topología del grafo forense actúa como el **nodo puente (*broker*) entre el Clan Piñera–Chadwick, la cúpula de la [[Union Democrata Independiente]] y la red de influencias de [[Luis Hermosilla Osorio]]**:
1. **Defensa en Acusación Constitucional (`2019`) financiada desde [[Factop SpA]]**: En diciembre de 2019 fue destituido e inhabilitado por 5 años por el [[Senado de la Republica de Chile]] al aprobarse la Acusación Constitucional en su contra. Su defensa jurídica ante el Congreso estuvo encabezada por su amigo y exasesor del Ministerio del Interior [[Luis Hermosilla Osorio]]. La investigación del [[Caso Audios]] reveló que el informe en derecho redactado por el catedrático alemán Kai Ambos para la defensa de Chadwick ante el Senado fue pagado con recursos triangulados desde el *factoring* [[Factop SpA]] por instrucción de [[Luis Hermosilla Osorio]] ([[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]).
2. **Comunidad de oficina en Alonso de Córdova y pagos por `$190.000.000 CLP` (Arista *Parque Capital*)**: Tras dejar La Moneda, compartió oficina en Alonso de Córdova 3788 (Vitacura) con [[Luis Hermosilla Osorio]] —mismo inmueble donde se grabó [[Audio-Reunion-Edificio-Alonso-2023]]—. Según la Fiscalía Oriente, las cartolas bancarias periciadas registran transferencias desde cuentas de [[Luis Hermosilla Osorio]] (nutridas por [[Factop SpA]]) hacia [[Andres Chadwick Pinera]] por más de **`$190.000.000 CLP`** entre 2020 y 2023 ([[TRX-2019-12-11-Defensa-AC-Transferencias-Factop-Hermosilla-Chadwick-01]]), coincidiendo con gestiones ante autoridades de Vivienda para destrabar permisos del proyecto industrial *Parque Capital* (Grupo Patio), por lo cual declaró en calidad de imputado bajo hipótesis de [[Trafico de Influencias]].
3. **Arista de Nombramientos Judiciales en la [[Corte Suprema de Chile]]**: Las pericias al teléfono de [[Luis Hermosilla Osorio]] documentaron la coordinación entre [[Andres Chadwick Pinera]], [[Luis Hermosilla Osorio]] y la exministra [[Angela Vivanco Martinez]] durante el segundo gobierno de [[Sebastian Pinera Echenique]] para impulsar nombramientos en el Poder Judicial y gestionar información sobre causas en tabla ([[TRX-2023-02-09-Gestion-Judicial-Hermosilla-Vivanco-01]]).

## Auditoría Contable: Montos Imputados en Aristas Reificadas
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

let totalClp = 0;
for (let page of pages) {
  totalClp += Number(page.monto_clp || 0);
}

const formattedTotal = new Intl.NumberFormat('es-CL', {
  style: 'currency',
  currency: 'CLP',
  maximumFractionDigits: 0
}).format(totalClp);

dv.header(4, `Monto Total Asociado en Aristas Reificadas: ${formattedTotal}`);
dv.table(
  ["Transacción / Nexo", "Fecha", "Entidad Origen", "Entidad Destino", "Monto (CLP)", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.entidad_origen,
    p.entidad_destino,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```
