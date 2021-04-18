# -*- coding: utf-8 -*-

from odoo import models, fields, api
  
class sale_design(models.Model):
    _name = 'sale.design'
    _description = 'Sale Design'
  
    name = fields.Char(string="Design Name", required=True, index=True)
    design = fields.Binary(string="Design",
        help='It is upload design.')
    design_filename = fields.Char()
    date_write = fields.Datetime(string="Write date", default=fields.Datetime.now())
    
