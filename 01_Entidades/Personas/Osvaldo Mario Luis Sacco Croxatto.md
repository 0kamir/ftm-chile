---
tipo_nodo: persona
rut: ""
aliases: []
rol_principal: "Imputado señalado por la Fiscalía como líder del 'Clan Croxatto' (Operación Tributos)"
afiliacion_politica: "Independiente"
situacion_procesal: formalizado
medida_cautelar: ""
estado_verificacion: parcial
fuentes: 
  - url: "https://www.latercera.com/la-tercera-pm/noticia/expediente-secreto-del-sii-como-funcionaba-los-seis-clanes-que-crearon-el-mecanismo-del-fraude-tributario-mas-grande-de-la-historia/I4RBDAJD2JEZZJLGXGIDE7ZR6A/"
    titulo: "Expediente secreto del SII: cómo funcionaban los seis clanes del fraude tributario"
    medio: "La Tercera"
    tipo: secundaria
    consultado: 2026-10-19
  - url: "https://www.latercera.com/nacional/noticia/el-listado-de-los-55-imputados-por-el-megafraude-tributario/JEH5YAOVRJHAPMLM5UIGN3N4CM/"
    titulo: "El listado de los 55 imputados por el megafraude tributario"
    medio: "La Tercera"
    tipo: secundaria
    fecha: 2023-12-15
    consultado: 2026-10-19
historial_correcciones:
  - "Nombre y rol corregidos el 2026-10-19 según el listado publicado por la prensa; RUT eliminado por no constar en fuente pública."
tags:
  - entidad/persona
  - megafraude-sii
  - operacion-tributos
  - clan-croxatto
---

# Osvaldo Mario Luis Sacco Croxatto

## Perfil Biográfico e Institucional
- **RUT**: `= this.rut`
- **Rol Principal**: `= this.rol_principal`
- **Afiliación Política**: `= this.afiliacion_politica`
- **Situación Procesal**: `= this.situacion_procesal`
- **Medida Cautelar / Sanciones**: `= this.medida_cautelar`

## Síntesis Forense
Figura en el listado de 55 imputados formalizados en diciembre de 2023. Según el expediente del [[Servicio Impuestos Internos]] reportado por La Tercera, la Fiscalía lo sindica como líder del denominado 'Clan Croxatto', que habría generado pérdidas fiscales por $422.727.859 mediante seis empresas proveedoras de facturas falsas en el [[Caso Megafraude Tributario Operacion Tributos]]. Rige la presunción de inocencia: la causa no tiene sentencia.

## Auditoría Contable: Registros Reificados
```dataviewjs
const pages = dv.pages('"03_Hechos_y_Nexos"')
  .where(p => (p.firmante_origen && String(p.firmante_origen).includes(dv.current().file.name)) ||
              (p.firmante_destino && String(p.firmante_destino).includes(dv.current().file.name)));

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
