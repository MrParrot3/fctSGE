# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Partner(models.Model):
    _inherit = 'res.partner'

    isFCTPartner = fields.Boolean("FCT Partner", default=False)

    pupils = fields.One2many('res.users','company',string="Pupils")
