---
tipo_nodo: persona
rut: "5.126.663-3"
aliases:
  - "Sebastián Piñera"
  - "Miguel Juan Sebastián Piñera Echenique"
rol_principal: "Ex Presidente de la República de Chile (2010–2014 y 2018–2022), Ex Senador y Controlador del Grupo Bancard"
afiliacion_politica: "[[Renovacion Nacional]]"
situacion_procesal: sancionado_administrativamente
medida_cautelar: "Fallecido en febrero de 2024 (Multado con 19.470 UF por la SVS en Caso LAN (2007); encargado reo en 1982 en Caso Banco de Talca; acusado constitucionalmente en 2021 por Caso Dominga / Pandora Papers)"
vinculos_familiares:
  - "[[Andres Chadwick Pinera]]"
estado_verificacion: parcial
fuentes:
  - url: "https://www.cooperativa.cl/noticias/site/artic/20070706/pags-amp/20070706181357.html"
    titulo: "Piñera acusó motivos políticos en sanción de la SVS, aunque pagará la multa"
    medio: "Cooperativa"
    tipo: secundaria
    fecha: 2007-07-06
    consultado: 2026-10-19
  - url: "https://www.ciperchile.cl/2024/11/10/fiscalia-reconstruye-los-pasos-de-manuel-guerra-asi-se-sello-la-salida-del-administrador-electoral-de-pinera-del-caso-penta/"
    titulo: "Fiscalía reconstruye los pasos de Manuel Guerra: así se selló la salida del administrador electoral de Piñera del caso Penta"
    medio: "CIPER Chile"
    tipo: secundaria
    fecha: 2024-11-10
    consultado: 2026-10-19
tags:
  - entidad/persona
  - caso-dominga
  - caso-lan
  - caso-exalmar
  - banco-de-talca
  - ex-presidente
  - clan-pinera-chadwick
---

# Sebastian Pinera Echenique

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Vínculos Familiares (Grafo de Parentesco)**: `= this.vinculos_familiares` *(Primo hermano de [[Andres Chadwick Pinera]])*
- **Situación Procesal / Regulatoria**: `= this.situacion_procesal`
- **Historial Cautelar y Sancionatorio**: `= this.medida_cautelar`

## Síntesis Forense
Economista, empresario multimillonario, expresidente y exsenador de [[Renovacion Nacional]], dos veces Presidente de la República (2010–2014 y 2018–2022) y primo hermano de su exministro del Interior [[Andres Chadwick Pinera]]. En la arquitectura del grafo forense chileno, su matriz de inversiones [[Bancard Inversiones Ltda]] (y vehículos *offshore* en Islas Vírgenes Británicas administrados junto a [[Santiago Valdes Gutierrez]]) conecta negocios privados con decisiones regulatorias y causas judiciales a lo largo de cuatro décadas:
1. **[[Caso LAN Informacion Privilegiada y Banco de Talca]] (`1982` y `2006–2007`)**: En agosto de 1982 fue encargado reo y tuvo orden de detención por estafa e infracción a la Ley General de Bancos tras el colapso del *Banco de Talca* por créditos relacionados sin garantías reales por más de US$ 38 millones (`$18.500.000.000 CLP` en [[TRX-1982-08-28-Creditos-Relacionados-BancoDeTalca-Pinera-01]]), permaneciendo 24 días prófugo hasta que la [[Corte Suprema de Chile]] acogió un recurso de amparo. En julio de 2007 fue sancionado por la [[Comision para el Mercado Financiero]] (ex SVS) mediante la [[Resolucion-SVS-306-InformacionPrivilegiada-LAN-2007]] con una **multa de 11.470 UF** por usar información privilegiada en la compra de 3 millones de acciones de *LAN Airlines* (`$5.300.000.000 CLP` en [[TRX-2006-07-24-Compra-Acciones-Informacion-Privilegiada-LAN-01]]).
2. **[[Caso Minera Dominga Pandora Papers]] (`2010` y `2021`)**: En diciembre de 2010, siendo Presidente en ejercicio, su *family office* [[Bancard Inversiones Ltda]] vendió en las Islas Vírgenes Británicas el proyecto minero-portuario Dominga a [[Andes Iron SpA]] —controlada por su socio y amigo [[Carlos Alberto Delano Abbott]] ([[Empresas Penta SA]])— por **US$ 152 millones** (`$75.500.000.000 CLP` en [[TRX-2010-12-10-Compraventa-Offshore-Dominga-Bancard-Delano-01]]), supeditando el último pago de US$ 9,9 millones a que su propio gobierno no declarara zona de exclusión ambiental en La Higuera ([[Contrato-Offshore-BVI-PandoraPapers-Dominga-2010]]).
3. **[[Caso Exalmar y Fideicomiso Ciego]] (`2010–2013` y `2021`)**: Adquisición a través de *Bancard International Investment Inc.* del `9,18%` de la pesquera peruana *Exalmar S.A.* (`$8.250.000.000 CLP` en [[TRX-2012-11-20-Inversion-Offshore-Bancard-Exalmar-LaHaya-01]]) mientras conducía la defensa de Chile ante Perú en la Corte Internacional de Justicia de La Haya.
4. **[[Caso SQM]] y [[Caso Penta]] (`2009–2015`)**: La Fiscalía investigó facturas emitidas por [[Bancard Inversiones Ltda]] a [[SQM SA]] por $340 millones durante la campaña presidencial de 2009 ([[TRX-2009-11-18-Facturas-Falsas-Bancard-SQM-Campana-Pinera-01]]). SQM rectificó los pagos ante el SII; su administrador electoral, [[Santiago Valdes Gutierrez]], fue sobreseído en 2019 por prescripción. Piñera no fue imputado en esta arista.

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

## Fuentes Verificables
```dataview
TABLE WITHOUT ID
  f.titulo AS "Título",
  f.medio AS "Medio / Organismo",
  f.tipo AS "Tipo",
  f.fecha AS "Fecha",
  f.url AS "URL"
FLATTEN fuentes AS f
WHERE file.path = this.file.path
```
