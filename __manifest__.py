# -*- coding: utf-8 -*-
{
    "name": "Leyenda de Orientación al Consumidor (Yagüven)",
    "summary": "Imprime en la factura la leyenda de orientación al consumidor que exige la "
               "provincia (Ley 13.987 PBA, Línea 148) cuando el cliente es consumidor final.",
    "description": """
Ley 13.987 de la Provincia de Buenos Aires: las facturas y tickets a consumidor final emitidos
en la provincia deben llevar, en forma legible y destacada, el teléfono gratuito de orientación
al consumidor. La Res. 386-MPCEITGP-2026 (BO 22/10/2026) fijó ese número en la Línea 148,
obligatoria desde el 21/11/2026.

La leyenda sale en facturas y notas de crédito de cliente cuando:
- el cliente es Consumidor Final (condición frente al IVA, código ARCA 5), y
- el punto de venta (domicilio del diario; si no tiene, el de la empresa) está en la
  provincia configurada en la empresa.

El texto y la provincia son campos de la empresa (Ajustes > Empresas), para poder corregirlos
sin instalar nada si cambia el número. Vienen precargados con el texto de la ley y Buenos Aires.
""",
    "version": "20.0.1.0.0",
    "category": "Accounting/Localizations",
    "author": "Yagüven C.G.",
    "website": "https://yaguven.com",
    "license": "LGPL-3",
    "depends": ["l10n_ar"],
    "data": [
        "views/res_company_views.xml",
        "views/report_invoice.xml",
    ],
    "installable": True,
    "application": False,
}
