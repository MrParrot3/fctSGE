# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class User(models.Model):
    _inherit = 'res.users'
    
    isPupil = fields.Boolean("Pupil", default=False)
    isTutor = fields.Boolean("Tutor", default=False)
    
    tutor = fields.Many2one('res.users',ondelete='set null',string="Tutor",index=True)
    company = fields.Many2one('res.partner',ondelete='set null',string="Company",index=True)
    activities = fields.One2many('fct.activity','owner',string="Activities")
    
    @api.constrains('isPupil', 'isTutor')
    def _verify_valid_user(self):
        for r in self:
            if r.isPupil and r.isTutor:
                raise exceptions.ValidationError("A user can't be pupil and tutor")
            
        
    