---
tipo_nodo: persona
rut: ""
aliases:
  - "Gabriel Zaliasnik"
  - "Gabriel Zaliasnik Schilkrut"
rol_principal: "Abogado Penalista, Socio Fundador de Albagli Zaliasnik (AZ) y Litigante del Sector Político-Empresarial"
afiliacion_politica: "Independiente (Histórico litigante de figuras de UDI y RN)"
situacion_procesal: en_investigacion
medida_cautelar: "Calidad de imputado confirmada por la Fiscalía Regional de Valparaíso por presunto tráfico de influencias en nombramientos judiciales (causa no formalizada)"
tags:
  - entidad/persona
  - abogado
  - caso-audios
  - caso-penta
  - nombramientos-judiciales
  - imputado
---

# Gabriel Zaliasnik Schilkrut

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Calidad Jurídica**: `= this.medida_cautelar`

## Síntesis y Arista en el Caso Audios
Abogado penalista, profesor de Derecho Penal de la Universidad de Chile, socio director del estudio *Albagli Zaliasnik* (AZ) y expresidente de la Comunidad Judía de Chile. Ha sido un litigante clave en causas de alta connotación institucional y política (defendió a parlamentarios de la [[Union Democrata Independiente]] en el [[Caso Penta]] y a ministros del gobierno de [[Sebastian Pinera Echenique]] como Jaime Mañalich y Víctor Pérez en acusaciones constitucionales).

En el marco del [[Caso Audios]], su situación procesal adquirió relevancia penal directa:
1. **Calidad de Imputado por Nombramientos Judiciales**: La Fiscal Regional de Valparaíso, Claudia Perivancich, confirmó formalmente que Zaliasnik tiene la calidad jurídica de **imputado** en la investigación penal sobre presunto [[Trafico de Influencias]] y gestiones extraprocesales en la designación de ministros en Cortes de Apelaciones y en la [[Corte Suprema de Chile]].
2. **Declaración y Vínculos con [[Luis Hermosilla Osorio]]**: El propio [[Luis Hermosilla Osorio]] declaró ante el Ministerio Público que mantenía habituales conversaciones y consultas con Zaliasnik (junto al penalista Samuel Donoso) respecto de quiénes consideraban los candidatos idóneos para asumir cargos vacantes en la magistratura, destacando la fluida llegada y redes de Zaliasnik ante integrantes del máximo tribunal.
3. **Comunicaciones Periciadas**: Las extracciones al teléfono de Hermosilla identificaron intercambios de mensajes en los cuales Zaliasnik solicitaba gestiones o colaboración de Hermosilla en causas judiciales de interés ([[TRX-2022-11-15-Gestion-Nombramientos-Hermosilla-Zaliasnik-01]]).

## Registros Reificados
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

dv.header(4, `Monto Total Imputado: ${formattedTotal}`);
dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Destino", "Delito", "Causa"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    p.entidad_destino,
    p.delito_imputado,
    p.causa_vinculada
  ])
);
```
