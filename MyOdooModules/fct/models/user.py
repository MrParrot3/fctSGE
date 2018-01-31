# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
    _inherit = 'res.users'
    
    isPupil = fields.Boolean("Pupil", default=False)
    isTutor = fields.Boolean("Tutor", default=False)
    