# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Activity(models.Model):
    _name = 'fct.activity'
    
    start_date = fields.Date()
    description = fields.Text()
    duration = fields.Float()
    remarks = fields.Char(string="Remarks")
    
    @api.constrains('duration')
    def _verify_valid_duration(self):
        for r in self:
            if r.duration > 8:
                raise exceptions.ValidationError("A duration can't be more than 8 hours")
    
    

    