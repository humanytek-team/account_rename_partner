# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    partner_id = fields.Many2one(string=_("Partner/Customer"))
