# -*- coding: utf-8 -*-

import logging
from odoo import api, models, _, fields
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class SaleOrderAmount(models.Model):
    _name = 'sale.order.amount'

    amount = fields.Monetary()
    sale_id = fields.Many2one(
        'sale.order'
    )
    name = fields.Char(
        'Description'
    )
    date_order = fields.Datetime()
    tc = fields.Float()
    currency_id = fields.Many2one(
        'res.currency'
    )
    amount_mxn = fields.Monetary()
    currency_mxn_id = fields.Many2one(
        'res.currency'
    )
    amount_usd = fields.Monetary()
    currency_usd_id = fields.Many2one(
        'res.currency'
    )
    amount_eu = fields.Monetary()
    currency_eu_id = fields.Many2one(
        'res.currency'
    )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        self.ensure_one()
        res = super(SaleOrder, self).action_confirm()
        self.env['sale.order.amount'].create(
            {
                'sale_id': self.id,
                'amount': self.amount_total,
                'name': self.name,
                'date_order': self.date_order,
                'currency_id': self.currency_id.id

            }
        )    
    