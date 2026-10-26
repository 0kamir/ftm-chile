---
tipo_nodo: persona
rut: ""
aliases:
  - "Andrónico Luksic"
  - "Andrónico Luksic Craig"
rol_principal: "Empresario y Ex Presidente del Holding Quiñenco S.A. y Banco de Chile"
afiliacion_politica: "Independiente"
situacion_procesal: ninguna
medida_cautelar: "Sin medidas cautelares ni procesos judiciales vigentes"
estado_verificacion: verificado
fuentes:
  - "https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml"
  - "https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/"
  - "https://www.elciudadano.com/?p=524007"
  - "https://www.fne.gob.cl/corte-suprema-acoge-parcialmente-reclamacion-de-la-fne-y-sanciona-a-todas-las-navieras-que-integraron-cartel-del-transporte-maritimo-de-vehiculos-hacia-chile-con-multas-totales-de-us-305-millones/"
  - "https://www.fne.gob.cl/fne-pide-a-la-corte-suprema-que-eleve-sanciones-contra-navieras-que-integraron-cartel-de-transporte-de-vehiculos-hacia-chile/"
tags:
  - entidad/persona
  - empresario
  - quinenco
  - caso-caval
---

# Andronico Luksic Craig

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar Vigente**: `= this.medida_cautelar`

## Síntesis
Empresario chileno, ex líder del consorcio empresarial Quiñenco S.A. y figura central del sector financiero y minero en Chile. Su registro en esta bóveda corresponde al [[Caso Caval]]:
   - En el ámbito corporativo nacional, en noviembre de 2013 sostuvo en la casa matriz del banco una reunión con [[Natalia Compagnon Soto]] y Sebastián Dávalos Bachelet en el marco de la tramitación de un crédito por `$6.500.000.000 CLP` solicitado por [[Exportadora y de Gestion Caval Ltda]] para la compra de terrenos en Machalí, arista investigada en el [[Caso Caval]] donde prestó declaración en calidad de testigo sin formulación de cargos penales en su contra.

## Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

dv.table(
  ["Registro / Hito", "Fecha", "Tipo Nexo", "Origen", "Monto (CLP)", "Causa / Ámbito"],
  pages.sort(p => p.fecha, 'asc').map(p => [
    p.file.link,
    p.fecha,
    p.tipo_nexo,
    p.entidad_origen,
    new Intl.NumberFormat('es-CL', { style: 'currency', currency: 'CLP', maximumFractionDigits: 0 }).format(Number(p.monto_clp || 0)),
    p.causa_vinculada
  ])
);
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Lectura de sentencia Caso Caval](https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) | BioBioChile | `secundaria` | 2018-07-11 | [Wayback ↺](https://web.archive.org/web/*/https://www.biobiochile.cl/noticias/nacional/chile/2018/07/11/lectura-de-sentencia-caso-caval.shtml) |
| [Rechazan recurso de nulidad presentado por Natalia Compagnon](https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) | CNN Chile | `secundaria` | 2018-10-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/pais/rechazan-recurso-de-nulidad-presentado-por-natalia-compagnon_20181018/) |
| [Mauricio Valero fue absuelto](https://www.elciudadano.com/?p=524007) | El Ciudadano | `secundaria` | 2026-10-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.elciudadano.com/?p=524007) |
| [Corte Suprema acoge reclamación de la FNE y sanciona a todas las navieras que integraron cartel del transporte marítimo de vehículos hacia Chile con multas de US$ 30,5 millones](https://www.fne.gob.cl/corte-suprema-acoge-parcialmente-reclamacion-de-la-fne-y-sanciona-a-todas-las-navieras-que-integraron-cartel-del-transporte-maritimo-de-vehiculos-hacia-chile-con-multas-totales-de-us-305-millones/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2020-08-14 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/corte-suprema-acoge-parcialmente-reclamacion-de-la-fne-y-sanciona-a-todas-las-navieras-que-integraron-cartel-del-transporte-maritimo-de-vehiculos-hacia-chile-con-multas-totales-de-us-305-millones/) |
| [FNE pide a la Corte Suprema que eleve sanciones contra navieras que integraron cartel de transporte de vehículos hacia Chile](https://www.fne.gob.cl/fne-pide-a-la-corte-suprema-que-eleve-sanciones-contra-navieras-que-integraron-cartel-de-transporte-de-vehiculos-hacia-chile/) | Fiscalía Nacional Económica (FNE) | `primaria` | 2017-08-18 | [Wayback ↺](https://web.archive.org/web/*/https://www.fne.gob.cl/fne-pide-a-la-corte-suprema-que-eleve-sanciones-contra-navieras-que-integraron-cartel-de-transporte-de-vehiculos-hacia-chile/) |
