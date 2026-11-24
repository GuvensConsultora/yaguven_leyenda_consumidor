# -*- coding: utf-8 -*-
from odoo import fields, models

# Texto del art. 2 de la Ley 13.987 PBA con el número que fijó la Res. 386-MPCEITGP-2026.
LEYENDA_LEY_13987 = 'Orientación al Consumidor Provincia de Buenos Aires 148'


def _provincia_bsas(self):
    return self.env.ref('base.state_ar_b', raise_if_not_found=False)


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Campos editables desde Ajustes > Empresas: si la provincia vuelve a cambiar el número,
    # se corrige el texto sin instalar nada. Al instalar, Odoo completa estos valores por
    # defecto también en las empresas que ya existen.
    yaguven_leyenda_consumidor = fields.Char(
        string='Leyenda de orientación al consumidor',
        default=LEYENDA_LEY_13987,
        help='Se imprime en las facturas y notas de crédito a Consumidor Final emitidas '
             'desde un punto de venta de la provincia indicada abajo (Ley 13.987 PBA). '
             'Vacío = no se imprime.',
    )
    yaguven_leyenda_state_id = fields.Many2one(
        'res.country.state',
        string='Provincia de la leyenda',
        default=_provincia_bsas,
        help='La leyenda sale sólo si el domicilio del punto de venta (o, si no tiene, el de '
             'la empresa) está en esta provincia.',
    )
