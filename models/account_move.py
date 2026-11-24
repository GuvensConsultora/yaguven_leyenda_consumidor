# -*- coding: utf-8 -*-
from odoo import models

# Código ARCA de la condición frente al IVA «Consumidor Final».
CODIGO_CONSUMIDOR_FINAL = '5'


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _yaguven_leyenda_consumidor(self):
        """Texto a imprimir, o '' si a este comprobante no le corresponde la leyenda.

        Ley 13.987 PBA: facturas y tickets a consumidor final emitidos en la provincia.
        - Sólo comprobantes de cliente (facturas y notas de crédito).
        - Consumidor Final según la condición guardada en la factura al emitirla (no la que el
          contacto tenga hoy); si la factura no la tiene, la del contacto comercial.
        - «Emitido en la provincia»: domicilio del punto de venta (diario); si el diario no
          tiene domicilio cargado, el de la empresa.
        """
        self.ensure_one()
        empresa = self.company_id
        texto = (empresa.yaguven_leyenda_consumidor or '').strip()
        if not texto or not empresa.yaguven_leyenda_state_id:
            return ''
        if self.move_type not in ('out_invoice', 'out_refund'):
            return ''
        condicion = (self.l10n_ar_afip_responsibility_type_id
                     or self.commercial_partner_id.l10n_ar_afip_responsibility_type_id)
        if condicion.code != CODIGO_CONSUMIDOR_FINAL:
            return ''
        domicilio = self.journal_id.l10n_ar_afip_pos_partner_id or empresa.partner_id
        if domicilio.state_id != empresa.yaguven_leyenda_state_id:
            return ''
        return texto
