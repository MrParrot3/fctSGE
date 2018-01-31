# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Activity(models.Model):
    _name = 'fct.activity'
    
    start_date = fields.Date()
    description = fields.Text()
    duration = fields.Float()
    remarks = fields.Char(string="Remarks")
    
    
    
    

    