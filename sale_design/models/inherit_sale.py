# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    design = fields.Many2many('sale.design', 'sale_order_design_rel', 'sale_order_id', 'design_id',
                                       string='Design', copy=False)