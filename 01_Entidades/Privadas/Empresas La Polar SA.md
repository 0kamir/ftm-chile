---
tipo_nodo: entidad_privada
rut: ""
razon_social: "Empresas La Polar S.A."
fecha_constitucion: "1920-01-01"
objeto_social: "Comercio minorista (retail), grandes tiendas y emisión de tarjetas de crédito no bancarias"
representante_legal: "[[Pablo Alcalde Saavedra]]"
estado_verificacion: verificado
fuentes:
  - "https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales"
  - "https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf"
  - "https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/"
  - "https://www.cnnchile.com/sin-categoria/caso-la-polar-corte-suprema-multa-a-pwc/"
  - "https://www.elmostrador.cl/noticias/pais/2014/02/25/la-svs-vuelve-a-sancionar-a-pwc-por-la-polar-esta-vez-por-fallas-en-auditoria-de-2009-2/"
  - "https://www.elmostrador.cl/mercados/2015/07/24/pwc-otra-vez-en-la-mira-svs-lo-sanciona-por-auditoria-a-operaciones-de-esquema-cascadas/"
tags:
  - entidad/privada
  - retail
  - caso-la-polar
---

# Empresas La Polar SA

## Ficha Societaria / Registro de Personas Jurídicas
- **RUT**: `= this.rut`
- **Razón Social**: `= this.razon_social`
- **Fecha de Constitución**: `= this.fecha_constitucion`
- **Objeto Social**: `= this.objeto_social`
- **Presidente / Gerente General en Período Investigado**: `= this.representante_legal`

## Contexto y Societario
Sociedad anónima abierta del sector retail protagonista del [[Caso La Polar]]. Entre 2006 y 2011 ejecutó repactaciones unilaterales masivas de deudas en su cartera de tarjetas de crédito sin consentimiento de los clientes ([[TRX-2011-06-09-Repactaciones-Unilaterales-LaPolar-01]]), ocultando provisiones de riesgo y falseando los estados financieros reportados a la [[Comision para el Mercado Financiero]] (ex SVS). Sus exejecutivos principales —[[Pablo Alcalde Saavedra]], [[Julian Moreno de Pablo]] y [[Maria Isabel Farah Silva]]— fueron condenados penalmente en 2015 ([[Sentencia-Condenatoria-y-Fallo-CS-LaPolar-2015]]) y civilmente por la [[Corte Suprema de Chile]].

## Historial de Recepción de Fondos y Nexos
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Transacción",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_origen AS "Entidad Origen",
  firmante_origen AS "Ejecutivo Origen",
  "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_destino), this.file.name) OR contains(string(entidad_origen), this.file.name)
SORT fecha DESC
```

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [La Polar: Fiscalía Centro Norte obtiene condena de principales ejecutivos por delitos de mercado de valores y lavado de activos](https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales) | Fiscalía de Chile | `primaria` | 2015-12-16 | [Wayback ↺](https://web.archive.org/web/*/https://www.fiscaliadechile.cl/actualidad/noticias/regionales/la-polar-fiscalia-centro-norte-obtiene-condena-de-principales) |
| [Sentencia Judicial sobre Sanciones SVS en Caso La Polar](https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf) | Poder Judicial (vía CIPER Chile) | `primaria` | 2014-09-03 | [Wayback ↺](https://web.archive.org/web/*/https://ciperchile.cl/pdfs/2015/10/lapolar/LaPolar_2014-09-03_Fallo-Ramirez.pdf) |
| [Corte Suprema confirma condena contra ex ejecutivos de La Polar y ordena indemnizar a AFP por pérdidas en fondos de pensiones](https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/) | Diario Constitucional | `secundaria` | 2026-03-19 | [Wayback ↺](https://web.archive.org/web/*/https://www.diarioconstitucional.cl/2026/03/19/corte-suprema-confirma-condena-contra-ex-ejecutivos-de-la-polar-y-ordena-indemnizar-a-afp-por-perdidas-en-fondos-de-pensiones/) |
| [Caso La Polar: Corte Suprema confirma multa contra auditora PwC](https://www.cnnchile.com/sin-categoria/caso-la-polar-corte-suprema-multa-a-pwc/) | CNN Chile / Corte Suprema | `secundaria` | 2016-12-20 | [Wayback ↺](https://web.archive.org/web/*/https://www.cnnchile.com/sin-categoria/caso-la-polar-corte-suprema-multa-a-pwc/) |
| [La SVS vuelve a sancionar a PwC por La Polar, esta vez por fallas en auditoría de 2009](https://www.elmostrador.cl/noticias/pais/2014/02/25/la-svs-vuelve-a-sancionar-a-pwc-por-la-polar-esta-vez-por-fallas-en-auditoria-de-2009-2/) | El Mostrador | `secundaria` | 2014-02-25 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/noticias/pais/2014/02/25/la-svs-vuelve-a-sancionar-a-pwc-por-la-polar-esta-vez-por-fallas-en-auditoria-de-2009-2/) |
| [PwC otra vez en la mira: SVS lo sanciona por auditoría a operaciones de esquema Cascadas](https://www.elmostrador.cl/mercados/2015/07/24/pwc-otra-vez-en-la-mira-svs-lo-sanciona-por-auditoria-a-operaciones-de-esquema-cascadas/) | El Mostrador | `secundaria` | 2015-07-24 | [Wayback ↺](https://web.archive.org/web/*/https://www.elmostrador.cl/mercados/2015/07/24/pwc-otra-vez-en-la-mira-svs-lo-sanciona-por-auditoria-a-operaciones-de-esquema-cascadas/) |
