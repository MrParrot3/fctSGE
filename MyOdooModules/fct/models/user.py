# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class User(models.Model):
    _inherit = 'res.users'
    
    isPupil = fields.Boolean("Pupil", default=False)
    isTutor = fields.Boolean("Tutor", default=False)
    
    
    @api.constrains('isPupil', 'isTutor')
    def _verify_valid_user(self):
        for r in self:
            if r.isPupil and r.isTutor:
                raise exceptions.ValidationError("A user can't be pupil and tutor")
            
        
    