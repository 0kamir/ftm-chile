---
tipo_nodo: entidad_publica
rut: ""
categoria: Ministerio # GORE | Ministerio | Municipio | Poder Judicial
region: ""
superior_jerarquico: ""
estado_verificacion: pendiente # verificado | parcial | desactualizado | sin_fuente | pendiente
fuentes:
  - "https://"
tags:
  - entidad/publica
---

# {{title}}

## Ficha Institucional
- **RUT**: `= this.rut`
- **Categoría**: `= this.categoria`
- **Región**: `= this.region`
- **Superior Jerárquico**: `= this.superior_jerarquico`

## Nexos y Transferencias Emitidas / Recibidas
```dataview
TABLE WITHOUT ID
  file.link AS "Nexo / Convenio",
  fecha AS "Fecha",
  tipo_nexo AS "Tipo",
  entidad_destino AS "Entidad Destino",
  firmante_origen AS "Firmante Público",
   "$" + regexreplace(string(monto_clp), "\B(?=(\d{3})+(?!\d))", ".") AS "Monto (CLP)",
  causa_vinculada AS "Causa"
FROM "03_Hechos_y_Nexos"
WHERE contains(string(entidad_origen), this.file.name) OR contains(string(entidad_destino), this.file.name)
SORT fecha DESC
```

## Observaciones de Contraloría / Auditoría
- 

## Fuentes Verificables

| Fuente (Link URL) | Medio / Organismo | Tipo | Fecha | Archivo |
| :--- | :--- | :---: | :---: | :---: |
| [Título del documento o nota](https://) | Medio | `primaria` | YYYY-MM-DD | [copia](https://web.archive.org/) |
