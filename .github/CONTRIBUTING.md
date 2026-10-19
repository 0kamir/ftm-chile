# Cómo contribuir a FTM-Chile

Toda la información del vault debe estar respaldada por fuentes públicas verificables. El procedimiento completo está en [`00_Meta/Flujo_Incorporacion_Informacion.md`](../00_Meta/Flujo_Incorporacion_Informacion.md). En resumen:

1. **Propón** el aporte con un Issue ("Nueva información" o "Rectificación") que incluya la URL de respaldo.
2. **Verifica** contra la fuente primaria y archiva la URL en web.archive.org.
3. **Registra** la nota desde `00_Meta/Plantillas/`, o agrega fuentes con `python3 00_Meta/Scripts/add_source.py`.
4. **Valida** con `make validate sources links test`.
5. **Abre un Pull Request** con la lista de verificación completa. El CI ejecuta `validate_vault.py --estricto`.

Reglas no negociables: sin fuente no hay nota publicada; presunción de inocencia; no se publican datos íntimos ni de víctimas; no se inventan RUC, RUT, montos ni fechas.
