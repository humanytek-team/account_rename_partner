# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    partner_id = fields.Many2one(
        string=_('Partner/Customer')
    )
